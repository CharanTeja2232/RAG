"""Tests for tools/summarize_human_grades.py. All grade data below is SYNTHETIC and lives only in temporary files; it never touches results/.
Run:  python tests/test_summarize_human_grades.py      (standard library only; no network, no model)"""
import csv, hashlib, importlib.util, io, json, sys, tempfile, unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("shg", ROOT / "tools" / "summarize_human_grades.py")
shg = importlib.util.module_from_spec(spec); spec.loader.exec_module(shg)
REAL = ROOT / "results" / "nist_stage6_human_review.csv"


def synthetic(grades):
    """grades: list of (a1_correct, a2_correct, better, lenient_baseline) -> rows with every column the tool needs."""
    rows = []
    for i, (c1, c2, better, lb) in enumerate(grades):
        r = dict(query_id=f"S{i}", category="synthetic", lenient_baseline=lb, lenient_reranked="success", strict_baseline=lb, strict_reranked="success", better=better)
        for t, c in (("a1", c1), ("a2", c2)):
            r.update({f"{t}_correct": c, f"{t}_supported_by_passages": "", f"{t}_complete": "", f"{t}_unsupported_claims": "", f"{t}_overall_judgment": "", f"{t}_unsupported_claims_notes": "", f"{t}_justification": ""})
            r.update({f"{t}_chk_{k}": "True" for k in shg.CHECKS})
        rows.append(r)
    return rows


def write_csv(rows, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)


class Tests(unittest.TestCase):
    def test_blank_real_review_sheet_has_no_grades_and_no_pairs(self):
        S = shg.summarize(shg.load_rows(REAL))
        self.assertEqual(S["n_queries"], 24)
        for t, _ in shg.TAGS:
            for k in shg.VOCAB:
                c = S["human"][t][k]
                self.assertEqual(c["ungraded"], 24); self.assertEqual(sum(v for a, v in c.items() if a != "ungraded"), 0)
        self.assertEqual(S["human"]["better"]["ungraded"], 24)
        self.assertEqual(S["paired"]["n_pairs_with_both_correctness_graded"], 0)
        self.assertEqual(sum(v["n"] for v in S["paired"]["categories"].values()), 0)
        self.assertEqual(shg.validate(shg.load_rows(REAL)), [])

    def test_frozen_retrieval_section_matches_the_persisted_files_not_the_grades(self):
        S = shg.summarize(shg.load_rows(REAL))
        base = json.loads((ROOT / "results/nist_baseline_top10.json").read_text()); rer = json.loads((ROOT / "results/nist_rerank_top10.json").read_text())
        for rule in ("lenient", "strict"):
            for pipe, d in (("baseline", base), ("reranked", rer)):
                from collections import Counter
                self.assertEqual(S["retrieval_frozen"][rule][pipe], dict(Counter(q[rule]["outcome"] for q in d["queries"])))

    def test_only_explicit_grades_are_counted_and_blanks_stay_ungraded(self):
        rows = synthetic([("correct", "correct", "neither clearly better", "success"), ("incorrect", "correct", "A2 better", "stumble"), ("", "correct", "", "success"), ("partially correct", "", "", "success")])
        S = shg.summarize(rows)
        self.assertEqual(S["human"]["a1"]["correct"], {"correct": 1, "partially correct": 1, "incorrect": 1, "ungraded": 1})
        self.assertEqual(S["human"]["a2"]["correct"], {"correct": 3, "partially correct": 0, "incorrect": 0, "ungraded": 1})
        self.assertEqual(S["paired"]["n_pairs_with_both_correctness_graded"], 2)          # rows 0 and 1 only
        self.assertEqual(S["human"]["a1"]["complete"]["ungraded"], 4)                       # never inferred from correctness

    def test_paired_categories_and_discordant_counts(self):
        rows = synthetic([("correct", "correct", "", "success"), ("correct", "incorrect", "", "success"), ("partially correct", "correct", "", "success"), ("incorrect", "incorrect", "", "success"),
                          ("partially correct", "incorrect", "", "success"), ("correct", "partially correct", "", "success"), ("partially correct", "partially correct", "", "success")])
        cat = shg.summarize(rows)["paired"]["categories"]
        self.assertEqual({k: v["query_ids"] for k, v in cat.items()}, {"both correct": ["S0"], "only Answer 1 correct": ["S1", "S5"], "only Answer 2 correct": ["S2"], "both incorrect": ["S3"],
                                                                      "other (no 'correct'; at least one 'partially correct')": ["S4", "S6"]})
        self.assertEqual(shg.summarize(rows)["paired"]["discordant_raw_counts"]["only_answer_1_correct"], 2)
        self.assertNotIn("p_value", json.dumps(shg.summarize(rows)).lower())

    def test_case_and_spacing_are_normalised_but_unknown_words_are_rejected(self):
        ok = synthetic([("  Partially   CORRECT ", "Correct", "a1 BETTER", "success")])
        self.assertEqual(shg.validate(ok), [])
        self.assertEqual(shg.summarize(ok)["human"]["a1"]["correct"]["partially correct"], 1)
        bad = synthetic([("mostly right", "correct", "A1", "success")])
        self.assertEqual({(q, c) for q, c, _, _ in shg.validate(bad)}, {("S0", "a1_correct"), ("S0", "better")})

    def test_invalid_file_stops_the_run_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "g.csv"; write_csv(synthetic([("yes", "correct", "", "success")]), p)
            with redirect_stdout(io.StringIO()) as out:
                code = shg.main([str(p), f"--out-prefix={tmp}/out"])
            self.assertEqual(code, 2); self.assertIn("INVALID ENTRIES", out.getvalue()); self.assertFalse(list(Path(tmp).glob("out*")))

    def test_the_tool_never_modifies_the_graded_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "g.csv"; write_csv(synthetic([("correct", "incorrect", "A1 better", "stumble"), ("", "", "", "success")]), p)
            before = hashlib.sha256(p.read_bytes()).hexdigest()
            with redirect_stdout(io.StringIO()):
                self.assertEqual(shg.main([str(p), f"--out-prefix={tmp}/out"]), 0)
            self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(), before)
            self.assertTrue((Path(tmp) / "out.md").exists() and (Path(tmp) / "out.json").exists())
            S = json.loads((Path(tmp) / "out.json").read_text()); self.assertEqual(S["input"]["sha256"], before)

    def test_human_grades_do_not_change_the_retrieval_or_objective_sections(self):
        a = shg.summarize(synthetic([("correct", "correct", "", "success"), ("incorrect", "incorrect", "", "stumble")]))
        b = shg.summarize(synthetic([("incorrect", "correct", "A2 better", "success"), ("correct", "incorrect", "A1 better", "stumble")]))
        self.assertEqual(a["retrieval_frozen"], b["retrieval_frozen"]); self.assertEqual(a["objective_format_checks"], b["objective_format_checks"])
        self.assertNotEqual(a["human"], b["human"])

    def test_failure_cases_are_listed_individually_with_ungraded_when_blank(self):
        S = shg.summarize(synthetic([("correct", "correct", "", "success"), ("", "correct", "", "stumble")]))
        self.assertEqual([r["query_id"] for r in S["failure_cases_individually"]], ["S1"])
        self.assertEqual(S["failure_cases_individually"][0]["a1_correct"], "ungraded")

    def test_template_matches_the_tool_and_contains_no_human_numbers(self):
        T = (ROOT / "results" / "nist_stage6_human_summary_template.md").read_text(encoding="utf-8")
        self.assertEqual(T, shg.render_md(shg.summarize(shg.load_rows(REAL)), template=True))
        self.assertIn("____", T); self.assertIn("(blank template)", T)

    def test_the_tool_cannot_reach_the_network(self):
        src = (ROOT / "tools" / "summarize_human_grades.py").read_text(encoding="utf-8")
        for word in ("urllib", "socket", "requests", "http.client", "subprocess"):
            self.assertNotIn(word, src)

    def test_warnings_flag_present_without_notes_and_judgment_without_justification(self):
        rows = synthetic([("correct", "correct", "", "success")]); rows[0]["a1_unsupported_claims"] = "present"; rows[0]["a2_overall_judgment"] = "acceptable"
        w = shg.summarize(rows)["warnings"]
        self.assertTrue(any("query S0, a1" in x and "notes field is empty" in x for x in w)); self.assertTrue(any("query S0, a2" in x and "no justification" in x for x in w))


if __name__ == "__main__":
    unittest.main(verbosity=2)
