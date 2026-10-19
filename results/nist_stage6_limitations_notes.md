# Evidence notes for the limitations (not report prose)

Facts only, each with its source. Every number is derived by `tools/limitations_evidence.py` into `results/nist_stage6_limitations_evidence.json` (deterministic; re-running gives the same file). Nothing here is a grade of answer correctness.

## 1. O2: in-scope prose bins vs excluded appendix-table bins
* The question "What example score ranges does the guide give for binning semi-quantitative values?" does not say which set of bins. The guide contains two.
* **In scope (frozen corpus):** `0-15, 16-35, 36-70, 71-85, 86-100` (and the example scale `1-10`), Section 2.3, chunk `nt-061` only (`O2_bins.chunks_containing_the_in_scope_bin_list`).
* **Out of scope (appendix tables, excluded from the corpus by the scope rule):** e.g. `96-100`, `80-95`, `21-79`, `5-20`. None of these four markers occurs in any frozen chunk; all four occur on PDF page 67 (`pdf_check`, checked against the source PDF on this machine).
* **Scoring rule (overlay v1.1, written before retrieval):** an answer is correct *in scope* only if it gives the Section 2.3 bins; an answer that gives the appendix bins is recorded separately as "accurate for the full PDF but not supported by the frozen corpus". The question was not reworded (a reworded question would need a separate dated registration before retrieval).
* **What happened (objective, lexical only):** `nt-061` was in both contexts (gold rank 1 in baseline and re-ranked). Both answers contain all five in-scope bins and neither contains an appendix-bin marker. Whether they are *correct* is your judgement.
* **Why it matters:** the in-scope definition is an authorial scoping decision; a grader reading the whole PDF could accept either set. The guide (`O2`) states the rule so it is applied consistently.

## 2. O3: the PDF page-break defect and the decision to keep the frozen corpus
* The list of external threat-information sources is one sentence that crosses a PDF page break (page 36 to 37). The stitcher joined page-break continuations only when the next paragraph began with a lowercase letter; this one begins "Sharing", so the sentence was split between `nt-121` (ends "...Collaborative Information") and `nt-122` (starts "Sharing Environment [DCISE], ..."). Confirmed in the PDF (`pdf_check`).
* **Scope of the defect (recomputed here):** a scan of consecutive same-section chunk pairs whose first chunk lacks terminal punctuation finds exactly two: `nt-121/nt-122` (this defect) and `nt-154/nt-155` (a list item continuing in the next bullet, not a gold passage). This reproduces the overlay's statement.
* **Decision (overlay v1.1):** keep the frozen corpus unchanged (re-chunking would change the corpus hash and every chunk id, invalidating the preregistered gold ids). Handle it in scoring: the primary lenient rule counts either chunk; the strict rule requires **both** chunks. The defect is disclosed, not hidden.
* **What happened:** both pipelines retrieved `nt-121` and `nt-122` at ranks 1 and 2 (re-ranking did not change them), so both contexts held both halves of the sentence and strict retrieval succeeded for both. In this run the defect therefore did not remove evidence from either context.
* **Lexical flags only (not a grade):** the Answer 1 text contains US-CERT, DCISE, ISAC, Software Engineering Institute and "security service providers"; the Answer 2 text contains all of these except the string "DCISE". Judge completeness yourself against the guide's four required points.

## 3. Size and design of the evaluation
* **N = 24** questions, 6 per category (keyword trap, exception, negation/constraint, buried detail); **one generation per query and pipeline** (48 of 48 first-attempt successes; no repeats, so run-to-run variability of the LLM is not measured).
* **Few retrieval failures:** 3 lenient baseline failures (A4, E3, N5) and 4 strict (adds E4). Any per-category or failure-case statement rests on very small counts.
* **Question mix:** 12 of 24 are yes/no-style; 9 of those expect "no / not by default / not necessarily" and 3 expect "yes" (A4, E3, E5). Three questions need joint evidence under the strict rule (E4, O3, O5).
* **No independent validation:** the questions, gold labels, scoring overlay and the grading guide were all written by the same AI assistant; the human grader is a single person; grading is **not blinded** (the Answer 1/Answer 2 labels and the rank tables show which pipeline produced each answer). The guide was written after the answers existed, from the frozen source and the pre-retrieval audit; the six answers the assistant had already seen are listed in the guide's `authoring` block.
* **No statistical test** was or will be computed by the project tools; paired counts are raw counts.
* The LLM is a *preview* model on a free tier; it can be discontinued, so the ledger (not a re-run) is the record of these answers.

## 4. Backend fingerprints and what they mean for paired differences
* Settings were identical for all 48 calls (same model id, temperature 0, top_p 1, n 1, 300-token cap, seed 1234, `reasoning_effort="none"`), but the API returned **4 different `system_fingerprint` values**: 21, 15, 10 and 2 calls.
* **16 of 24 pairs** were served by different fingerprints; 8 by the same one. Answer 1 and Answer 2 differ in the fingerprint mix (`fingerprint_by_pipeline`).
* Groq documents determinism as best effort only (a seed is not a guarantee), and the fingerprint identifies a backend configuration that can change.
* **Descriptive observations (not inference):** the answer text is identical in 8 of 24 pairs: 3 of the 8 same-fingerprint pairs and 5 of the 16 different-fingerprint pairs. E1 and O1 have the same three passages in a different order: O1's answers are identical, E1's differ in wording, and both were served by different fingerprints. Of the three retrieval-failure queries, E3 had the same fingerprint for both answers; A4 and N5 did not.
* **Implication:** a wording difference between Answer 1 and Answer 2 can come from the different context, the different order, or backend variation, and these cannot be separated with one generation per pair and no repeated runs. Treat small wording differences as uninformative; judge substantive differences (correct vs incorrect, supported vs unsupported).

## 5. Input-token difference between the pipelines
* API prompt tokens, summed over the 24 queries: **Answer 1 = 12,784, Answer 2 = 14,454** (+1,670, +13.1 %). Completion tokens: 977 vs 1,106.
* Per query (Answer 2 minus Answer 1): median +86 tokens, range -63 to +178; Answer 2's prompt is longer in 18 queries, shorter in 4, equal in 2 (E1 and O1, same set of passages).
* Frozen-chunk size agrees (embedding-tokenizer tokens of the three passages): 8,981 vs 10,713. For the three retrieval-failure queries the re-ranked context is also longer (A4 279 to 457, E3 323 to 498, N5 289 to 385 chunk tokens).
* **Reading:** in this data the re-ranked contexts are longer, which is consistent with the earlier observation that short glossary entries held Top-3 slots in the baseline failure cases; that is an observation, not a tested explanation. More context is a confound for any answer difference (more relevant text, but also more room for distraction); the design cannot separate "better passages" from "more text".

## 6. Two different kinds of latency measurement
* **Retrieval and re-ranking (local):** CPU, single-threaded (`OMP_NUM_THREADS=1`), models loaded and warmed up, 3 discarded warm-up passes, 20 timed passes x 24 queries (**n = 480** per component), Apple M5 with other processes running. Pipeline 1 median 2.85 ms; Pipeline 2 median 95.95 ms; re-ranking overhead median 93.04 ms (stdev 12.34 ms).
* **LLM generation (remote):** wall clock of each successful HTTPS call, including network and queueing and a new TLS connection per call; pacing sleeps and retries excluded; **n = 24 per pipeline**, one call per query and pipeline. Answer 1 median 325.9 ms (mean 422.6, stdev 297.0, max 1354.7); Answer 2 median 316.2 ms (mean 397.4, stdev 292.1, max 1689.8). Server-reported processing time: median 104.1 ms vs 131.8 ms.
* **Not comparable and not additive:** different hardware, a network and a shared service vs a warmed local process, n = 480 vs 24, and different token counts. The first call of each pair was a little slower than the second (median 346 vs 311.5 ms), so call order is another small confound; the order alternated by query.
* The project makes **no claim** that either LLM latency is lower or higher.

## 7. Claims the evidence does NOT support
* That re-ranking improves answer correctness (answer correctness is not graded yet, and N = 24 with one generation per pair would not support significance anyway).
* That the Cross-Encoder *caused* any difference in answers (context length, passage order and backend all differ between the pipelines).
* That the objective checks (cites a passage, cites a gold chunk, refusal sentence, sentence count) measure factual correctness.
* That the retrieval result generalises beyond this corpus, these 24 questions and this author.
* That the LLM is deterministic, or that the preview model is available later.
