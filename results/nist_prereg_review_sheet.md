# NIST SP 800-30 Rev. 1: review sheet for the 24 preregistered questions

*Read-only audit of the frozen corpus and the preregistered question set. Nothing in the corpus, the questions, their wording, order, gold labels or the preregistration was changed. No embedding, retrieval, Cross-Encoder, generation or timing was run; the audit used only the saved chunk text, a literal string search over it, and (for page labels and one scope check) the PDF's own text.*

## 0. Integrity of what was audited

| Item | Value |
|---|---|
| Frozen corpus SHA-256 (recomputed from `results/nist_chunks.jsonl`) | `795fb2a6e043a28dc39d01e2db30d4b05d74ca1535df4ca7519d386b15f0fc92` (305 chunks) |
| Preregistration SHA-256 (recomputed from `results/nist_preregistration.json`) | `cb7a05a13b16fd0aacbe310e7903df4f5ee34137d3cac3ebf85714ec197ace33` (24 questions) |
| Source PDF SHA-256 | `f214087f0bdb35932a28c16eb93932a33c67a6edfb5e6f1638866bd201c98e04` |
| Page numbers | 'PDF p.N' is the page recorded in each chunk's metadata; the printed footer label ('PAGE ...') was read from the PDF itself. |
| Chunk text | reproduced programmatically from the frozen file, so it is exact; every 'exact supporting passage' below was asserted to be a literal substring of its chunk. |

## 1. Rating rubric (applied uniformly)

* **Evidence sufficiency of a gold chunk:** *Sufficient* = the chunk alone supports a complete answer; *Partially sufficient* = it supports part of the answer or lacks a needed antecedent or context; *Insufficient* = it cannot answer the question by itself.
* **Question-level sufficiency** is that of the best single gold chunk. If only the chunks *together* answer it, the question is rated *Partially sufficient*.
* **Label validity:** *Valid* = at least one gold chunk is independently sufficient, no gold chunk is unsupported, and no other chunk fully answers the question while being left out of the gold set. *Needs review* = the labels are not wrong, but the gold set is under-inclusive, contains an overlap-only member, splits the answer across chunks, or the question wording has a material ambiguity or qualification mismatch. *Invalid* = the gold does not support the answer or the question is not answerable from the source.

## 2. Summary

| Label validity | Count |
|---|---|
| Valid | 17 |
| Needs review | 7 |
| Invalid | 0 |

| Question-level evidence sufficiency | Count |
|---|---|
| Sufficient | 21 |
| Partially sufficient | 3 |
| Insufficient | 0 |

| Gold-chunk level (34 question/chunk pairs) | Count |
|---|---|
| Sufficient | 25 |
| Partially sufficient | 8 |
| Insufficient | 1 |

| Category | Valid | Needs review | Invalid |
|---|---|---|---|
| keyword trap | 5 | 1 | 0 |
| exception | 4 | 2 | 0 |
| negation/constraint | 5 | 1 | 0 |
| other (buried detail) | 3 | 3 | 0 |

| ID | Category | Gold chunks | Question sufficiency | Label validity |
|---|---|---|---|---|
| A1 | keyword trap | nt-063 | Sufficient | Valid |
| A2 | keyword trap | nt-235 | Sufficient | Valid |
| A3 | keyword trap | nt-185 | Sufficient | Valid |
| A4 | keyword trap | nt-040 | Sufficient | Valid |
| A5 | keyword trap | nt-043, nt-044 | Sufficient | Needs review |
| A6 | keyword trap | nt-035, nt-281 | Sufficient | Valid |
| E1 | exception | nt-053, nt-054, nt-153 | Sufficient | Valid |
| E2 | exception | nt-146, nt-147 | Sufficient | Needs review |
| E3 | exception | nt-286 | Sufficient | Valid |
| E4 | exception | nt-163, nt-164 | Partially sufficient | Needs review |
| E5 | exception | nt-105 | Sufficient | Valid |
| E6 | exception | nt-076, nt-077 | Sufficient | Valid |
| N1 | negation/constraint | nt-126 | Sufficient | Valid |
| N2 | negation/constraint | nt-002 | Sufficient | Valid |
| N3 | negation/constraint | nt-131 | Sufficient | Valid |
| N4 | negation/constraint | nt-161, nt-162 | Sufficient | Needs review |
| N5 | negation/constraint | nt-010 | Sufficient | Valid |
| N6 | negation/constraint | nt-145 | Sufficient | Valid |
| O1 | other (buried detail) | nt-018, nt-244 | Sufficient | Valid |
| O2 | other (buried detail) | nt-061 | Sufficient | Needs review |
| O3 | other (buried detail) | nt-121, nt-122 | Partially sufficient | Needs review |
| O4 | other (buried detail) | nt-080 | Sufficient | Valid |
| O5 | other (buried detail) | nt-301 | Partially sufficient | Needs review |
| O6 | other (buried detail) | nt-125 | Sufficient | Valid |

## 3. Concerns and proposed corrections (NONE of these has been applied)

| # | Question | Concern | Evidence | Proposed correction |
|---|---|---|---|---|
| C1 | A5 | **Under-inclusive gold set; one gold chunk only partial** | nt-042 states the contrast almost word for word ('combines an estimate of the likelihood that the threat event will be initiated with an estimate of the likelihood of impact (i.e., the likelihood that the threat event results in adverse impacts)'), and nt-144 repeats the three-step process, yet neither is gold. nt-043 defines only the impact side. | Do not edit the registration. In a separately hashed *analysis overlay*, list nt-042 and nt-144 as additional answer-bearing chunks and mark nt-043 as partial. |
| C2 | E2 | **Overlap-only gold member** | nt-147 contains just the repeated closing sentence; the condition ('no vulnerabilities or predisposing conditions are identified') is only in nt-146. | Overlay: strict gold = {nt-146}; nt-147 flagged 'cannot answer alone'. |
| C3 | E4 | **Answer split across a chunk boundary; wording drops a qualifier** | Neither nt-163 ('significant changes' branch) nor nt-164 ('Otherwise' branch) answers alone. The question says 'conditions have changed', while the source distinguishes 'significant changes'. | Overlay: strict gold = all-of {nt-163, nt-164}; note the qualifier as a limitation. |
| C4 | N4 | **Overlap-only gold member** | nt-162 starts with the repeated sentence whose 'such situations' lacks its antecedent; nt-161 contains the full context. | Overlay: strict gold = {nt-161}; nt-162 flagged partial. |
| C5 | O3 | **Extraction defect: sentence split at a PDF page break** | The list of external sources is cut after 'Collaborative Information' (nt-121) and resumes at 'Sharing Environment [DCISE]' (nt-122). The stitching rule only joined continuations that begin with a lowercase letter. A scan of the whole corpus found this to be the only mid-sentence split between consecutive chunks of one section (nt-154 to nt-155 splits a list item, not a gold passage). | Do not re-freeze. Overlay: strict gold = all-of {nt-121, nt-122}. Record the defect and its cause in the report's limitations. |
| C6 | O5 | **Heading context absent from the gold chunk** | The answer is in nt-301 but the words 'Executive Summary' are only in nt-300. Metadata is invisible to the retriever and the LLM. | Overlay: strict = nt-301 together with nt-300 as required context, or accept nt-301 and state the limitation. |
| C7 | O2 | **The guide gives more than one set of example bins** | nt-061 (narrative) gives 0-15, 16-35, 36-70, 71-85, 86-100; the excluded appendix tables give other bins (for example 96-100, 80-95, 21-79 on PDF page 67). The question does not say which. | Keep gold nt-061. When judging generated answers later, accept answers based on either set only if they cite their source; state the ambiguity in the report. |
| C8 | systemic | **Any-of scoring is lenient for overlap-linked and split gold sets** | A5, E2, E4, N4, O3 and O5 would be scored as successes when only the weaker half of the evidence is retrieved. | Report two scorings computed from the same retrieval: the preregistered *lenient* rule unchanged, and a *strict* rule from the overlay above. Pin the overlay's hash before any retrieval. |
| C9 | systemic | **Several 'keyword trap' questions are weak traps** | A2, A3, A5 and A6 reuse the definition's own words, so they test definition lookup more than a lexical distractor. Expect few baseline failures there; this is a limitation of the set, not a label error. | No change; say so in the report. Do not add or rewrite questions to create failures. |
| C10 | systemic | **Yes/no polarity skew** | Of the 12 yes/no-style questions (A4, E1 to E5, N1 to N6), 9 have the answer 'No' (E1, E2, E4, N1, N2, N3, N4, N5 by default, N6) and 3 have 'Yes' (A4, E3, E5). When LLM answers are compared later, a model prior toward 'No' could inflate correctness. | No change to the set. Report the polarity counts and read the generated answers, not only the yes/no. |
| C11 | systemic | **Authorship and independence** | I wrote the questions after reading all chunks, and the labels were derived from phrases I chose. This audit is my own re-reading, so it is not an independent check. | You should read at least the flagged sheets (A5, E2, E4, N4, O2, O3, O5) and the questions themselves, since you will have to defend them. |

### Proposed strict-gold overlay (a proposal only)

| Question | Preregistered gold (lenient, unchanged) | Proposed strict rule |
|---|---|---|
| A5 | nt-043, nt-044 | nt-044 (nt-043 partial); additional answer-bearing: nt-042, nt-144 |
| E1 | nt-053, nt-054, nt-153 | nt-153 or nt-053 (nt-054 partial) |
| E2 | nt-146, nt-147 | nt-146 |
| E4 | nt-163, nt-164 | all-of nt-163 + nt-164 |
| N4 | nt-161, nt-162 | nt-161 |
| O3 | nt-121, nt-122 | all-of nt-121 + nt-122 |
| O5 | nt-301 | nt-301 with nt-300 as context |

All other questions: strict rule = the preregistered gold set.

## 4. Recommendation

**The preregistered set is usable for baseline retrieval, with conditions.** No question is invalid, 17 of 24 labels are fully valid, and 21 of 24 questions have at least one independently sufficient gold chunk. The 7 flagged questions affect how success is *scored*, not whether the gold chunks are relevant. I recommend: (1) leave the preregistration untouched; (2) before any retrieval, approve and pin the separately hashed strict overlay in section 3 so that both the lenient and strict scorings are reported; (3) record the O3 extraction defect and the limitations C9 to C11 in the report. If you would rather change any question or label, that must be done as a new, dated, separately hashed registration with a stated reason, again before any retrieval. I did not make any such change.

## 5. Review sheet

### Category: keyword trap

#### A1. keyword trap

**Exact question:** Which risk assessment orientation begins with the consequences we care about and our most critical assets, rather than with attackers or weaknesses?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-063 | PDF p.23 (printed 'PAGE 14') to PDF p.24 (printed 'PAGE 15') | CHAPTER TWO — THE FUNDAMENTALS — BASIC CONCEPTS ASSOCIATED WITH RISK ASSESSMENTS > 2.3 KEY RISK CONCEPTS > Uncertainty | 194 | yes | Sufficient |

**Full text of nt-063** (exact):

```text
For example, organizations can associate a specific time period with assessments of likelihood of occurrence and assessments of impact severity.
Analysis approaches differ with respect to the orientation or starting point of the risk assessment, level of detail in the assessment, and how risks due to similar threat scenarios are treated. An analysis approach can be: (i) threat-oriented; (ii) asset/impact-oriented; or (iii) vulnerability-oriented. A threat-oriented approach starts with the identification of threat sources and threat events, and focuses on the development of threat scenarios; vulnerabilities are identified in the context of threats, and for adversarial threats, impacts are identified based on adversary intent. An asset/impact-oriented approach starts with the identification of impacts or consequences of concern and critical assets, possibly using the results of a mission or business impact analyses and identifying threat events that could lead to and/or threat sources that could seek those impacts or consequences.
```

**Expected answer (from the source only):** The asset/impact-oriented analysis approach (it starts from the impacts or consequences of concern and the critical assets).

**Exact supporting passage(s):**

* `nt-063`: "An asset/impact-oriented approach starts with the identification of impacts or consequences of concern and critical assets, possibly using the results of a mission or business impact analyses and identifying threat events that could lead to and/or threat sources that could seek those impacts or consequences."

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Valid
* **Justification:** The chunk defines all the orientations and the asset/impact-oriented one is stated explicitly, with the starting point the question describes.
* **Another chunk required?** No. nt-028, nt-117 and nt-124 only list the three names without defining them; the vulnerability-oriented definition (nt-064) is not needed.
* **Ambiguity / missing qualification / extraction defect:** Chunk begins with a repeated overlap sentence (irrelevant to the answer). The chunk also defines the threat-oriented approach, which the question explicitly excludes ('rather than with attackers'), so the polarity is preserved. Category fit: the question keeps the source's key words ('consequences', 'critical assets'), so it is only a mild keyword trap.

#### A2. keyword trap

**Exact question:** Which term describes different experts arriving at the same results from the same data?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-235 | PDF p.59 (printed 'PAGE B-9') | APPENDIX B — GLOSSARY — COMMON TERMS AND DEFINITIONS > Reproducibility | 21 | no | Sufficient |

**Full text of nt-235** (exact):

```text
Reproducibility
The ability of different experts to produce the same results from the same data.
```

**Expected answer (from the source only):** Reproducibility.

**Exact supporting passage(s):**

* `nt-235`: "The ability of different experts to produce the same results from the same data."

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Valid
* **Justification:** The whole glossary entry (21 tokens) is the definition the question paraphrases; the term itself is the chunk's first line.
* **Another chunk required?** No. The term is used in nt-030, nt-059, nt-060 and nt-106 but defined only in the glossary.
* **Ambiguity / missing qualification / extraction defect:** The question reproduces the definition almost word for word, so this is a definition lookup, not a lexical trap. A true competitor exists: the 'Repeatability' entry (nt-234, 'ability to repeat an assessment in the future').

#### A3. keyword trap

**Exact question:** What do you call a safeguard used in place of a recommended baseline control that still gives comparable protection?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-185 | PDF p.53 (printed 'PAGE B-3') | APPENDIX B — GLOSSARY — COMMON TERMS AND DEFINITIONS > Compensating Security Control | 71 | no | Sufficient |

**Full text of nt-185** (exact):

```text
Compensating Security Control
A management, operational, and/or technical control (i.e., safeguard or countermeasure) employed by an organization in lieu of a recommended security control in the low, moderate, or high baselines that provides equivalent or comparable protection for an information system. [CNSSI No. 4009]
```

**Expected answer (from the source only):** A compensating security control.

**Exact supporting passage(s):**

* `nt-185`: "employed by an organization in lieu of a recommended security control in the low, moderate, or high baselines that provides equivalent or comparable protection for an information system"

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Valid
* **Justification:** The glossary entry defines exactly this concept and names it in its first line.
* **Another chunk required?** No. 'compensating' also appears in nt-025, nt-086, nt-103 and nt-274, but only as usage.
* **Ambiguity / missing qualification / extraction defect:** The question's words ('safeguard', 'recommended', 'baseline', 'comparable protection') mirror the definition, so it is a weak keyword trap.

#### A4. keyword trap

**Exact question:** Can something about an organization's environment, such as a system with no outside network connection, make a successful attack less likely?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-040 | PDF p.19 (printed 'PAGE 10') | CHAPTER TWO — THE FUNDAMENTALS — BASIC CONCEPTS ASSOCIATED WITH RISK ASSESSMENTS > 2.3 KEY RISK CONCEPTS > Vulnerabilities and Predisposing Conditions | 179 | yes | Sufficient |

**Full text of nt-040** (exact):

```text
In addition, a threat scenario tells a story, and hence is useful for risk communication as well as for analysis.
In addition to vulnerabilities as described above, organizations also consider predisposing conditions. A predisposing condition is a condition that exists within an organization, a mission or business process, enterprise architecture, information system, or environment of operation, which affects (i.e., increases or decreases) the likelihood that threat events, once initiated, result in adverse impacts to organizational operations and assets, individuals, other organizations, or the Nation. Predisposing conditions include, for example, the location of a facility in a hurricane- or flood-prone region (increasing the likelihood of exposure to hurricanes or floods) or a stand-alone information system with no external network connectivity (decreasing the likelihood of exposure to a network-based cyber attack).
```

**Expected answer (from the source only):** Yes: a predisposing condition such as a stand-alone system with no external network connectivity decreases the likelihood of exposure to a network-based cyber attack.

**Exact supporting passage(s):**

* `nt-040`: "a stand-alone information system with no external network connectivity (decreasing the likelihood of exposure to a network-based cyber attack)"

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Valid
* **Justification:** The chunk gives the definition of a predisposing condition (increases or decreases likelihood) and exactly the example in the question.
* **Another chunk required?** No. nt-142 and nt-231 say predisposing conditions can 'increase or decrease' likelihood but give no example, so they support the yes without the specific case.
* **Ambiguity / missing qualification / extraction defect:** Chunk begins with a repeated overlap sentence. The source says 'decreasing the likelihood of exposure to a network-based cyber attack' (network-based only); the question says 'a successful attack less likely', which is slightly broader.

#### A5. keyword trap

**Exact question:** How is the chance that an event actually causes harm different from the chance that someone starts it?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-043 | PDF p.19 (printed 'PAGE 10') | CHAPTER TWO — THE FUNDAMENTALS — BASIC CONCEPTS ASSOCIATED WITH RISK ASSESSMENTS > 2.3 KEY RISK CONCEPTS > Likelihood | 161 | no | Partially sufficient |
| nt-044 | PDF p.19 (printed 'PAGE 10') to PDF p.20 (printed 'PAGE 11') | CHAPTER TWO — THE FUNDAMENTALS — BASIC CONCEPTS ASSOCIATED WITH RISK ASSESSMENTS > 2.3 KEY RISK CONCEPTS > Likelihood | 149 | yes | Sufficient |

**Full text of nt-043** (exact):

```text
If a threat event is almost certain to be initiated or occur in the (specified or implicit) time frame, the risk assessment may take into consideration the estimated frequency of the event. The likelihood of threat occurrence can also be based on the state of the organization (including for example, its core mission/business processes, enterprise architecture, information security architecture, information systems, and environments in which those systems operate)—taking into consideration predisposing conditions and the presence and effectiveness of deployed security controls to protect against unauthorized/undesirable behavior, detect and limit damage, and/or maintain or restore mission/business capabilities. The likelihood of impact addresses the probability (or possibility) that the threat event will result in an adverse impact, regardless of the magnitude of harm that can be expected.
```

**Full text of nt-044** (exact):

```text
The likelihood of impact addresses the probability (or possibility) that the threat event will result in an adverse impact, regardless of the magnitude of harm that can be expected.
Organizations typically employ a three-step process to determine the overall likelihood of threat events. First, organizations assess the likelihood that threat events will be initiated (for adversarial threat events) or will occur (for non-adversarial threat events). Second, organizations assess the likelihood that the threat events once initiated or occurring, will result in adverse impacts or harm to organizational operations and assets, individuals, other organizations, or the Nation. Finally, organizations assess the overall likelihood as a combination of likelihood of initiation/occurrence and likelihood of resulting in adverse impact.
```

**Expected answer (from the source only):** The likelihood of initiation/occurrence is the chance a threat event is started (adversarial) or occurs (non-adversarial); the likelihood of impact is the chance that, once initiated, it results in adverse impact regardless of the magnitude of harm; the overall likelihood combines the two.

**Exact supporting passage(s):**

* `nt-043`: "The likelihood of impact addresses the probability (or possibility) that the threat event will result in an adverse impact, regardless of the magnitude of harm that can be expected."
* `nt-044`: "First, organizations assess the likelihood that threat events will be initiated (for adversarial threat events) or will occur (for non-adversarial threat events). Second, organizations assess the likelihood that the threat events once initiated or occurring, will result in adverse impacts or harm to organizational operations and assets, individuals, other organizations, or the Nation."

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Needs review
* **Justification:** nt-044 is independently sufficient. nt-043 defines only the impact side. The gold set is under-inclusive: other chunks state the contrast just as explicitly and would be scored as misses.
* **Another chunk required?** Not for nt-044. Other chunks that also answer: nt-042 ('combines an estimate of the likelihood that the threat event will be initiated with an estimate of the likelihood of impact'), nt-144 (the same three-step process), and jointly nt-145 and nt-146.
* **Ambiguity / missing qualification / extraction defect:** Under-inclusive gold (nt-042 and nt-144 are not listed). nt-044 begins with an overlap sentence that is the whole of nt-043's key sentence; the two gold chunks therefore share their evidence.

#### A6. keyword trap

**Exact question:** What is it called when adversaries change their behaviour after noticing our safeguards?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-035 | PDF p.18 (printed 'PAGE 9') | CHAPTER TWO — THE FUNDAMENTALS — BASIC CONCEPTS ASSOCIATED WITH RISK ASSESSMENTS > 2.3 KEY RISK CONCEPTS > Threats | 184 | no | Sufficient |
| nt-281 | PDF p.63 (printed 'PAGE B-13') | APPENDIX B — GLOSSARY — COMMON TERMS AND DEFINITIONS > Threat Shifting | 62 | no | Sufficient |

**Full text of nt-035** (exact):

```text
Threat shifting is the response of adversaries to perceived safeguards and/or countermeasures (i.e., security controls), in which adversaries change some characteristic of their intent/targeting in order to avoid and/or overcome those safeguards/countermeasures. Threat shifting can occur in one or more domains including: (i) the time domain (e.g., a delay in an attack or illegal entry to conduct additional surveillance); (ii) the target domain (e.g., selecting a different target that is not as well protected); (iii) the resource domain (e.g., adding resources to the attack in order to reduce uncertainty or overcome safeguards and/or countermeasures); or (iv) the attack planning/attack method domain (e.g., changing the attack weapon or attack path).
```

**Full text of nt-281** (exact):

```text
Threat Shifting
Response from adversaries to perceived safeguards and/or countermeasures (i.e., security controls), in which the adversaries change some characteristic of their intent to do harm in order to avoid and/or overcome those safeguards/countermeasures.
```

**Expected answer (from the source only):** Threat shifting.

**Exact supporting passage(s):**

* `nt-035`: "Threat shifting is the response of adversaries to perceived safeguards and/or countermeasures (i.e., security controls), in which adversaries change some characteristic of their intent/targeting in order to avoid and/or overcome those safeguards/countermeasures."
* `nt-281`: "Response from adversaries to perceived safeguards and/or countermeasures (i.e., security controls), in which the adversaries change some characteristic of their intent to do harm in order to avoid and/or overcome those safeguards/countermeasures."

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Valid
* **Justification:** Both chunks independently define the concept and name it (the narrative and the glossary versions are consistent).
* **Another chunk required?** No. nt-036 continues the discussion and nt-145 mentions the term, but neither defines it.
* **Ambiguity / missing qualification / extraction defect:** Two independent gold chunks make success easier. The glossary entry 'Advanced Persistent Threat' (nt-167) mentions 'adapting to a defender's efforts' and is a plausible lexical competitor, but it names a type of adversary, not this behaviour.

### Category: exception

#### E1. exception

**Exact question:** Is the level of risk always capped by the level of impact?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-053 | PDF p.22 (printed 'PAGE 13') | CHAPTER TWO — THE FUNDAMENTALS — BASIC CONCEPTS ASSOCIATED WITH RISK ASSESSMENTS > 2.3 KEY RISK CONCEPTS > Aggregation | 173 | no | Sufficient |
| nt-054 | PDF p.22 (printed 'PAGE 13') | CHAPTER TWO — THE FUNDAMENTALS — BASIC CONCEPTS ASSOCIATED WITH RISK ASSESSMENTS > 2.3 KEY RISK CONCEPTS > Aggregation | 113 | yes | Partially sufficient |
| nt-153 | PDF p.44 (printed 'PAGE 35') | CHAPTER THREE — THE PROCESS — CONDUCTING RISK ASSESSMENTS WITHIN ORGANIZATIONS > STEP 2: CONDUCT THE ASSESSMENT > TASK 2-6 | 184 | no | Sufficient |

**Full text of nt-053** (exact):

```text
Aggregation
Organizations may use risk aggregation to roll up several discrete or lower-level risks into a more general or higher-level risk. Organizations may also use risk aggregation to efficiently manage the scope and scale of risk assessments involving multiple information systems and multiple mission/business processes with specified relationships and dependencies among those systems and processes. Risk aggregation, conducted primarily at Tiers 1 and 2 and occasionally at Tier 3, assesses the overall risk to organizational operations, assets, and individuals given the set of discrete risks. In general, for discrete risks (e.g., the risk associated with a single information system supporting a well-defined mission/business process), the worst-case impact establishes an upper bound for the overall risk to organizational operations, assets, and individuals. One issue for risk aggregation is that this upper bound for risk may fail to apply.
```

**Full text of nt-054** (exact):

```text
One issue for risk aggregation is that this upper bound for risk may fail to apply.
For example, it may be advantageous for organizations to assess risk at the organization level when multiple risks materialize concurrently or when the same risk materializes repeatedly over a period of time. In such situations, there is the possibility that the amount of overall risk incurred is beyond the risk capacity of the organization, and therefore the overall impact to organizational operations and assets (i.e., mission/business impact) goes beyond that which was originally assessed for each specific risk.
```

**Full text of nt-153** (exact):

```text
In general, the risk level is typically not higher than the impact level, and likelihood can serve to reduce risk below that impact level. However, when addressing organization-wide risk management issues with a large number of missions/business functions, mission/business processes, and supporting information systems, impact as an upper bound on risk may not hold. For example, when multiple risks materialize, even if each risk is at the moderate level, the set of those moderate-level risks could aggregate to a higher level of risk for organizations. To address situations where harm occurs multiple times, organizations can define a threat event as multiple occurrences of harm and an impact level associated with the cumulative degree of harm. During the execution of Tasks 2-1 through 2-5, organizations capture key information related to uncertainties in risk assessments. These uncertainties arise from sources such as missing information, subjective determinations, and assumptions made.
```

**Expected answer (from the source only):** No: risk is typically not higher than impact, but when risks aggregate (several risks materialize at once or one repeatedly), the impact upper bound may not hold.

**Exact supporting passage(s):**

* `nt-053`: "In general, for discrete risks (e.g., the risk associated with a single information system supporting a well-defined mission/business process), the worst-case impact establishes an upper bound for the overall risk to organizational operations, assets, and individuals. One issue for risk aggregation is that this upper bound for risk may fail to apply."
* `nt-054`: "For example, it may be advantageous for organizations to assess risk at the organization level when multiple risks materialize concurrently or when the same risk materializes repeatedly over a period of time."
* `nt-153`: "In general, the risk level is typically not higher than the impact level, and likelihood can serve to reduce risk below that impact level. However, when addressing organization-wide risk management issues with a large number of missions/business functions, mission/business processes, and supporting information systems, impact as an upper bound on risk may not hold."

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Valid
* **Justification:** nt-153 states the rule and its exception in one place and is independently sufficient. nt-053 also states both (rule, then 'may fail to apply'). nt-054 gives the reason but not the rule (the rule appears only in its overlap sentence).
* **Another chunk required?** No. nt-153 alone answers it fully; nt-053 and nt-054 are complementary.
* **Ambiguity / missing qualification / extraction defect:** Polarity check: 'always capped' -> 'No', which both the general statement and the exception support. nt-054 begins with an overlap sentence from nt-053.

#### E2. exception

**Exact question:** If a threat event has no identified weaknesses that could be exploited, do we keep analysing it in the current assessment?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-146 | PDF p.42 (printed 'PAGE 33') | CHAPTER THREE — THE PROCESS — CONDUCTING RISK ASSESSMENTS WITHIN ORGANIZATIONS > STEP 2: CONDUCT THE ASSESSMENT > TASK 2-4 | 196 | no | Sufficient |
| nt-147 | PDF p.42 (printed 'PAGE 33') to PDF p.43 (printed 'PAGE 34') | CHAPTER THREE — THE PROCESS — CONDUCTING RISK ASSESSMENTS WITHIN ORGANIZATIONS > STEP 2: CONDUCT THE ASSESSMENT > TASK 2-4 | 157 | yes | Insufficient |

**Full text of nt-146** (exact):

```text
Organizations assess the likelihood that threat events result in adverse impacts by taking into consideration the set of identified vulnerabilities and predisposing conditions (see Task 2-3 and Appendix F). For threat events initiated by adversaries, organizations consider characteristics of associated threat sources. For non-adversarial threat events, organizations take into account the anticipated severity and duration of the event (as included in the description of the event). Organizations use the assessment scale in Table G-4 and provide a rationale for the assessment allowing explicit consideration as stated above. Threat events for which no vulnerabilities or predisposing conditions are identified, have a very low likelihood of resulting in adverse impacts. Such threat events can be highlighted and moved to the end of the table (or to a separate table), so that they can be tracked for consideration in follow-on risk assessments. However, no further consideration during the current assessment is warranted.
```

**Full text of nt-147** (exact):

```text
However, no further consideration during the current assessment is warranted.
The overall likelihood of a threat event is a combination of: (i) the likelihood that the event will occur (e.g., due to human error or natural disaster) or be initiated by an adversary; and (ii) the likelihood that the initiation/occurrence will result in adverse impacts. Organizations assess the overall likelihood of threat events by using inputs from Tables G-2, G-3, and G-4. Any specific algorithm or rule for combining the determined likelihood values depends on: (i) general organizational attitudes toward risk, including overall risk tolerance and tolerance for uncertainty; (ii) specific tolerances toward uncertainty in different risk factors; and (iii) organizational weighting of risk factors.
```

**Expected answer (from the source only):** No: such threat events have a very low likelihood of adverse impact; they can be tracked for follow-on assessments, but no further consideration is warranted in the current assessment.

**Exact supporting passage(s):**

* `nt-146`: "Threat events for which no vulnerabilities or predisposing conditions are identified, have a very low likelihood of resulting in adverse impacts. Such threat events can be highlighted and moved to the end of the table (or to a separate table), so that they can be tracked for consideration in follow-on risk assessments. However, no further consideration during the current assessment is warranted."
* `nt-147`: "However, no further consideration during the current assessment is warranted."

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Needs review
* **Justification:** nt-146 is independently sufficient. nt-147 contains only the repeated closing sentence, with no antecedent (the 'no vulnerabilities' condition is not in the chunk), so by itself it cannot answer the question.
* **Another chunk required?** No (nt-146 alone).
* **Ambiguity / missing qualification / extraction defect:** Overlap-only gold member (nt-147) would credit a chunk that cannot answer. The question says 'weaknesses' and omits 'predisposing conditions' from the source condition. A different rule nt-136/nt-137 ('If a threat event is deemed to be irrelevant, no further consideration is given') is a genuine, legitimate distractor for this question.

#### E3. exception

**Exact question:** Can a threat event be dropped from the analysis when no adversary is known to have the ability to carry it out?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-286 | PDF p.69 (printed 'PAGE E-1') | APPENDIX E — THREAT EVENTS — REPRESENTATIVE THREAT EVENTS INITIATED BY THREAT SOURCES | 208 | no | Sufficient |

**Full text of nt-286** (exact):

```text
APPENDIX E — THREAT EVENTS
REPRESENTATIVE THREAT EVENTS INITIATED BY THREAT SOURCES
This appendix provides: (i) a description of potentially useful inputs to the threat event identification task; (ii) representative examples of adversarial threat events expressed as tactics, techniques, and procedures (TTPs) and non-adversarial threat events; (iii) an exemplary assessment scale for the relevance of those threat events; and (iv) templates for summarizing and documenting the results of the threat identification Task 2-2. Organizations can eliminate certain threat events from further consideration if no adversary with the necessary capability has been identified. Organizations can also modify the threat events provided to describe specific TTPs with sufficient detail and at the appropriate classification level. Organizations can use the representative threat events and predicated/expected values for the relevance of those events as a starting point with tailoring to adjust for any organization-specific conditions.
Table E-5, an output from Task 2-2, provides relevant inputs to the risk tables in Appendix I.
```

**Expected answer (from the source only):** Yes: organizations can eliminate a threat event from further consideration if no adversary with the necessary capability has been identified.

**Exact supporting passage(s):**

* `nt-286`: "Organizations can eliminate certain threat events from further consideration if no adversary with the necessary capability has been identified."

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Valid
* **Justification:** The sentence states the rule and its condition directly, with the polarity the question asks about.
* **Another chunk required?** No. Related but different rules: nt-136/nt-137 (events deemed irrelevant need no further consideration) and nt-145 (adversaries are not expected to initiate events that exceed their capability).
* **Ambiguity / missing qualification / extraction defect:** The statement sits in the introduction of Appendix E (PDF page 69, printed 'PAGE E-1'). It is a permission ('can eliminate'), not an obligation; the question's 'can' matches.

#### E4. exception

**Exact question:** When conditions have changed since the last assessment, must every task be redone?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-163 | PDF p.48 (printed 'PAGE 39') | CHAPTER THREE — THE PROCESS — CONDUCTING RISK ASSESSMENTS WITHIN ORGANIZATIONS > STEP 4: MAINTAIN THE ASSESSMENT > TASK 4-2 | 123 | no | Partially sufficient |
| nt-164 | PDF p.48 (printed 'PAGE 39') | CHAPTER THREE — THE PROCESS — CONDUCTING RISK ASSESSMENTS WITHIN ORGANIZATIONS > STEP 4: MAINTAIN THE ASSESSMENT > TASK 4-2 | 126 | no | Partially sufficient |

**Full text of nt-163** (exact):

```text
TASK 4-2: Update existing risk assessment using the results from ongoing monitoring of risk factors. Supplemental Guidance: Organizations determine the frequency and the circumstances under which risk assessments are updated. Such determinations can include, for example, the current level of risk to and/or the importance of, core organizational missions/business functions. If significant changes (as defined by organizational policies, direction, or guidance) have occurred since the risk assessment was conducted, organizations can revisit the purpose, scope, assumptions, and constraints of the assessment to determine whether all tasks in the risk assessment process need to be repeated.
```

**Full text of nt-164** (exact):

```text
Otherwise, the updates constitute subsequent risk assessments, identifying and assessing only how selected risk factors have changed, for example: (i) the identification of new threat events, vulnerabilities, predisposing conditions, undesirable consequences and/or affected assets; and (ii) the assessments of threat source characteristics (e.g., capability, intent, targeting, range of effects), likelihoods, and impacts. Organizations communicate the results of subsequent risk assessments to entities across all risk management tiers to ensure that responsible organizational officials have access to critical information needed to make ongoing risk-based decisions.
```

**Expected answer (from the source only):** Not necessarily: if significant changes have occurred, organizations revisit purpose, scope, assumptions and constraints to decide whether all tasks must be repeated; otherwise the update covers only the risk factors that changed.

**Exact supporting passage(s):**

* `nt-163`: "If significant changes (as defined by organizational policies, direction, or guidance) have occurred since the risk assessment was conducted, organizations can revisit the purpose, scope, assumptions, and constraints of the assessment to determine whether all tasks in the risk assessment process need to be repeated."
* `nt-164`: "Otherwise, the updates constitute subsequent risk assessments, identifying and assessing only how selected risk factors have changed,"

* **Evidence sufficiency (question level):** Partially sufficient
* **Label validity:** Needs review
* **Justification:** The complete answer is split across a chunk boundary: nt-163 gives the 'significant changes' branch and nt-164 begins with 'Otherwise,' and gives the other branch. Neither chunk alone is sufficient.
* **Another chunk required?** Yes: both nt-163 and nt-164 are needed.
* **Ambiguity / missing qualification / extraction defect:** Any-of scoring would credit half an answer. The question says 'conditions have changed', but the source distinguishes 'significant changes' from other changes, so the wording is slightly looser than the source. nt-164 is a continuation whose 'Otherwise' has no antecedent inside the chunk.

#### E5. exception

**Exact question:** Can the scope of a system-level assessment ignore weaknesses that come from controls the system inherits?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-105 | PDF p.34 (printed 'PAGE 25') | CHAPTER THREE — THE PROCESS — CONDUCTING RISK ASSESSMENTS WITHIN ORGANIZATIONS > STEP 1: PREPARE FOR THE ASSESSMENT > Architectural/Technology Considerations | 168 | no | Sufficient |

**Full text of nt-105** (exact):

```text
Architectural/Technology Considerations
Organizations use architectural and technology considerations to clarify the scope of the risk assessment. For example, at Tier 3, the scope of the risk assessment can be an organizational information system in its environment of operations. This entails placing the information system in its architectural context, so that vulnerabilities in inherited controls can be taken into consideration. Alternately, the scope of the assessment can be limited solely to the information system, without consideration of inherited vulnerabilities. At Tier 2, the scope of the risk assessment can be defined in terms of the mission/business segment architecture (e.g., including all systems, services, and infrastructures that support a specific mission/function). For a targeted risk assessment at any tier, the specific question to be answered can restrict the scope to a specific technology.
```

**Expected answer (from the source only):** Yes: the scope can be limited solely to the system without considering inherited vulnerabilities (alternatively it can place the system in its architectural context so that inherited-control vulnerabilities are considered).

**Exact supporting passage(s):**

* `nt-105`: "This entails placing the information system in its architectural context, so that vulnerabilities in inherited controls can be taken into consideration. Alternately, the scope of the assessment can be limited solely to the information system, without consideration of inherited vulnerabilities."

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Valid
* **Justification:** The chunk states both scoping options and matches the question's Tier 3 / system-level setting.
* **Another chunk required?** No. 'inherited' appears in nt-025, nt-079, nt-084, nt-085, nt-183 and nt-184, but none of them addresses the scope of an assessment.
* **Ambiguity / missing qualification / extraction defect:** The answer is a permitted option, not a rule, and the same chunk also describes the opposite option. The question's 'Yes' polarity is therefore conditional.

#### E6. exception

**Exact question:** What extra step may be needed when rolling up mission-level results in an organization whose missions differ a lot?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-076 | PDF p.27 (printed 'PAGE 18') | CHAPTER TWO — THE FUNDAMENTALS — BASIC CONCEPTS ASSOCIATED WITH RISK ASSESSMENTS > 2.4 APPLICATION OF RISK ASSESSMENTS | 182 | no | Sufficient |
| nt-077 | PDF p.27 (printed 'PAGE 18') | CHAPTER TWO — THE FUNDAMENTALS — BASIC CONCEPTS ASSOCIATED WITH RISK ASSESSMENTS > 2.4 APPLICATION OF RISK ASSESSMENTS | 93 | yes | Sufficient |

**Full text of nt-076** (exact):

```text
Organization-wide assessments of risk can be based solely on the assumptions, constraints, risk tolerances, priorities, and trade-offs established in the risk framing step (i.e., derived primarily from Tier 1 activities). However, more realistic and meaningful risk assessments are based on assessments conducted across multiple mission/business lines (i.e., derived primarily from Tier 2 activities). The ability of organizations to effectively use Tier 2 risk assessments as inputs to Tier 1 risk assessments is shaped by such considerations as: (i) the similarity of organizational missions/business functions and mission/business processes; and (ii) the degree of autonomy that organizational entities or subcomponents have with respect to parent organizations. In decentralized organizations or organizations with varied missions/business functions and/or environments of operation, expert analysis may be needed to normalize the results from Tier 2 risk assessments.
```

**Full text of nt-077** (exact):

```text
In decentralized organizations or organizations with varied missions/business functions and/or environments of operation, expert analysis may be needed to normalize the results from Tier 2 risk assessments.
Finally, risk assessments at Tier 1 take into consideration the identification of mission-essential functions from Continuity of Operations Plans (COOP) prepared by organizations when determining the contribution of Tier 2 risks. Risk assessment results at Tier 1 are communicated to organizational entities at Tier 2 and Tier 3.
```

**Expected answer (from the source only):** Expert analysis may be needed to normalize the results of the Tier 2 risk assessments.

**Exact supporting passage(s):**

* `nt-076`: "In decentralized organizations or organizations with varied missions/business functions and/or environments of operation, expert analysis may be needed to normalize the results from Tier 2 risk assessments."
* `nt-077`: "In decentralized organizations or organizations with varied missions/business functions and/or environments of operation, expert analysis may be needed to normalize the results from Tier 2 risk assessments."

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Valid
* **Justification:** Both chunks contain the complete, self-contained sentence (in nt-077 as the repeated overlap sentence), so each is independently sufficient.
* **Another chunk required?** No.
* **Ambiguity / missing qualification / extraction defect:** 'Mission-level results' and 'rolling up' are paraphrases of 'Tier 2 risk assessments' as 'inputs to Tier 1' (explained in the preceding sentences of nt-076). The same sentence is the only evidence in both gold chunks.

### Category: negation/constraint

#### N1. negation/constraint

**Exact question:** Does the guide prescribe a formula for combining semi-quantitative factor values?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-126 | PDF p.37 (printed 'PAGE 28') | CHAPTER THREE — THE PROCESS — CONDUCTING RISK ASSESSMENTS WITHIN ORGANIZATIONS > STEP 1: PREPARE FOR THE ASSESSMENT > TASK 1-5 | 186 | no | Sufficient |

**Full text of nt-126** (exact):

```text
Therefore, this guideline does not specify algorithms for combining semi-quantitative values. Organization-specific risk models include algorithms (e.g., formulas, tables, rules) for combining risk factors. If an organization-specific risk model is not provided in the risk management strategy as part of the risk framing step, then part of this task is to specify the algorithms for combining values. Algorithms for combining risk factors reflect organizational risk tolerance (see the supplemental guidance to Task 2-4 for examples). Organization-specific risk models are refined as part of preparation for a risk assessment by: (i) identifying the risk model and the rationale for using it (when multiple organization-specific risk models are provided); (ii) providing additional examples for values of risk factors; and (iii) identifying any assessment-specific algorithms (e.g., algorithms specific to the use of an attack graph analysis technique).
```

**Expected answer (from the source only):** No: the guide does not specify algorithms for combining semi-quantitative values; organization-specific risk models provide them (or the organization specifies them in the task).

**Exact supporting passage(s):**

* `nt-126`: "Therefore, this guideline does not specify algorithms for combining semi-quantitative values. Organization-specific risk models include algorithms (e.g., formulas, tables, rules) for combining risk factors."

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Valid
* **Justification:** The negation is explicit and matches the question's polarity ('prescribe a formula' vs 'does not specify algorithms').
* **Another chunk required?** No. nt-147/nt-148 give example rules for combining likelihood values (maximum, minimum, weighted average) but present them as options ('or could define a different rule'), so they do not contradict the answer.
* **Ambiguity / missing qualification / extraction defect:** The chunk opens with 'Therefore,' (the antecedent is in nt-125). Plausible lexical competitors: nt-147, nt-148.

#### N2. negation/constraint

**Exact question:** Are there fixed requirements for how formal or detailed a risk assessment has to be?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-002 | PDF p.9 (printed 'PAGE ix') | CAUTIONARY NOTES — SCOPE AND APPLICABILITY OF RISK ASSESSMENTS | 195 | no | Sufficient |

**Full text of nt-002** (exact):

```text
• There are no specific requirements with regard to: (i) the formality, rigor, or level of detail that characterizes any particular risk assessment; (ii) the methodologies, tools, and techniques used to conduct such risk assessments; or (iii) the format and content of assessment results and any associated reporting mechanisms. Organizations have maximum flexibility on how risk assessments are conducted and are encouraged to apply the guidance in this document so that the various needs of organizations can be addressed and the risk assessment activities can be integrated into broader organizational risk management processes.
• Organizations are also cautioned that risk assessments are often not precise instruments of measurement and reflect: (i) the limitations of the specific assessment methodologies, tools, and techniques employed; (ii) the subjectivity, quality, and trustworthiness of the data used; (iii) the interpretation of assessment results; and (iv) the skills and expertise of those individuals or groups conducting the assessments.
```

**Expected answer (from the source only):** No: the document states there are no specific requirements regarding the formality, rigor or level of detail of a risk assessment.

**Exact supporting passage(s):**

* `nt-002`: "There are no specific requirements with regard to: (i) the formality, rigor, or level of detail that characterizes any particular risk assessment;"

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Valid
* **Justification:** Direct statement with the polarity the question tests.
* **Another chunk required?** No.
* **Ambiguity / missing qualification / extraction defect:** The chunk comes from the front-matter 'Cautionary Notes' (PDF page 9, printed 'PAGE ix'); the heading is in nt-001, not in nt-002's text, which does not affect the answer. 'Formality' also appears in nt-094 (risk framing) without contradicting it.

#### N3. negation/constraint

**Exact question:** Is it mandatory to use the sample tables in the appendices when carrying out an assessment?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-131 | PDF p.38 (printed 'PAGE 29') | CHAPTER THREE — THE PROCESS — CONDUCTING RISK ASSESSMENTS WITHIN ORGANIZATIONS > 3.2 CONDUCTING THE RISK ASSESSMENT | 176 | no | Sufficient |

**Full text of nt-131** (exact):

```text
The specific tasks are presented in a sequential manner for clarity. However, in practice, some iteration among the tasks is both necessary and expected. Depending on the purpose of the risk assessment, organizations may find reordering the tasks advantageous. Whatever adjustments organizations make to the tasks described below, risk assessments should meet the stated purpose, scope, assumptions, and constraints established by the organizations initiating the assessments. To assist organizations in executing the individual tasks in the risk assessment process, a set of templates is provided in Appendices D through I. These appendices provide useful information for organizations in assessing risk and can also be used to record assessment results produced during essential calculations and analyses. The templates are exemplary and can be tailored by organizations in accordance with specific organizational mission/business requirements. The use of the templates is not required in order to conduct risk assessments.
```

**Expected answer (from the source only):** No: the templates are exemplary and tailorable, and their use is not required to conduct risk assessments.

**Exact supporting passage(s):**

* `nt-131`: "The templates are exemplary and can be tailored by organizations in accordance with specific organizational mission/business requirements. The use of the templates is not required in order to conduct risk assessments."

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Valid
* **Justification:** The chunk contains the explicit negation 'not required'.
* **Another chunk required?** No.
* **Ambiguity / missing qualification / extraction defect:** The question says 'sample tables'; the chunk says 'templates' (Appendices D through I). The appendices also contain assessment scales, which are not literally 'templates', but the source calls the whole set 'exemplary tables' in nt-133 and nt-137, so the mapping is reasonable.

#### N4. negation/constraint

**Exact question:** Is watching only the security posture of the information systems enough to know the organization's overall risk?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-161 | PDF p.47 (printed 'PAGE 38') | CHAPTER THREE — THE PROCESS — CONDUCTING RISK ASSESSMENTS WITHIN ORGANIZATIONS > STEP 4: MAINTAIN THE ASSESSMENT > TASK 4-1 | 190 | no | Sufficient |
| nt-162 | PDF p.47 (printed 'PAGE 38') | CHAPTER THREE — THE PROCESS — CONDUCTING RISK ASSESSMENTS WITHIN ORGANIZATIONS > STEP 4: MAINTAIN THE ASSESSMENT > TASK 4-1 | 122 | yes | Partially sufficient |

**Full text of nt-161** (exact):

```text
The objective is to maintain an ongoing situational awareness of the organizational governance structures and activities, mission/business processes, information systems, and environments of operation, and thereby all of the risk factors that may affect the risk being incurred by organizations. Therefore, in applying the risk assessment context or risk frame (i.e., scope, purpose, assumptions, constraints, risk tolerances, priorities, and trade-offs), organizations consider the part risk factors play in the risk response plan executed. For example, it is expected to be quite common for the security posture of information systems (that is, the risk factors measured within those systems) to reflect only a part of the organizational risk response, with response actions at the organization level or mission/business process level providing a significant portion of that response. In such situations, monitoring only the security posture of information systems would likely not provide sufficient information to determine the overall risk being incurred by organizations.
```

**Full text of nt-162** (exact):

```text
In such situations, monitoring only the security posture of information systems would likely not provide sufficient information to determine the overall risk being incurred by organizations.
Highly capable, well-resourced, and purpose-driven threat sources can be expected to defeat commonly available protection mechanisms (e.g., by bypassing or tampering with such mechanisms). Thus, process-level risk response measures such as reengineering mission/business processes, wise use of information technology, or the use of alternate execution processes, in the event of compromised information systems, can be major elements of organizational risk response plans.
```

**Expected answer (from the source only):** No: where organization- or process-level actions form a significant part of the risk response, monitoring only the security posture of information systems would likely not give enough information on the overall risk.

**Exact supporting passage(s):**

* `nt-161`: "For example, it is expected to be quite common for the security posture of information systems (that is, the risk factors measured within those systems) to reflect only a part of the organizational risk response, with response actions at the organization level or mission/business process level providing a significant portion of that response. In such situations, monitoring only the security posture of information systems would likely not provide sufficient information to determine the overall risk being incurred by organizations."
* `nt-162`: "In such situations, monitoring only the security posture of information systems would likely not provide sufficient information to determine the overall risk being incurred by organizations."

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Needs review
* **Justification:** nt-161 is independently sufficient. nt-162 begins with the repeated sentence whose 'such situations' has no antecedent inside the chunk.
* **Another chunk required?** No (nt-161 alone).
* **Ambiguity / missing qualification / extraction defect:** Overlap-only gold member (nt-162). The source answer is hedged ('would likely not', 'in such situations'); the question asks in general terms.

#### N5. negation/constraint

**Exact question:** Does this guidance cover systems that are designated as national security systems?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-010 | PDF p.11 (printed 'PAGE 2') | CHAPTER ONE — INTRODUCTION — THE NEED FOR RISK ASSESSMENTS TO SUPPORT ENTERPRISE-WIDE RISK MANAGEMENT > 1.1 PURPOSE AND APPLICABILITY | 151 | no | Sufficient |

**Full text of nt-010** (exact):

```text
This publication satisfies the requirements of FISMA and meets or exceeds the information security requirements established for executive agencies by the Office of Management and Budget (OMB) in Circular A-130, Appendix III, Security of Federal Automated Information Resources. The guidelines in this publication are applicable to all federal information systems other than those systems designated as national security systems as defined in 44 U.S.C., Section 3542. The guidelines have been broadly developed from a technical perspective to complement similar guidelines for national security systems and may be used for such systems with the approval of appropriate federal officials exercising policy authority over such systems. State, local, and tribal governments, as well as private sector organizations are encouraged to consider using these guidelines, as appropriate.
```

**Expected answer (from the source only):** Not by default: the guidelines apply to federal information systems other than national security systems, but may be used for them with the approval of the appropriate federal officials.

**Exact supporting passage(s):**

* `nt-010`: "The guidelines in this publication are applicable to all federal information systems other than those systems designated as national security systems as defined in 44 U.S.C., Section 3542. The guidelines have been broadly developed from a technical perspective to complement similar guidelines for national security systems and may be used for such systems with the approval of appropriate federal officials exercising policy authority over such systems."

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Valid
* **Justification:** The chunk contains both the exclusion and the conditional allowance, so the qualification that changes the answer is present.
* **Another chunk required?** No. The glossary entry 'National Security System' (nt-227) defines the term but says nothing about coverage; nt-252 mentions national security systems only in the categorization entry.
* **Ambiguity / missing qualification / extraction defect:** Yes/no polarity is conditional ('cover' is answered 'no, unless approved'). A strong lexical competitor exists in the glossary entry nt-227.

#### N6. negation/constraint

**Exact question:** Should we expect an adversary to attack an organization it is not actively targeting?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-145 | PDF p.42 (printed 'PAGE 33') | CHAPTER THREE — THE PROCESS — CONDUCTING RISK ASSESSMENTS WITHIN ORGANIZATIONS > STEP 2: CONDUCT THE ASSESSMENT > TASK 2-4 | 199 | no | Sufficient |

**Full text of nt-145** (exact):

```text
Organizations assess the likelihood of threat event initiation by taking into consideration the characteristics of the threat sources of concern including capability, intent, and targeting (see Task 2-1 and Appendix D). If threat events require more capability than adversaries possess (and adversaries are cognizant of this fact), then the adversaries are not expected to initiate the events. If adversaries do not expect to achieve intended objectives by executing threat events, then the adversaries are not expected to initiate the events. And finally, if adversaries are not actively targeting specific organizations or their missions/business functions, adversaries are not expected to initiate threat events. Organizations use the assessment scale in Table G-2 and provide a rationale for the assessment allowing explicit consideration of deterrence and threat shifting. Organizations can assess the likelihood of threat event occurrence (non-adversarial) using Table G-3 and provide a similar rationale for the assessment.
```

**Expected answer (from the source only):** No: if adversaries are not actively targeting an organization or its missions/business functions, they are not expected to initiate threat events against it.

**Exact supporting passage(s):**

* `nt-145`: "And finally, if adversaries are not actively targeting specific organizations or their missions/business functions, adversaries are not expected to initiate threat events."

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Valid
* **Justification:** The sentence states the condition and the negative expectation directly.
* **Another chunk required?** No. nt-042 lists targeting as a determinant of likelihood, without this statement.
* **Ambiguity / missing qualification / extraction defect:** 'Attack' in the question corresponds to 'initiate threat events' in the source. The relevant sentence is in the middle of a 199-token chunk.

### Category: other (buried detail)

#### O1. other (buried detail)

**Exact question:** What are the four components of the risk management process?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-018 | PDF p.13 (printed 'PAGE 4') | CHAPTER TWO — THE FUNDAMENTALS — BASIC CONCEPTS ASSOCIATED WITH RISK ASSESSMENTS > 2.1 RISK MANAGEMENT PROCESS | 112 | no | Sufficient |
| nt-244 | PDF p.60 (printed 'PAGE B-10') | APPENDIX B — GLOSSARY — COMMON TERMS AND DEFINITIONS > Risk Management | 97 | no | Sufficient |

**Full text of nt-018** (exact):

```text
2.1 RISK MANAGEMENT PROCESS
Risk assessment is a key component of a holistic, organization-wide risk management process as defined in NIST Special Publication 800-39, Managing Information Security Risk: Organization, Mission, and Information System View. Risk management processes include: (i) framing risk; (ii) assessing risk; (iii) responding to risk; and (iv) monitoring risk. Figure 1 illustrates the four steps in the risk management process—including the risk assessment step and the information and communications flows necessary to make the process work effectively.
```

**Full text of nt-244** (exact):

```text
Risk Management
The program and supporting processes to manage information security risk to organizational operations (including mission, functions, image, reputation), organizational assets, individuals, other organizations, and the Nation, and includes: (i) establishing the context for risk-related activities; (ii) assessing risk; (iii) responding to risk once determined; and (iv) monitoring risk over time. [NIST SP 800-39] [CNSSI No. 4009, adapted]
```

**Expected answer (from the source only):** Framing risk, assessing risk, responding to risk, and monitoring risk.

**Exact supporting passage(s):**

* `nt-018`: "Risk management processes include: (i) framing risk; (ii) assessing risk; (iii) responding to risk; and (iv) monitoring risk."
* `nt-244`: "includes: (i) establishing the context for risk-related activities; (ii) assessing risk; (iii) responding to risk once determined; and (iv) monitoring risk over time."

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Valid
* **Justification:** Both chunks independently list the four components. nt-244 is a glossary definition of 'risk management' (a program and its processes) rather than 'the risk management process', and names the first component 'establishing the context' instead of 'framing'.
* **Another chunk required?** No. nt-019 to nt-022 describe each component separately (partial).
* **Ambiguity / missing qualification / extraction defect:** The two gold chunks use different names for the first component; a correct answer from nt-244 will not use the word 'framing'.

#### O2. other (buried detail)

**Exact question:** What example score ranges does the guide give for binning semi-quantitative values?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-061 | PDF p.23 (printed 'PAGE 14') | CHAPTER TWO — THE FUNDAMENTALS — BASIC CONCEPTS ASSOCIATED WITH RISK ASSESSMENTS > 2.3 KEY RISK CONCEPTS > Uncertainty | 182 | no | Sufficient |

**Full text of nt-061** (exact):

```text
Finally, semi-quantitative assessments typically employ a set of methods, principles, or rules for assessing risk that uses bins, scales, or representative numbers whose values and meanings are not maintained in other contexts. This type of assessment can provide the benefits of quantitative and qualitative assessments. The bins (e.g., 0-15, 16-35, 36-70, 71-85, 86-100) or scales (e.g., 1-10) translate easily into qualitative terms that support risk communications for decision makers (e.g., a score of 95 can be interpreted as very high), while also allowing relative comparisons between values in different bins or even within the same bin (e.g., the difference between risks scored 70 and 71 respectively is relatively insignificant, while the difference between risks scored 36 and 70 is relatively significant).
```

**Expected answer (from the source only):** Example bins of 0-15, 16-35, 36-70, 71-85 and 86-100 (or scales such as 1-10).

**Exact supporting passage(s):**

* `nt-061`: "The bins (e.g., 0-15, 16-35, 36-70, 71-85, 86-100) or scales (e.g., 1-10) translate easily into qualitative terms"

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Needs review
* **Justification:** Within the frozen corpus nt-061 is the only chunk that gives example bins, and it contains them in full.
* **Another chunk required?** No within the corpus. However, the PDF's excluded appendix tables give a different set of semi-quantitative bins (for example 'Very High 96-100', 'High 80-95', 'Moderate 21-79', verified on PDF page 67).
* **Ambiguity / missing qualification / extraction defect:** Ambiguity: the guide gives more than one set of example ranges, and the question does not say which. The label is correct for the in-scope narrative text, but a grader reading the whole PDF could expect either set. nt-125 mentions '(0-100)' without bins.

#### O3. other (buried detail)

**Exact question:** Which external organizations does the guide name as sources of threat information?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-121 | PDF p.36 (printed 'PAGE 27') | CHAPTER THREE — THE PROCESS — CONDUCTING RISK ASSESSMENTS WITHIN ORGANIZATIONS > STEP 1: PREPARE FOR THE ASSESSMENT > TASK 1-4 | 186 | no | Partially sufficient |
| nt-122 | PDF p.37 (printed 'PAGE 28') | CHAPTER THREE — THE PROCESS — CONDUCTING RISK ASSESSMENTS WITHIN ORGANIZATIONS > STEP 1: PREPARE FOR THE ASSESSMENT > TASK 1-4 | 177 | no | Partially sufficient |

**Full text of nt-121** (exact):

```text
Sources of information as described in Tables D-1, E-1, F-1, H-1, and I-1 can be either internal or external to organizations. Internal sources of information that can provide insights into both threats and vulnerabilities can include, for example, risk assessment reports, incident reports, security logs, trouble tickets, and monitoring results. Note that internally, information from risk assessment reports at one tier can serve as input to risk assessments at other tiers. Mission/business owners are encouraged to identify not only common infrastructure and/or support services they depend on, but also those they might use under specific operational circumstances. External sources of threat information can include cross-community organizations (e.g., US Computer Emergency Readiness Team [US-CERT], sector partners (e.g., Defense Industrial Base [DIB] using the DoD-Defense Industrial Base Collaborative Information
```

**Full text of nt-122** (exact):

```text
Sharing Environment [DCISE], Information Sharing and Analysis Centers [ISACs] for critical infrastructure sectors), research and nongovernmental organizations (e.g. Carnegie Mellon University, Software Engineering Institute-CERT), and security service providers). Organizations using external sources, consider the timeliness, specificity, and relevance of threat information. Similar to sources of threat information, sources of vulnerability information can also be either internal or external to organizations (see Table F-1). Internal sources can include, for example, vulnerability assessment reports. External sources of vulnerability information are similar to the sources identified above for threat information. As described in Table F-1, information about predisposing conditions can be found in a variety of sources including, for example, descriptions of information systems, environments of operation, shared services, common infrastructures, and enterprise architecture.
```

**Expected answer (from the source only):** US-CERT; sector partners such as the DoD Defense Industrial Base Collaborative Information Sharing Environment (DCISE) and the ISACs for critical infrastructure sectors; research and non-governmental organizations such as Carnegie Mellon's Software Engineering Institute-CERT; and security service providers.

**Exact supporting passage(s):**

* `nt-121`: "External sources of threat information can include cross-community organizations (e.g., US Computer Emergency Readiness Team [US-CERT], sector partners (e.g., Defense Industrial Base [DIB] using the DoD-Defense Industrial Base Collaborative Information"
* `nt-122`: "Sharing Environment [DCISE], Information Sharing and Analysis Centers [ISACs] for critical infrastructure sectors), research and nongovernmental organizations (e.g. Carnegie Mellon University, Software Engineering Institute-CERT), and security service providers)."

* **Evidence sufficiency (question level):** Partially sufficient
* **Label validity:** Needs review
* **Justification:** One sentence is split mid-phrase across the two chunks ('...Collaborative Information' / 'Sharing Environment [DCISE]...'). Neither chunk alone has the full list.
* **Another chunk required?** Yes: both nt-121 and nt-122 are needed.
* **Ambiguity / missing qualification / extraction defect:** EXTRACTION DEFECT: the sentence crosses a PDF page break (pages 36 to 37); the continuation starts with a capital letter, so my stitching rule (which only joined lowercase continuations) left it unjoined, and the chunker kept the two pieces as separate blocks. Any-of scoring would credit half the list.

#### O4. other (buried detail)

**Exact question:** At what point in the system development life cycle should an initial risk assessment ideally be performed?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-080 | PDF p.28 (printed 'PAGE 19') | CHAPTER TWO — THE FUNDAMENTALS — BASIC CONCEPTS ASSOCIATED WITH RISK ASSESSMENTS > 2.4 APPLICATION OF RISK ASSESSMENTS | 186 | no | Sufficient |

**Full text of nt-080** (exact):

```text
The Tier 2 context and the system development life cycle determine the purpose and define the scope of risk assessment activities at Tier 3. While initial risk assessments (i.e., risk assessments performed for the first time, rather than updating prior risk assessments) can be performed at any phase in the system development life cycle, ideally these assessments should be performed in the Initiation phase. In the Initiation phase, risk assessments evaluate the anticipated vulnerabilities and predisposing conditions affecting the confidentiality, integrity, and availability of information systems in the context of the planned environments of operation. Such assessments inform risk response, enabling information system owners/program managers, together with mission/business owners to make the final decisions about the security controls necessary based on the security categorization and the environment of operation. Risk assessments are also conducted at later phases in the system development life cycle, updating risk assessment results from earlier phases.
```

**Expected answer (from the source only):** Ideally in the Initiation phase (although initial assessments can be performed at any phase).

**Exact supporting passage(s):**

* `nt-080`: "While initial risk assessments (i.e., risk assessments performed for the first time, rather than updating prior risk assessments) can be performed at any phase in the system development life cycle, ideally these assessments should be performed in the Initiation phase."

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Valid
* **Justification:** The sentence gives the answer together with its 'can be performed at any phase' qualification.
* **Another chunk required?** No. nt-023, nt-081 and nt-082 discuss later phases and ongoing assessment without contradicting it.
* **Ambiguity / missing qualification / extraction defect:** The passage is in the Tier 3 discussion, which the question does not mention; the claim is stated for initial assessments in general.

#### O5. other (buried detail)

**Exact question:** What should the executive summary of a risk assessment report say about the overall level of risk?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-301 | PDF p.92 (printed 'PAGE K-1') | APPENDIX K — RISK ASSESSMENT REPORTS — ESSENTIAL ELEMENTS OF INFORMATION > Executive Summary | 85 | yes | Partially sufficient |

**Full text of nt-301** (exact):

```text
If a subsequent risk assessment, state the circumstances that prompted the update and include a reference to the previous Risk Assessment Report.
• Describe the overall level of risk (e.g., Very Low, Low, Moderate, High, or Very High).
• List the number of risks identified for each level of risk (e.g., Very Low, Low, Moderate, High, or Very High).
```

**Expected answer (from the source only):** It should describe the overall level of risk (e.g., Very Low, Low, Moderate, High or Very High) and list the number of risks identified at each level.

**Exact supporting passage(s):**

* `nt-301`: "Describe the overall level of risk (e.g., Very Low, Low, Moderate, High, or Very High)."
* `nt-301`: "List the number of risks identified for each level of risk (e.g., Very Low, Low, Moderate, High, or Very High)."

* **Evidence sufficiency (question level):** Partially sufficient
* **Label validity:** Needs review
* **Justification:** The requested fact is present in full, but nothing in nt-301's text says these bullets belong to the executive summary: the heading 'Executive Summary' is in nt-300, and nt-301 begins with a repeated sentence from the previous bullet.
* **Another chunk required?** Yes, for the scoping: nt-300 (contains the 'Executive Summary' heading and the earlier bullets). The fact itself needs only nt-301.
* **Ambiguity / missing qualification / extraction defect:** The section label that makes this an 'executive summary' answer exists only in metadata, which neither the Bi-Encoder nor the LLM sees. Chunk-boundary defect, not an extraction error.

#### O6. other (buried detail)

**Exact question:** How many assessment scales does the guide provide for each risk factor, and of what kinds?

| Gold chunk | Page | Section (chunk metadata) | Tokens | Starts with overlap sentence | Sufficiency of this chunk |
|---|---|---|---|---|---|
| nt-125 | PDF p.37 (printed 'PAGE 28') | CHAPTER THREE — THE PROCESS — CONDUCTING RISK ASSESSMENTS WITHIN ORGANIZATIONS > STEP 1: PREPARE FOR THE ASSESSMENT > TASK 1-5 | 192 | no | Sufficient |

**Full text of nt-125** (exact):

```text
For each assessable risk factor, the appendices include three assessment scales (one qualitative and two semi-quantitative scales) with correspondingly different representations. Organizations typically define (or select and tailor from the appendices) the assessment scales to be used in their risk assessments, annotating with organizationally-meaningful examples for specific values and defining break points between bins for semi-quantitative approaches. In addition, mission/business owners can provide further annotations with mission/business-specific examples. Organizations can identify different assessment scales to be used in different circumstances. For example, for low-impact information systems, organizations could use qualitative values, while for moderate- and high-impact systems, the most granular semi-quantitative values (0-100) could be used. As discussed in Special Publication 800-39, Task 1-1, Risk Assumptions, organizations vary in the relative weights applied to risk factors.
```

**Expected answer (from the source only):** Three scales per assessable risk factor: one qualitative and two semi-quantitative.

**Exact supporting passage(s):**

* `nt-125`: "For each assessable risk factor, the appendices include three assessment scales (one qualitative and two semi-quantitative scales) with correspondingly different representations."

* **Evidence sufficiency (question level):** Sufficient
* **Label validity:** Valid
* **Justification:** The count and the kinds are stated explicitly in one sentence.
* **Another chunk required?** No.
* **Ambiguity / missing qualification / extraction defect:** The scales themselves are in the appendix tables, which are outside the corpus scope; the narrative statement is sufficient to answer.

---
*Method note.* Alternative answer-bearing chunks were located by literal string search over the frozen text (no embeddings), then read. A search can miss a paraphrase, so the 'another chunk' lists are what I found, not a proof of completeness.
