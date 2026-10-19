# NIST strict-scoring overlay v1.0 (proposed): change log and recommendation

*Created 2026-10-18 01:05 IST. Status: **proposed, awaiting your approval**. No embeddings, retrieval, reranking, generation or timing were run. The frozen corpus and the preregistration were not modified.*

| Item | Value |
|---|---|
| Overlay file | `results/nist_scoring_overlay_v1.json` |
| **Overlay SHA-256** | `c99f3cfe7cd7ec5898982fa499e9457dd2f2ed364a6a839c2424d7cd55d1a2ef` |
| How it is hashed | SHA-256 of the file's JSON (sorted keys) without the `status` and `overlay_sha256` fields |
| Frozen corpus SHA-256 (parent) | `795fb2a6e043a28dc39d01e2db30d4b05d74ca1535df4ca7519d386b15f0fc92` |
| Preregistration SHA-256 (parent) | `cb7a05a13b16fd0aacbe310e7903df4f5ee34137d3cac3ebf85714ec197ace33` |
| Review sheet SHA-256 (parent) | `4f4007b70f8660270c02e6db410aae91d72094a129526a53aff6d6e6fd576e52` |

## 1. Rules in one paragraph

Both scorings are computed from the **same** retrieval. **Lenient** is the preregistered rule (any preregistered gold chunk in the Top 3), unchanged. **Strict** gives credit only for chunks that are independently sufficient, or for complete *joint sets* where the answer is split. A fragment that cannot answer alone never earns strict credit on its own; an incomplete joint set is reported as *partial*, not as success. For the 17 unflagged questions, strict equals lenient.

## 2. The seven changes

| Q | Original gold | Strict rule | Added or dropped evidence | Reason |
|---|---|---|---|---|
| A5 | nt-043, nt-044 | any of nt-044, nt-042, nt-144; or ALL of nt-145 + nt-146 | adds nt-042, nt-144 (single); adds joint nt-145 + nt-146; drops nt-043 | The preregistered gold set was under-inclusive (two chunks that state the contrast explicitly were missing) and contained one partial chunk (nt-043). |
| E2 | nt-146, nt-147 | any of nt-146 | drops nt-147 | A chunk that cannot answer on its own must not earn strict credit. |
| E4 | nt-163, nt-164 | ALL of nt-163 + nt-164 | both required | The answer is split across a chunk boundary; counting either half alone would credit a fragment. |
| N4 | nt-161, nt-162 | any of nt-161 | drops nt-162 | A chunk that cannot answer on its own must not earn strict credit. |
| O2 | nt-061 | any of nt-061 | none (in-scope answer defined) | The question does not say which of the guide's two sets of example bins it means; the retrieval label is correct, so the ambiguity is resolved in the scoring definition and not by rewriting the question. |
| O3 | nt-121, nt-122 | ALL of nt-121 + nt-122 | both required | Neither chunk can list the organizations alone; the defect is documented and handled in scoring, not by editing the frozen corpus. |
| O5 | nt-301 | ALL of nt-300 + nt-301 | adds nt-300 as required context | The scope word in the question ('executive summary') is supported only by nt-300; the content only by nt-301. |

## 3. Evidence for each change (exact passages from the frozen chunks)

### A5 (keyword trap)

**Original gold:** nt-043, nt-044. **Change:** Gold set widened to every chunk whose frozen text states the contrast on its own; nt-043 dropped from strict credit.

* *Sufficient alone* `nt-044` (PDF p.[19, 20]): "First, organizations assess the likelihood that threat events will be initiated (for adversarial threat events) or will occur (for non-adversarial threat events). Second, organizations assess the likelihood that the threat events once initiated or occurring, will result in adverse impacts or harm to organizational operations and assets, individuals, other organizations, or the Nation."
* *Sufficient alone* `nt-042` (PDF p.19): "The likelihood risk factor combines an estimate of the likelihood that the threat event will be initiated with an estimate of the likelihood of impact (i.e., the likelihood that the threat event results in adverse impacts)."
* *Sufficient alone* `nt-144` (PDF p.42): "First, organizations assess the likelihood that threat events will be initiated (for adversarial threat events) or will occur (for non-adversarial threat events). Second, organizations assess the likelihood that threat events once initiated or occurring, will result in adverse impacts to organizational operations and assets, individuals, other organizations, or the Nation."
* *Sufficient only jointly:* nt-145 + nt-146. nt-145 describes the initiation assessment and nt-146 the adverse-impact assessment; only together do they show how the two likelihoods differ. Neither answers the contrast alone.
    * `nt-145` (PDF p.42): "Organizations assess the likelihood of threat event initiation by taking into consideration the characteristics of the threat sources of concern including capability, intent, and targeting"
    * `nt-146` (PDF p.42): "Organizations assess the likelihood that threat events result in adverse impacts by taking into consideration the set of identified vulnerabilities and predisposing conditions"
* *Excluded from strict credit* `nt-043`: Defines only the likelihood of impact ('regardless of the magnitude of harm'); it contains no statement of the initiation side, so by itself it cannot show the difference the question asks about. Passage: "The likelihood of impact addresses the probability (or possibility) that the threat event will result in an adverse impact, regardless of the magnitude of harm that can be expected."
* *Not evidence* `nt-148`: Lists table G-2 and G-4 as scales for two likelihoods but does not explain how they differ.
* *Not evidence* `nt-149`: Same: an index of tables G-2 to G-5, no explanation.
* **Residual limitation:** The three single-chunk additions can only raise strict success relative to the preregistered rule; the justification is that each contains the answer.

### E2 (exception)

**Original gold:** nt-146, nt-147. **Change:** nt-147 removed from strict credit (overlap-only).

* *Sufficient alone* `nt-146` (PDF p.42): "Threat events for which no vulnerabilities or predisposing conditions are identified, have a very low likelihood of resulting in adverse impacts. Such threat events can be highlighted and moved to the end of the table (or to a separate table), so that they can be tracked for consideration in follow-on risk assessments. However, no further consideration during the current assessment is warranted."
* *Excluded from strict credit* `nt-147`: Contains only the repeated closing sentence; the condition ('no vulnerabilities or predisposing conditions are identified') does not occur in this chunk (verified by search), so the sentence has no antecedent. Passage: "However, no further consideration during the current assessment is warranted."
* *Not evidence* `nt-136`: Different rule: threat events deemed irrelevant need no further consideration; it does not address events with no identified vulnerabilities.
* *Not evidence* `nt-137`: Starts with the 'irrelevant events' sentence of nt-136 (overlap); same different rule.
* **Residual limitation:** None beyond the wording gap already noted in the review sheet ('weaknesses' omits 'predisposing conditions').

### E4 (exception)

**Original gold:** nt-163, nt-164. **Change:** Strict credit requires BOTH chunks (joint evidence).

* *Sufficient only jointly:* nt-163 + nt-164. nt-163 gives the 'significant changes' branch; nt-164 starts with 'Otherwise,' and gives the other branch, whose condition is stated only in nt-163. Neither chunk answers 'must every task be redone?' by itself.
    * `nt-163` (PDF p.48): "If significant changes (as defined by organizational policies, direction, or guidance) have occurred since the risk assessment was conducted, organizations can revisit the purpose, scope, assumptions, and constraints of the assessment to determine whether all tasks in the risk assessment process need to be repeated."
    * `nt-164` (PDF p.48): "Otherwise, the updates constitute subsequent risk assessments, identifying and assessing only how selected risk factors have changed,"
* **Residual limitation:** The question says 'conditions have changed' while the source says 'significant changes'; this wording gap is unchanged.

### N4 (negation/constraint)

**Original gold:** nt-161, nt-162. **Change:** nt-162 removed from strict credit (overlap-only).

* *Sufficient alone* `nt-161` (PDF p.47): "For example, it is expected to be quite common for the security posture of information systems (that is, the risk factors measured within those systems) to reflect only a part of the organizational risk response, with response actions at the organization level or mission/business process level providing a significant portion of that response. In such situations, monitoring only the security posture of information systems would likely not provide sufficient information to determine the overall risk being incurred by organizations."
* *Excluded from strict credit* `nt-162`: Begins with the repeated sentence whose 'such situations' has no antecedent in this chunk (the 'quite common' context occurs only in nt-161, verified by search). Passage: "In such situations, monitoring only the security posture of information systems would likely not provide sufficient information to determine the overall risk being incurred by organizations."
* **Residual limitation:** The source answer is hedged ('would likely not'); the question asks in general terms.

### O2 (other (buried detail))

**Original gold:** nt-061. **Change:** No change to the gold chunk. The intended in-scope answer is defined explicitly; a possible wording correction is recorded but NOT adopted.

* *Sufficient alone* `nt-061` (PDF p.23): "The bins (e.g., 0-15, 16-35, 36-70, 71-85, 86-100) or scales (e.g., 1-10) translate easily into qualitative terms"
* *Not evidence* `nt-125`: Mentions a 0-100 scale only, without bins.
* *Not evidence* `(outside the frozen corpus)`: The appendix tables give other semi-quantitative bins (for example 'Very High 96-100', 'High 80-95', 'Moderate 21-79', read from PDF page 67). They are excluded from the corpus by the documented scope rule, so no retrievable chunk contains them.
* **Intended in-scope answer:** The example bins 0-15, 16-35, 36-70, 71-85 and 86-100 (and the example scale 1-10) given in the discussion of semi-quantitative assessments in Section 2.3. These are the only bin ranges in the frozen corpus (a pattern search found nt-061 as the sole chunk that lists bin ranges).
* **Answer-level rule:** When generated answers are judged later: an answer is correct in scope only if it gives the Section 2.3 bins. An answer that gives the appendix bins is recorded separately as 'accurate for the full PDF but not supported by the frozen corpus'.
* **Possible wording correction (NOT adopted; would need a new dated registration):** "In its discussion of semi-quantitative assessments (Section 2.3), what example score ranges does the guide give for translating scores into qualitative terms?"
* **Residual limitation:** If you prefer a reworded question, it must be a separately dated and hashed registration made before any retrieval.

### O3 (other (buried detail))

**Original gold:** nt-121, nt-122. **Change:** Strict credit requires BOTH chunks (joint evidence). The corpus is NOT modified.

* *Sufficient only jointly:* nt-121 + nt-122. One sentence is split mid-phrase across the two chunks. nt-121 names US-CERT and starts the DIB/DCISE name; nt-122 completes it and names the ISACs, the research organizations and security service providers.
    * `nt-121` (PDF p.36): "External sources of threat information can include cross-community organizations (e.g., US Computer Emergency Readiness Team [US-CERT], sector partners (e.g., Defense Industrial Base [DIB] using the DoD-Defense Industrial Base Collaborative Information"
    * `nt-122` (PDF p.37): "Sharing Environment [DCISE], Information Sharing and Analysis Centers [ISACs] for critical infrastructure sectors), research and nongovernmental organizations (e.g. Carnegie Mellon University, Software Engineering Institute-CERT), and security service providers)."
* **Extraction defect:** A paragraph that crosses a PDF page break was left unjoined: the sentence runs from the last line of PDF page 36 ('...Collaborative Information') to the first line of PDF page 37 ('Sharing Environment [DCISE], ...').
    * Cause: The stitching rule joined page-break continuations only when the next paragraph began with a lowercase letter; this one begins with a capital letter ('Sharing'). The chunker then kept the two pieces as separate blocks, and the chunk boundary fell inside the sentence.
    * Verified against the PDF: PDF p.36 last body line: 'sector partners (e.g., Defense Industrial Base [DIB] using the DoD-Defense Industrial Base Collaborative Information'; PDF p.37 first body line: 'Sharing Environment [DCISE], Information Sharing and Analysis Centers [ISACs] for critical infrastructure sectors),'.
    * Scope: A corpus-wide scan of consecutive same-section chunk pairs found exactly two whose earlier chunk ends without terminal punctuation: nt-121/nt-122 (this defect) and nt-154/nt-155 (a list item continuing in the next bullet, not a gold passage).
    * **Recommended** T1 strict joint rule, corpus untouched (disruption: none): Both chunks must be in the context for strict credit; lenient credit is unchanged; the defect is disclosed.
    * T2 fix the stitcher, re-chunk, re-freeze, re-register (disruption: high): Changes the corpus hash and shifts chunk ids, so every preregistered gold id would have to be re-derived and re-registered. Not recommended before any retrieval, and not done without approval.
    * T3 drop or replace the question (disruption: n/a): Not allowed: it would be an after-the-fact change to the question set.
* **Residual limitation:** The defect remains in the corpus and must be disclosed in the report.

### O5 (other (buried detail))

**Original gold:** nt-301. **Change:** Strict credit requires BOTH nt-300 (scope) and nt-301 (fact).

* *Sufficient only jointly:* nt-300 + nt-301. The requested fact is in nt-301 but nothing in its text says these bullets belong to the executive summary: the heading 'Executive Summary' occurs only in nt-300 (verified by search of the whole corpus). nt-300 alone has the heading but not the fact.
    * `nt-300` (PDF p.92): "Executive Summary
• List the date of the risk assessment."
    * `nt-301` (PDF p.92): "Describe the overall level of risk (e.g., Very Low, Low, Moderate, High, or Very High)."
    * `nt-301` also: "List the number of risks identified for each level of risk (e.g., Very Low, Low, Moderate, High, or Very High)."
* *Not evidence* `nt-299`: Appendix K introduction: names the three report sections but does not connect any bullet to them.
* **Residual limitation:** If only nt-301 is retrieved the case is reported as 'fact without scope' (partial), never as strict success.

## 4. Change log

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-10-18 01:05 IST | Initial proposal. Seven questions addressed: A5 (widened and one partial chunk dropped), E2 and N4 (overlap-only members removed), E4, O3 and O5 (joint evidence required), O2 (in-scope answer defined, wording untouched). Corpus, preregistration, wording, ids and order unchanged. |

## 5. Final recommendation

**The original 24 questions plus this overlay are defensible for baseline evaluation, on these conditions:**

1. The preregistration and the corpus stay exactly as frozen; the overlay is a second scoring, was fixed before any retrieval, and is derived from reading the text, not from results.
2. You approve the overlay and its hash is pinned in the notebook before Stage 4, so it cannot be adjusted after seeing results.
3. Both scorings are always reported together for every query (k of N), with the preregistered lenient rule labelled as such. The overlay mostly tightens credit; its one loosening (A5, three added single chunks) is justified by chunks that contain the answer.
4. The limitations are stated in the report: the O3 page-break defect remains in the corpus; O2's ambiguity is resolved in scoring only; several keyword-trap questions reuse the source's wording; 9 of 12 yes/no questions have the answer 'No'; N = 24 is too small for significance claims; and the questions, the audit and this overlay were all written by the same author (me), so they are not independently validated. Please read the seven flagged questions and the overlay rules yourself.

## 6. Unresolved decisions for you

| # | Decision | My recommendation |
|---|---|---|
| D1 | Approve overlay v1.0 as written (then its hash is pinned before Stage 4), or request changes (creates v1.1 with a new hash) | Approve |
| D2 | O2: keep the wording and use the in-scope answer definition, or register a reworded O2 as a separate, dated question | Keep wording and the definition; reword only if you want a stricter test |
| D3 | O3: strict joint rule with the corpus untouched, or fix the stitcher, re-chunk, re-freeze and re-register (changes all later chunk ids) | Strict joint rule, corpus untouched |
| D4 | O5: require nt-300 together with nt-301, or accept nt-301 alone | Require both |
| D5 | E1 (not flagged): nt-054 is only partial at chunk level; apply the same fragment rule to E1, or leave it | Leave unchanged, but note it |
| D6 | A5: keep the optional joint set nt-145 + nt-146 and the added singles nt-042 and nt-144 | Keep the two singles; the joint set is optional |
| D7 | Which scoring is the headline in the report | Report both; label the preregistered lenient rule as the primary and the overlay as the strict check |
| D8 | LLM provider and key for the later generation stage (still undecided) | Decide before Stage 6 |

## 7. Verification log

* Every passage in the overlay was asserted to be a literal substring of its frozen chunk when the file was generated.
* The overlay hash was recomputed from the saved JSON and matched.
* Hashes of the corpus, manifest, preregistration, review sheet and data copy were compared before and after: see the final report.