# Stage 6 human-grade summary

Computed from `/Users/charan/Documents/LanguageModels&Agents/RAGAssignment/results/nist_stage6_human_grades.csv`. Every number in section C is computed ONLY from explicit human-entered values; a blank cell is counted as *ungraded*, never guessed.

**Three separate metrics. They are never merged:** (A) frozen retrieval outcomes, (B) objective format checks, (C) your human grades of the answers.

No significance test is computed. N = 24 queries, one generation per query and pipeline, one grader (see the limitations notes).

## A. Retrieval success (frozen Stage 4/5 result; not a human grade)

| rule | pipeline | success | stumble | miss |
|---|---|---|---|---|
| lenient | baseline | 21 | 3 | 0 |
| lenient | reranked | 24 | 0 | 0 |
| strict | baseline | 20 | 4 | 0 |
| strict | reranked | 24 | 0 | 0 |

## B. Objective format checks of the answers (automatic; NOT evidence of factual correctness)

| check | Answer 1 (baseline) | Answer 2 (re-ranked) |
|---|---|---|
| cites a passage | 21 / 24 | 24 / 24 |
| cites only supplied passages | 21 / 24 | 24 / 24 |
| cites a preregistered gold chunk | 21 / 24 | 24 / 24 |
| is the refusal sentence | 3 / 24 | 0 / 24 |
| finish reason stop | 24 / 24 | 24 / 24 |
| within three sentence limit | 24 / 24 | 24 / 24 |

## C. Human grades (from the values you entered)

### C.1 Correctness

| pipeline | correct | partially correct | incorrect | ungraded |
|---|---|---|---|---|
| Answer 1 (baseline) | 0 | 0 | 0 | 24 |
| Answer 2 (re-ranked) | 0 | 0 | 0 | 24 |

### C.2 Evidence support (against the passages shown to that answer)

| pipeline | fully supported | partially supported | unsupported | ungraded |
|---|---|---|---|---|
| Answer 1 (baseline) | 0 | 0 | 0 | 24 |
| Answer 2 (re-ranked) | 0 | 0 | 0 | 24 |

### C.3 Completeness

| pipeline | complete | incomplete | ungraded |
|---|---|---|---|
| Answer 1 (baseline) | 0 | 0 | 24 |
| Answer 2 (re-ranked) | 0 | 0 | 24 |

### C.4 Unsupported claims

| pipeline | none | present | ungraded |
|---|---|---|---|
| Answer 1 (baseline) | 0 | 0 | 24 |
| Answer 2 (re-ranked) | 0 | 0 | 24 |

### C.5 Overall judgment

| pipeline | acceptable | borderline | unacceptable | ungraded |
|---|---|---|---|---|
| Answer 1 (baseline) | 0 | 0 | 0 | 24 |
| Answer 2 (re-ranked) | 0 | 0 | 0 | 24 |

### C.6 Paired judgment (`better`)

| A1 better | A2 better | neither clearly better | ungraded |
|---|---|---|---|
| 0 | 0 | 0 | 24 |

### C.7 Paired correctness (queries where BOTH answers have a correctness grade)

Pairs with both graded: 0 of 24.

| category | number of queries | query ids |
|---|---|---|
| both correct | 0 |  |
| only Answer 1 correct | 0 |  |
| only Answer 2 correct | 0 |  |
| both incorrect | 0 |  |
| other (no 'correct'; at least one 'partially correct') | 0 |  |

Cross-tab (rows = Answer 1 grade, columns = Answer 2 grade):

| A1 \ A2 | correct | partially correct | incorrect |
|---|---|---|---|
| correct | 0 | 0 | 0 |
| partially correct | 0 | 0 | 0 |
| incorrect | 0 | 0 | 0 |

Cases the grader marked: a1 better: none; a2 better: none; neither clearly better: none

## D. Descriptive views (not inference)

### D.1 The retrieval failure cases, one by one

| query | category | lenient (base -> rerank) | strict | Answer 1 correct? | Answer 2 correct? | better |
|---|---|---|---|---|---|---|
| A4 | keyword trap | stumble -> success | stumble -> success | ungraded | ungraded | ungraded |
| E3 | exception | stumble -> success | stumble -> success | ungraded | ungraded | ungraded |
| E4 | exception | success -> success | stumble -> success | ungraded | ungraded | ungraded |
| N5 | negation/constraint | stumble -> success | stumble -> success | ungraded | ungraded | ungraded |

### D.2 Human correctness split by the baseline's retrieval outcome

| stratum | pipeline | correct | partially correct | incorrect | ungraded |
|---|---|---|---|---|---|
| baseline retrieval success | Answer 1 (baseline) | 0 | 0 | 0 | 21 |
| baseline retrieval success | Answer 2 (re-ranked) | 0 | 0 | 0 | 21 |
| baseline retrieval stumble or miss | Answer 1 (baseline) | 0 | 0 | 0 | 3 |
| baseline retrieval stumble or miss | Answer 2 (re-ranked) | 0 | 0 | 0 | 3 |

## E. Entry problems

(none)

