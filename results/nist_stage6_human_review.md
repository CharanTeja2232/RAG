# Human-review sheet: Answer 1 (baseline Top 3) vs Answer 2 (re-ranked Top 3)

Model `qwen/qwen3.8-27b` via groq; identical prompt and parameters for both answers (settings sha256 `fc869685494b2d61...`). Retrieval files pinned: baseline `c697c05d6430...`, re-ranked `1282c5190017...`.

**How to read it.** *Frozen retrieval outcome* is the preregistered Stage 4/5 result and is not changed by anything here. *Objective checks* only test format and consistency (does the answer cite a passage it was given, is it the refusal sentence, was it cut off, does it respect the three-sentence limit). **They are not proof that an answer is factually correct.** Judge correctness yourself against the passages shown; the grading fields are blank.

## Grading legend (applies to every query)

*Key status: DRAFT expected-answer key for human grading; review it before you start and do not change it after you have seen an answer.* Guide sha256 `156cd5480b7febad...`. Authored by the AI assistant (the same author as the questions, the gold labels and overlay v1.1): the key is therefore NOT an independent validation.

| CSV field (Answer 1 / Answer 2) | allowed values | judged against |
|---|---|---|
| `a1_correct` / `a2_correct` | correct / partially correct / incorrect | the expected answer in this key (derived from the frozen source), independent of which passages the model was shown |
| `a1_supported_by_passages` / `a2_supported_by_passages` | fully supported / partially supported / unsupported | the passages shown to THAT answer (listed in the sheet), not the whole NIST publication |
| `a1_complete` / `a2_complete` | complete / incomplete | the required points of this key; complete = every point marked required (and the qualification where qualification_affects is 'completeness') is present |
| `a1_unsupported_claims` / `a2_unsupported_claims` | none / present (+ details in `*_unsupported_claims_notes`) | 'present' = at least one substantive claim that is neither stated in nor directly entailed by the shown passages (see unsupported_claim_examples per query); describe it in the notes field. A citation to the wrong passage does not by itself make a claim unsupported: judge the claim against the shown passages. |
| `a1_overall_judgment` / `a2_overall_judgment` (+ `*_justification`) | acceptable / borderline / unacceptable | acceptable = correct, fully supported, no unsupported claims; unacceptable = incorrect or unsupported; borderline = everything else. Add a one-sentence justification. |
| `better` | A1 better / A2 better / neither clearly better | judged on the combination of correctness, evidence support and completeness, not on length or style; objective citation checks must not decide it |

**Conventions:**
* Refusal convention: the exact refusal sentence makes no factual claim, so unsupported_claims = none and evidence_support = fully supported; correctness = incorrect (the expected answer is missing) and completeness = incomplete. Apply the same convention to every refusal.
* Grade against this key, not against the other answer. Do not use the objective citation checks (cites a gold chunk, only supplied passages, refusal sentence, sentence count) as evidence of correctness.
* Retrieval success (lenient/strict outcome, ranks), the objective format checks and your human grades are three separate metrics; never merge them.
* If you disagree with an item of this key, do not edit it while grading: record the disagreement in reviewer_notes and decide afterwards whether to issue a dated key v1.1.
* The one-line 'Your grading (blank)' prompt under each query is the ORIGINAL free-text prompt and is kept unchanged. In the CSV use the vocabulary of this legend (for `better`: 'A1 better' / 'A2 better' / 'neither clearly better').
* O2 and O3 carry scope decisions from overlay v1.1 (see their grader_notes).

---

## A1  (keyword trap)

**Question:** Which risk assessment orientation begins with the consequences we care about and our most critical assets, rather than with attackers or weaknesses?

**Preregistered gold chunk(s):** nt-063

**Preregistered evidence phrase(s):**
> an asset/impact-oriented approach starts with the identification of impacts or consequences of concern and critical assets

**Frozen retrieval outcome:** lenient success -> success (best gold rank 3 -> 2; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-064 | yes (rank 1) | yes (rank 1, was 1) |  |  |
| nt-020 | yes (rank 2) | no (re-ranked rank 6) |  |  |
| nt-063 | yes (rank 3) | yes (rank 2, was 3) | GOLD | strict-single |
| nt-238 | no (was rank 7) | yes (rank 3, was 7) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-064** (PDF page 24)
> A vulnerability-oriented approach starts with a set of predisposing conditions or exploitable weaknesses/deficiencies in organizational information systems or the environments in which the systems operate, and identifies threat events that could exercise those vulnerabilities together with possible consequences of vulnerabilities being exercised. Each analysis approach takes into consideration the same risk factors, and thus entails the same set of risk assessment activities, albeit in different order. Differences in the starting point of the risk assessment can potentially bias the results, causing some risks not to be identified. Therefore, identification of risks from a second orientation (e.g., complementing a threat-oriented analysis approach with an asset/impact-oriented analysis approach) can improve the rigor and effectiveness of the analysis.
>
> **nt-020** (PDF page 13)
> The risk management strategy establishes a foundation for managing risk and delineates the boundaries for risk-based decisions within organizations.
> The second component of risk management addresses how organizations assess risk within the context of the organizational risk frame. The purpose of the risk assessment component is to identify: (i) threats to organizations (i.e., operations, assets, or individuals) or threats directed through organizations against other organizations or the Nation; (ii) vulnerabilities internal and external to organizations; (iii) the harm (i.e., adverse impact) that may occur given the potential for threats exploiting vulnerabilities; and (iv) the likelihood that harm will occur. The end result is a determination of risk (i.e., typically a function of the degree of harm and likelihood of harm occurring).
>
> **nt-063** (PDF page 23)
> For example, organizations can associate a specific time period with assessments of likelihood of occurrence and assessments of impact severity.
> Analysis approaches differ with respect to the orientation or starting point of the risk assessment, level of detail in the assessment, and how risks due to similar threat scenarios are treated. An analysis approach can be: (i) threat-oriented; (ii) asset/impact-oriented; or (iii) vulnerability-oriented. A threat-oriented approach starts with the identification of threat sources and threat events, and focuses on the development of threat scenarios; vulnerabilities are identified in the context of threats, and for adversarial threats, impacts are identified based on adversary intent. An asset/impact-oriented approach starts with the identification of impacts or consequences of concern and critical assets, possibly using the results of a mission or business impact analyses and identifying threat events that could lead to and/or threat sources that could seek those impacts or consequences.
>
> **nt-238** (PDF page 59)
> Risk Assessment
> The process of identifying, estimating, and prioritizing risks to organizational operations (including mission, functions, image, reputation), organizational assets, individuals, other organizations, and the Nation, resulting from the operation of an information system. Part of risk management, incorporates threat and vulnerability analyses, and considers mitigations provided by security controls planned or in place. Synonymous with risk analysis. [NIST SP 800-39]
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** The asset/impact-oriented approach (it starts from the impacts or consequences of concern and the critical assets).
* **Expected polarity:** n/a (names an approach)  |  type: term
* **Required points:** (1) Names the asset/impact-oriented approach.
* **Must it mention an exception / qualification / negation?** no
* **Acceptable wording:** 'impact-oriented', 'asset-oriented' or 'asset/impact-oriented'; a description of starting from consequences/critical assets without the name also counts.
* **Would count as an unsupported claim / error:** (1) Naming the threat-oriented or the vulnerability-oriented approach as the answer. (2) Saying it starts from threat sources, adversary intent or weaknesses.
* **Supporting passages:** `nt-063`: "An asset/impact-oriented approach starts with the identification of impacts or consequences of concern and critical assets"
* **Grader notes:** The source lists three approaches (threat-, asset/impact-, vulnerability-oriented); the question excludes the first and last.

**Answer 1 (baseline)**  | context order: nt-064, nt-020, nt-063

> The asset/impact-oriented approach begins with the identification of impacts or consequences of concern and critical assets. [nt-063]

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.2929 s; tokens in/out 655/28

**Answer 2 (re-ranked)**  | context order: nt-064, nt-063, nt-238

> The asset/impact-oriented approach begins with the identification of impacts or consequences of concern and critical assets. [nt-063]

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.2787 s; tokens in/out 592/28

**Answers textually identical:** yes

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## A2  (keyword trap)

**Question:** Which term describes different experts arriving at the same results from the same data?

**Preregistered gold chunk(s):** nt-235

**Preregistered evidence phrase(s):**
> the ability of different experts to produce the same results from the same data

**Frozen retrieval outcome:** lenient success -> success (best gold rank 1 -> 1; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-235 | yes (rank 1) | yes (rank 1, was 1) | GOLD | strict-single |
| nt-059 | yes (rank 2) | yes (rank 3, was 2) |  |  |
| nt-062 | yes (rank 3) | no (re-ranked rank 7) |  |  |
| nt-060 | no (was rank 6) | yes (rank 2, was 6) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-235** (PDF page 59)
> Reproducibility
> The ability of different experts to produce the same results from the same data.
>
> **nt-059** (PDF page 23)
> However, the meaning of the quantitative results may not always be clear and may require interpretation and explanation—particularly to explain the assumptions and constraints on using the results.
> For example, organizations may typically ask if the numbers or results obtained in the risk assessments are reliable or if the differences in the obtained values are meaningful or insignificant. Additionally, the rigor of quantification is significantly lessened when subjective determinations are buried within the quantitative assessments, or when significant uncertainty surrounds the determination of values. The benefits of quantitative assessments (in terms of the rigor, repeatability, and reproducibility of assessment results) can, in some cases, be outweighed by the costs (in terms of the expert time and effort and the possible deployment and use of tools required to make such assessments).
>
> **nt-062** (PDF page 23)
> The role of expert judgment in assigning values is more evident than in a purely quantitative approach. Moreover, if the scales or sets of bins provide sufficient granularity, relative prioritization among results is better supported than in a purely qualitative approach. As in a quantitative approach, rigor is significantly lessened when subjective determinations are buried within assessments, or when significant uncertainty surrounds a determination of value. As with the nonnumeric categories or levels used in a well-founded qualitative approach, each bin or range of values needs to be clearly defined and/or characterized by meaningful examples.
> Independent of the type of value scale selected, assessments make explicit the temporal element of risk factors. For example, organizations can associate a specific time period with assessments of likelihood of occurrence and assessments of impact severity.
>
> **nt-060** (PDF page 23)
> In contrast to quantitative assessments, qualitative assessments typically employ a set of methods, principles, or rules for assessing risk based on nonnumerical categories or levels (e.g., very low, low, moderate, high, very high). This type of assessment supports communicating risk results to decision makers. However, the range of values in qualitative assessments is comparatively small in most cases, making the relative prioritization or comparison within the set of reported risks difficult. Additionally, unless each value is very clearly defined or is characterized by meaningful examples, different experts relying on their individual experiences could produce significantly different assessment results. The repeatability and reproducibility of qualitative assessments are increased by the annotation of assessed values (e.g., this value is high because of the following reasons) and by the use of tables or other well-defined functions to combine qualitative values.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** Reproducibility.
* **Expected polarity:** n/a (names a term)  |  type: term
* **Required points:** (1) Names 'reproducibility'.
* **Must it mention an exception / qualification / negation?** no
* **Acceptable wording:** Only the term 'reproducibility'.
* **Would count as an unsupported claim / error:** (1) Naming 'repeatability' (the glossary entry 'Repeatability' means the ability to repeat an assessment in the future: a different term). (2) Naming any other term (e.g. 'validity', 'consistency') as the NIST term.
* **Supporting passages:** `nt-235`: "The ability of different experts to produce the same results from the same data."
* **Grader notes:** True competitor: the glossary entry 'Repeatability' (nt-234).

**Answer 1 (baseline)**  | context order: nt-235, nt-059, nt-062

> The term that describes the ability of different experts to produce the same results from the same data is reproducibility [nt-235].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.3137 s; tokens in/out 498/29

**Answer 2 (re-ranked)**  | context order: nt-235, nt-060, nt-059

> The term that describes different experts arriving at the same results from the same data is reproducibility [nt-235].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.2673 s; tokens in/out 513/26

**Answers textually identical:** no

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## A3  (keyword trap)

**Question:** What do you call a safeguard used in place of a recommended baseline control that still gives comparable protection?

**Preregistered gold chunk(s):** nt-185

**Preregistered evidence phrase(s):**
> employed by an organization in lieu of a recommended security control

**Frozen retrieval outcome:** lenient success -> success (best gold rank 1 -> 1; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-185 | yes (rank 1) | yes (rank 1, was 1) | GOLD | strict-single |
| nt-275 | yes (rank 2) | no (re-ranked rank 4) |  |  |
| nt-270 | yes (rank 3) | no (re-ranked rank 6) |  |  |
| nt-258 | no (was rank 10) | yes (rank 2, was 10) |  |  |
| nt-255 | no (was rank 5) | yes (rank 3, was 5) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-185** (PDF page 53)
> Compensating Security Control
> A management, operational, and/or technical control (i.e., safeguard or countermeasure) employed by an organization in lieu of a recommended security control in the low, moderate, or high baselines that provides equivalent or comparable protection for an information system. [CNSSI No. 4009]
>
> **nt-275** (PDF page 63)
> Tailored Security Control Baseline
> A set of security controls resulting from the application of tailoring guidance to the security control baseline. See Tailoring. [NIST SP 800-39]
>
> **nt-270** (PDF page 62)
> Supplementation (Security Controls)
> The process of adding security controls or control enhancements to a security control baseline from NIST Special Publication 800-53 or CNSSI No. 1253 in order to adequately meet the organization’s risk management needs. [NIST SP 800-39]
>
> **nt-258** (PDF page 61)
> Security Controls
> The management, operational, and technical controls (i.e., safeguards or countermeasures) prescribed for an information system to protect the confidentiality, integrity, and availability of the system and its information. [FIPS 199, CNSSI No. 4009]
>
> **nt-255** (PDF page 61)
> Security Control Baseline
> The set of minimum security controls defined for a low- impact, moderate-impact, or high-impact information system. A set of information security controls that has been established through information security strategic planning activities to address one or more specified security categorizations; this set of security controls is intended to be the initial security control set selected for a specific system once that system’s security categorization is determined. [CNSSI No. 4009] [CNSSI No. 1253]
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** A compensating security control.
* **Expected polarity:** n/a (names a term)  |  type: term
* **Required points:** (1) Names a 'compensating security control' (compensating control).
* **Must it mention an exception / qualification / negation?** no
* **Acceptable wording:** 'compensating control' / 'compensating security control'.
* **Would count as an unsupported claim / error:** (1) Naming a different kind of control (e.g. 'supplemental', 'tailored', 'common' or 'inherited' control). (2) Adding requirements not in the passage (e.g. that an auditor must approve it).
* **Supporting passages:** `nt-185`: "employed by an organization in lieu of a recommended security control in the low, moderate, or high baselines that provides equivalent or comparable protection for an information system"

**Answer 1 (baseline)**  | context order: nt-185, nt-275, nt-270

> It is called a Compensating Security Control. [nt-185]

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.2764 s; tokens in/out 353/18

**Answer 2 (re-ranked)**  | context order: nt-185, nt-258, nt-255

> It is called a Compensating Security Control. [nt-185]

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.2379 s; tokens in/out 410/18

**Answers textually identical:** yes

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## A4  (keyword trap)

**Question:** Can something about an organization's environment, such as a system with no outside network connection, make a successful attack less likely?

**Preregistered gold chunk(s):** nt-040

**Preregistered evidence phrase(s):**
> stand-alone information system with no external network connectivity

**Frozen retrieval outcome:** lenient stumble -> success (best gold rank 6 -> 1; RESTORED into Top 3); strict stumble -> success (Top-3 evidence none -> sufficient; RESTORED into Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-277 | yes (rank 1) | no (re-ranked rank 6) |  |  |
| nt-038 | yes (rank 2) | no (re-ranked rank 7) |  |  |
| nt-283 | yes (rank 3) | no (re-ranked rank 10) |  |  |
| nt-040 | no (was rank 6) | yes (rank 1, was 6) | GOLD | strict-single |
| nt-041 | no (was rank 8) | yes (rank 2, was 8) |  |  |
| nt-043 | no (was rank 10) | yes (rank 3, was 10) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-277** (PDF page 63)
> Threat
> Any circumstance or event with the potential to adversely impact organizational operations (including mission, functions, image, or reputation), organizational assets, individuals, other organizations, or the Nation through an information system via unauthorized access, destruction, disclosure, or modification of information, and/or denial of service. [CNSSI No.4009]
>
> **nt-038** (PDF page 18)
> Vulnerabilities are not identified only within information systems. Viewing information systems in a broader context, vulnerabilities can be found in organizational governance structures (e.g., the lack of effective risk management strategies and adequate risk framing, poor intra-agency communications, inconsistent decisions about relative priorities of missions/business functions, or misalignment of enterprise architecture to support mission/business activities). Vulnerabilities can also be found in external relationships (e.g., dependencies on particular energy sources, supply chains, information technologies, and telecommunications providers), mission/business processes (e.g., poorly defined processes or processes that are not risk-aware), and enterprise/information security architectures (e.g., poor architectural decisions resulting in lack of diversity or resiliency in organizational information systems).
>
> **nt-283** (PDF page 63)
> Vulnerability
> Weakness in an information system, system security procedures, internal controls, or implementation that could be exploited by a threat source. [CNSSI No. 4009]
>
> **nt-040** (PDF page 19)
> In addition, a threat scenario tells a story, and hence is useful for risk communication as well as for analysis.
> In addition to vulnerabilities as described above, organizations also consider predisposing conditions. A predisposing condition is a condition that exists within an organization, a mission or business process, enterprise architecture, information system, or environment of operation, which affects (i.e., increases or decreases) the likelihood that threat events, once initiated, result in adverse impacts to organizational operations and assets, individuals, other organizations, or the Nation. Predisposing conditions include, for example, the location of a facility in a hurricane- or flood-prone region (increasing the likelihood of exposure to hurricanes or floods) or a stand-alone information system with no external network connectivity (decreasing the likelihood of exposure to a network-based cyber attack).
>
> **nt-041** (PDF page 19)
> Vulnerabilities resulting from predisposing conditions that cannot be easily corrected could include, for example, gaps in contingency plans, use of outdated technologies, or weaknesses/deficiencies in information system backup and failover mechanisms. In all cases, these types of vulnerabilities create a predisposition toward threat events having adverse impacts on organizations. Vulnerabilities (including those attributed to predisposing conditions) are part of the overall security posture of organizational information systems and environments of operation that can affect the likelihood of occurrence of a threat event.
>
> **nt-043** (PDF page 19)
> If a threat event is almost certain to be initiated or occur in the (specified or implicit) time frame, the risk assessment may take into consideration the estimated frequency of the event. The likelihood of threat occurrence can also be based on the state of the organization (including for example, its core mission/business processes, enterprise architecture, information security architecture, information systems, and environments in which those systems operate)—taking into consideration predisposing conditions and the presence and effectiveness of deployed security controls to protect against unauthorized/undesirable behavior, detect and limit damage, and/or maintain or restore mission/business capabilities. The likelihood of impact addresses the probability (or possibility) that the threat event will result in an adverse impact, regardless of the magnitude of harm that can be expected.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** Yes: a predisposing condition such as a stand-alone information system with no external network connectivity decreases the likelihood of exposure to a network-based cyber attack.
* **Expected polarity:** Yes  |  type: yes/no
* **Required points:** (1) Answers yes. (2) Identifies the isolated / no-external-network system as a predisposing condition (or equivalent environmental condition) that lowers the likelihood of attack exposure.
* **Must it mention an exception / qualification / negation?** yes: qualification: The effect is a DECREASE in likelihood of exposure to a NETWORK-BASED attack, not elimination of attack risk. (affects correctness)
* **Acceptable wording:** 'less likely', 'decreases the likelihood', 'reduces exposure'.
* **Would count as an unsupported claim / error:** (1) Claiming the isolated system is immune to attack or that attacks become impossible. (2) Claiming it lowers the likelihood of every kind of attack (the source says network-based). (3) Presenting it as a security control rather than a predisposing condition, with details not in the passage.
* **Supporting passages:** `nt-040`: "a stand-alone information system with no external network connectivity (decreasing the likelihood of exposure to a network-based cyber attack)"
* **Grader notes:** The question says 'a successful attack less likely', slightly broader than the source's 'exposure to a network-based cyber attack'; an answer that says 'yes, network-based attacks' is fully correct.

**Answer 1 (baseline)**  | context order: nt-277, nt-038, nt-283

> The provided context does not contain the answer.

*Objective checks (format only):* cites a passage: False; only supplied passages: False; cites a gold chunk: False; refusal sentence: True; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.2211 s; tokens in/out 437/10

**Answer 2 (re-ranked)**  | context order: nt-040, nt-041, nt-043

> Yes, a predisposing condition such as a stand-alone information system with no external network connectivity can decrease the likelihood of exposure to a network-based cyber attack [nt-040].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.2963 s; tokens in/out 602/38

**Answers textually identical:** no

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## A5  (keyword trap)

**Question:** How is the chance that an event actually causes harm different from the chance that someone starts it?

**Preregistered gold chunk(s):** nt-043, nt-044

**Preregistered evidence phrase(s):**
> regardless of the magnitude of harm that can be expected

**Frozen retrieval outcome:** lenient success -> success (best gold rank 2 -> 1; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-279 | yes (rank 1) | no (re-ranked rank 5) |  |  |
| nt-043 | yes (rank 2) | yes (rank 2, was 2) | GOLD | excluded-fragment |
| nt-044 | yes (rank 3) | yes (rank 1, was 3) | GOLD | strict-single |
| nt-147 | no (was rank 5) | yes (rank 3, was 5) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-279** (PDF page 63)
> Threat Event
> An event or situation that has the potential for causing undesirable consequences or impact.
>
> **nt-043** (PDF page 19)
> If a threat event is almost certain to be initiated or occur in the (specified or implicit) time frame, the risk assessment may take into consideration the estimated frequency of the event. The likelihood of threat occurrence can also be based on the state of the organization (including for example, its core mission/business processes, enterprise architecture, information security architecture, information systems, and environments in which those systems operate)—taking into consideration predisposing conditions and the presence and effectiveness of deployed security controls to protect against unauthorized/undesirable behavior, detect and limit damage, and/or maintain or restore mission/business capabilities. The likelihood of impact addresses the probability (or possibility) that the threat event will result in an adverse impact, regardless of the magnitude of harm that can be expected.
>
> **nt-044** (PDF page 19)
> The likelihood of impact addresses the probability (or possibility) that the threat event will result in an adverse impact, regardless of the magnitude of harm that can be expected.
> Organizations typically employ a three-step process to determine the overall likelihood of threat events. First, organizations assess the likelihood that threat events will be initiated (for adversarial threat events) or will occur (for non-adversarial threat events). Second, organizations assess the likelihood that the threat events once initiated or occurring, will result in adverse impacts or harm to organizational operations and assets, individuals, other organizations, or the Nation. Finally, organizations assess the overall likelihood as a combination of likelihood of initiation/occurrence and likelihood of resulting in adverse impact.
>
> **nt-147** (PDF page 42)
> However, no further consideration during the current assessment is warranted.
> The overall likelihood of a threat event is a combination of: (i) the likelihood that the event will occur (e.g., due to human error or natural disaster) or be initiated by an adversary; and (ii) the likelihood that the initiation/occurrence will result in adverse impacts. Organizations assess the overall likelihood of threat events by using inputs from Tables G-2, G-3, and G-4. Any specific algorithm or rule for combining the determined likelihood values depends on: (i) general organizational attitudes toward risk, including overall risk tolerance and tolerance for uncertainty; (ii) specific tolerances toward uncertainty in different risk factors; and (iii) organizational weighting of risk factors.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** Likelihood of initiation/occurrence = the chance a threat event is started (adversarial) or occurs (non-adversarial). Likelihood of impact = the chance that, once initiated or occurring, it results in adverse impact, regardless of the magnitude of harm. The overall likelihood combines the two.
* **Expected polarity:** n/a (explains a difference)  |  type: contrast
* **Required points:** (1) States that one likelihood is that the event is initiated/occurs. (2) States that the other is that, once initiated, it results in adverse impact (not the size of the harm). (3) (Completeness) mentions that the overall likelihood combines the two.
* **Must it mention an exception / qualification / negation?** yes: qualification: The likelihood of impact is about whether harm results, 'regardless of the magnitude of harm' (it is not the severity). (affects correctness)
* **Acceptable wording:** Any faithful paraphrase; 'probability' and 'chance' are interchangeable.
* **Would count as an unsupported claim / error:** (1) Describing the likelihood of impact as the severity or size of the harm. (2) Swapping the two definitions. (3) Stating that the two are multiplied or combined by a specific formula (the guide specifies no algorithm; see also N1).
* **Supporting passages:** `nt-044`: "The likelihood of impact addresses the probability (or possibility) that the threat event will result in an adverse impact, regardless of the magnitude of harm that can be expected."; `nt-042`: "The likelihood risk factor combines an estimate of the likelihood that the threat event will be initiated with an estimate of the likelihood of impact"; `nt-144`: "Second, organizations assess the likelihood that threat events once initiated or occurring, will result in adverse impacts to organizational operations and assets"
* **Grader notes:** Preregistered gold nt-043 + nt-044; overlay v1.1 also accepts nt-042 and nt-144 as independently sufficient and treats nt-043 as a partial fragment.

**Answer 1 (baseline)**  | context order: nt-279, nt-043, nt-044

> The likelihood of initiation or occurrence refers to the probability that a threat event will be started or happen, while the likelihood of impact addresses the probability that the event will result in an adverse impact [nt-043]. These two distinct probabilities are combined to determine the overall likelihood of the threat event [nt-044].

[nt-043] [nt-044]

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 3 (limit 3: True); latency 0.4128 s; tokens in/out 490/82

**Answer 2 (re-ranked)**  | context order: nt-044, nt-043, nt-147

> The likelihood of impact addresses the probability that a threat event will result in an adverse impact, regardless of the magnitude of harm, while the likelihood of initiation or occurrence addresses the probability that the event will be started or happen [nt-044]. These two distinct components are then combined to determine the overall likelihood of the threat event [nt-044].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.3569 s; tokens in/out 624/74

**Answers textually identical:** no

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## A6  (keyword trap)

**Question:** What is it called when adversaries change their behaviour after noticing our safeguards?

**Preregistered gold chunk(s):** nt-035, nt-281

**Preregistered evidence phrase(s):**
> threat shifting is the response of adversaries to perceived safeguards
> response from adversaries to perceived safeguards

**Frozen retrieval outcome:** lenient success -> success (best gold rank 1 -> 1; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-281 | yes (rank 1) | yes (rank 1, was 1) | GOLD | strict-single |
| nt-168 | yes (rank 2) | no (re-ranked rank 10) |  |  |
| nt-035 | yes (rank 3) | yes (rank 2, was 3) | GOLD | strict-single |
| nt-036 | no (was rank 4) | yes (rank 3, was 4) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-281** (PDF page 63)
> Threat Shifting
> Response from adversaries to perceived safeguards and/or countermeasures (i.e., security controls), in which the adversaries change some characteristic of their intent to do harm in order to avoid and/or overcome those safeguards/countermeasures.
>
> **nt-168** (PDF page 51)
> Adversary
> Individual, group, organization, or government that conducts or has the intent to conduct detrimental activities. [DHS Risk Lexicon]
>
> **nt-035** (PDF page 18)
> Threat shifting is the response of adversaries to perceived safeguards and/or countermeasures (i.e., security controls), in which adversaries change some characteristic of their intent/targeting in order to avoid and/or overcome those safeguards/countermeasures. Threat shifting can occur in one or more domains including: (i) the time domain (e.g., a delay in an attack or illegal entry to conduct additional surveillance); (ii) the target domain (e.g., selecting a different target that is not as well protected); (iii) the resource domain (e.g., adding resources to the attack in order to reduce uncertainty or overcome safeguards and/or countermeasures); or (iv) the attack planning/attack method domain (e.g., changing the attack weapon or attack path).
>
> **nt-036** (PDF page 18)
> Threat shifting is a natural consequence of a dynamic set of interactions between threat sources and types of organizational assets targeted. With more sophisticated threat sources, it also tends to default to the path of least resistance to exploit particular vulnerabilities, and the responses are not always predictable. In addition to the safeguards and/or countermeasures implemented and the impact of a successful exploit of an organizational vulnerability, another influence on threat shifting is the benefit to the attacker. That perceived benefit on the attacker side can also influence how much and when threat shifting occurs.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** Threat shifting.
* **Expected polarity:** n/a (names a term)  |  type: term
* **Required points:** (1) Names 'threat shifting'.
* **Must it mention an exception / qualification / negation?** no
* **Acceptable wording:** Only the term 'threat shifting'.
* **Would count as an unsupported claim / error:** (1) Naming 'advanced persistent threat', 'deterrence' or 'adversary adaptation' as the NIST term. (2) Describing a different phenomenon (e.g. adversaries abandoning an attack permanently).
* **Supporting passages:** `nt-035`: "Threat shifting is the response of adversaries to perceived safeguards and/or countermeasures (i.e., security controls)"; `nt-281`: "Response from adversaries to perceived safeguards and/or countermeasures (i.e., security controls)"

**Answer 1 (baseline)**  | context order: nt-281, nt-168, nt-035

> This behavior is called threat shifting, which occurs when adversaries change some characteristic of their intent to do harm in order to avoid and/or overcome perceived safeguards and countermeasures [nt-281].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.2891 s; tokens in/out 406/41

**Answer 2 (re-ranked)**  | context order: nt-281, nt-035, nt-036

> This behavior is called threat shifting, which occurs when adversaries change some characteristic of their intent to do harm in order to avoid or overcome perceived safeguards and countermeasures [nt-281]. It can manifest across various domains, including time, target, resource, and attack planning [nt-035].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.4108 s; tokens in/out 482/64

**Answers textually identical:** no

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## E1  (exception)

**Question:** Is the level of risk always capped by the level of impact?

**Preregistered gold chunk(s):** nt-053, nt-054, nt-153

**Preregistered evidence phrase(s):**
> upper bound for risk may fail to apply
> impact as an upper bound on risk may not hold

**Frozen retrieval outcome:** lenient success -> success (best gold rank 1 -> 1; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-054 | yes (rank 1) | yes (rank 2, was 1) | GOLD | excluded-fragment |
| nt-052 | yes (rank 2) | yes (rank 3, was 2) |  |  |
| nt-153 | yes (rank 3) | yes (rank 1, was 3) | GOLD | strict-single |

**Passages shown to the LLM (union of the two contexts):**

> **nt-054** (PDF page 22)
> One issue for risk aggregation is that this upper bound for risk may fail to apply.
> For example, it may be advantageous for organizations to assess risk at the organization level when multiple risks materialize concurrently or when the same risk materializes repeatedly over a period of time. In such situations, there is the possibility that the amount of overall risk incurred is beyond the risk capacity of the organization, and therefore the overall impact to organizational operations and assets (i.e., mission/business impact) goes beyond that which was originally assessed for each specific risk.
>
> **nt-052** (PDF page 21)
> This broad definition also allows risk to be represented as a single value or as a vector (i.e., multiple values), in which different types of impacts are assessed separately. For purposes of risk communication, risk is generally grouped according to the types of adverse impacts (and possibly the time frames in which those impacts are likely to be experienced).
>
> **nt-153** (PDF page 44)
> In general, the risk level is typically not higher than the impact level, and likelihood can serve to reduce risk below that impact level. However, when addressing organization-wide risk management issues with a large number of missions/business functions, mission/business processes, and supporting information systems, impact as an upper bound on risk may not hold. For example, when multiple risks materialize, even if each risk is at the moderate level, the set of those moderate-level risks could aggregate to a higher level of risk for organizations. To address situations where harm occurs multiple times, organizations can define a threat event as multiple occurrences of harm and an impact level associated with the cumulative degree of harm. During the execution of Tasks 2-1 through 2-5, organizations capture key information related to uncertainties in risk assessments. These uncertainties arise from sources such as missing information, subjective determinations, and assumptions made.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** No. The risk level is typically not higher than the impact level (impact is an upper bound), but this upper bound may fail to apply, e.g. when multiple risks materialize concurrently or the same risk repeatedly, so aggregated risk can exceed the originally assessed impact.
* **Expected polarity:** No  |  type: yes/no with exception
* **Required points:** (1) Answers no (risk is not ALWAYS capped by impact). (2) Gives the exception: the upper bound may fail when risks aggregate / multiple risks materialize (organization-wide view).
* **Must it mention an exception / qualification / negation?** yes: exception: The general rule (risk is typically not higher than impact; likelihood can reduce risk below impact) AND its exception (aggregation of multiple/repeated risks). (affects correctness)
* **Acceptable wording:** 'does not always hold', 'may fail to apply'.
* **Would count as an unsupported claim / error:** (1) Answering yes / 'always capped'. (2) Claiming likelihood can push risk ABOVE the impact level (the source says likelihood can reduce risk below impact). (3) Giving specific numeric thresholds or levels not in the passages.
* **Supporting passages:** `nt-153`: "In general, the risk level is typically not higher than the impact level, and likelihood can serve to reduce risk below that impact level."; `nt-153`: "impact as an upper bound on risk may not hold"; `nt-053`: "this upper bound for risk may fail to apply"; `nt-054`: "when multiple risks materialize concurrently or when the same risk materializes repeatedly over a period of time"
* **Grader notes:** A bare 'No' without the exception is at most partially correct and incomplete. Overlay v1.1: nt-053 and nt-153 are independently sufficient; nt-054 only explains why.

**Answer 1 (baseline)**  | context order: nt-054, nt-052, nt-153

> No, the risk level is typically not higher than the impact level, but this upper bound may fail to apply when multiple risks materialize concurrently or repeatedly, causing the overall risk to exceed the organization's risk capacity [nt-054]. In such scenarios, the aggregate risk can be higher than the individual impact levels [nt-153].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.353 s; tokens in/out 523/72

**Answer 2 (re-ranked)**  | context order: nt-153, nt-054, nt-052

> No, the risk level is typically not higher than the impact level, but impact as an upper bound on risk may not hold when addressing organization-wide issues or when multiple risks materialize concurrently or repeatedly [nt-153]. In such situations, the overall risk incurred can exceed the organization's risk capacity, causing the total impact to go beyond what was originally assessed for each specific risk [nt-054].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 1.6898 s; tokens in/out 523/85

**Answers textually identical:** no

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## E2  (exception)

**Question:** If a threat event has no identified weaknesses that could be exploited, do we keep analysing it in the current assessment?

**Preregistered gold chunk(s):** nt-146, nt-147

**Preregistered evidence phrase(s):**
> no further consideration during the current assessment is warranted

**Frozen retrieval outcome:** lenient success -> success (best gold rank 2 -> 2; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-045 | yes (rank 1) | yes (rank 1, was 1) |  |  |
| nt-146 | yes (rank 2) | yes (rank 2, was 2) | GOLD | strict-single |
| nt-117 | yes (rank 3) | no (re-ranked rank 9) |  |  |
| nt-039 | no (was rank 5) | yes (rank 3, was 5) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-045** (PDF page 20)
> Threat-vulnerability pairing (i.e., establishing a one-to-one relationship between threats and vulnerabilities) may be undesirable when assessing likelihood at the mission/business function level, and in many cases, can be problematic even at the information system level due to the potentially large number of threats and vulnerabilities. This approach typically drives the level of detail in identifying threat events and vulnerabilities, rather than allowing organizations to make effective use of threat information and/or to identify threats at a level of detail that is meaningful. Depending on the level of detail in threat specification, a given threat event could exploit multiple vulnerabilities. In assessing likelihoods, organizations examine vulnerabilities that threat events could exploit and also the mission/business function susceptibility to events for which no security controls or viable implementations of security controls exist (e.g., due to functional dependencies, particularly external dependencies).
>
> **nt-146** (PDF page 42)
> Organizations assess the likelihood that threat events result in adverse impacts by taking into consideration the set of identified vulnerabilities and predisposing conditions (see Task 2-3 and Appendix F). For threat events initiated by adversaries, organizations consider characteristics of associated threat sources. For non-adversarial threat events, organizations take into account the anticipated severity and duration of the event (as included in the description of the event). Organizations use the assessment scale in Table G-4 and provide a rationale for the assessment allowing explicit consideration as stated above. Threat events for which no vulnerabilities or predisposing conditions are identified, have a very low likelihood of resulting in adverse impacts. Such threat events can be highlighted and moved to the end of the table (or to a separate table), so that they can be tracked for consideration in follow-on risk assessments. However, no further consideration during the current assessment is warranted.
>
> **nt-117** (PDF page 36)
> Analytic Approach
> Risk assessments include both assessment approaches (i.e., quantitative, qualitative, semi-quantitative) and analysis approaches (i.e., threat-oriented, asset/impact-oriented, vulnerability-oriented). Together, the assessment and analysis approaches form the analytic approach for the risk assessment. Organizations determine the level of detail and in what form, threats are analyzed including the level of granularity to describe threat events or threat scenarios. Different analysis approaches can lead to different levels of detail in characterizing adverse events for which likelihoods are determined. For example, an adverse event could be characterized in several ways (with increasing levels of detail): (i) a threat event (for which the likelihood is determined by taking the maximum overall threat sources); (ii) a pairing of a threat event and a threat source; or (iii) a detailed threat scenario/attack tree.
>
> **nt-039** (PDF page 19)
> In general, risks materialize as a result of a series of threat events, each of which takes advantage of one or more vulnerabilities. Organizations define threat scenarios to describe how the events caused by a threat source can contribute to or cause harm. Development of threat scenarios is analytically useful, since some vulnerabilities may not be exposed to exploitation unless and until other vulnerabilities have been exploited. Analysis that illuminates how a set of vulnerabilities, taken together, could be exploited by one or more threat events is therefore more useful than the analysis of individual vulnerabilities. In addition, a threat scenario tells a story, and hence is useful for risk communication as well as for analysis.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** No. Threat events with no identified vulnerabilities or predisposing conditions have a very low likelihood of resulting in adverse impacts; they can be tracked for follow-on assessments, but no further consideration during the current assessment is warranted.
* **Expected polarity:** No  |  type: yes/no with exception
* **Required points:** (1) Answers no (stop analysing it in the current assessment). (2) (Completeness) mentions that it can be tracked / moved to the end or a separate table for follow-on assessments.
* **Must it mention an exception / qualification / negation?** yes: qualification: 'Very low likelihood' (not zero) and the follow-on-tracking allowance. (affects completeness)
* **Acceptable wording:** 'no further consideration is warranted in the current assessment'.
* **Would count as an unsupported claim / error:** (1) Saying the event must be deleted or ignored permanently (the source says it is tracked for follow-on assessments). (2) Claiming zero likelihood (the source says 'very low'). (3) Justifying it with the different rule for events 'deemed irrelevant' (nt-136/nt-137) instead of 'no vulnerabilities or predisposing conditions identified'.
* **Supporting passages:** `nt-146`: "Threat events for which no vulnerabilities or predisposing conditions are identified, have a very low likelihood of resulting in adverse impacts."; `nt-146`: "so that they can be tracked for consideration in follow-on risk assessments"; `nt-146`: "However, no further consideration during the current assessment is warranted."
* **Grader notes:** The question says 'weaknesses'; the source says 'vulnerabilities or predisposing conditions' (noted in the overlay). nt-147 only repeats the last sentence.

**Answer 1 (baseline)**  | context order: nt-045, nt-146, nt-117

> No, no further consideration during the current assessment is warranted for threat events with no identified vulnerabilities or predisposing conditions. Instead, such events can be highlighted and moved to the end of the table or a separate table to be tracked for consideration in follow-on risk assessments [nt-146].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 1.3387 s; tokens in/out 694/60

**Answer 2 (re-ranked)**  | context order: nt-045, nt-146, nt-039

> No, no further consideration during the current assessment is warranted for threat events with no identified vulnerabilities or predisposing conditions. Instead, such events can be highlighted and moved to the end of the table or a separate table to be tracked for follow-on risk assessments [nt-146].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.3663 s; tokens in/out 654/58

**Answers textually identical:** no

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## E3  (exception)

**Question:** Can a threat event be dropped from the analysis when no adversary is known to have the ability to carry it out?

**Preregistered gold chunk(s):** nt-286

**Preregistered evidence phrase(s):**
> eliminate certain threat events from further consideration if no adversary with the necessary capability has been identified

**Frozen retrieval outcome:** lenient stumble -> success (best gold rank 7 -> 2; RESTORED into Top 3); strict stumble -> success (Top-3 evidence none -> sufficient; RESTORED into Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-279 | yes (rank 1) | no (re-ranked rank 7) |  |  |
| nt-034 | yes (rank 2) | yes (rank 1, was 2) |  |  |
| nt-043 | yes (rank 3) | no (re-ranked rank 6) |  |  |
| nt-286 | no (was rank 7) | yes (rank 2, was 7) | GOLD | strict-single |
| nt-039 | no (was rank 4) | yes (rank 3, was 4) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-279** (PDF page 63)
> Threat Event
> An event or situation that has the potential for causing undesirable consequences or impact.
>
> **nt-034** (PDF page 17)
> Risk models differ in the degree of detail and complexity with which threat events are identified. When threat events are identified with great specificity, threat scenarios can be modeled, developed, and analyzed. Threat events for cyber or physical attacks are characterized by the tactics, techniques, and procedures (TTPs) employed by adversaries. Understanding adversary-based threat events gives organizations insights into the capabilities associated with certain threat sources. In addition, having greater knowledge about who is carrying out the attacks gives organizations a better understanding of what adversaries desire to gain by the attacks. Knowing the intent and targeting aspects of a potential attack helps organizations narrow the set of threat events that are most relevant to consider.
>
> **nt-043** (PDF page 19)
> If a threat event is almost certain to be initiated or occur in the (specified or implicit) time frame, the risk assessment may take into consideration the estimated frequency of the event. The likelihood of threat occurrence can also be based on the state of the organization (including for example, its core mission/business processes, enterprise architecture, information security architecture, information systems, and environments in which those systems operate)—taking into consideration predisposing conditions and the presence and effectiveness of deployed security controls to protect against unauthorized/undesirable behavior, detect and limit damage, and/or maintain or restore mission/business capabilities. The likelihood of impact addresses the probability (or possibility) that the threat event will result in an adverse impact, regardless of the magnitude of harm that can be expected.
>
> **nt-286** (PDF page 69)
> APPENDIX E — THREAT EVENTS
> REPRESENTATIVE THREAT EVENTS INITIATED BY THREAT SOURCES
> This appendix provides: (i) a description of potentially useful inputs to the threat event identification task; (ii) representative examples of adversarial threat events expressed as tactics, techniques, and procedures (TTPs) and non-adversarial threat events; (iii) an exemplary assessment scale for the relevance of those threat events; and (iv) templates for summarizing and documenting the results of the threat identification Task 2-2. Organizations can eliminate certain threat events from further consideration if no adversary with the necessary capability has been identified. Organizations can also modify the threat events provided to describe specific TTPs with sufficient detail and at the appropriate classification level. Organizations can use the representative threat events and predicated/expected values for the relevance of those events as a starting point with tailoring to adjust for any organization-specific conditions.
> Table E-5, an output from Task 2-2, provides relevant inputs to the risk tables in Appendix I.
>
> **nt-039** (PDF page 19)
> In general, risks materialize as a result of a series of threat events, each of which takes advantage of one or more vulnerabilities. Organizations define threat scenarios to describe how the events caused by a threat source can contribute to or cause harm. Development of threat scenarios is analytically useful, since some vulnerabilities may not be exposed to exploitation unless and until other vulnerabilities have been exploited. Analysis that illuminates how a set of vulnerabilities, taken together, could be exploited by one or more threat events is therefore more useful than the analysis of individual vulnerabilities. In addition, a threat scenario tells a story, and hence is useful for risk communication as well as for analysis.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** Yes: organizations can eliminate certain threat events from further consideration if no adversary with the necessary capability has been identified.
* **Expected polarity:** Yes (permitted)  |  type: yes/no with condition
* **Required points:** (1) Answers yes (it is permitted). (2) States the condition: no adversary with the necessary capability has been identified.
* **Must it mention an exception / qualification / negation?** yes: qualification: It is a permission ('can'), conditional on no adversary with the necessary capability having been identified. (affects correctness)
* **Acceptable wording:** 'can be eliminated', 'may be dropped from further consideration'.
* **Would count as an unsupported claim / error:** (1) Presenting elimination as mandatory. (2) Allowing elimination when adversary capability is merely unknown or unassessed (the source: 'no adversary ... has been identified'). (3) Citing the rules about 'irrelevant' events or adversary intent instead (different rules).
* **Supporting passages:** `nt-286`: "Organizations can eliminate certain threat events from further consideration if no adversary with the necessary capability has been identified."

**Answer 1 (baseline)**  | context order: nt-279, nt-034, nt-043

> The provided context does not contain the answer.

*Objective checks (format only):* cites a passage: False; only supplied passages: False; cites a gold chunk: False; refusal sentence: True; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.2369 s; tokens in/out 483/10

**Answer 2 (re-ranked)**  | context order: nt-034, nt-286, nt-039

> Yes, organizations can eliminate certain threat events from further consideration if no adversary with the necessary capability has been identified. [nt-286]

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.2832 s; tokens in/out 661/30

**Answers textually identical:** no

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## E4  (exception)

**Question:** When conditions have changed since the last assessment, must every task be redone?

**Preregistered gold chunk(s):** nt-163, nt-164

**Preregistered evidence phrase(s):**
> determine whether all tasks in the risk assessment process need to be repeated
> identifying and assessing only how selected risk factors have changed

**Frozen retrieval outcome:** lenient success -> success (best gold rank 1 -> 1; kept in Top 3); strict stumble -> success (Top-3 evidence partial -> sufficient; RESTORED into Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-163 | yes (rank 1) | yes (rank 1, was 1) | GOLD | joint-member-1 |
| nt-160 | yes (rank 2) | yes (rank 3, was 2) |  |  |
| nt-234 | yes (rank 3) | no (re-ranked rank 7) |  |  |
| nt-164 | no (was rank 8) | yes (rank 2, was 8) | GOLD | joint-member-1 |

**Passages shown to the LLM (union of the two contexts):**

> **nt-163** (PDF page 48)
> TASK 4-2: Update existing risk assessment using the results from ongoing monitoring of risk factors. Supplemental Guidance: Organizations determine the frequency and the circumstances under which risk assessments are updated. Such determinations can include, for example, the current level of risk to and/or the importance of, core organizational missions/business functions. If significant changes (as defined by organizational policies, direction, or guidance) have occurred since the risk assessment was conducted, organizations can revisit the purpose, scope, assumptions, and constraints of the assessment to determine whether all tasks in the risk assessment process need to be repeated.
>
> **nt-160** (PDF page 47)
> STEP 4: MAINTAIN THE ASSESSMENT
> TASK 4-1: Conduct ongoing monitoring of the risk factors that contribute to changes in risk to organizational operations and assets, individuals, other organizations, or the Nation. Supplemental Guidance: Organizations monitor risk factors of importance on an ongoing basis to ensure that the information needed to make credible, risk-based decisions continues to be available over time. Monitoring risk factors (e.g., threat sources and threat events, vulnerabilities and predisposing conditions, capabilities and intent of adversaries, targeting of organizational operations, assets, or individuals) can provide critical information on changing conditions that could potentially affect the ability of organizations to conduct core missions and business functions. Information derived from the ongoing monitoring of risk factors can be used to refresh risk assessments at whatever frequency deemed appropriate. Organizations can also attempt to capture changes in the effectiveness of risk response measures in order to maintain the currency of risk assessments.
>
> **nt-234** (PDF page 58)
> Repeatability
> The ability to repeat an assessment in the future, in a manner that is consistent with, and hence comparable to, prior assessments.
>
> **nt-164** (PDF page 48)
> Otherwise, the updates constitute subsequent risk assessments, identifying and assessing only how selected risk factors have changed, for example: (i) the identification of new threat events, vulnerabilities, predisposing conditions, undesirable consequences and/or affected assets; and (ii) the assessments of threat source characteristics (e.g., capability, intent, targeting, range of effects), likelihoods, and impacts. Organizations communicate the results of subsequent risk assessments to entities across all risk management tiers to ensure that responsible organizational officials have access to critical information needed to make ongoing risk-based decisions.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** Not necessarily. If significant changes (as defined by organizational policies) have occurred, organizations revisit the purpose, scope, assumptions and constraints to determine whether all tasks need to be repeated; otherwise the update covers only how selected risk factors have changed (a subsequent risk assessment).
* **Expected polarity:** Not necessarily  |  type: yes/no with exception
* **Required points:** (1) Answers 'not necessarily / no, not every task must always be redone'. (2) States that significant changes trigger a review of purpose/scope/assumptions/constraints to decide whether all tasks are repeated. (3) States that otherwise only the changed risk factors are identified and assessed.
* **Must it mention an exception / qualification / negation?** yes: exception: The decision depends on whether the changes are SIGNIFICANT (per organizational policy); the update may be limited to changed risk factors. (affects correctness)
* **Acceptable wording:** 'subsequent risk assessment', 'only the factors that changed'.
* **Would count as an unsupported claim / error:** (1) Answering that every task must always be redone (or that nothing ever needs redoing). (2) Claiming a specific threshold or schedule for 'significant' (the source defers to organizational policy). (3) Saying all tasks are automatically repeated whenever any condition changes.
* **Supporting passages:** `nt-163`: "If significant changes (as defined by organizational policies, direction, or guidance) have occurred since the risk assessment was conducted, organizations can revisit the purpose, scope, assumptions, and constraints of the assessment to determine whether all tasks in the risk assessment process need to be repeated."; `nt-164`: "Otherwise, the updates constitute subsequent risk assessments, identifying and assessing only how selected risk factors have changed"
* **Grader notes:** Joint evidence (nt-163 + nt-164) under overlay v1.1. The question says 'conditions have changed'; the source says 'significant changes'.

**Answer 1 (baseline)**  | context order: nt-163, nt-160, nt-234

> No, organizations can revisit the purpose, scope, assumptions, and constraints to determine whether all tasks in the risk assessment process need to be repeated. [nt-163]

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.2944 s; tokens in/out 508/37

**Answer 2 (re-ranked)**  | context order: nt-163, nt-164, nt-160

> No, organizations can revisit the purpose, scope, assumptions, and constraints to determine whether all tasks need to be repeated, and otherwise, the updates constitute subsequent risk assessments that identify and assess only how selected risk factors have changed [nt-163] [nt-164].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.7145 s; tokens in/out 587/59

**Answers textually identical:** no

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## E5  (exception)

**Question:** Can the scope of a system-level assessment ignore weaknesses that come from controls the system inherits?

**Preregistered gold chunk(s):** nt-105

**Preregistered evidence phrase(s):**
> without consideration of inherited vulnerabilities

**Frozen retrieval outcome:** lenient success -> success (best gold rank 1 -> 1; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-105 | yes (rank 1) | yes (rank 1, was 1) | GOLD | strict-single |
| nt-253 | yes (rank 2) | no (re-ranked rank 8) |  |  |
| nt-257 | yes (rank 3) | yes (rank 2, was 3) |  |  |
| nt-080 | no (was rank 8) | yes (rank 3, was 8) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-105** (PDF page 34)
> Architectural/Technology Considerations
> Organizations use architectural and technology considerations to clarify the scope of the risk assessment. For example, at Tier 3, the scope of the risk assessment can be an organizational information system in its environment of operations. This entails placing the information system in its architectural context, so that vulnerabilities in inherited controls can be taken into consideration. Alternately, the scope of the assessment can be limited solely to the information system, without consideration of inherited vulnerabilities. At Tier 2, the scope of the risk assessment can be defined in terms of the mission/business segment architecture (e.g., including all systems, services, and infrastructures that support a specific mission/function). For a targeted risk assessment at any tier, the specific question to be answered can restrict the scope to a specific technology.
>
> **nt-253** (PDF page 60)
> Security Control Assessment
> The testing and/or evaluation of the management, operational, and technical security controls to determine the extent to which the controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting the security requirements for an information system or organization. [NIST SP 800-39] [CNSSI No. 4009, Adapted]
>
> **nt-257** (PDF page 61)
> Security Control Inheritance
> A situation in which an information system or application receives protection from security controls (or portions of security controls) that are developed, implemented, assessed, authorized, and monitored by entities other than those responsible for the system or application; entities either internal or external to the organization where the system or application resides. See Common Control. [CNSSI No. 4009]
>
> **nt-080** (PDF page 28)
> The Tier 2 context and the system development life cycle determine the purpose and define the scope of risk assessment activities at Tier 3. While initial risk assessments (i.e., risk assessments performed for the first time, rather than updating prior risk assessments) can be performed at any phase in the system development life cycle, ideally these assessments should be performed in the Initiation phase. In the Initiation phase, risk assessments evaluate the anticipated vulnerabilities and predisposing conditions affecting the confidentiality, integrity, and availability of information systems in the context of the planned environments of operation. Such assessments inform risk response, enabling information system owners/program managers, together with mission/business owners to make the final decisions about the security controls necessary based on the security categorization and the environment of operation. Risk assessments are also conducted at later phases in the system development life cycle, updating risk assessment results from earlier phases.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** Yes: the scope of a system-level assessment can be limited solely to the information system, without consideration of inherited vulnerabilities (the alternative is to place the system in its architectural context so that vulnerabilities in inherited controls are considered).
* **Expected polarity:** Yes (permitted option)  |  type: yes/no with option
* **Required points:** (1) Answers yes (it is a permitted scoping choice). (2) (Completeness) mentions the alternative scope that does consider inherited vulnerabilities.
* **Must it mention an exception / qualification / negation?** yes: qualification: It is one of two permitted options, not a requirement. (affects completeness)
* **Acceptable wording:** 'can be limited solely to the system', 'without consideration of inherited vulnerabilities'.
* **Would count as an unsupported claim / error:** (1) Saying inherited vulnerabilities must never be considered, or must always be considered. (2) Attributing the option to a different tier or technique not in the passage.
* **Supporting passages:** `nt-105`: "Alternately, the scope of the assessment can be limited solely to the information system, without consideration of inherited vulnerabilities."; `nt-105`: "so that vulnerabilities in inherited controls can be taken into consideration"

**Answer 1 (baseline)**  | context order: nt-105, nt-253, nt-257

> Yes, the scope of the assessment can be limited solely to the information system without consideration of inherited vulnerabilities. [nt-105]

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 1.3547 s; tokens in/out 497/29

**Answer 2 (re-ranked)**  | context order: nt-105, nt-257, nt-080

> Yes, the scope of the assessment can be limited solely to the information system without consideration of inherited vulnerabilities. [nt-105]

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.2857 s; tokens in/out 593/29

**Answers textually identical:** yes

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## E6  (exception)

**Question:** What extra step may be needed when rolling up mission-level results in an organization whose missions differ a lot?

**Preregistered gold chunk(s):** nt-076, nt-077

**Preregistered evidence phrase(s):**
> expert analysis may be needed to normalize the results from tier 2 risk assessments

**Frozen retrieval outcome:** lenient success -> success (best gold rank 2 -> 1; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-226 | yes (rank 1) | no (re-ranked rank 7) |  |  |
| nt-076 | yes (rank 2) | yes (rank 3, was 2) | GOLD | strict-single |
| nt-118 | yes (rank 3) | no (re-ranked rank 5) |  |  |
| nt-077 | no (was rank 4) | yes (rank 1, was 4) | GOLD | strict-single |
| nt-053 | no (was rank 7) | yes (rank 2, was 7) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-226** (PDF page 57)
> Mission/Business Segment
> Elements of organizations describing mission areas, common/shared business services, and organization-wide services. Mission/business segments can be identified with one or more information systems which collectively support a mission/business process.
>
> **nt-076** (PDF page 27)
> Organization-wide assessments of risk can be based solely on the assumptions, constraints, risk tolerances, priorities, and trade-offs established in the risk framing step (i.e., derived primarily from Tier 1 activities). However, more realistic and meaningful risk assessments are based on assessments conducted across multiple mission/business lines (i.e., derived primarily from Tier 2 activities). The ability of organizations to effectively use Tier 2 risk assessments as inputs to Tier 1 risk assessments is shaped by such considerations as: (i) the similarity of organizational missions/business functions and mission/business processes; and (ii) the degree of autonomy that organizational entities or subcomponents have with respect to parent organizations. In decentralized organizations or organizations with varied missions/business functions and/or environments of operation, expert analysis may be needed to normalize the results from Tier 2 risk assessments.
>
> **nt-118** (PDF page 36)
> In general, organizations can be expected to require more detail for highly critical missions/business functions, common infrastructures, or shared services on which multiple missions or business functions depend (as common points of failure), and information systems with high criticality or sensitivity. Mission/business owners may amplify this guidance for risk hot spots (information systems, services, or critical infrastructure components of particular concern) in mission/business segments.
>
> **nt-077** (PDF page 27)
> In decentralized organizations or organizations with varied missions/business functions and/or environments of operation, expert analysis may be needed to normalize the results from Tier 2 risk assessments.
> Finally, risk assessments at Tier 1 take into consideration the identification of mission-essential functions from Continuity of Operations Plans (COOP) prepared by organizations when determining the contribution of Tier 2 risks. Risk assessment results at Tier 1 are communicated to organizational entities at Tier 2 and Tier 3.
>
> **nt-053** (PDF page 22)
> Aggregation
> Organizations may use risk aggregation to roll up several discrete or lower-level risks into a more general or higher-level risk. Organizations may also use risk aggregation to efficiently manage the scope and scale of risk assessments involving multiple information systems and multiple mission/business processes with specified relationships and dependencies among those systems and processes. Risk aggregation, conducted primarily at Tiers 1 and 2 and occasionally at Tier 3, assesses the overall risk to organizational operations, assets, and individuals given the set of discrete risks. In general, for discrete risks (e.g., the risk associated with a single information system supporting a well-defined mission/business process), the worst-case impact establishes an upper bound for the overall risk to organizational operations, assets, and individuals. One issue for risk aggregation is that this upper bound for risk may fail to apply.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** Expert analysis may be needed to normalize the results from Tier 2 risk assessments (in decentralized organizations or organizations with varied missions/business functions).
* **Expected polarity:** n/a  |  type: short fact
* **Required points:** (1) States that expert analysis may be needed to normalize the (Tier 2) results.
* **Must it mention an exception / qualification / negation?** yes: qualification: It is conditional ('may be needed') and applies to decentralized organizations / varied missions or environments. (affects completeness)
* **Acceptable wording:** 'normalize the results', 'expert analysis'.
* **Would count as an unsupported claim / error:** (1) Describing a specific normalization method or tool (none is given). (2) Stating it is always required for every organization.
* **Supporting passages:** `nt-076`: "In decentralized organizations or organizations with varied missions/business functions and/or environments of operation, expert analysis may be needed to normalize the results from Tier 2 risk assessments."
* **Grader notes:** 'Mission-level results' = Tier 2 risk assessments used as inputs to Tier 1.

**Answer 1 (baseline)**  | context order: nt-226, nt-076, nt-118

> Expert analysis may be needed to normalize the results from Tier 2 risk assessments in organizations with varied missions/business functions. [nt-076]

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.3094 s; tokens in/out 467/31

**Answer 2 (re-ranked)**  | context order: nt-077, nt-053, nt-076

> Expert analysis may be needed to normalize the results from Tier 2 risk assessments in decentralized organizations or those with varied missions/business functions. [nt-076] [nt-077]

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.2968 s; tokens in/out 607/41

**Answers textually identical:** no

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## N1  (negation/constraint)

**Question:** Does the guide prescribe a formula for combining semi-quantitative factor values?

**Preregistered gold chunk(s):** nt-126

**Preregistered evidence phrase(s):**
> does not specify algorithms for combining semi-quantitative values

**Frozen retrieval outcome:** lenient success -> success (best gold rank 1 -> 1; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-126 | yes (rank 1) | yes (rank 1, was 1) | GOLD | strict-single |
| nt-061 | yes (rank 2) | yes (rank 3, was 2) |  |  |
| nt-265 | yes (rank 3) | no (re-ranked rank 4) |  |  |
| nt-125 | no (was rank 4) | yes (rank 2, was 4) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-126** (PDF page 37)
> Therefore, this guideline does not specify algorithms for combining semi-quantitative values. Organization-specific risk models include algorithms (e.g., formulas, tables, rules) for combining risk factors. If an organization-specific risk model is not provided in the risk management strategy as part of the risk framing step, then part of this task is to specify the algorithms for combining values. Algorithms for combining risk factors reflect organizational risk tolerance (see the supplemental guidance to Task 2-4 for examples). Organization-specific risk models are refined as part of preparation for a risk assessment by: (i) identifying the risk model and the rationale for using it (when multiple organization-specific risk models are provided); (ii) providing additional examples for values of risk factors; and (iii) identifying any assessment-specific algorithms (e.g., algorithms specific to the use of an attack graph analysis technique).
>
> **nt-061** (PDF page 23)
> Finally, semi-quantitative assessments typically employ a set of methods, principles, or rules for assessing risk that uses bins, scales, or representative numbers whose values and meanings are not maintained in other contexts. This type of assessment can provide the benefits of quantitative and qualitative assessments. The bins (e.g., 0-15, 16-35, 36-70, 71-85, 86-100) or scales (e.g., 1-10) translate easily into qualitative terms that support risk communications for decision makers (e.g., a score of 95 can be interpreted as very high), while also allowing relative comparisons between values in different bins or even within the same bin (e.g., the difference between risks scored 70 and 71 respectively is relatively insignificant, while the difference between risks scored 36 and 70 is relatively significant).
>
> **nt-265** (PDF page 62)
> Semi-Quantitative Assessment
> Use of a set of methods, principles, or rules for assessing risk based on bins, scales, or representative numbers whose values and meanings are not maintained in other contexts. [Department of Homeland Security (DHS) Risk Lexicon]
>
> **nt-125** (PDF page 37)
> For each assessable risk factor, the appendices include three assessment scales (one qualitative and two semi-quantitative scales) with correspondingly different representations. Organizations typically define (or select and tailor from the appendices) the assessment scales to be used in their risk assessments, annotating with organizationally-meaningful examples for specific values and defining break points between bins for semi-quantitative approaches. In addition, mission/business owners can provide further annotations with mission/business-specific examples. Organizations can identify different assessment scales to be used in different circumstances. For example, for low-impact information systems, organizations could use qualitative values, while for moderate- and high-impact systems, the most granular semi-quantitative values (0-100) could be used. As discussed in Special Publication 800-39, Task 1-1, Risk Assumptions, organizations vary in the relative weights applied to risk factors.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** No. The guide does not specify algorithms for combining semi-quantitative values; organization-specific risk models supply the algorithms (or the organization specifies them as part of the task).
* **Expected polarity:** No  |  type: yes/no with negation
* **Required points:** (1) Answers no (no prescribed formula). (2) (Completeness) says the algorithms come from organization-specific risk models / are specified by the organization.
* **Must it mention an exception / qualification / negation?** yes: negation: The guide explicitly does NOT specify algorithms. (affects correctness)
* **Acceptable wording:** 'does not specify algorithms', 'no prescribed formula'.
* **Would count as an unsupported claim / error:** (1) Presenting a specific formula (e.g. multiply likelihood by impact) as the guide's prescription. (2) Saying the guide mandates a particular combination rule (it only gives example rules as options in other places).
* **Supporting passages:** `nt-126`: "this guideline does not specify algorithms for combining semi-quantitative values"; `nt-126`: "Organization-specific risk models include algorithms (e.g., formulas, tables, rules) for combining risk factors."

**Answer 1 (baseline)**  | context order: nt-126, nt-061, nt-265

> No, the guide does not specify algorithms for combining semi-quantitative values. Instead, it states that organization-specific risk models include these algorithms, which must be specified if not already provided in the risk management strategy [nt-126].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.3275 s; tokens in/out 589/50

**Answer 2 (re-ranked)**  | context order: nt-126, nt-125, nt-061

> No, the guideline does not specify algorithms for combining semi-quantitative values. Instead, organization-specific risk models include the necessary algorithms, which must be specified if not already provided in the risk management strategy [nt-126].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.3638 s; tokens in/out 725/48

**Answers textually identical:** no

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## N2  (negation/constraint)

**Question:** Are there fixed requirements for how formal or detailed a risk assessment has to be?

**Preregistered gold chunk(s):** nt-002

**Preregistered evidence phrase(s):**
> there are no specific requirements with regard to

**Frozen retrieval outcome:** lenient success -> success (best gold rank 1 -> 1; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-002 | yes (rank 1) | yes (rank 1, was 1) | GOLD | strict-single |
| nt-094 | yes (rank 2) | yes (rank 2, was 2) |  |  |
| nt-003 | yes (rank 3) | no (re-ranked rank 10) |  |  |
| nt-291 | no (was rank 10) | yes (rank 3, was 10) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-002** (PDF page 9)
> • There are no specific requirements with regard to: (i) the formality, rigor, or level of detail that characterizes any particular risk assessment; (ii) the methodologies, tools, and techniques used to conduct such risk assessments; or (iii) the format and content of assessment results and any associated reporting mechanisms. Organizations have maximum flexibility on how risk assessments are conducted and are encouraged to apply the guidance in this document so that the various needs of organizations can be addressed and the risk assessment activities can be integrated into broader organizational risk management processes.
> • Organizations are also cautioned that risk assessments are often not precise instruments of measurement and reflect: (i) the limitations of the specific assessment methodologies, tools, and techniques employed; (ii) the subjectivity, quality, and trustworthiness of the data used; (iii) the interpretation of assessment results; and (iv) the skills and expertise of those individuals or groups conducting the assessments.
>
> **nt-094** (PDF page 33)
> 3.1 PREPARING FOR THE RISK ASSESSMENT
> The first step in the risk assessment process is to prepare for the assessment. The objective of this step is to establish a context for the risk assessment. This context is established and informed by the results from the risk framing step of the risk management process. Risk framing identifies, for example, organizational information regarding policies and requirements for conducting risk assessments, specific assessment methodologies to be employed, procedures for selecting risk factors to be considered, scope of the assessments, rigor of analyses, degree of formality, and requirements that facilitate consistent and repeatable risk determinations across the organization. Organizations use the risk management strategy to the extent practicable to obtain information to prepare for the risk assessment. Preparing for a risk assessment includes the following tasks:
> • Identify the purpose of the assessment;
> • Identify the scope of the assessment;
> • Identify the assumptions and constraints associated with the assessment;
> • Identify the sources of information to be used as inputs to the assessment; and
> • Identify the risk model and analytic approaches (i.e., assessment and analysis approaches) to be employed during the assessment.
>
> **nt-003** (PDF page 9)
> • Since cost, timeliness, and ease of use are a few of the many important factors in the application of risk assessments, organizations should attempt to reduce the level of effort for risk assessments by sharing risk-related information, whenever possible.
>
> **nt-291** (PDF page 90)
> APPENDIX J — INFORMING RISK RESPONSE
> APPROACHES TO REFINING RISK ASSESSMENT RESULTS
> A risk assessment may identify a number of risks that have similar scores (e.g., 78, 82, 83) or levels (e.g., moderate, high). When too many risks are clustered at or about the same value, organizations need a method to refine the presentation of risk assessment results, prioritizing within sets of risks with similar values, to better inform the risk response component of the risk management process. Such a method should be associated with the mission/business requirements of the organization, consistent with the organizational risk tolerance, and maximize the use of available resources. Prioritization is a key component of risk-based protection and becomes necessary when requirements cannot be fully satisfied or when resources do not allow all risks to be mitigated within a reasonable time frame.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** No. The guide states there are no specific requirements regarding the formality, rigor or level of detail of a risk assessment (nor the methodologies/tools or the format of results); organizations have maximum flexibility.
* **Expected polarity:** No  |  type: yes/no with negation
* **Required points:** (1) Answers no (there are no fixed requirements). (2) (Completeness) names formality/rigor/level of detail.
* **Must it mention an exception / qualification / negation?** yes: negation: The source is a statement of absence of requirements; organizations have flexibility. (affects correctness)
* **Acceptable wording:** 'no specific requirements', 'maximum flexibility'.
* **Would count as an unsupported claim / error:** (1) Stating that a particular level of rigor, a methodology or a report format is mandatory. (2) Inventing minimum documentation requirements.
* **Supporting passages:** `nt-002`: "There are no specific requirements with regard to: (i) the formality, rigor, or level of detail that characterizes any particular risk assessment"

**Answer 1 (baseline)**  | context order: nt-002, nt-094, nt-003

> No, there are no specific requirements regarding the formality, rigor, or level of detail that characterizes any particular risk assessment. Organizations have maximum flexibility on how risk assessments are conducted and are encouraged to apply the guidance to address their various needs [nt-002].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.3243 s; tokens in/out 640/56

**Answer 2 (re-ranked)**  | context order: nt-002, nt-094, nt-291

> No, there are no specific requirements regarding the formality, rigor, or level of detail that characterizes any particular risk assessment. Organizations have maximum flexibility on how risk assessments are conducted and are encouraged to apply the guidance to address their various needs [nt-002].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.3393 s; tokens in/out 777/56

**Answers textually identical:** yes

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## N3  (negation/constraint)

**Question:** Is it mandatory to use the sample tables in the appendices when carrying out an assessment?

**Preregistered gold chunk(s):** nt-131

**Preregistered evidence phrase(s):**
> the use of the templates is not required in order to conduct risk assessments

**Frozen retrieval outcome:** lenient success -> success (best gold rank 3 -> 2; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-305 | yes (rank 1) | yes (rank 1, was 1) |  |  |
| nt-016 | yes (rank 2) | no (re-ranked rank 4) |  |  |
| nt-131 | yes (rank 3) | yes (rank 2, was 3) | GOLD | strict-single |
| nt-092 | no (was rank 9) | yes (rank 3, was 9) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-305** (PDF page 93)
> Appendices
> • List references and sources of information.
> • List the team or individuals conducting the risk assessment including contact information.
> • List risk assessment details and any supporting evidence (e.g., Tables D-7, D-8, E-5, F-3, F-6, H-4), as needed to understand and enable reuse of results (e.g., for reciprocity, for subsequent risk assessments, to serve as input to Tier 1 and Tier 2 risk assessments).
>
> **nt-016** (PDF page 12)
> • Supporting appendices provide additional risk assessment information including: (i) general references; (ii) a glossary of terms; (iii) acronyms; (iv) threat sources; (v) threat events; (vi) vulnerabilities and predisposing conditions; (vii) likelihood of threat event occurrence; (viii) organizational impact; (ix) risk determination; (x) informing risk response; (xi) essential information for risk assessment reports; and (xii) a summary of risk assessment tasks.
>
> **nt-131** (PDF page 38)
> The specific tasks are presented in a sequential manner for clarity. However, in practice, some iteration among the tasks is both necessary and expected. Depending on the purpose of the risk assessment, organizations may find reordering the tasks advantageous. Whatever adjustments organizations make to the tasks described below, risk assessments should meet the stated purpose, scope, assumptions, and constraints established by the organizations initiating the assessments. To assist organizations in executing the individual tasks in the risk assessment process, a set of templates is provided in Appendices D through I. These appendices provide useful information for organizations in assessing risk and can also be used to record assessment results produced during essential calculations and analyses. The templates are exemplary and can be tailored by organizations in accordance with specific organizational mission/business requirements. The use of the templates is not required in order to conduct risk assessments.
>
> **nt-092** (PDF page 31)
> To reinforce the importance of risk communication and information sharing within organizations, the input tables in Appendices D, E, F, G, H, and I (i.e., threat sources, threat events, vulnerabilities, predisposing conditions, likelihood, impact, and risk) and the recommended elements of a risk assessment report (Appendix K) provide recommendations for risk communication/sharing among the tiers.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** No. The templates in Appendices D through I are exemplary and can be tailored; the use of the templates is not required in order to conduct risk assessments.
* **Expected polarity:** No  |  type: yes/no with negation
* **Required points:** (1) Answers no (not mandatory). (2) (Completeness) says they are exemplary / can be tailored.
* **Must it mention an exception / qualification / negation?** yes: negation: Use of the templates is explicitly NOT required. (affects correctness)
* **Acceptable wording:** 'templates' = the question's 'sample tables'.
* **Would count as an unsupported claim / error:** (1) Claiming the appendix tables must be used for compliance. (2) Claiming a specific subset is mandatory.
* **Supporting passages:** `nt-131`: "The use of the templates is not required in order to conduct risk assessments."; `nt-131`: "The templates are exemplary and can be tailored by organizations"
* **Grader notes:** The question says 'sample tables'; the source says 'templates' (Appendices D-I).

**Answer 1 (baseline)**  | context order: nt-305, nt-016, nt-131

> No, the use of the templates provided in Appendices D through I is not required in order to conduct risk assessments. [nt-131]

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.4229 s; tokens in/out 549/32

**Answer 2 (re-ranked)**  | context order: nt-305, nt-131, nt-092

> No, the use of the templates is not required in order to conduct risk assessments. [nt-131]

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.2661 s; tokens in/out 522/25

**Answers textually identical:** no

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## N4  (negation/constraint)

**Question:** Is watching only the security posture of the information systems enough to know the organization's overall risk?

**Preregistered gold chunk(s):** nt-161, nt-162

**Preregistered evidence phrase(s):**
> monitoring only the security posture of information systems would likely not provide sufficient information

**Frozen retrieval outcome:** lenient success -> success (best gold rank 1 -> 1; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-161 | yes (rank 1) | yes (rank 2, was 1) | GOLD | strict-single |
| nt-005 | yes (rank 2) | yes (rank 3, was 2) |  |  |
| nt-213 | yes (rank 3) | no (re-ranked rank 4) |  |  |
| nt-162 | no (was rank 4) | yes (rank 1, was 4) | GOLD | excluded-fragment |

**Passages shown to the LLM (union of the two contexts):**

> **nt-161** (PDF page 47)
> The objective is to maintain an ongoing situational awareness of the organizational governance structures and activities, mission/business processes, information systems, and environments of operation, and thereby all of the risk factors that may affect the risk being incurred by organizations. Therefore, in applying the risk assessment context or risk frame (i.e., scope, purpose, assumptions, constraints, risk tolerances, priorities, and trade-offs), organizations consider the part risk factors play in the risk response plan executed. For example, it is expected to be quite common for the security posture of information systems (that is, the risk factors measured within those systems) to reflect only a part of the organizational risk response, with response actions at the organization level or mission/business process level providing a significant portion of that response. In such situations, monitoring only the security posture of information systems would likely not provide sufficient information to determine the overall risk being incurred by organizations.
>
> **nt-005** (PDF page 10)
> Therefore, it is imperative that leaders and managers at all levels understand their responsibilities and are held accountable for managing information security risk—that is, the risk associated with the operation and use of information systems that support the missions and business functions of their organizations.
>
> **nt-213** (PDF page 56)
> Information Security Risk
> The risk to organizational operations (including mission, functions, image, reputation), organizational assets, individuals, other organizations, and the Nation due to the potential for unauthorized access, use, disclosure, disruption, modification, or destruction of information and/or information systems. See Risk.
>
> **nt-162** (PDF page 47)
> In such situations, monitoring only the security posture of information systems would likely not provide sufficient information to determine the overall risk being incurred by organizations.
> Highly capable, well-resourced, and purpose-driven threat sources can be expected to defeat commonly available protection mechanisms (e.g., by bypassing or tampering with such mechanisms). Thus, process-level risk response measures such as reengineering mission/business processes, wise use of information technology, or the use of alternate execution processes, in the event of compromised information systems, can be major elements of organizational risk response plans.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** No. Where organization- or process-level actions form a significant part of the risk response, monitoring only the security posture of information systems would likely not provide sufficient information to determine the organization's overall risk.
* **Expected polarity:** No (hedged)  |  type: yes/no with negation
* **Required points:** (1) Answers no (not enough by itself). (2) (Completeness) gives the reason: response actions at the organization or mission/business-process level are a significant part of the risk response.
* **Must it mention an exception / qualification / negation?** yes: qualification: The source is hedged: 'would likely not provide sufficient information', 'in such situations'. (affects completeness)
* **Acceptable wording:** 'would likely not be sufficient', 'not enough on its own'.
* **Would count as an unsupported claim / error:** (1) Answering yes (sufficient). (2) Stating absolute certainty ('never sufficient') where the source says 'would likely not'.
* **Supporting passages:** `nt-161`: "monitoring only the security posture of information systems would likely not provide sufficient information to determine the overall risk being incurred by organizations"; `nt-161`: "it is expected to be quite common for the security posture of information systems (that is, the risk factors measured within those systems) to reflect only a part of the organizational risk response"
* **Grader notes:** nt-162 repeats the last sentence of nt-161 (overlap).

**Answer 1 (baseline)**  | context order: nt-161, nt-005, nt-213

> No, monitoring only the security posture of information systems would likely not provide sufficient information to determine the overall risk being incurred by organizations. This is because the security posture reflects only a part of the organizational risk response, with significant portions of the response occurring at the organization or mission/business process level [nt-161].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.3344 s; tokens in/out 465/65

**Answer 2 (re-ranked)**  | context order: nt-162, nt-161, nt-005

> No, monitoring only the security posture of information systems would likely not provide sufficient information to determine the overall risk being incurred by organizations. This is because the security posture reflects only a part of the organizational risk response, with significant response actions often occurring at the organization or mission/business process level [nt-161].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.3526 s; tokens in/out 519/64

**Answers textually identical:** no

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## N5  (negation/constraint)

**Question:** Does this guidance cover systems that are designated as national security systems?

**Preregistered gold chunk(s):** nt-010

**Preregistered evidence phrase(s):**
> other than those systems designated as national security systems

**Frozen retrieval outcome:** lenient stumble -> success (best gold rank 4 -> 1; RESTORED into Top 3); strict stumble -> success (Top-3 evidence none -> sufficient; RESTORED into Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-227 | yes (rank 1) | yes (rank 2, was 1) |  |  |
| nt-262 | yes (rank 2) | no (re-ranked rank 5) |  |  |
| nt-274 | yes (rank 3) | no (re-ranked rank 7) |  |  |
| nt-010 | no (was rank 4) | yes (rank 1, was 4) | GOLD | strict-single |
| nt-273 | no (was rank 6) | yes (rank 3, was 6) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-227** (PDF page 58)
> National Security System
> Any information system (including any telecommunications system) used or operated by an agency or by a contractor of an agency, or other organization on behalf of an agency (i) the function, operation, or use of which involves intelligence activities; involves cryptologic activities related to national security; involves command and control of military forces; involves equipment that is an integral part of a weapon or weapons system; or is critical to the direct fulfillment of military or intelligence missions (excluding a system that is to be used for routine administrative and business applications, for example, payroll, finance, logistics, and personnel management applications); or (ii) is protected at all times by procedures established for information that have been specifically authorized under criteria established by an Executive Order or an Act of Congress to be kept classified in the interest of national defense or foreign policy. [44 U.S.C., Sec. 3542]
>
> **nt-262** (PDF page 61)
> Security Policy
> A set of criteria for the provision of security services. [CNSSI No. 4009]
>
> **nt-274** (PDF page 63)
> Tailoring
> The process by which a security control baseline is modified based on: (i) the application of scoping guidance; (ii) the specification of compensating security controls, if needed; and (iii) the specification of organization-defined parameters in the security controls via explicit assignment and selection statements. [NIST SP 800-53, CNSSI No. 4009]
>
> **nt-010** (PDF page 11)
> This publication satisfies the requirements of FISMA and meets or exceeds the information security requirements established for executive agencies by the Office of Management and Budget (OMB) in Circular A-130, Appendix III, Security of Federal Automated Information Resources. The guidelines in this publication are applicable to all federal information systems other than those systems designated as national security systems as defined in 44 U.S.C., Section 3542. The guidelines have been broadly developed from a technical perspective to complement similar guidelines for national security systems and may be used for such systems with the approval of appropriate federal officials exercising policy authority over such systems. State, local, and tribal governments, as well as private sector organizations are encouraged to consider using these guidelines, as appropriate.
>
> **nt-273** (PDF page 62)
> System-Specific Security Control
> A security control for an information system that has not been designated as a common control or the portion of a hybrid control that is to be implemented within an information system. [NIST SP 800-37]
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** Not by default. The guidelines apply to federal information systems other than those designated as national security systems, but they may be used for such systems with the approval of the appropriate federal officials exercising policy authority over them.
* **Expected polarity:** No, unless approved  |  type: yes/no with exception
* **Required points:** (1) Answers 'no / not by default' (national security systems are excluded). (2) States the exception: may be used for them with the approval of appropriate federal officials.
* **Must it mention an exception / qualification / negation?** yes: exception: Excluded by default, but may be used with approval of the appropriate federal officials with policy authority. (affects correctness)
* **Acceptable wording:** 'applicable to all federal information systems other than ... national security systems'.
* **Would count as an unsupported claim / error:** (1) Answering that national security systems are covered by default. (2) Answering a flat no that omits the approval exception (partial). (3) Claiming the guidance is mandatory for national security systems, or naming specific approving officials not in the passage.
* **Supporting passages:** `nt-010`: "The guidelines in this publication are applicable to all federal information systems other than those systems designated as national security systems as defined in 44 U.S.C., Section 3542."; `nt-010`: "may be used for such systems with the approval of appropriate federal officials exercising policy authority over such systems"
* **Grader notes:** A bare 'No' without the approval exception should be at most 'partially correct'.

**Answer 1 (baseline)**  | context order: nt-227, nt-262, nt-274

> The provided context does not contain the answer.

*Objective checks (format only):* cites a passage: False; only supplied passages: False; cites a gold chunk: False; refusal sentence: True; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.2289 s; tokens in/out 462/10

**Answer 2 (re-ranked)**  | context order: nt-010, nt-227, nt-273

> No, the guidelines in this publication are applicable to all federal information systems other than those designated as national security systems. However, they may be used for such systems with the approval of appropriate federal officials exercising policy authority over them [nt-010].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.3189 s; tokens in/out 555/52

**Answers textually identical:** no

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## N6  (negation/constraint)

**Question:** Should we expect an adversary to attack an organization it is not actively targeting?

**Preregistered gold chunk(s):** nt-145

**Preregistered evidence phrase(s):**
> if adversaries are not actively targeting specific organizations or their missions/business functions, adversaries are not expected to initiate threat events

**Frozen retrieval outcome:** lenient success -> success (best gold rank 1 -> 1; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-145 | yes (rank 1) | yes (rank 1, was 1) | GOLD | strict-single |
| nt-168 | yes (rank 2) | no (re-ranked rank 4) |  |  |
| nt-034 | yes (rank 3) | yes (rank 2, was 3) |  |  |
| nt-167 | no (was rank 10) | yes (rank 3, was 10) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-145** (PDF page 42)
> Organizations assess the likelihood of threat event initiation by taking into consideration the characteristics of the threat sources of concern including capability, intent, and targeting (see Task 2-1 and Appendix D). If threat events require more capability than adversaries possess (and adversaries are cognizant of this fact), then the adversaries are not expected to initiate the events. If adversaries do not expect to achieve intended objectives by executing threat events, then the adversaries are not expected to initiate the events. And finally, if adversaries are not actively targeting specific organizations or their missions/business functions, adversaries are not expected to initiate threat events. Organizations use the assessment scale in Table G-2 and provide a rationale for the assessment allowing explicit consideration of deterrence and threat shifting. Organizations can assess the likelihood of threat event occurrence (non-adversarial) using Table G-3 and provide a similar rationale for the assessment.
>
> **nt-168** (PDF page 51)
> Adversary
> Individual, group, organization, or government that conducts or has the intent to conduct detrimental activities. [DHS Risk Lexicon]
>
> **nt-034** (PDF page 17)
> Risk models differ in the degree of detail and complexity with which threat events are identified. When threat events are identified with great specificity, threat scenarios can be modeled, developed, and analyzed. Threat events for cyber or physical attacks are characterized by the tactics, techniques, and procedures (TTPs) employed by adversaries. Understanding adversary-based threat events gives organizations insights into the capabilities associated with certain threat sources. In addition, having greater knowledge about who is carrying out the attacks gives organizations a better understanding of what adversaries desire to gain by the attacks. Knowing the intent and targeting aspects of a potential attack helps organizations narrow the set of threat events that are most relevant to consider.
>
> **nt-167** (PDF page 51)
> Advanced Persistent Threat
> An adversary with sophisticated levels of expertise and significant resources, allowing it through the use of multiple different attack vectors (e.g., cyber, physical, and deception), to generate opportunities to achieve its objectives which are typically to establish and extend its presence within the information technology infrastructure of organizations for purposes of continually exfiltrating information and/or to undermine or impede critical aspects of a mission, program, or organization, or place itself in a position to do so in the future; moreover, the advanced persistent threat pursues its objectives repeatedly over an extended period of time, adapting to a defender’s efforts to resist it, and with determination to maintain the level of interaction needed to execute its objectives. [NIST SP 800-39]
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** No. If adversaries are not actively targeting specific organizations or their missions/business functions, adversaries are not expected to initiate threat events (against them).
* **Expected polarity:** No  |  type: yes/no with negation
* **Required points:** (1) Answers no (not expected). (2) States the condition: adversaries are not actively targeting the organization or its missions/business functions.
* **Must it mention an exception / qualification / negation?** yes: negation: 'Not expected' is a likelihood assessment for adversarial events, not a guarantee; non-adversarial events are separate. (affects correctness)
* **Acceptable wording:** 'are not expected to initiate threat events'.
* **Would count as an unsupported claim / error:** (1) Claiming such an organization has no risk or can never be harmed. (2) Applying the statement to non-adversarial threat events (natural disasters, errors).
* **Supporting passages:** `nt-145`: "if adversaries are not actively targeting specific organizations or their missions/business functions, adversaries are not expected to initiate threat events"

**Answer 1 (baseline)**  | context order: nt-145, nt-168, nt-034

> No, if adversaries are not actively targeting specific organizations or their missions/business functions, they are not expected to initiate threat events. [nt-145]

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.5473 s; tokens in/out 512/33

**Answer 2 (re-ranked)**  | context order: nt-145, nt-034, nt-167

> No, if adversaries are not actively targeting specific organizations or their missions/business functions, they are not expected to initiate threat events. [nt-145]

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.5091 s; tokens in/out 635/33

**Answers textually identical:** yes

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## O1  (other (buried detail))

**Question:** What are the four components of the risk management process?

**Preregistered gold chunk(s):** nt-018, nt-244

**Preregistered evidence phrase(s):**
> (i) framing risk; (ii) assessing risk; (iii) responding to risk; and (iv) monitoring risk
> (i) establishing the context for risk-related activities; (ii) assessing risk; (iii) responding to risk once determined; and (iv) monitoring risk over time

**Frozen retrieval outcome:** lenient success -> success (best gold rank 3 -> 2; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-022 | yes (rank 1) | yes (rank 3, was 1) |  |  |
| nt-019 | yes (rank 2) | yes (rank 1, was 2) |  |  |
| nt-018 | yes (rank 3) | yes (rank 2, was 3) | GOLD | strict-single |

**Passages shown to the LLM (union of the two contexts):**

> **nt-022** (PDF page 14)
> The fourth component of risk management addresses how organizations monitor risk over time. The purpose of the risk monitoring component is to: (i) determine the ongoing effectiveness of risk responses (consistent with the organizational risk frame); (ii) identify risk-impacting changes to organizational information systems and the environments in which the systems operate; and (iii) verify that planned risk responses are implemented and information security requirements derived from and traceable to organizational missions/business functions, federal legislation, directives, regulations, policies, standards, and guidelines are satisfied.
>
> **nt-019** (PDF page 13)
> Figure 1 illustrates the four steps in the risk management process—including the risk assessment step and the information and communications flows necessary to make the process work effectively.
> The first component of risk management addresses how organizations frame risk or establish a risk context—that is, describing the environment in which risk-based decisions are made. The purpose of the risk framing component is to produce a risk management strategy that addresses how organizations intend to assess risk, respond to risk, and monitor risk—making explicit and transparent the risk perceptions that organizations routinely use in making both investment and operational decisions. The risk management strategy establishes a foundation for managing risk and delineates the boundaries for risk-based decisions within organizations.
>
> **nt-018** (PDF page 13)
> 2.1 RISK MANAGEMENT PROCESS
> Risk assessment is a key component of a holistic, organization-wide risk management process as defined in NIST Special Publication 800-39, Managing Information Security Risk: Organization, Mission, and Information System View. Risk management processes include: (i) framing risk; (ii) assessing risk; (iii) responding to risk; and (iv) monitoring risk. Figure 1 illustrates the four steps in the risk management process—including the risk assessment step and the information and communications flows necessary to make the process work effectively.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** Framing risk, assessing risk, responding to risk, and monitoring risk.
* **Expected polarity:** n/a (list of four)  |  type: list
* **Required points:** (1) Names all four components: framing (or establishing the context for) risk, assessing risk, responding to risk, monitoring risk.
* **Must it mention an exception / qualification / negation?** no
* **Acceptable wording:** 'Establishing the context for risk-related activities' is the glossary wording for 'framing risk' (nt-244) and is accepted.
* **Would count as an unsupported claim / error:** (1) Listing a different set (e.g. identify/protect/detect/respond/recover). (2) Adding a fifth component. (3) Replacing 'monitoring' with 'reporting' or 'authorizing'.
* **Supporting passages:** `nt-018`: "Risk management processes include: (i) framing risk; (ii) assessing risk; (iii) responding to risk; and (iv) monitoring risk."; `nt-244`: "(i) establishing the context for risk-related activities; (ii) assessing risk; (iii) responding to risk once determined; and (iv) monitoring risk over time"
* **Grader notes:** Missing one or more of the four = partially correct and incomplete.

**Answer 1 (baseline)**  | context order: nt-022, nt-019, nt-018

> The four components of the risk management process are framing risk, assessing risk, responding to risk, and monitoring risk [nt-018].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.3528 s; tokens in/out 522/30

**Answer 2 (re-ranked)**  | context order: nt-019, nt-018, nt-022

> The four components of the risk management process are framing risk, assessing risk, responding to risk, and monitoring risk [nt-018].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.2994 s; tokens in/out 522/30

**Answers textually identical:** yes

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## O2  (other (buried detail))

**Question:** What example score ranges does the guide give for binning semi-quantitative values?

**Preregistered gold chunk(s):** nt-061

**Preregistered evidence phrase(s):**
> 0-15, 16-35, 36-70, 71-85, 86-100

**Frozen retrieval outcome:** lenient success -> success (best gold rank 1 -> 1; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-061 | yes (rank 1) | yes (rank 1, was 1) | GOLD | strict-single |
| nt-265 | yes (rank 2) | no (re-ranked rank 5) |  |  |
| nt-125 | yes (rank 3) | yes (rank 2, was 3) |  |  |
| nt-126 | no (was rank 7) | yes (rank 3, was 7) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-061** (PDF page 23)
> Finally, semi-quantitative assessments typically employ a set of methods, principles, or rules for assessing risk that uses bins, scales, or representative numbers whose values and meanings are not maintained in other contexts. This type of assessment can provide the benefits of quantitative and qualitative assessments. The bins (e.g., 0-15, 16-35, 36-70, 71-85, 86-100) or scales (e.g., 1-10) translate easily into qualitative terms that support risk communications for decision makers (e.g., a score of 95 can be interpreted as very high), while also allowing relative comparisons between values in different bins or even within the same bin (e.g., the difference between risks scored 70 and 71 respectively is relatively insignificant, while the difference between risks scored 36 and 70 is relatively significant).
>
> **nt-265** (PDF page 62)
> Semi-Quantitative Assessment
> Use of a set of methods, principles, or rules for assessing risk based on bins, scales, or representative numbers whose values and meanings are not maintained in other contexts. [Department of Homeland Security (DHS) Risk Lexicon]
>
> **nt-125** (PDF page 37)
> For each assessable risk factor, the appendices include three assessment scales (one qualitative and two semi-quantitative scales) with correspondingly different representations. Organizations typically define (or select and tailor from the appendices) the assessment scales to be used in their risk assessments, annotating with organizationally-meaningful examples for specific values and defining break points between bins for semi-quantitative approaches. In addition, mission/business owners can provide further annotations with mission/business-specific examples. Organizations can identify different assessment scales to be used in different circumstances. For example, for low-impact information systems, organizations could use qualitative values, while for moderate- and high-impact systems, the most granular semi-quantitative values (0-100) could be used. As discussed in Special Publication 800-39, Task 1-1, Risk Assumptions, organizations vary in the relative weights applied to risk factors.
>
> **nt-126** (PDF page 37)
> Therefore, this guideline does not specify algorithms for combining semi-quantitative values. Organization-specific risk models include algorithms (e.g., formulas, tables, rules) for combining risk factors. If an organization-specific risk model is not provided in the risk management strategy as part of the risk framing step, then part of this task is to specify the algorithms for combining values. Algorithms for combining risk factors reflect organizational risk tolerance (see the supplemental guidance to Task 2-4 for examples). Organization-specific risk models are refined as part of preparation for a risk assessment by: (i) identifying the risk model and the rationale for using it (when multiple organization-specific risk models are provided); (ii) providing additional examples for values of risk factors; and (iii) identifying any assessment-specific algorithms (e.g., algorithms specific to the use of an attack graph analysis technique).
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** The example bins 0-15, 16-35, 36-70, 71-85 and 86-100 (and the example scale 1-10), from Section 2.3 on semi-quantitative assessments.
* **Expected polarity:** n/a (example ranges)  |  type: list of ranges
* **Required points:** (1) Gives the bins 0-15, 16-35, 36-70, 71-85, 86-100 (the scale 1-10 may also be mentioned).
* **Must it mention an exception / qualification / negation?** no
* **Acceptable wording:** The five bins in any format.
* **Would count as an unsupported claim / error:** (1) Giving the appendix bins (e.g. Very High 96-100, High 80-95, Moderate 21-79 ...): these are NOT in the frozen corpus (appendix tables are out of scope). (2) Inventing other ranges.
* **Supporting passages:** `nt-061`: "The bins (e.g., 0-15, 16-35, 36-70, 71-85, 86-100) or scales (e.g., 1-10) translate easily into qualitative terms"
* **Grader notes:** Overlay v1.1 answer-level rule: an answer is correct in scope only if it gives the Section 2.3 bins. An answer that gives the appendix bins should be tagged in reviewer_notes as 'accurate for the full PDF but not supported by the frozen corpus' and is not correct in scope.

**Answer 1 (baseline)**  | context order: nt-061, nt-265, nt-125

> The guide provides the example bin ranges of 0-15, 16-35, 36-70, 71-85, and 86-100 [nt-061].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.3666 s; tokens in/out 609/51

**Answer 2 (re-ranked)**  | context order: nt-061, nt-125, nt-126

> The guide provides the example bin ranges of 0-15, 16-35, 36-70, 71-85, and 86-100 for semi-quantitative assessments [nt-061].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.3366 s; tokens in/out 727/57

**Answers textually identical:** no

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## O3  (other (buried detail))

**Question:** Which external organizations does the guide name as sources of threat information?

**Preregistered gold chunk(s):** nt-121, nt-122

**Preregistered evidence phrase(s):**
> us computer emergency readiness team
> information sharing and analysis centers

**Frozen retrieval outcome:** lenient success -> success (best gold rank 1 -> 1; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-121 | yes (rank 1) | yes (rank 1, was 1) | GOLD | joint-member-1 |
| nt-122 | yes (rank 2) | yes (rank 2, was 2) | GOLD | joint-member-1 |
| nt-285 | yes (rank 3) | no (re-ranked rank 8) |  |  |
| nt-109 | no (was rank 5) | yes (rank 3, was 5) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-121** (PDF page 36)
> Sources of information as described in Tables D-1, E-1, F-1, H-1, and I-1 can be either internal or external to organizations. Internal sources of information that can provide insights into both threats and vulnerabilities can include, for example, risk assessment reports, incident reports, security logs, trouble tickets, and monitoring results. Note that internally, information from risk assessment reports at one tier can serve as input to risk assessments at other tiers. Mission/business owners are encouraged to identify not only common infrastructure and/or support services they depend on, but also those they might use under specific operational circumstances. External sources of threat information can include cross-community organizations (e.g., US Computer Emergency Readiness Team [US-CERT], sector partners (e.g., Defense Industrial Base [DIB] using the DoD-Defense Industrial Base Collaborative Information
>
> **nt-122** (PDF page 37)
> Sharing Environment [DCISE], Information Sharing and Analysis Centers [ISACs] for critical infrastructure sectors), research and nongovernmental organizations (e.g. Carnegie Mellon University, Software Engineering Institute-CERT), and security service providers). Organizations using external sources, consider the timeliness, specificity, and relevance of threat information. Similar to sources of threat information, sources of vulnerability information can also be either internal or external to organizations (see Table F-1). Internal sources can include, for example, vulnerability assessment reports. External sources of vulnerability information are similar to the sources identified above for threat information. As described in Table F-1, information about predisposing conditions can be found in a variety of sources including, for example, descriptions of information systems, environments of operation, shared services, common infrastructures, and enterprise architecture.
>
> **nt-285** (PDF page 65)
> APPENDIX D — THREAT SOURCES
> TAXONOMY OF THREATS SOURCES CAPABLE OF INITIATING THREAT EVENTS
> This appendix provides: (i) a description of potentially useful inputs to the threat source identification task; (ii) an exemplary taxonomy of threat sources by type, description, and risk factors (i.e., characteristics) used to assess the likelihood and/or impact of such threat sources initiating threat events; (iii) an exemplary set of tailorable assessment scales for assessing those risk factors; and (iv) templates for summarizing and documenting the results of the threat source identification Task 2-1. The taxonomy and assessment scales in this appendix can be used by organizations as a starting point with appropriate tailoring to adjust for organization-specific conditions. Tables D-7 and D-8, outputs from Task 2-1, provide relevant inputs to the risk tables in Appendix I.
>
> **nt-109** (PDF page 35)
> Threat Sources
> Organizations determine which types of threat sources are to be considered during risk assessments. Organizations make explicit the process used to identify threats and any assumptions related to the threat identification process. If such information is identified during the risk framing step and included as part of the organizational risk management strategy, the information need not be repeated in each individual risk assessment. Risk assessments can address all types of threat sources, a single broad threat source (e.g., adversarial), or a specific threat source (e.g., trusted insider). Table D-2 provides a sample taxonomy of threat sources that can be considered by organizations in identifying assumptions for risk assessments. Organizational assumptions about threat sources to consider inform Task 2-1.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** US-CERT (cross-community); sector partners such as the DoD Defense Industrial Base Collaborative Information Sharing Environment (DCISE) and the Information Sharing and Analysis Centers (ISACs) for critical infrastructure sectors; research and nongovernmental organizations such as Carnegie Mellon University's Software Engineering Institute-CERT; and security service providers.
* **Expected polarity:** n/a (list)  |  type: list of organizations
* **Required points:** (1) Names US-CERT. (2) Names the sector partners (DCISE for the Defense Industrial Base; ISACs). (3) Names research / nongovernmental organizations (e.g. Carnegie Mellon University SEI-CERT). (4) Names security service providers.
* **Must it mention an exception / qualification / negation?** yes: qualification: The source lists examples ('can include'); the list spans two chunks because of a page-break extraction defect. (affects completeness)
* **Acceptable wording:** Category names or the specific examples.
* **Would count as an unsupported claim / error:** (1) Naming organizations that are not in the passages (e.g. CISA, FBI, MITRE, NSA) as the guide's sources. (2) Presenting internal sources (risk assessment reports, incident reports, logs) as external.
* **Supporting passages:** `nt-121`: "External sources of threat information can include cross-community organizations (e.g., US Computer Emergency Readiness Team [US-CERT]"; `nt-121`: "using the DoD-Defense Industrial Base Collaborative Information"; `nt-122`: "Sharing Environment [DCISE], Information Sharing and Analysis Centers [ISACs] for critical infrastructure sectors)"; `nt-122`: "research and nongovernmental organizations (e.g. Carnegie Mellon University, Software Engineering Institute-CERT), and security service providers"
* **Grader notes:** Joint evidence under overlay v1.1: the sentence is split across nt-121 and nt-122 by a PDF page-break defect, so an answer built from only one chunk is expected to be incomplete (nt-121 alone lacks the ISACs/research/service providers; nt-122 alone lacks US-CERT).

**Answer 1 (baseline)**  | context order: nt-121, nt-122, nt-285

> The guide names cross-community organizations such as the US Computer Emergency Readiness Team (US-CERT), sector partners like the Defense Industrial Base (DIB) using the DoD-Defense Industrial Base Collaborative Information Sharing Environment (DCISE), and Information Sharing and Analysis Centers (ISACs) for critical infrastructure sectors. It also lists research and nongovernmental organizations, such as Carnegie Mellon University and the Software Engineering Institute-CERT, along with security service providers. [nt-121] [nt-122]

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 3 (limit 3: True); latency 0.4433 s; tokens in/out 695/109

**Answer 2 (re-ranked)**  | context order: nt-121, nt-122, nt-109

> The guide names cross-community organizations such as the US Computer Emergency Readiness Team (US-CERT), sector partners like the Defense Industrial Base (DIB) and Information Sharing and Analysis Centers (ISACs), research and nongovernmental organizations like Carnegie Mellon University and the Software Engineering Institute-CERT, and security service providers [nt-121, nt-122].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.369 s; tokens in/out 655/79

**Answers textually identical:** no

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## O4  (other (buried detail))

**Question:** At what point in the system development life cycle should an initial risk assessment ideally be performed?

**Preregistered gold chunk(s):** nt-080

**Preregistered evidence phrase(s):**
> ideally these assessments should be performed in the initiation phase

**Frozen retrieval outcome:** lenient success -> success (best gold rank 3 -> 1; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-001 | yes (rank 1) | no (re-ranked rank 4) |  |  |
| nt-082 | yes (rank 2) | yes (rank 3, was 2) |  |  |
| nt-080 | yes (rank 3) | yes (rank 1, was 3) | GOLD | strict-single |
| nt-081 | no (was rank 8) | yes (rank 2, was 8) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-001** (PDF page 9)
> CAUTIONARY NOTES
> SCOPE AND APPLICABILITY OF RISK ASSESSMENTS
> • Risk assessments are a key part of effective risk management and facilitate decision making at all three tiers in the risk management hierarchy including the organization level, mission/business process level, and information system level.
> • Because risk management is ongoing, risk assessments are conducted throughout the system development life cycle, from pre-system acquisition (i.e., material solution analysis and technology development), through system acquisition (i.e., engineering/manufacturing development and production/deployment), and on into sustainment (i.e., operations/support).
>
> **nt-082** (PDF page 28)
> Risk assessment results at Tier 3 are communicated to organizational entities at Tier 1 and Tier 2.
> Risk assessment activities can be integrated with the steps in the Risk Management Framework (RMF), as defined in NIST Special Publication 800-37. The RMF, in its system development life cycle approach, operates primarily at Tier 3 with some application at Tiers 1 and 2, for example, in the selection of common controls. Risk assessments can be tailored to each step in the RMF as reflected in the purpose and scope of the assessments described in Section 3.1. Risk assessments can also help determine the type of security assessments conducted during various phases of the system development life cycle, the frequency of such assessments, the level of rigor applied during the assessments, the assessment methods used, and the types/number of objects assessed. The benefit of risk assessments conducted as part of the RMF can be realized from both initial assessments and from updated assessments, as described below.
>
> **nt-080** (PDF page 28)
> The Tier 2 context and the system development life cycle determine the purpose and define the scope of risk assessment activities at Tier 3. While initial risk assessments (i.e., risk assessments performed for the first time, rather than updating prior risk assessments) can be performed at any phase in the system development life cycle, ideally these assessments should be performed in the Initiation phase. In the Initiation phase, risk assessments evaluate the anticipated vulnerabilities and predisposing conditions affecting the confidentiality, integrity, and availability of information systems in the context of the planned environments of operation. Such assessments inform risk response, enabling information system owners/program managers, together with mission/business owners to make the final decisions about the security controls necessary based on the security categorization and the environment of operation. Risk assessments are also conducted at later phases in the system development life cycle, updating risk assessment results from earlier phases.
>
> **nt-081** (PDF page 28)
> Risk assessments are also conducted at later phases in the system development life cycle, updating risk assessment results from earlier phases.
> These risk assessment results for as-built or as-deployed information systems typically include descriptions of vulnerabilities in the systems, an assessment of the risks associated with each vulnerability (thereby updating the assessment of vulnerability severity), and corrective actions that can be taken to mitigate the risks. The risk assessment results also include an assessment of the overall risk to the organization and the information contained in the information systems by operating the systems as evaluated. Risk assessment results at Tier 3 are communicated to organizational entities at Tier 1 and Tier 2.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** Ideally in the Initiation phase of the system development life cycle (initial risk assessments can be performed at any phase).
* **Expected polarity:** n/a  |  type: short fact
* **Required points:** (1) States the Initiation phase.
* **Must it mention an exception / qualification / negation?** yes: qualification: 'Ideally' in the Initiation phase; initial assessments can be performed at any phase. (affects completeness)
* **Acceptable wording:** 'Initiation phase'.
* **Would count as an unsupported claim / error:** (1) Naming a different phase (e.g. development/acquisition, operations/maintenance, disposal) as the ideal point. (2) Saying it must be done only in the Initiation phase.
* **Supporting passages:** `nt-080`: "ideally these assessments should be performed in the Initiation phase"; `nt-080`: "initial risk assessments (i.e., risk assessments performed for the first time, rather than updating prior risk assessments) can be performed at any phase in the system development life cycle"
* **Grader notes:** A bare 'Initiation phase' is correct but not complete without the 'ideally / any phase' qualification.

**Answer 1 (baseline)**  | context order: nt-001, nt-082, nt-080

> Ideally, initial risk assessments should be performed in the Initiation phase of the system development life cycle [nt-080].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.2787 s; tokens in/out 674/28

**Answer 2 (re-ranked)**  | context order: nt-080, nt-081, nt-082

> Ideally, initial risk assessments should be performed in the Initiation phase of the system development life cycle [nt-080].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.2818 s; tokens in/out 684/28

**Answers textually identical:** yes

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## O5  (other (buried detail))

**Question:** What should the executive summary of a risk assessment report say about the overall level of risk?

**Preregistered gold chunk(s):** nt-301

**Preregistered evidence phrase(s):**
> describe the overall level of risk

**Frozen retrieval outcome:** lenient success -> success (best gold rank 1 -> 1; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-301 | yes (rank 1) | yes (rank 1, was 1) | GOLD | joint-member-1 |
| nt-240 | yes (rank 2) | no (re-ranked rank 5) |  |  |
| nt-300 | yes (rank 3) | yes (rank 2, was 3) |  | joint-member-1 |
| nt-299 | no (was rank 6) | yes (rank 3, was 6) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-301** (PDF page 92)
> If a subsequent risk assessment, state the circumstances that prompted the update and include a reference to the previous Risk Assessment Report.
> • Describe the overall level of risk (e.g., Very Low, Low, Moderate, High, or Very High).
> • List the number of risks identified for each level of risk (e.g., Very Low, Low, Moderate, High, or Very High).
>
> **nt-240** (PDF page 59)
> Risk Assessment Report
> The report which contains the results of performing a risk assessment or the formal output from the process of assessing risk.
>
> **nt-300** (PDF page 92)
> Executive Summary
> • List the date of the risk assessment.
> • Summarize the purpose of the risk assessment.
> • Describe the scope of the risk assessment.
> - For Tier 1 and Tier 2 risk assessments, identify: organizational governance structures or processes associated with the assessment (e.g., risk executive [function], budget process, acquisition process, systems engineering process, enterprise architecture, information security architecture, organizational missions/business functions, mission/business processes, information systems supporting the mission/business processes).
> - For Tier 3 risk assessments, identify: the information system name and location(s), security categorization, and information system (i.e., authorization) boundary.
> • State whether this is an initial or subsequent risk assessment. If a subsequent risk assessment, state the circumstances that prompted the update and include a reference to the previous Risk Assessment Report.
>
> **nt-299** (PDF page 92)
> APPENDIX K — RISK ASSESSMENT REPORTS
> ESSENTIAL ELEMENTS OF INFORMATION
> This appendix provides the essential elements of information that organizations can use to communicate the results of risk assessments. Risk assessment results provide decision makers with an understanding of the information security risk to organizational operations and assets, individuals, other organizations, or the Nation that derive from the operation and use of organizational information systems and the environments in which those systems operate. The essential elements of information in a risk assessment can be described in three sections of the risk assessment report (or whatever vehicle is chosen by organizations to convey the results of the assessment): (i) an executive summary; (ii) the main body containing detailed risk assessment results; and (iii) supporting appendices.
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** It should describe the overall level of risk (e.g., Very Low, Low, Moderate, High or Very High) and list the number of risks identified for each level of risk.
* **Expected polarity:** n/a  |  type: short fact
* **Required points:** (1) Says the executive summary describes the overall level of risk (with the example levels). (2) (Completeness) also lists the number of risks identified for each level.
* **Must it mention an exception / qualification / negation?** yes: qualification: The levels are examples ('e.g.'). (affects completeness)
* **Acceptable wording:** 'overall level of risk'.
* **Would count as an unsupported claim / error:** (1) Stating a specific risk level as the required content. (2) Inventing further required elements not in the passages (the date, purpose and scope bullets in nt-300 are supported but are not what the question asks).
* **Supporting passages:** `nt-301`: "Describe the overall level of risk (e.g., Very Low, Low, Moderate, High, or Very High)."; `nt-301`: "List the number of risks identified for each level of risk"
* **Grader notes:** Overlay v1.1: strict credit needs nt-300 (the 'Executive Summary' scope) and nt-301 (the fact). An answer drawn from nt-301 alone states the fact without the scope.

**Answer 1 (baseline)**  | context order: nt-301, nt-240, nt-300

> The executive summary should describe the overall level of risk, such as Very Low, Low, Moderate, High, or Very High [nt-301].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.5438 s; tokens in/out 452/33

**Answer 2 (re-ranked)**  | context order: nt-301, nt-300, nt-299

> The executive summary should describe the overall level of risk using categories such as Very Low, Low, Moderate, High, or Very High. It should also list the number of risks identified for each of these specific risk levels [nt-301].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 2 (limit 3: True); latency 0.3135 s; tokens in/out 579/51

**Answers textually identical:** no

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

## O6  (other (buried detail))

**Question:** How many assessment scales does the guide provide for each risk factor, and of what kinds?

**Preregistered gold chunk(s):** nt-125

**Preregistered evidence phrase(s):**
> three assessment scales (one qualitative and two semi-quantitative scales)

**Frozen retrieval outcome:** lenient success -> success (best gold rank 2 -> 1; kept in Top 3); strict success -> success (Top-3 evidence sufficient -> sufficient; kept in Top 3)

| chunk | Answer 1 context? (baseline rank) | Answer 2 context? (re-ranked rank, was baseline rank) | preregistered gold | strict role |
|---|---|---|---|---|
| nt-002 | yes (rank 1) | no (re-ranked rank 10) |  |  |
| nt-125 | yes (rank 2) | yes (rank 1, was 2) | GOLD | strict-single |
| nt-233 | yes (rank 3) | no (re-ranked rank 9) |  |  |
| nt-061 | no (was rank 9) | yes (rank 2, was 9) |  |  |
| nt-068 | no (was rank 10) | yes (rank 3, was 10) |  |  |

**Passages shown to the LLM (union of the two contexts):**

> **nt-002** (PDF page 9)
> • There are no specific requirements with regard to: (i) the formality, rigor, or level of detail that characterizes any particular risk assessment; (ii) the methodologies, tools, and techniques used to conduct such risk assessments; or (iii) the format and content of assessment results and any associated reporting mechanisms. Organizations have maximum flexibility on how risk assessments are conducted and are encouraged to apply the guidance in this document so that the various needs of organizations can be addressed and the risk assessment activities can be integrated into broader organizational risk management processes.
> • Organizations are also cautioned that risk assessments are often not precise instruments of measurement and reflect: (i) the limitations of the specific assessment methodologies, tools, and techniques employed; (ii) the subjectivity, quality, and trustworthiness of the data used; (iii) the interpretation of assessment results; and (iv) the skills and expertise of those individuals or groups conducting the assessments.
>
> **nt-125** (PDF page 37)
> For each assessable risk factor, the appendices include three assessment scales (one qualitative and two semi-quantitative scales) with correspondingly different representations. Organizations typically define (or select and tailor from the appendices) the assessment scales to be used in their risk assessments, annotating with organizationally-meaningful examples for specific values and defining break points between bins for semi-quantitative approaches. In addition, mission/business owners can provide further annotations with mission/business-specific examples. Organizations can identify different assessment scales to be used in different circumstances. For example, for low-impact information systems, organizations could use qualitative values, while for moderate- and high-impact systems, the most granular semi-quantitative values (0-100) could be used. As discussed in Special Publication 800-39, Task 1-1, Risk Assumptions, organizations vary in the relative weights applied to risk factors.
>
> **nt-233** (PDF page 58)
> Quantitative Assessment
> Use of a set of methods, principles, or rules for assessing risks based on the use of numbers where the meanings and proportionality of values are maintained inside and outside the context of the assessment. [DHS Risk Lexicon]
>
> **nt-061** (PDF page 23)
> Finally, semi-quantitative assessments typically employ a set of methods, principles, or rules for assessing risk that uses bins, scales, or representative numbers whose values and meanings are not maintained in other contexts. This type of assessment can provide the benefits of quantitative and qualitative assessments. The bins (e.g., 0-15, 16-35, 36-70, 71-85, 86-100) or scales (e.g., 1-10) translate easily into qualitative terms that support risk communications for decision makers (e.g., a score of 95 can be interpreted as very high), while also allowing relative comparisons between values in different bins or even within the same bin (e.g., the difference between risks scored 70 and 71 respectively is relatively insignificant, while the difference between risks scored 36 and 70 is relatively significant).
>
> **nt-068** (PDF page 26)
> 2.4 APPLICATION OF RISK ASSESSMENTS
> As stated previously, risk assessments can be conducted at all three tiers in the risk management hierarchy—organization level, mission/business process level, and information system level. Figure 4 illustrates the risk management hierarchy defined in NIST Special Publication 800-39, which provides multiple risk perspectives from the strategic level to the tactical level. Traditional risk assessments generally focus at the Tier 3 level (i.e., information system level) and as a result, tend to overlook other significant risk factors that may be more appropriately assessed at the Tier 1 or Tier 2 levels (e.g., exposure of a core mission/business function to an adversarial threat based on information system interconnections).
>

**Grading guide (draft key; derived from the frozen source, not from any answer)**

* **Expected answer:** Three assessment scales for each assessable risk factor: one qualitative and two semi-quantitative.
* **Expected polarity:** n/a  |  type: number and kinds
* **Required points:** (1) States three scales. (2) States one qualitative and two semi-quantitative.
* **Must it mention an exception / qualification / negation?** no
* **Acceptable wording:** 'three scales: one qualitative, two semi-quantitative'.
* **Would count as an unsupported claim / error:** (1) Giving a different number of scales. (2) Naming specific tables or scale values as the three kinds.
* **Supporting passages:** `nt-125`: "the appendices include three assessment scales (one qualitative and two semi-quantitative scales)"

**Answer 1 (baseline)**  | context order: nt-002, nt-125, nt-233

> The guide provides three assessment scales for each assessable risk factor, consisting of one qualitative scale and two semi-quantitative scales [nt-125].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.279 s; tokens in/out 604/33

**Answer 2 (re-ranked)**  | context order: nt-125, nt-061, nt-068

> The guide provides three assessment scales for each assessable risk factor, consisting of one qualitative scale and two semi-quantitative scales [nt-125].

*Objective checks (format only):* cites a passage: True; only supplied passages: True; cites a gold chunk: True; refusal sentence: False; finish_reason stop: True; approx. sentences: 1 (limit 3: True); latency 0.3031 s; tokens in/out 706/33

**Answers textually identical:** yes

**Your grading** (blank):  Answer 1 correct? ____  supported by its passages? ____  complete? ____  unsupported claims: ____   |   Answer 2 correct? ____  supported? ____  complete? ____  unsupported claims: ____   |   better: A1 / A2 / tie  ____

*Enter the structured grades in the CSV row for this query (allowed values: see the legend at the top).*

---

