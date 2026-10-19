# RAG Assignment: Baseline Retrieval vs Cross-Encoder Re-Ranking

Two pipelines over the **same chunked corpus**: (1) Bi-Encoder Top-10 -> first 3 chunks -> LLM (Answer 1); (2) the *same* Top-10 -> Cross-Encoder
re-rank -> first 3 chunks -> LLM (Answer 2). The LLM, prompt and parameters are identical; only the selected Top-3 context differs.

## Repository layout
| Path | What it is |
|---|---|
| `RAG_Baseline_vs_Rerank.ipynb` | **Primary experiment**, corpus: NIST SP 800-30 Rev. 1 (extraction, chunking, frozen corpus, preregistration, baseline, re-ranking, audit, Stage 6 generation code, latency) |
| `results/nist_*` | corpus, preregistration, review sheet, scoring overlays, baseline and re-ranked Top-10, per-query table, evaluation manifest, Stage 6 prompt spec, latency |
| `results/nist_stage6_*` | prompt spec, smoke test, answers ledger (`.jsonl`, one line per answer), attempt log (every API call), assembled answers, comparison table, **human-review sheet** (`.md` to read, `.csv` to grade) |
| `tests/check_frozen_artifacts.py` | independent integrity check: pinned hashes, a from-scratch re-scoring of every persisted outcome, a from-scratch rebuild of the 48 prompts, Stage 6 and latency consistency |
| `tools/run_notebook.py` | executes the notebook top to bottom in the chosen mode (see below) |
| `results/nist_stage6_grading_guide.json` | **draft expected-answer key** for the 24 queries (what a correct answer must contain, required qualification, unsupported-claim examples, supporting passages; every quote verified as an exact substring of its frozen chunk) |
| `results/nist_stage6_human_summary_template.md` | blank layout of the grade summary (frozen retrieval and objective-check numbers filled, every human-grade cell blank) |
| `results/nist_stage6_limitations_notes.md` / `..._evidence.json` | evidence notes for the report's limitations and the machine-derived figures behind them |
| `tools/summarize_human_grades.py` | computes the human-grade summary **only from the values you type**; `tests/test_summarize_human_grades.py` tests it |
| `tools/limitations_evidence.py` | re-derives every figure quoted in the limitations notes from the project files |
| `tools/run_stage6_only.py` | executes **only** the Stage 6 cells (Stages 1-5 are not re-executed; their state is restored from the hash-verified files) and refreshes the manifest's Stage 6 fields |
| `.env.example` | placeholder for the git-ignored `.env` that will hold `GROQ_API_KEY` |
| `pilot_catan/` | **Pilot study, kept separate**: CATAN *Cities & Knights* rulebook, a clearly labelled negative result |
| `data/` (git-ignored) | PDFs, embeddings, indexes, model cache |

**The pilot's metrics are never combined with the NIST results.** On the pilot (20 pages, 98 chunks) the Cross-Encoder produced 0 promotions
and 0 demotions over 19 queries; that corpus was too small and too easy for the effect to show, which is why the primary experiment uses NIST.

## Status
| Stage | State |
|---|---|
| NIST extraction, chunking, **frozen corpus** (305 chunks) | done |
| 24 preregistered questions, verified gold chunks, review sheet | done |
| Scoring overlay v1.1 pinned before any retrieval | done |
| Embeddings, FAISS index, **baseline retrieval** (Top-10 / Top-3) | done |
| **Cross-Encoder re-ranking** of exactly the persisted Top-10, failure-case audit | done |
| Stage 6 generation code (Groq), resumable, gated, offline-tested | done (40 new offline self-tests, no network) |
| Retrieval and re-ranking **latency** (single-threaded CPU) | measured, see below |
| Groq API key, **smoke test** (synthetic prompts only) | done 2026-10-18: passed, see below (`results/nist_stage6_smoke_test.json`) |
| The 48 evaluation **answers** (24 baseline, 24 re-ranked) | done 2026-10-18, user-approved: 48 of 48 first-attempt successes, see below |
| Grading guide, structured review sheet, summary tool, limitations evidence | done (see 'Human grading workflow') |
| Human grading of answer correctness | **not done: yours to do, in a copy of `results/nist_stage6_human_review.csv`** |

### Smoke test result (3 synthetic prompts about an invented village; no evaluation question used)
* Request succeeded (HTTP 200, 3 of 3); the API returned model id `qwen/qwen3.8-27b`, equal to the configured one, and the models endpoint lists it (11 models visible to the account).
* Accepted without error: temperature 0, top_p 1, n 1, `max_completion_tokens` 300, seed 1234, `reasoning_effort="none"`. No reasoning text or reasoning tokens; every call ended with `finish_reason="stop"` (23, 10 and 23 completion tokens against the 300 cap).
* The answerable prompt was answered correctly with its citation, the unanswerable prompt received the exact refusal sentence, and repeating a prompt returned identical text.
* Latency of the three calls (wall clock of the HTTP call, a new HTTPS connection each time, so connection set-up is included): 0.24 s, 0.53 s, 0.28 s; the server reported 0.03-0.06 s of total processing time. Three samples are a sanity check, not a measurement.
* The response headers reported this account's limits as 1,000 requests (per day) and 8,000 tokens (per minute), matching the documentation. The smoke test used 3 requests and 541 tokens. The calibrated estimate for the 48 evaluation answers is about 34,900 input tokens plus at most 14,400 output tokens (about 25 % of the daily token limit), roughly 8 minutes when paced.

## Scoring (frozen before retrieval)
* **Primary: preregistered lenient rule**: success if any preregistered gold chunk is in the Top 3; *stumble* if the best gold chunk is at rank 4-10; *miss* if none in the Top 10.
* **Secondary sensitivity analysis: strict overlay v1.1**: credit only for independently sufficient chunks or complete joint sets; partial evidence is reported as partial and never counted as success.
* Both appear in the per-query table `results/nist_per_query_results.csv`. Bi-Encoder cosines and Cross-Encoder logits are never compared with each other; only ranks and outcomes are.

## Retrieval result, as observed (N = 24 preregistered questions; nothing was changed after seeing it)
| | Baseline | Re-ranked |
|---|---|---|
| Lenient (primary): success | 21 of 24 | 24 of 24 |
| Strict (secondary): success | 20 of 24 | 24 of 24 |
| A preregistered gold chunk at rank 1 | 13 of 24 | 19 of 24 |

* **Genuine baseline failures** (evidence at rank 4-10, excluded from the Top 3): A4 (rank 6), E3 (rank 7), N5 (rank 4); under the strict rule also E4 (one of two needed chunks at rank 8).
* **Restored by re-ranking:** 3 of 3 (lenient), 4 of 4 (strict). **Demotions:** 0. **Candidate-pool misses:** 0. The assignment's requirement of at least two restored failures is met.
* In all three lenient failures, short glossary entries took Top-3 slots from the chunk that holds the answer.
* **This is retrieval only.** A retrieved gold chunk does not guarantee a correct answer; answer quality is not yet measured.
* **Limits:** N = 24 and only 3 failures, so no significance claim; the questions, labels and overlay were written by one author (the AI assistant) and are not independently validated; several keyword-trap questions reuse the source's wording; the O3 page-break extraction defect remains in the corpus (see `results/nist_prereg_review_sheet.md` and the overlay).

## Answer generation, as observed (Groq `qwen/qwen3.8-27b`, approved run of 2026-10-18)
48 requests, 48 HTTP 200, **0 retries**, 0 failures, every `finish_reason` = `stop`, returned model id `qwen/qwen3.8-27b` every time. Each answer record stores the query id, pipeline, context chunk ids (verified equal to the persisted Top 3), prompt and request hashes, usage, timestamps and latency.
The Stage 4-5 files were not re-executed or modified (byte-identical before and after).

**What the automated checks show. They test format and consistency only; they are NOT evidence of factual correctness** (an answer can cite the right passage and still be wrong):
| Objective check | Answer 1 (baseline) | Answer 2 (re-ranked) |
|---|---|---|
| cites a passage / cites only passages it was given | 21 / 24 | 24 / 24 |
| cites a preregistered gold chunk | 21 / 24 | 24 / 24 |
| is the exact refusal sentence ("The provided context does not contain the answer.") | 3 / 24 | 0 / 24 |
| within the three-sentence limit (approximate count) | 24 / 24 | 24 / 24 |

* The 3 refusals are exactly the 3 queries whose gold chunk the baseline left out of its Top 3 (A4, E3, N5); for those the re-ranked context produced a cited answer instead. For the 21 other queries both contexts contained gold evidence. Whether each answer is *correct* and *complete* is for the human review.
* The two answers are word-for-word identical for 8 of 24 queries. For E1 and O1 the two contexts hold the same three passages in a different order; E1's answers still differ in wording, so ordering and backend variation are both possible causes.
* **Uncontrolled factor:** Groq served the 48 calls from 4 different backend builds (`system_fingerprint`); for 16 of 24 queries the two answers came from different builds. Temperature 0 and a fixed seed were sent, but Groq documents determinism as best effort only.
* Tokens: baseline contexts 12,784 input / 977 output in total, re-ranked 14,454 input / 1,106 output (the re-ranked passages are longer on average).

**LLM generation latency** (wall clock of each successful HTTP call from this machine, a new HTTPS connection per call so connection set-up is included; pacing sleeps and retries excluded; n = 24 per pipeline). A remote service, **not comparable with the local CPU timings below**:
| Pipeline | mean ms | median ms | stdev ms | p95 ms | min ms | max ms |
|---|---|---|---|---|---|---|
| Answer 1 (baseline context) | 422.6 | 325.9 | 297.0 | 1338.7 | 221.1 | 1354.7 |
| Answer 2 (re-ranked context) | 397.4 | 316.2 | 292.1 | 714.5 | 237.9 | 1689.8 |

Both distributions are dominated by network and queueing noise (a few slow calls); the server-reported processing time had a median of 104 ms (baseline) and 132 ms (re-ranked). One sample per query and pipeline, so no latency difference between the pipelines is claimed.

## Latency of retrieval and re-ranking (measured; local CPU, single-threaded)
Apple M5, 16 GB, macOS, Python 3.14.7, `OMP_NUM_THREADS=1`, torch and FAISS using 1 thread, other processes running (load average about 2). Wall clock via `time.perf_counter`,
models and index loaded, 3 discarded warm-up passes, then 20 timed passes over the 24 questions (**n = 480 per row**). Every timed output was checked against the persisted Stage 4/5 results (0 mismatches).

| Component (milliseconds) | mean | median | stdev | p95 |
|---|---|---|---|---|
| (1) query embedding | 2.87 | 2.83 | 0.28 | 3.10 |
| (2) FAISS exact Top-10 search | 0.02 | 0.02 | 0.00 | 0.03 |
| (3) Cross-Encoder, 10 pairs | 92.60 | 93.03 | 12.34 | 108.20 |
| **Pipeline 1** = (1)+(2) | 2.89 | 2.85 | 0.28 | 3.13 |
| **Pipeline 2** = (1)+(2)+(3)+sort | 95.51 | 95.95 | 12.40 | 111.10 |
| re-ranking overhead (P2 minus P1) | 92.62 | 93.04 | 12.34 | 108.21 |

* The Cross-Encoder adds roughly 90 ms per query here: Pipeline 2 takes about 33 times as long as Pipeline 1 (95.5 ms vs 2.9 ms mean); most of the spread is between questions (per-question medians of Pipeline 2 range 51-110 ms with passage length), the rest is machine noise.
* One-time costs are excluded: loading the Bi-Encoder 0.03 s, the Cross-Encoder 0.02 s (from the local cache), reading the index 0.001 s, embedding all 305 chunks 1.7 s. Model download time is never included.
* **Why not run the Cross-Encoder over the whole collection:** measured here, scoring all 305 chunks per question took a median 1,952 ms (n = 72), 21 times the cost of scoring the Top 10, for a corpus of only 305 chunks.
  A *projection* (linear, **not measured**) from the per-pair cost gives about 64 s per question for 10,000 chunks and about 6,400 s for 1,000,000 chunks; the Bi-Encoder + FAISS pre-filter is what keeps the cost bounded.
* **LLM latency is a different kind of measurement** (a remote service, network included) and will be recorded per call; it must not be added to or compared with the numbers above as if the conditions were the same.

## Stage 6 design (answer generation)
* **The retrieval evaluation is frozen.** Stage 6 only reads `results/nist_baseline_top10.json` and `results/nist_rerank_top10.json`, after checking them against pinned SHA-256 values; a mismatch stops the run.
* **One prompt, one model, one set of parameters** for both pipelines: the instruction, context format and generation parameters (temperature 0, top_p 1, n 1, max 300 output tokens) were frozen before any provider was chosen (`prompt_and_generation_config_sha256 013f4a4c...`).
  The 48 prompts are rebuilt independently by the checker; for every query they differ only in the three passages.
* **Mode switch** `RAG_STAGE6_MODE`: `off` (default; Run All never touches the network), `smoke` (three synthetic prompts about an invented village: model id, parameter support, no reasoning tokens eating the cap, citation, exact refusal, determinism), `evaluate` (the 48 answers; refuses to start unless a smoke test passed for exactly these settings).
* **Resumable and auditable:** every finished answer is appended to a ledger, every API attempt (failures included) to an attempt log; a re-run skips finished answers and refuses a ledger written under other settings. Retries resend the byte-identical request; a response from a different model aborts the run (no silent model switch).
* **Answer quality is not measured by an LLM judge.** The comparison table puts the frozen retrieval outcomes next to the answers with objective checks (cites only the supplied passages, refusal sentence, truncation); correctness is a human judgement made on a review sheet.

### Provider: Groq free tier (facts read from Groq's documentation on 2026-10-18; not guaranteed)
* Free-plan chat models listed: `openai/gpt-oss-120b`, `openai/gpt-oss-20b` (production), `qwen/qwen3.8-27b` (**preview, may be discontinued at short notice**) and `openai/gpt-oss-safeguard-20b` (a safety classifier, not suitable). Llama 3.x chat models are enterprise-only: `llama-3.1-8b-instant` and `llama-3.3-70b-versatile` were shut down for free and developer tiers on 2026-08-16, and Groq's own migration advice for them was `gpt-oss-20b` / `gpt-oss-120b`.
* Documented free-plan limits for the three general chat models: **30 requests/min, 1,000 requests/day, 8,000 tokens/min, 200,000 tokens/day**, per organisation, whichever is reached first. The 8,000 tokens/min limit is the binding one. The account's own *Limits* page is authoritative; every response's rate-limit headers are logged.
* Estimated need for the 48 answers: about 33,000-44,000 input tokens (the prompts total roughly 133,000 characters) plus at most 14,400 output tokens (48 x the 300-token cap): **under 30 % of the daily token limit**, 48 of 1,000 requests, and about 9-10 minutes when paced at 80 % of the per-minute limit.
* Recommended model: **`qwen/qwen3.8-27b` with `reasoning_effort="none"`**, because it is the only free-tier chat model for which the frozen 300-token cap applies to the visible answer. The gpt-oss models cannot switch reasoning off and their reasoning tokens count toward the completion tokens, so the 300-token cap could truncate answers; using them would need a recorded, approved deviation. Trade-off: it is a preview model, and Groq has retired two Qwen generations within about two months (`qwen3-32b` on 2026-07-17, `qwen3.6-27b` on 2026-09-14), so it could disappear again; its answers would then have to be reproduced from the recorded ledger, not re-generated. Its answer quality is **unverified** by this project until the smoke test and the evaluation have run. The fallback with the most stable status is `openai/gpt-oss-120b` (production), at the price of the 300-token question above.
* Provider quirks, documented rather than hidden: Groq converts temperature 0 to 1e-8; `n` must be 1; `seed` is best effort only (a fixed seed is sent); `max_output_tokens` is sent as `max_completion_tokens`. Inputs and outputs are not retained by default but may be logged for up to 30 days for reliability or abuse investigation.
* If Groq proves unavailable or insufficient, the proposed alternative is a local model through Ollama; it will not be switched to without approval.

### Groq credentials (the key never goes into chat, a notebook or a source file)
1. Sign in at <https://console.groq.com> and open **API Keys**, then **Create API Key**; copy it (it is shown once).
2. In a terminal, from the project folder, type the key into a hidden prompt so it is not echoed or stored in shell history:
```bash
cd "/Users/charan/Documents/LanguageModels&Agents/RAGAssignment"
read -rs "KEY?Paste the Groq key (hidden), then press Return: " && echo
printf 'GROQ_API_KEY=%s\n' "$KEY" > .env && chmod 600 .env && unset KEY
git check-ignore -v .env
```
3. The last command must print a `.gitignore` rule for `.env`. **If it prints nothing, stop and do not use the key.** The notebook independently refuses to read a `.env` that git does not ignore.
4. Tell the assistant that the key is configured. It will only check that the variable exists (never print it) and run the smoke test.

## Human grading workflow (nothing is graded for you)
Do **not** type into the generated files: `results/nist_stage6_human_review.csv` / `.md` are regenerated by the notebook and the checker expects the grading fields in them to be blank.

1. **Read first:** the legend, conventions and per-query *grading guide* in `results/nist_stage6_human_review.md` (it also shows both contexts, the passage text, ranks, both answers and the objective format checks). The guide is a **draft key written by the AI assistant** from the frozen source and the pre-retrieval audit (not from any answer; the six answers it had already seen are listed in `results/nist_stage6_grading_guide.json`, `authoring`). Check it before you start. Do not edit it while grading; if you disagree with an item write that in `reviewer_notes`.
2. **Make your copy:**
```bash
cp results/nist_stage6_human_review.csv results/nist_stage6_human_grades.csv
```
3. **Grade in the copy** (a spreadsheet is fine; save as UTF-8 CSV with the same columns). For each query fill, separately for Answer 1 (`a1_*`) and Answer 2 (`a2_*`):

| column | allowed values (case does not matter; blank = ungraded) |
|---|---|
| `a1_correct` / `a2_correct` | `correct`, `partially correct`, `incorrect` (against the guide's expected answer) |
| `a1_supported_by_passages` / `a2_supported_by_passages` | `fully supported`, `partially supported`, `unsupported` (against the passages shown to that answer) |
| `a1_complete` / `a2_complete` | `complete`, `incomplete` (against the guide's required points) |
| `a1_unsupported_claims` / `a2_unsupported_claims` | `none`, `present`; describe in `a1_unsupported_claims_notes` / `a2_unsupported_claims_notes` |
| `a1_overall_judgment` / `a2_overall_judgment` | `acceptable`, `borderline`, `unacceptable`; one sentence in `a1_justification` / `a2_justification` |
| `better` | `A1 better`, `A2 better`, `neither clearly better` |
| `reviewer_notes` | free text (disagreements with the guide, the O2 tag 'accurate for the full PDF but not supported by the frozen corpus', anything unusual) |

   Do not use the objective checks (cites a gold chunk, refusal sentence, ...) as evidence of correctness. Refusals follow the convention in the legend. Do not change any other column.
4. **Validate, then summarise:**
```bash
python tools/summarize_human_grades.py --check
```
```bash
python tools/summarize_human_grades.py
```
   The first command lists any entry outside the vocabulary (a run with an invalid entry produces no summary). The second writes `results/nist_stage6_human_summary.md` and `.json`: retrieval success, objective checks and your human grades as **three separate sections**; counts of correctness, evidence support, completeness, unsupported claims and overall judgment per pipeline; the paired table (both correct / only Answer 1 correct / only Answer 2 correct / both incorrect / other) with query ids; your `better` marks; the retrieval-failure queries one by one. No significance test is computed.
5. **Record and re-verify:**
```bash
python tools/run_stage6_only.py
```
```bash
python tests/check_frozen_artifacts.py
```
   The first (no network, Stages 1-5 not re-executed) records the hashes of your graded copy and the summary in the manifest; the checker confirms your copy altered nothing except the grading fields.

## Reproducibility
| Item | Value |
|---|---|
| Source | https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-30r1.pdf (US government work, public domain) |
| PDF SHA-256 | `f214087f0bdb35932a28c16eb93932a33c67a6edfb5e6f1638866bd201c98e04` |
| Frozen corpus SHA-256 | `795fb2a6e043a28dc39d01e2db30d4b05d74ca1535df4ca7519d386b15f0fc92` (305 chunks) |
| Preregistration SHA-256 (unchanged) | `cb7a05a13b16fd0aacbe310e7903df4f5ee34137d3cac3ebf85714ec197ace33` |
| Scoring overlay v1.1 SHA-256 | `180c80dee8cf63207866cea103ec3c7c0e5dbeb80c9fd10d06b7e0460b8ab9ea` (supersedes v1.0, `c99f3cfe...`, kept unchanged) |
| Baseline / re-ranked Top-10 files | `c697c05d64304be40714750070aaba022f0540da347530d44f78d1a46f7c137d` / `1282c5190017579a26925ce6ad706c486b969eee997c590caeb786749c800838` (pinned in the notebook and the checker) |
| Prompt + generation parameters | `013f4a4cbaf737a3b498ebfd23d06c1293d55c37024c9baab09e82da9a37300c` |

All hashes, versions, parameters and the latency methodology are in `results/nist_evaluation_manifest.json`; its statements about what has been run are derived from the files on disk.
**Corpus scope:** only body-typeface text is indexed (Chapters 1-3, Cautionary Notes, the glossary one chunk per entry, the prose of Appendices D-K); tables, figures, footnotes, headers/footers, front matter, Appendices A and C are excluded.
Re-running the whole notebook reproduces every Stage 4/5 artifact **byte for byte** (verified, including the FAISS index and embeddings).

## Run and test
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python tests/check_frozen_artifacts.py      # fast, loads no model, makes no network call
python tests/test_summarize_human_grades.py   # tests of the grade-summary tool (synthetic data only)
python tools/run_notebook.py                # Run All with Stage 6 mode off (no network); about 25 seconds
```
Or open `RAG_Baseline_vs_Rerank.ipynb` with the `.venv` kernel and *Run All*; 73 self-tests run inside it. To run only Stage 6 (smoke test or the answers) without re-executing Stages 1-5: `RAG_STAGE6_MODE=smoke python tools/run_stage6_only.py`.
*Note:* the last cell of the notebook (the manifest writer) was edited after the last full Run All and is therefore shown without output; its code was executed against a scratch copy and reproduces the manifest on disk exactly (hashes included). A full Run All also regenerates it. Other modes: `RAG_STAGE6_MODE=smoke`, `RAG_STAGE6_MODE=evaluate`, `RAG_LATENCY_MODE=measure` (see `tools/run_notebook.py`).

## Known issue: OpenMP clash on macOS (single-threaded by design)
`torch`, `faiss-cpu` and `scikit-learn` each bundle their own `libomp.dylib`; with more than one OpenMP thread the process crashed with SIGSEGV.
The notebooks set `OMP_NUM_THREADS=1` before importing them, so **all CPU timings are single-threaded** and are not representative of multi-threaded or GPU speed.
