"""Independent integrity and re-scoring check. Standard library only: it loads no model and re-implements the scoring rules from scratch.
Run from the repository root:  python tests/check_frozen_artifacts.py     (exit code 0 = every check passed)"""
import hashlib, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
R = ROOT / "results"
results, failures = [], []


def check(name, ok):
    results.append(name)
    if not ok:
        failures.append(name)
    print(("PASS  " if ok else "FAIL  ") + name)


sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
J = lambda p: json.load(open(p, encoding="utf-8"))

# ---- pinned values (the same constants are pinned inside the notebook) -----------------------------------------------------------------
PDF_SHA = "f214087f0bdb35932a28c16eb93932a33c67a6edfb5e6f1638866bd201c98e04"
CORPUS_SHA = "795fb2a6e043a28dc39d01e2db30d4b05d74ca1535df4ca7519d386b15f0fc92"
PREREG_SHA = "cb7a05a13b16fd0aacbe310e7903df4f5ee34137d3cac3ebf85714ec197ace33"
OVERLAY_V10 = "c99f3cfe7cd7ec5898982fa499e9457dd2f2ed364a6a839c2424d7cd55d1a2ef"
OVERLAY_V11 = "180c80dee8cf63207866cea103ec3c7c0e5dbeb80c9fd10d06b7e0460b8ab9ea"
PILOT_FILE_PREFIXES = {"corpus_manifest": "e4705a822a4c", "index_manifest": "4b62ed3ffe29", "baseline_top10": "a06706270c58", "stage4b_baseline": "7c9126df95c7",
                       "stage4b_preregistration": "8dafdd2ab007", "stage5_rerank": "ffbe71944d6e", "near_duplicate_pairs": "ee837df93eca"}

# ---- corpus, preregistration, overlays ---------------------------------------------------------------------------------------------------
chunks = [json.loads(l) for l in open(R / "nist_chunks.jsonl", encoding="utf-8")]
h = hashlib.sha256()
for c in chunks:
    h.update(c["chunk_id"].encode() + b"\x00" + c["text"].encode("utf-8") + b"\x01")
check("corpus: 305 chunks hash to the frozen corpus value", len(chunks) == 305 and h.hexdigest() == CORPUS_SHA == J(R / "nist_corpus_manifest.json")["corpus_sha256"])
pdf = ROOT / "data/nist/nist_sp_800-30r1.pdf"
check("source PDF hash (skipped when the PDF is not downloaded)", (not pdf.exists()) or sha(pdf) == PDF_SHA)
pre = J(R / "nist_preregistration.json")
pre_h = hashlib.sha256(json.dumps(dict(corpus_sha256=pre["corpus_sha256"], queries=pre["queries"]), sort_keys=True, ensure_ascii=False).encode()).hexdigest()
check("preregistration: 24 questions, six per category, hash recomputes to the registered value", pre_h == pre["prereg_sha256"] == PREREG_SHA and len(pre["queries"]) == 24
      and all(sum(q["category"] == c for q in pre["queries"]) == 6 for c in {q["category"] for q in pre["queries"]}))
def overlay(path, pinned):
    o = J(path)
    core = {k: v for k, v in o.items() if k not in ("overlay_sha256", "status")}
    return o, hashlib.sha256(json.dumps(core, sort_keys=True, ensure_ascii=False).encode()).hexdigest() == o["overlay_sha256"] == pinned
o10, ok10 = overlay(R / "nist_scoring_overlay_v1.json", OVERLAY_V10)
o11, ok11 = overlay(R / "nist_scoring_overlay_v1_1.json", OVERLAY_V11)
check("overlay v1.0 (preserved) recomputes to its hash", ok10)
check("overlay v1.1 recomputes to its pinned hash and names v1.0 and the frozen parents", ok11 and o11["supersedes"]["overlay_sha256"] == OVERLAY_V10
      and o11["parents"]["corpus_sha256"] == CORPUS_SHA and o11["parents"]["preregistration_sha256"] == PREREG_SHA and o11["supersedes"]["file_sha256"] == sha(R / "nist_scoring_overlay_v1.json"))
by_id = {c["chunk_id"]: c for c in chunks}
exact = all(x["passage"] in by_id[x["chunk"]]["text"] for e in o11["entries"] for key in ("sufficient_single",) for x in e["strict_rule"][key]) \
    and all(m["passage"] in by_id[m["chunk"]]["text"] for e in o11["entries"] for j in e["strict_rule"]["joint_sets"] for m in j["members"])
check("overlay v1.1: every quoted passage is an exact substring of its frozen chunk", exact)

# ---- independent re-implementation of the scoring ------------------------------------------------------------------------------------
K_INIT, K_FINAL = 10, 3
rules = {}
for q in pre["queries"]:
    ent = next((e for e in o11["entries"] if e["question_id"] == q["id"]), None)
    if ent:
        r = ent["strict_rule"]
        rules[q["id"]] = (set(x["chunk"] for x in r["sufficient_single"]), [[m["chunk"] for m in j["members"]] for j in r["joint_sets"]], set(x["chunk"] for x in r["excluded_from_strict"]))
    else:
        rules[q["id"]] = (set(q["gold_chunk_ids"]), [], set())


def lenient(gold, ranked):
    pos = {c: i for i, c in enumerate(ranked[:K_INIT], 1)}
    best = min((pos[g] for g in gold if g in pos), default=None)
    return ("success" if best and best <= K_FINAL else "stumble" if best else "miss"), best


def strict(rule, ranked):
    singles, joints, excl = rule
    pos = {c: i for i, c in enumerate(ranked[:K_INIT], 1)}
    top = set(ranked[:K_FINAL])
    ok = any(s in top for s in singles) or any(all(m in top for m in j) for j in joints)
    part = any(any(m in top for m in j) and not all(m in top for m in j) for j in joints) or any(c in top for c in excl)
    cand = [pos[s] for s in singles if s in pos] + [max(pos[m] for m in j) for j in joints if all(m in pos for m in j)]
    return ("success" if ok else "stumble" if cand else "miss"), ("sufficient" if ok else "partial" if part else "none"), (min(cand) if cand else None)


base, rer = J(R / "nist_baseline_top10.json"), J(R / "nist_rerank_top10.json")
ok_b = ok_r = True
for q in base["queries"]:
    ids = [x["chunk_id"] for x in q["top10"]]
    lo, lb = lenient(q["gold_chunk_ids"], ids)
    so, se, sb = strict(rules[q["id"]], ids)
    ok_b &= (lo, lb, so, se, sb) == (q["lenient"]["outcome"], q["lenient"]["best_gold_rank"], q["strict"]["outcome"], q["strict"]["top3_evidence"], q["strict"]["best_sufficient_rank"])
for q in rer["queries"]:
    ids = [x["chunk_id"] for x in q["reranked_top10"]]
    lo, lb = lenient(q["gold_chunk_ids"], ids)
    so, se, sb = strict(rules[q["id"]], ids)
    ok_r &= (lo, lb, so, se, sb) == (q["lenient"]["outcome"], q["lenient"]["best_gold_rank"], q["strict"]["outcome"], q["strict"]["top3_evidence"], q["strict"]["best_sufficient_rank"])
check("independent re-scoring reproduces every persisted BASELINE outcome (24 queries, lenient and strict)", ok_b)
check("independent re-scoring reproduces every persisted RERANKED outcome (24 queries, lenient and strict)", ok_r)
check("questions in the result files are exactly the registered questions, in order", [q["id"] for q in base["queries"]] == [q["id"] for q in pre["queries"]] == [q["id"] for q in rer["queries"]]
      and [q["question"] for q in base["queries"]] == [q["question"] for q in pre["queries"]])

# ---- Stage 4 -> Stage 5 contract and the manifest ----------------------------------------------------------------------------------------
check("Stage 5 re-ranked exactly the persisted baseline candidates (same ten chunks, same file hash)",
      rer["baseline_file_sha256"] == sha(R / "nist_baseline_top10.json")
      and all(q["baseline_top10"] == [x["chunk_id"] for x in b["top10"]] and sorted(q["baseline_top10"]) == sorted(x["chunk_id"] for x in q["reranked_top10"]) for q, b in zip(rer["queries"], base["queries"])))
check("each query has 10 baseline rows and 10 reranked rows with consistent rank shifts", all(len(q["top10"]) == 10 for q in base["queries"])
      and all(len(q["reranked_top10"]) == 10 and all(x["rank_shift"] == x["original_rank"] - x["rank"] for x in q["reranked_top10"]) for q in rer["queries"]))
man = J(R / "nist_evaluation_manifest.json")
hh = man["hashes"]
check("evaluation manifest hashes match the files on disk", hh["corpus_sha256"] == CORPUS_SHA and hh["preregistration_sha256"] == PREREG_SHA and hh["overlay_v1_1_sha256"] == OVERLAY_V11
      and hh["overlay_v1_0_sha256"] == OVERLAY_V10 and hh["baseline_top10_file_sha256"] == sha(R / "nist_baseline_top10.json") and hh["rerank_top10_file_sha256"] == sha(R / "nist_rerank_top10.json")
      and hh["preregistration_file_sha256"] == sha(R / "nist_preregistration.json") and hh["review_sheet_file_sha256"] == sha(R / "nist_prereg_review_sheet.md")
      and hh["overlay_v1_1_file_sha256"] == sha(R / "nist_scoring_overlay_v1_1.json") and hh["per_query_results_csv_sha256"] == sha(R / "nist_per_query_results.csv"))
smoke_p, ledger_p, attempts_p, answers_p, cmp_p, lat_p = (R / n for n in ("nist_stage6_smoke_test.json", "nist_stage6_answers.jsonl", "nist_stage6_attempts.jsonl",
                                                                          "nist_stage6_answers.json", "nist_stage6_comparison.csv", "nist_latency_retrieval.json"))
ledger_lines = [l for l in ledger_p.read_text(encoding="utf-8").splitlines() if l.strip()] if ledger_p.exists() else []
check("manifest statements about the smoke test, the answers and latency agree with the files on disk (nothing is claimed as run, or not run, against the evidence)",
      man["llm_status"]["smoke_test_recorded"] == smoke_p.exists() and man["llm_status"]["evaluation_answers_on_disk"] == len(ledger_lines)
      and ("latency measurement" in man["not_run"]) == (not lat_p.exists()) and any(s.startswith("LLM answer generation") for s in man["not_run"]) == (not ledger_lines)
      and any(s.startswith("LLM smoke test") for s in man["not_run"]) == (not smoke_p.exists())
      and man["latency_methodology"]["status"].startswith("DEFINED ONLY") == (not lat_p.exists() and not ledger_lines))
check("manifest Stage 6 file hashes match the files on disk (absent file <-> null hash)",
      all(hh[k] == (sha(p) if p.exists() else None) for k, p in (("stage6_prompt_spec_file_sha256", R / "nist_stage6_prompt_spec.json"), ("stage6_smoke_test_file_sha256", smoke_p),
                                                                 ("stage6_answers_ledger_file_sha256", ledger_p), ("stage6_attempts_log_file_sha256", attempts_p), ("stage6_answers_file_sha256", answers_p),
                                                                 ("stage6_comparison_csv_sha256", cmp_p), ("stage6_human_review_md_sha256", R / "nist_stage6_human_review.md"),
                                                                 ("stage6_human_review_csv_sha256", R / "nist_stage6_human_review.csv"), ("stage6_grading_guide_file_sha256", R / "nist_stage6_grading_guide.json"),
                                                                 ("stage6_human_summary_template_sha256", R / "nist_stage6_human_summary_template.md"), ("stage6_human_grades_file_sha256", R / "nist_stage6_human_grades.csv"), ("stage6_human_summary_sha256", R / "nist_stage6_human_summary.md"),
                                                                 ("stage6_limitations_evidence_sha256", R / "nist_stage6_limitations_evidence.json"), ("stage6_limitations_notes_sha256", R / "nist_stage6_limitations_notes.md"),
                                                                 ("latency_retrieval_file_sha256", lat_p))))

# ---- Stage 6: the 48 prompts are rebuilt from scratch; generation artifacts are verified when they exist -------------------------------------
PROMPT_CFG_SHA = "013f4a4cbaf737a3b498ebfd23d06c1293d55c37024c9baab09e82da9a37300c"
spec = J(R / "nist_stage6_prompt_spec.json")
canon = lambda obj: hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
cfg_h = hashlib.sha256(json.dumps(dict(system=spec["system_instruction"], header=spec["context_header"], template=spec["prompt_template"], config=spec["generation_config"]), sort_keys=True).encode()).hexdigest()
check("Stage 6 prompt spec: instruction, header, template and generation parameters hash to the value frozen in Stage 5 (temperature 0, 300 tokens)",
      cfg_h == spec["prompt_and_generation_config_sha256"] == PROMPT_CFG_SHA == man["hashes"]["prompt_and_generation_config_sha256"]
      and spec["generation_config"] == dict(temperature=0.0, top_p=1.0, max_output_tokens=300, n=1))
ctx = lambda ids: "\n\n".join(f"[{c}] (PDF page {by_id[c]['page_start']})\n{by_id[c]['text']}" for c in ids)
msgs = lambda question, ids: [dict(role="system", content=spec["system_instruction"]), dict(role="user", content=f"{spec['context_header']}\n{ctx(ids)}\n\nQuestion: {question}\nAnswer:")]
top3 = {("baseline", b["id"]): b["top3_chunk_ids"] for b in base["queries"]} | {("reranked", r["id"]): r["reranked_top3_chunk_ids"] for r in rer["queries"]}
qtext = {q["id"]: q["question"] for q in pre["queries"]}
tasks = {t["key"]: t for t in spec["tasks"]}
rebuilt = {k: msgs(qtext[t["query_id"]], t["context_chunk_ids"]) for k, t in tasks.items()}
check("Stage 6: the 48 prompts rebuilt independently from the frozen chunks match the recorded hashes, and join to exactly the template string",
      len(tasks) == 48 and all(canon(rebuilt[k]) == t["prompt_sha256"] for k, t in tasks.items())
      and all(spec["prompt_template"].format(system=spec["system_instruction"], header=spec["context_header"], context=ctx(t["context_chunk_ids"]), question=qtext[t["query_id"]]) == "\n\n".join(m["content"] for m in rebuilt[k])
              for k, t in tasks.items())
      and canon([[t["key"], t["prompt_sha256"]] for t in spec["tasks"]]) == spec["eval_prompts_sha256"] == man["hashes"]["stage6_eval_prompts_sha256"])
check("Stage 6: Answer 1 uses exactly the persisted baseline Top 3 and Answer 2 exactly the persisted re-ranked Top 3, for all 24 queries",
      all(t["context_chunk_ids"] == top3[(t["pipeline"], t["query_id"])] and t["label"] == ("Answer 1" if t["pipeline"] == "baseline" else "Answer 2") for t in tasks.values())
      and all({p for (p, i) in top3 if i == q["id"]} == {"baseline", "reranked"} and f"{q['id']}|baseline" in tasks and f"{q['id']}|reranked" in tasks for q in pre["queries"]))
check("Stage 6: for every query the two prompts differ only in the context passages (same instruction, same question)",
      all(rebuilt[f"{q['id']}|baseline"][0] == rebuilt[f"{q['id']}|reranked"][0]
          and rebuilt[f"{q['id']}|baseline"][1]["content"].split("\n\nQuestion: ", 1)[1] == rebuilt[f"{q['id']}|reranked"][1]["content"].split("\n\nQuestion: ", 1)[1] for q in pre["queries"]))
check("Stage 6: the prompt spec pins the very retrieval files that are on disk",
      spec["baseline_file_sha256"] == sha(R / "nist_baseline_top10.json") and spec["rerank_file_sha256"] == sha(R / "nist_rerank_top10.json") and spec["corpus_sha256"] == CORPUS_SHA)

if not smoke_p.exists():
    check("Stage 6 smoke test: not run yet (skipped)", True)
else:
    sm = J(smoke_p)
    check("Stage 6 smoke test: three synthetic prompts only (none contains an evaluation question), every check passed, the API returned the configured model id, settings match the manifest",
          sm["all_checks_passed"] and len(sm["cases"]) == 3 and all(not any(q["question"] in c["question"] for q in pre["queries"]) for c in sm["cases"])
          and sm["model_returned"] == sm["model_requested"] == man["models"]["llm"]["model"] and sm["settings_sha256"] == man["hashes"]["stage6_settings_sha256"]
          and sm["request_template"] == man["models"]["llm"]["request_template"] and all(c["http_status"] == 200 and c["finish_reason"] == "stop" and c["reasoning_tokens"] == 0 for c in sm["cases"])
          and sm["models_endpoint_lists_the_model"])
if not ledger_lines:
    check("Stage 6 answers: none generated yet (nothing to verify; skipped)", True)
else:
    recs = [json.loads(l) for l in ledger_lines]
    llm = man["models"]["llm"]
    settings = {r["settings_sha256"] for r in recs}
    check("Stage 6 answers: every record matches its frozen task (query, pipeline, context ids, prompt hash), no duplicates, one model, one settings hash",
          len({r["key"] for r in recs}) == len(recs) <= 48 and all(r["key"] in tasks for r in recs)
          and all(r["context_chunk_ids"] == tasks[r["key"]]["context_chunk_ids"] and r["prompt_sha256"] == tasks[r["key"]]["prompt_sha256"] and r["status"] == "ok" for r in recs)
          and settings == {man["hashes"]["stage6_settings_sha256"]} and {r["model_requested"] for r in recs} == {llm["model"]} and all(r["model_returned"] == r["model_requested"] for r in recs))
    check("Stage 6 answers: same request settings for every call (temperature 0, top_p 1, n 1, 300-token cap) and each answer is non-empty text with usage, timestamps and latency",
          llm["request_template"]["temperature"] == 0.0 and llm["request_template"]["max_completion_tokens"] == 300
          and llm["request_template"]["n"] == 1 and llm["request_template"]["top_p"] == 1.0
          and all(isinstance(r["answer"], str) and r["answer"].strip() and r["usage"] and r["started_at_utc"] <= r["finished_at_utc"] and r["latency_s"] > 0 for r in recs))
    smoke = J(smoke_p) if smoke_p.exists() else None
    check("Stage 6 answers: a passing smoke test on synthetic prompts, recorded under the same settings, precedes the first evaluation answer",
          bool(smoke) and smoke["all_checks_passed"] and smoke["settings_sha256"] == next(iter(settings)) and smoke["run_at_utc"] <= min(r["started_at_utc"] for r in recs)
          and all(not any(q["question"] in c["question"] for q in pre["queries"]) for c in smoke["cases"]))
    if answers_p.exists():
        ans = J(answers_p)
        check("Stage 6 assembled answers: record count and text agree with the ledger; missing answers are listed as missing, never invented",
              len(ans["records"]) == 48 and ans["counts"]["ok"] == len(recs) and ans["counts"]["missing_or_failed"] == 48 - len(recs)
              and all((r["status"] == "ok") == (r["key"] in {x["key"] for x in recs}) for r in ans["records"])
              and all(r["answer"] == next(x for x in recs if x["key"] == r["key"])["answer"] for r in ans["records"] if r["status"] == "ok"))
    if attempts_p.exists():
        att = [json.loads(l) for l in attempts_p.read_text(encoding="utf-8").splitlines() if l.strip()]
        check("Stage 6 attempt log: every call is logged (failures included), only an allow-list of headers is kept, and each saved answer has a matching successful attempt",
              all(set(a["headers"]) <= {"retry-after", "x-ratelimit-limit-requests", "x-ratelimit-remaining-requests", "x-ratelimit-limit-tokens", "x-ratelimit-remaining-tokens",
                                        "x-ratelimit-reset-requests", "x-ratelimit-reset-tokens", "x-request-id", "date"} for a in att)
              and {a["key"] for a in att if a["verdict"] == "ok"} == {r["key"] for r in recs} and "authorization" not in attempts_p.read_text(encoding="utf-8").lower())

review_csv, review_md = R / "nist_stage6_human_review.csv", R / "nist_stage6_human_review.md"
if ledger_lines and len(ledger_lines) == 48 and review_csv.exists():
    import csv
    by = {r["key"]: r for r in recs}
    rows = list(csv.DictReader(open(review_csv, encoding="utf-8")))
    cites = lambda t: list(dict.fromkeys(re.findall(r"nt-\d{3}", t or "")))
    grading = ("a1_correct", "a1_supported_by_passages", "a1_complete", "a1_unsupported_claims", "a2_correct", "a2_supported_by_passages", "a2_complete", "a2_unsupported_claims", "better", "reviewer_notes")
    md_text = review_md.read_text(encoding="utf-8")
    ok = len(rows) == 24 and [r["query_id"] for r in rows] == [q["id"] for q in pre["queries"]]
    for r, q in zip(rows, pre["queries"]):
        a1, a2 = by[f"{q['id']}|baseline"], by[f"{q['id']}|reranked"]
        ok &= r["question"] == q["question"] and r["gold_chunk_ids"] == " ".join(q["gold_chunk_ids"])
        ok &= r["baseline_context"] == " ".join(top3[("baseline", q["id"])]) and r["reranked_context"] == " ".join(top3[("reranked", q["id"])])
        for tag, a in (("a1", a1), ("a2", a2)):
            c = cites(a["answer"])
            ok &= r[f"{tag}_answer"] == a["answer"] and r[f"{tag}_cited_ids"] == " ".join(c)
            ok &= r[f"{tag}_chk_cites_only_supplied_passages"] == str(bool(c) and set(c) <= set(a["context_chunk_ids"]))
            ok &= r[f"{tag}_chk_is_the_refusal_sentence"] == str(a["answer"].strip() == "The provided context does not contain the answer.")
            ok &= r[f"{tag}_chk_cites_a_preregistered_gold_chunk"] == str(bool(set(c) & set(q["gold_chunk_ids"])))
        ok &= r["answers_identical"] == str(a1["answer"].strip() == a2["answer"].strip())
        ok &= all(r[g] == "" for g in grading)
        ok &= q["question"] in md_text and all(f"**{cid}** (PDF page" in md_text for cid in set(a1["context_chunk_ids"]) | set(a2["context_chunk_ids"]))
    check("Stage 6 human-review sheet: 24 rows in preregistered order, contexts, answers, citations and objective flags agree with the ledger and frozen files; grading fields are blank; every shown passage is in the markdown",
          ok and "not proof that an answer is factually correct" in md_text)
else:
    check("Stage 6 human-review sheet: not generated yet (skipped)", True)

# ---- grading guide, extended review sheet, limitations evidence ---------------------------------------------------------------------------
ORIG_REVIEW_COLUMNS = ["query_id", "category", "question", "gold_chunk_ids", "preregistered_evidence", "baseline_context", "reranked_context", "baseline_best_gold_rank", "reranked_best_gold_rank",
                       "lenient_baseline", "lenient_reranked", "strict_baseline", "strict_reranked", "answers_identical", "a1_answer", "a1_cited_ids", "a1_chk_generated", "a1_chk_finish_reason_stop",
                       "a1_chk_cites_a_passage", "a1_chk_cites_only_supplied_passages", "a1_chk_cites_a_preregistered_gold_chunk", "a1_chk_is_the_refusal_sentence", "a1_chk_approx_sentences",
                       "a1_chk_within_three_sentence_limit", "a2_answer", "a2_cited_ids", "a2_chk_generated", "a2_chk_finish_reason_stop", "a2_chk_cites_a_passage", "a2_chk_cites_only_supplied_passages",
                       "a2_chk_cites_a_preregistered_gold_chunk", "a2_chk_is_the_refusal_sentence", "a2_chk_approx_sentences", "a2_chk_within_three_sentence_limit", "a1_correct", "a1_supported_by_passages",
                       "a1_complete", "a1_unsupported_claims", "a2_correct", "a2_supported_by_passages", "a2_complete", "a2_unsupported_claims", "better", "reviewer_notes"]
ORIG_GRADING = ORIG_REVIEW_COLUMNS[34:]
GRADE_FIELDS = set(ORIG_GRADING) | {"a1_unsupported_claims_notes", "a1_overall_judgment", "a1_justification", "a2_unsupported_claims_notes", "a2_overall_judgment", "a2_justification"}
ORIG_CONTENT_SHA = "4500d2680f39c97cf4adfc7ec369a906fbaae00201f67dfc881d7029c90eb81b"       # fingerprint of the first 34 columns of the sheet as first delivered (answers, contexts, retrieval, objective checks)
guide_p = R / "nist_stage6_grading_guide.json"
if not guide_p.exists():
    check("Stage 6 grading guide: not created yet (skipped)", True)
else:
    gd = J(guide_p)
    gq = {g["id"]: g for g in gd["queries"]}
    ok = [g["id"] for g in gd["queries"]] == [q["id"] for q in pre["queries"]]
    for q in pre["queries"]:
        g = gq[q["id"]]
        ok &= g["question"] == q["question"] and g["preregistered_gold_chunk_ids"] == q["gold_chunk_ids"] and g["category"] == q["category"]
        ok &= bool(g["expected_answer"].strip() and g["required_points"] and g["unsupported_claim_examples"] and g["supporting_passages"])
        ok &= all(p["chunk"] in by_id and p["quote"] in by_id[p["chunk"]]["text"] for p in g["supporting_passages"])           # every quote is an exact substring of its frozen chunk
        ok &= g["must_mention_qualification"] == (g["qualification_kind"] != "none") and (not g["must_mention_qualification"] or bool(g["qualification"].strip()))
    d = gd["definitions"]
    ok &= d["correctness"]["values"] == ["correct", "partially correct", "incorrect"] and d["evidence_support"]["values"] == ["fully supported", "partially supported", "unsupported"]
    ok &= d["completeness"]["values"] == ["complete", "incomplete"] and d["unsupported_claims"]["values"] == ["none", "present"] and d["paired_judgment"]["values"] == ["A1 better", "A2 better", "neither clearly better"]
    check("Stage 6 grading guide: covers the 24 preregistered questions in order, question text and gold ids match, every one of its quoted supporting passages is an exact substring of its frozen chunk, vocabularies as agreed",
          ok and len(gd["queries"]) == 24 and sum(len(g["supporting_passages"]) for g in gd["queries"]) >= 24 and "NOT an independent validation" in gd["authoring"]["author"])
    import difflib
    audit_parts = re.split(r"\n#### ([A-Z]\d)\. ", (R / "nist_prereg_review_sheet.md").read_text(encoding="utf-8"))
    audit = {audit_parts[i]: re.search(r"\*\*Expected answer \(from the source only\):\*\* (.*)", audit_parts[i + 1]).group(1).lower() for i in range(1, len(audit_parts), 2)}
    lcs = {g["id"]: difflib.SequenceMatcher(None, audit[g["id"]], g["expected_answer"].lower(), autojunk=False).find_longest_match(0, len(audit[g["id"]]), 0, len(g["expected_answer"])).size for g in gd["queries"]}
    check("Stage 6 grading guide: provenance: every expected answer closely tracks the matching 'Expected answer (from the source only)' line of the pre-retrieval audit (hash-pinned review sheet; common text of at least min(20, line length) characters); "
          "lexical overlap with the generated answers cannot show independence because both quote the same source passages, so independence rests on this derivation and on the recorded authoring statement",
          all(lcs[q] >= min(20, len(audit[q])) for q in lcs) and len(lcs) == 24 and sha(R / "nist_prereg_review_sheet.md") == man["hashes"]["review_sheet_file_sha256"])
if ledger_lines and len(ledger_lines) == 48 and review_csv.exists():
    import csv as _csv
    rows2 = list(_csv.DictReader(open(review_csv, encoding="utf-8")))
    cols = list(rows2[0])
    fp = hashlib.sha256(json.dumps([[r[c] for c in ORIG_REVIEW_COLUMNS[:34]] for r in rows2], ensure_ascii=False).encode()).hexdigest()
    check("Stage 6 review sheet: the 44 original columns are an unchanged prefix, the answer/context/retrieval/objective-check content equals the sheet as first delivered (fingerprint), and every original grading field is still blank",
          cols[:44] == ORIG_REVIEW_COLUMNS and fp == ORIG_CONTENT_SHA and all(r[c] == "" for r in rows2 for c in ORIG_GRADING))
    if guide_p.exists():
        new_cols = ["a1_unsupported_claims_notes", "a1_overall_judgment", "a1_justification", "a2_unsupported_claims_notes", "a2_overall_judgment", "a2_justification", "guide_expected_answer", "guide_expected_polarity",
                    "guide_required_points", "guide_must_mention_qualification", "guide_qualification_kind", "guide_qualification", "guide_qualification_affects", "guide_acceptable_wording",
                    "guide_unsupported_claim_examples", "guide_supporting_passages", "guide_grader_notes"]
        md_text2 = review_md.read_text(encoding="utf-8")
        ok = cols[44:] == new_cols
        for r in rows2:
            g = gq[r["query_id"]]
            ok &= r["guide_expected_answer"] == g["expected_answer"] and r["guide_required_points"] == " || ".join(g["required_points"]) and r["guide_unsupported_claim_examples"] == " || ".join(g["unsupported_claim_examples"])
            ok &= r["guide_supporting_passages"] == " || ".join(f"{p['chunk']}: {p['quote']}" for p in g["supporting_passages"]) and r["guide_must_mention_qualification"] == ("yes" if g["must_mention_qualification"] else "no")
            ok &= all(r[c] == "" for c in new_cols[:6])
            ok &= g["expected_answer"] in md_text2 and all(p["quote"] in md_text2 for p in g["supporting_passages"])
        ok &= all(f"> {r['answer']}" in md_text2 for r in recs) and md_text2.count("**Grading guide (draft key") == 24 and "## Grading legend" in md_text2
        check("Stage 6 review sheet: the guide appears for all 24 queries in the markdown and in the guide_* CSV columns (matching the guide file), the structured grading columns exist and are blank, and every ledger answer is shown verbatim",
              ok)
else:
    check("Stage 6 extended review sheet: not generated yet (skipped)", True)
grades_p = R / "nist_stage6_human_grades.csv"
if not grades_p.exists():
    check("Stage 6 human grades: no graded copy yet (skipped; grade in a COPY named results/nist_stage6_human_grades.csv, never in the generated sheet)", True)
else:
    import csv as _csv2
    g_rows = list(_csv2.DictReader(open(grades_p, encoding="utf-8")))
    o_rows = list(_csv2.DictReader(open(review_csv, encoding="utf-8")))
    check("Stage 6 human grades: your graded copy has the same columns and 24 rows, and you changed nothing except the grading fields (answers, contexts, ranks, retrieval outcomes, objective checks and guide columns are identical to the generated sheet)",
          list(g_rows[0]) == list(o_rows[0]) and len(g_rows) == 24 and all(g[c] == o[c] for g, o in zip(g_rows, o_rows) for c in o_rows[0] if c not in GRADE_FIELDS))
lim_p = R / "nist_stage6_limitations_evidence.json"
notes_p = R / "nist_stage6_limitations_notes.md"
if not (lim_p.exists() and ledger_lines):
    check("Stage 6 limitations evidence: not generated yet (skipped)", True)
else:
    ev, notes = J(lim_p), notes_p.read_text(encoding="utf-8")
    tok1 = sum(r["usage"]["prompt_tokens"] for r in recs if r["pipeline"] == "baseline"); tok2 = sum(r["usage"]["prompt_tokens"] for r in recs if r["pipeline"] == "reranked")
    fps = {}
    for r in recs: fps[r["system_fingerprint"]] = fps.get(r["system_fingerprint"], 0) + 1
    qs = [q["id"] for q in pre["queries"]]
    A = lambda q, p: next(r for r in recs if r["key"] == f"{q}|{p}")
    same = [q for q in qs if A(q, "baseline")["system_fingerprint"] == A(q, "reranked")["system_fingerprint"]]
    ident_n = sum(A(q, "baseline")["answer"].strip() == A(q, "reranked")["answer"].strip() for q in qs)
    scan = [(chunks[i]["chunk_id"], chunks[i + 1]["chunk_id"]) for i in range(len(chunks) - 1) if chunks[i]["section"] == chunks[i + 1]["section"] and chunks[i]["text"].rstrip()[-1] not in (".", "!", "?", ":", ";", ")", "”", '"')]
    ok = ev["input_tokens"]["api_prompt_tokens_total"] == dict(answer_1=tok1, answer_2=tok2) and ev["input_tokens"]["difference"] == tok2 - tok1
    ok &= ev["backend_fingerprints"]["distinct"] == len(fps) and ev["backend_fingerprints"]["calls_per_fingerprint"] == fps
    ok &= ev["backend_fingerprints"]["pairs_with_the_same_fingerprint"] == len(same) and ev["backend_fingerprints"]["identical_answer_text"]["total"] == ident_n
    ok &= ev["O3_page_break_defect"]["recomputed_corpus_scan_same_section_pairs_whose_first_chunk_lacks_terminal_punctuation"] == [list(p) for p in scan]
    ok &= ev["O2_bins"]["chunks_containing_the_in_scope_bin_list"] == [c["chunk_id"] for c in chunks if "0-15, 16-35, 36-70, 71-85, 86-100" in c["text"]] == ["nt-061"]
    ok &= all(v == [] for v in ev["O2_bins"]["chunks_containing_each_appendix_bin_marker"].values())
    ok &= ev["evaluation_size_and_design"]["n_queries"] == 24 and ev["evaluation_size_and_design"]["total_answers"] == 48 and ev["evaluation_size_and_design"]["generations_per_query_and_pipeline"] == {"1": 48}
    ok &= ev["latency_two_kinds"]["retrieval_and_reranking"]["n"] == 480 and ev["latency_two_kinds"]["llm_generation"]["answer_1_baseline_context"]["n"] == 24
    ok &= f"{tok1:,}" in notes and f"{tok2:,}" in notes and f"{tok2 - tok1:,}" in notes and f"{len(fps)} different" in notes and f"{len(qs) - len(same)} of 24" in notes
    check("Stage 6 limitations evidence: token totals, fingerprint counts, identical-answer count, the O2 bin chunks and the O3 page-break scan are re-derived here from the ledger and the frozen chunks and agree with the evidence file; the notes quote the same figures",
          ok)
if not lat_p.exists():
    check("Latency: not measured yet (skipped)", True)
else:
    lat = J(lat_p)
    ss = lat["steady_state_ms"]
    check("Latency measurement: outputs identical to the persisted Stage 4/5 results, 480 samples per component, single-threaded, internally consistent",
          lat["outputs_identical_to_persisted_results"]["mismatches"] == 0 and all(ss[k]["n"] == 480 for k in ("embed", "search", "ce_score", "sort", "pipeline1", "pipeline2", "overhead"))
          and lat["machine_before"]["torch_threads"] == 1 and lat["machine_before"]["omp_num_threads"] == "1"
          and ss["pipeline2"]["median_ms"] > ss["pipeline1"]["median_ms"] > 0 and ss["ce_score"]["median_ms"] > ss["search"]["median_ms"]
          and abs(ss["pipeline2"]["mean_ms"] - (ss["pipeline1"]["mean_ms"] + ss["overhead"]["mean_ms"])) < 1e-6 + 0.01 * ss["pipeline2"]["mean_ms"])

# ---- pilot preserved, no secrets ----------------------------------------------------------------------------------------------------------
check("CATAN pilot result files are unchanged (hash prefixes recorded when the pilot was verified)",
      all(sha(ROOT / f"pilot_catan/results/{k}.json").startswith(v) for k, v in PILOT_FILE_PREFIXES.items()))
pats = re.compile(r"(AIza[0-9A-Za-z_\-]{30,}|sk-[A-Za-z0-9]{20,}|sk-ant-[A-Za-z0-9\-_]{20,}|(?i:api[_-]?key)\s*[=:]\s*['\"][^'\"]{12,}|hf_[A-Za-z0-9]{30,}|gsk_[A-Za-z0-9]{20,})")
hits = []
SECRET_HOME = lambda p: p.name == ".env" or (p.name.startswith(".env.") and p.name != ".env.example")        # the git-ignored place where a key is SUPPOSED to live
for p in ROOT.rglob("*"):
    if not p.is_file() or any(part in (".venv", ".git", "data", "__pycache__") for part in p.relative_to(ROOT).parts) or p.suffix in (".pdf", ".npy", ".faiss") or SECRET_HOME(p):
        continue
    try:
        txt = p.read_text(encoding="utf-8")
    except Exception:
        continue
    if pats.search(txt):
        hits.append(str(p.relative_to(ROOT)))
check("no API key or token pattern appears in any project file outside data/, .venv and .git", not hits)
import subprocess
git = lambda *a: subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True)
env_files = [p for p in ROOT.iterdir() if p.is_file() and SECRET_HOME(p)]
example = ROOT / ".env.example"
check("credentials: every .env file present is ignored by git and untracked, and the committable .env.example holds no value",
      all(git("check-ignore", "-q", p.name).returncode == 0 and git("ls-files", "--error-unmatch", p.name).returncode != 0 for p in env_files)
      and (not example.exists() or all(not l.split("=", 1)[1].strip() for l in example.read_text().splitlines() if "=" in l and not l.lstrip().startswith("#"))))
ign = (ROOT / ".gitignore").read_text()
check(".gitignore keeps environments, model caches, indexes and .env out of version control", all(x in ign for x in (".venv/", "data/", ".env")))

print(f"\n{len(results) - len(failures)} of {len(results)} checks passed")
if failures:
    print("FAILED:", failures)
sys.exit(1 if failures else 0)
