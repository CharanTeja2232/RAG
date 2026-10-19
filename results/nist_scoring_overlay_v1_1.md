# NIST strict-scoring overlay v1.1: decision summary and change log

*Created 2026-10-18 16:02 IST. v1.0 (`results/nist_scoring_overlay_v1.json`) and the preregistration are preserved byte-for-byte. No retrieval result was used for any decision here: none exists yet.*

| Item | Value |
|---|---|
| **Overlay v1.1 SHA-256** | `180c80dee8cf63207866cea103ec3c7c0e5dbeb80c9fd10d06b7e0460b8ab9ea` |
| Supersedes | v1.0, `c99f3cfe7cd7ec5898982fa499e9457dd2f2ed364a6a839c2424d7cd55d1a2ef` |
| Frozen corpus SHA-256 | `795fb2a6e043a28dc39d01e2db30d4b05d74ca1535df4ca7519d386b15f0fc92` |
| Preregistration SHA-256 (unchanged) | `cb7a05a13b16fd0aacbe310e7903df4f5ee34137d3cac3ebf85714ec197ace33` |

## 1. Decisions

**E1.** `nt-053` is independently sufficient: it states the rule ('the worst-case impact establishes an upper bound for the overall risk') and the exception ('this upper bound for risk may fail to apply'). `nt-054` contributes only the explanation of why the bound can fail. Its first sentence is an overlap copy of nt-053's last sentence, and a search shows that the chunk never states the rule or identifies the bound. Leaving E1 unchanged would have been **inconsistent** with E2 (nt-147 excluded) and N4 (nt-162 excluded), so v1.1 excludes `nt-054` from strict credit. If it is the only gold chunk in the Top 3, the case is reported as *partial*, never as strict success.

**A5.** `nt-042` and `nt-144` are retained because each independently states the contrast between the likelihood of initiation and the likelihood of adverse impact (exact passages in the JSON). The optional joint set `nt-145 + nt-146` is **removed**: those chunks describe how each likelihood is *assessed* (different inputs), not how the two chances differ, and the answer from them needs two chunks plus an inference.

## 2. Strict rule for every question

| Q | Preregistered gold (lenient, PRIMARY) | Strict rule (SECONDARY) |
|---|---|---|
| A1 | nt-063 | any of nt-063 |
| A2 | nt-235 | any of nt-235 |
| A3 | nt-185 | any of nt-185 |
| A4 | nt-040 | any of nt-040 |
| A5 | nt-043, nt-044 | any of nt-044, nt-042, nt-144 (excluded fragment: nt-043) |
| A6 | nt-035, nt-281 | any of nt-035, nt-281 |
| E1 | nt-053, nt-054, nt-153 | any of nt-053, nt-153 (excluded fragment: nt-054) |
| E2 | nt-146, nt-147 | any of nt-146 (excluded fragment: nt-147) |
| E3 | nt-286 | any of nt-286 |
| E4 | nt-163, nt-164 | ALL of nt-163 + nt-164 |
| E5 | nt-105 | any of nt-105 |
| E6 | nt-076, nt-077 | any of nt-076, nt-077 |
| N1 | nt-126 | any of nt-126 |
| N2 | nt-002 | any of nt-002 |
| N3 | nt-131 | any of nt-131 |
| N4 | nt-161, nt-162 | any of nt-161 (excluded fragment: nt-162) |
| N5 | nt-010 | any of nt-010 |
| N6 | nt-145 | any of nt-145 |
| O1 | nt-018, nt-244 | any of nt-018, nt-244 |
| O2 | nt-061 | any of nt-061 |
| O3 | nt-121, nt-122 | ALL of nt-121 + nt-122 |
| O4 | nt-080 | any of nt-080 |
| O5 | nt-301 | ALL of nt-300 + nt-301 |
| O6 | nt-125 | any of nt-125 |

## 3. Consistency check over all 34 gold-chunk pairs

Sufficiency ratings are those of the saved review sheet. Rule: a chunk rated *Sufficient* is a strict single; a *Partially sufficient* or *Insufficient* chunk is never a strict single (it is a joint member or an excluded fragment). Result: **0 problems**.

| Q | Chunk | Review-sheet rating | v1.1 strict role |
|---|---|---|---|
| A1 | nt-063 | Sufficient | single |
| A2 | nt-235 | Sufficient | single |
| A3 | nt-185 | Sufficient | single |
| A4 | nt-040 | Sufficient | single |
| A5 | nt-043 | Partially sufficient | excluded fragment |
| A5 | nt-044 | Sufficient | single |
| A6 | nt-035 | Sufficient | single |
| A6 | nt-281 | Sufficient | single |
| E1 | nt-053 | Sufficient | single |
| E1 | nt-054 | Partially sufficient | excluded fragment |
| E1 | nt-153 | Sufficient | single |
| E2 | nt-146 | Sufficient | single |
| E2 | nt-147 | Insufficient | excluded fragment |
| E3 | nt-286 | Sufficient | single |
| E4 | nt-163 | Partially sufficient | joint member |
| E4 | nt-164 | Partially sufficient | joint member |
| E5 | nt-105 | Sufficient | single |
| E6 | nt-076 | Sufficient | single |
| E6 | nt-077 | Sufficient | single |
| N1 | nt-126 | Sufficient | single |
| N2 | nt-002 | Sufficient | single |
| N3 | nt-131 | Sufficient | single |
| N4 | nt-161 | Sufficient | single |
| N4 | nt-162 | Partially sufficient | excluded fragment |
| N5 | nt-010 | Sufficient | single |
| N6 | nt-145 | Sufficient | single |
| O1 | nt-018 | Sufficient | single |
| O1 | nt-244 | Sufficient | single |
| O2 | nt-061 | Sufficient | single |
| O3 | nt-121 | Partially sufficient | joint member |
| O3 | nt-122 | Partially sufficient | joint member |
| O4 | nt-080 | Sufficient | single |
| O5 | nt-301 | Partially sufficient | joint member |
| O6 | nt-125 | Sufficient | single |

## 4. Evaluation protocol frozen with this overlay

* **Primary metric:** the preregistered lenient rule (any preregistered gold chunk in the Top 3). **Secondary sensitivity analysis:** the strict rule above. Both are reported for every query.
* Partial evidence is reported as partial and never counted as strict success.
* No change to the corpus, queries, gold labels, models or parameters after observing any evaluation outcome. Any such change would break a pinned hash.

## 5. Change log

| Version | Date | Change |
|---|---|---|
| v1.0 | see results/nist_scoring_overlay_v1.md | Seven questions addressed (A5, E2, E4, N4, O2, O3, O5). |
| v1.1 | 2026-10-18 16:02 IST | A5: optional joint set nt-145 + nt-146 removed. E1: nt-054 excluded from strict credit for consistency. Everything else identical to v1.0. |