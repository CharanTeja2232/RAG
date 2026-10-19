# Stage 6 human-grade summary (blank template)

This is the empty layout. Run `python tools/summarize_human_grades.py` after entering your grades; every cell below is then computed ONLY from the values you typed.

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
| Answer 1 (baseline) | ____ | ____ | ____ | ____ |
| Answer 2 (re-ranked) | ____ | ____ | ____ | ____ |

### C.2 Evidence support (against the passages shown to that answer)

| pipeline | fully supported | partially supported | unsupported | ungraded |
|---|---|---|---|---|
| Answer 1 (baseline) | ____ | ____ | ____ | ____ |
| Answer 2 (re-ranked) | ____ | ____ | ____ | ____ |

### C.3 Completeness

| pipeline | complete | incomplete | ungraded |
|---|---|---|---|
| Answer 1 (baseline) | ____ | ____ | ____ |
| Answer 2 (re-ranked) | ____ | ____ | ____ |

### C.4 Unsupported claims

| pipeline | none | present | ungraded |
|---|---|---|---|
| Answer 1 (baseline) | ____ | ____ | ____ |
| Answer 2 (re-ranked) | ____ | ____ | ____ |

### C.5 Overall judgment

| pipeline | acceptable | borderline | unacceptable | ungraded |
|---|---|---|---|---|
| Answer 1 (baseline) | ____ | ____ | ____ | ____ |
| Answer 2 (re-ranked) | ____ | ____ | ____ | ____ |

### C.6 Paired judgment (`better`)

| A1 better | A2 better | neither clearly better | ungraded |
|---|---|---|---|
| ____ | ____ | ____ | ____ |

### C.7 Paired correctness (queries where BOTH answers have a correctness grade)

Pairs with both graded: ____ of 24.

| category | number of queries | query ids |
|---|---|---|
| both correct | ____ |  |
| only Answer 1 correct | ____ |  |
| only Answer 2 correct | ____ |  |
| both incorrect | ____ |  |
| other (no 'correct'; at least one 'partially correct') | ____ |  |

Cross-tab (rows = Answer 1 grade, columns = Answer 2 grade):

| A1 \ A2 | correct | partially correct | incorrect |
|---|---|---|---|
| correct | ____ | ____ | ____ |
| partially correct | ____ | ____ | ____ |
| incorrect | ____ | ____ | ____ |

Cases the grader marked: 

## D. Descriptive views (not inference)

### D.1 The retrieval failure cases, one by one

| query | category | lenient (base -> rerank) | strict | Answer 1 correct? | Answer 2 correct? | better |
|---|---|---|---|---|---|---|
| A4 | keyword trap | stumble -> success | stumble -> success | ____ | ____ | ____ |
| E3 | exception | stumble -> success | stumble -> success | ____ | ____ | ____ |
| E4 | exception | success -> success | stumble -> success | ____ | ____ | ____ |
| N5 | negation/constraint | stumble -> success | stumble -> success | ____ | ____ | ____ |

### D.2 Human correctness split by the baseline's retrieval outcome

| stratum | pipeline | correct | partially correct | incorrect | ungraded |
|---|---|---|---|---|---|
| baseline retrieval success | Answer 1 (baseline) | ____ | ____ | ____ | ____ |
| baseline retrieval success | Answer 2 (re-ranked) | ____ | ____ | ____ | ____ |
| baseline retrieval stumble or miss | Answer 1 (baseline) | ____ | ____ | ____ | ____ |
| baseline retrieval stumble or miss | Answer 2 (re-ranked) | ____ | ____ | ____ | ____ |

## E. Entry problems

(none)
