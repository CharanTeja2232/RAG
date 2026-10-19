"""Derive, from the project files only, every number cited in results/nist_stage6_limitations_notes.md. No network, no model, no API call.
Standard library; if the source PDF is on disk AND pymupdf is installed, the O2/O3 claims are also checked against the PDF itself (otherwise that part is reported as not checked).

    python tools/limitations_evidence.py          # writes results/nist_stage6_limitations_evidence.json (deterministic) and prints a summary

Lexical flags below ("mentions X") are plain substring tests of the answer text. They are NOT judgements of correctness."""
import collections
import json
import re
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
R = ROOT / "results"
J = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))
chunks = [json.loads(l) for l in open(R / "nist_chunks.jsonl", encoding="utf-8")]
by_id = {c["chunk_id"]: c for c in chunks}
pre = J(R / "nist_preregistration.json")["queries"]
base = {q["id"]: q for q in J(R / "nist_baseline_top10.json")["queries"]}
rer = {q["id"]: q for q in J(R / "nist_rerank_top10.json")["queries"]}
overlay = J(R / "nist_scoring_overlay_v1_1.json")
guide = J(R / "nist_stage6_grading_guide.json")
recs = [json.loads(l) for l in open(R / "nist_stage6_answers.jsonl", encoding="utf-8")]
att = [json.loads(l) for l in open(R / "nist_stage6_attempts.jsonl", encoding="utf-8")]
lat = J(R / "nist_latency_retrieval.json")
ans = {r["key"]: r for r in recs}
a1 = lambda q: ans[f"{q}|baseline"]
a2 = lambda q: ans[f"{q}|reranked"]
E = {}

# ---- O2 ------------------------------------------------------------------------------------------------------------------------------
INSCOPE = "0-15, 16-35, 36-70, 71-85, 86-100"
APPX = ["96-100", "80-95", "21-79", "5-20"]
o2 = dict(in_scope_bins=INSCOPE, chunks_containing_the_in_scope_bin_list=[c["chunk_id"] for c in chunks if INSCOPE in c["text"]],
          chunks_containing_each_appendix_bin_marker={m: [c["chunk_id"] for c in chunks if m in c["text"]] for m in APPX},
          gold_chunk="nt-061", overlay_rule=next(e for e in overlay["entries"] if e["question_id"] == "O2")["answer_level_rule"],
          retrieval=dict(baseline_gold_rank=base["O2"]["lenient"]["best_gold_rank"], reranked_gold_rank=rer["O2"]["lenient"]["best_gold_rank"],
                         both_contexts_contain_nt_061=all("nt-061" in a["context_chunk_ids"] for a in (a1("O2"), a2("O2")))),
          answers_lexical_flags={t: dict(mentions_each_in_scope_bin={b: b in a["answer"] for b in ("0-15", "16-35", "36-70", "71-85", "86-100")}, mentions_an_appendix_bin_marker=any(m in a["answer"] for m in APPX))
                                 for t, a in (("answer_1", a1("O2")), ("answer_2", a2("O2")))})
try:
    import pymupdf
    pdf = ROOT / "data" / "nist" / "nist_sp_800-30r1.pdf"
    if pdf.exists():
        doc = pymupdf.open(pdf)
        t67 = doc[66].get_text()
        o2["pdf_check"] = dict(checked=True, page_67_contains_appendix_bin_markers={m: bool(re.search(re.escape(m).replace("\\-", r"\s*[-–]\s*"), t67)) for m in APPX},
                               excluded_from_corpus=("tables are outside the corpus scope (README)"))
    else:
        o2["pdf_check"] = dict(checked=False, reason="source PDF not on disk")
except ImportError:
    o2["pdf_check"] = dict(checked=False, reason="pymupdf not installed")
E["O2_bins"] = o2

# ---- O3 ------------------------------------------------------------------------------------------------------------------------------
TERMINAL = (".", "!", "?", ":", ";", ")", "”", '"')
pairs = [(chunks[i]["chunk_id"], chunks[i + 1]["chunk_id"]) for i in range(len(chunks) - 1)
         if chunks[i]["section"] == chunks[i + 1]["section"] and chunks[i]["text"].rstrip()[-1] not in TERMINAL]
c121, c122 = by_id["nt-121"], by_id["nt-122"]
items = {"US-CERT": "US-CERT", "DCISE": "DCISE", "ISACs": "ISAC", "Carnegie Mellon / SEI-CERT": "Software Engineering Institute", "security service providers": "security service providers"}
ctx = lambda a: set(a["context_chunk_ids"])
o3 = dict(defect="one sentence crosses the PDF page break between pages 36 and 37 and was left in two chunks (nt-121 / nt-122)",
          nt_121=dict(page=c121["page_start"], section=c121["section"], ends_with=c121["text"][-100:], ends_without_terminal_punctuation=c121["text"].rstrip()[-1] not in TERMINAL),
          nt_122=dict(page=c122["page_start"], starts_with=c122["text"][:70], same_section_as_nt_121=c121["section"] == c122["section"]),
          recomputed_corpus_scan_same_section_pairs_whose_first_chunk_lacks_terminal_punctuation=pairs,
          overlay_statement_of_scan_result="exactly two pairs: nt-121/nt-122 (this defect) and nt-154/nt-155 (a list item continuing in the next bullet; not a gold passage)",
          treatment="corpus preserved (frozen hash); strict rule requires BOTH chunks (overlay v1.1); lenient (primary) rule counts either chunk",
          retrieval=dict(baseline_ranks={c: next((r["rank"] for r in base["O3"]["top10"] if r["chunk_id"] == c), None) for c in ("nt-121", "nt-122")},
                         reranked_ranks={c: next((r["rank"] for r in rer["O3"]["reranked_top10"] if r["chunk_id"] == c), None) for c in ("nt-121", "nt-122")},
                         strict_outcome=dict(baseline=base["O3"]["strict"]["outcome"], reranked=rer["O3"]["strict"]["outcome"]), strict_top3_evidence=dict(baseline=base["O3"]["strict"]["top3_evidence"], reranked=rer["O3"]["strict"]["top3_evidence"])),
          contexts_given_to_the_llm={t: dict(order=a["context_chunk_ids"], has_nt_121="nt-121" in ctx(a), has_nt_122="nt-122" in ctx(a)) for t, a in (("answer_1", a1("O3")), ("answer_2", a2("O3")))},
          answers_lexical_flags={t: {name: key.lower() in a["answer"].lower() for name, key in items.items()} for t, a in (("answer_1", a1("O3")), ("answer_2", a2("O3")))})
try:
    import pymupdf
    pdf = ROOT / "data" / "nist" / "nist_sp_800-30r1.pdf"
    if pdf.exists():
        doc = pymupdf.open(pdf)
        p36, p37 = doc[35].get_text(), doc[36].get_text()
        o3["pdf_check"] = dict(checked=True, page_36_contains="Collaborative Information" in p36, page_37_contains="Sharing Environment [DCISE]" in p37)
    else:
        o3["pdf_check"] = dict(checked=False, reason="source PDF not on disk")
except ImportError:
    o3["pdf_check"] = dict(checked=False, reason="pymupdf not installed")
E["O3_page_break_defect"] = o3

# ---- size, design, independence -------------------------------------------------------------------------------------------------------
cat = collections.Counter(q["category"] for q in pre)
E["evaluation_size_and_design"] = dict(
    n_queries=len(pre), per_category=dict(cat), generations_per_query_and_pipeline=dict(collections.Counter(collections.Counter(a["key"] for a in att if a["verdict"] == "ok").values())),
    total_answers=len(recs), retrieval_failures=dict(lenient_baseline_stumbles=[q for q in base if base[q]["lenient"]["outcome"] != "success"], strict_baseline_stumbles=[q for q in base if base[q]["strict"]["outcome"] != "success"]),
    questions_with_expected_yes_no_style_answer=sum(g["answer_type"].startswith("yes/no") for g in guide["queries"]),
    expected_polarity_counts=dict(collections.Counter("yes" if g["expected_polarity"].startswith("Yes") else "no, or not by default / not necessarily" for g in guide["queries"] if g["answer_type"].startswith("yes/no"))),
    yes_no_style_question_ids={k: [g["id"] for g in guide["queries"] if g["answer_type"].startswith("yes/no") and (g["expected_polarity"].startswith("Yes")) == (k == "yes")] for k in ("yes", "no")},
    strict_joint_evidence_questions=[e["question_id"] for e in overlay["entries"] if e["strict_rule"]["joint_sets"]],
    authors=dict(questions_gold_overlay_and_grading_key="the same AI assistant", independent_validation="none", graders="one (the user)", blinding="none: the Answer 1 / Answer 2 labels and the rank tables reveal which pipeline produced each answer"),
    statistical_testing="none performed")

# ---- backend fingerprints --------------------------------------------------------------------------------------------------------------
fp = collections.Counter(a["system_fingerprint"] for a in recs)
qids = [q["id"] for q in pre]
same_fp = [q for q in qids if a1(q)["system_fingerprint"] == a2(q)["system_fingerprint"]]
diff_fp = [q for q in qids if q not in same_fp]
ident = lambda q: a1(q)["answer"].strip() == a2(q)["answer"].strip()
same_set = [q for q in qids if set(a1(q)["context_chunk_ids"]) == set(a2(q)["context_chunk_ids"])]
E["backend_fingerprints"] = dict(
    distinct=len(fp), calls_per_fingerprint=dict(fp.most_common()), fingerprint_by_pipeline={p: dict(collections.Counter(a["system_fingerprint"] for a in recs if a["pipeline"] == p)) for p in ("baseline", "reranked")},
    pairs_with_the_same_fingerprint=len(same_fp), pairs_with_different_fingerprints=len(diff_fp),
    identical_answer_text=dict(among_same_fingerprint_pairs=sum(ident(q) for q in same_fp), among_different_fingerprint_pairs=sum(ident(q) for q in diff_fp), total=sum(ident(q) for q in qids)),
    identical_context_set_different_order=[dict(query=q, same_fingerprint=q in same_fp, identical_answer=ident(q), a1_order=a1(q)["context_chunk_ids"], a2_order=a2(q)["context_chunk_ids"]) for q in same_set],
    retrieval_failure_queries=[dict(query=q, same_fingerprint=q in same_fp) for q in base if base[q]["lenient"]["outcome"] != "success"],
    request_settings_identical_for_all=len({r["settings_sha256"] for r in recs}) == 1, seed_sent=1234, temperature_sent=0.0, groq_determinism="documented as best effort only")

# ---- input tokens ------------------------------------------------------------------------------------------------------------------------
tok = lambda p: sum(r["usage"]["prompt_tokens"] for r in recs if r["pipeline"] == p)
diff_q = {q: a2(q)["usage"]["prompt_tokens"] - a1(q)["usage"]["prompt_tokens"] for q in qids}
ctx_tok = lambda a: sum(by_id[c]["n_tokens"] for c in a["context_chunk_ids"])
E["input_tokens"] = dict(
    api_prompt_tokens_total=dict(answer_1=tok("baseline"), answer_2=tok("reranked")), difference=tok("reranked") - tok("baseline"), difference_percent_of_answer_1=round(100 * (tok("reranked") - tok("baseline")) / tok("baseline"), 1),
    api_completion_tokens_total=dict(answer_1=sum(r["usage"]["completion_tokens"] for r in recs if r["pipeline"] == "baseline"), answer_2=sum(r["usage"]["completion_tokens"] for r in recs if r["pipeline"] == "reranked")),
    per_query_difference_answer2_minus_answer1=dict(median=statistics.median(diff_q.values()), min=min(diff_q.values()), max=max(diff_q.values()), queries_where_answer_2_prompt_is_longer=sum(v > 0 for v in diff_q.values()),
                                                    queries_where_shorter=sum(v < 0 for v in diff_q.values()), queries_equal=sum(v == 0 for v in diff_q.values())),
    context_chunk_tokens_embedding_tokenizer_total=dict(answer_1=sum(ctx_tok(a1(q)) for q in qids), answer_2=sum(ctx_tok(a2(q)) for q in qids)),
    retrieval_failure_queries={q: dict(prompt_tokens=[a1(q)["usage"]["prompt_tokens"], a2(q)["usage"]["prompt_tokens"]], context_chunk_tokens=[ctx_tok(a1(q)), ctx_tok(a2(q))]) for q in base if base[q]["lenient"]["outcome"] != "success"},
    reading="the re-ranked Top 3 contains longer passages on average (short glossary entries are displaced); the LLM therefore saw more text for Answer 2 than for Answer 1")

# ---- latency: two different kinds of measurement ---------------------------------------------------------------------------------------
def stats(x):
    x = sorted(x)
    return dict(n=len(x), mean_ms=round(statistics.fmean(x), 1), median_ms=round(statistics.median(x), 1), stdev_ms=round(statistics.stdev(x), 1), min_ms=round(x[0], 1), max_ms=round(x[-1], 1))
llm = {p: [r["latency_s"] * 1000 for r in recs if r["pipeline"] == p] for p in ("baseline", "reranked")}
srv = {p: [r["usage"]["total_time"] * 1000 for r in recs if r["pipeline"] == p] for p in ("baseline", "reranked")}
E["latency_two_kinds"] = dict(
    retrieval_and_reranking=dict(what="local CPU, single-threaded (OMP_NUM_THREADS=1), models already loaded and warmed up, 3 discarded warm-up passes, 20 timed passes x 24 queries", n=lat["protocol"]["samples_per_component"],
                                 pipeline_1_ms=lat["steady_state_ms"]["pipeline1"], pipeline_2_ms=lat["steady_state_ms"]["pipeline2"], reranking_overhead_ms=lat["steady_state_ms"]["overhead"],
                                 machine=dict(cpu=lat["machine_before"]["cpu"], memory_gb=lat["machine_before"]["memory_gb"], other_processes_running=True)),
    llm_generation=dict(what="wall clock of each successful HTTPS call to a remote service from this machine (network, queueing and a new TLS connection per call included; pacing sleeps and retries excluded); one call per query and pipeline",
                        answer_1_baseline_context=stats(llm["baseline"]), answer_2_reranked_context=stats(llm["reranked"]),
                        server_reported_total_time_ms=dict(answer_1=stats(srv["baseline"]), answer_2=stats(srv["reranked"])), first_vs_second_call_in_pair_median_ms={pos: round(statistics.median([r["latency_s"] * 1000 for r in recs if r["call_position_in_pair"] == pos]), 1) for pos in (1, 2)}),
    not_comparable_because="different hardware, network vs none, warmed local models vs a shared remote service, n = 480 vs n = 24, and different tokens processed; the two are never added or ranked against each other",
    no_latency_claim="no difference between the pipelines is claimed for LLM latency (dominated by a few slow calls; one sample per query and pipeline)")

(R / "nist_stage6_limitations_evidence.json").write_text(json.dumps(E, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(E, indent=1, ensure_ascii=False, sort_keys=True))
