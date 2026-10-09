# Marking guide — the final practical

**Sat in session 16. 70 points over seven questions, plus a separately reported eighth.**

This is the sitting that decides whether a participant can teach grade 11.

| Q | Measures | Days | Points |
|---|---|---|---|
| 1 | `pd.read_csv` and the first checks | 16 | 8 |
| 2 | filtering rows | 16 | 8 |
| 3 | `groupby` | 17 | 10 |
| 4 | **a chart: drawn, titled, saved** | 14–15 | **12** |
| 5 | **objects built from a file** | 6–11, 16 | **12** |
| 6 | recursion | 19 | 10 |
| 7 | the silent wrong answer | 21 | 10 |
| | | | **70** |
| 8 | **transfer question — separate** | — | **10** |

## The pass criterion

A participant counts as "can code" when **both** hold:

1. **`python main.py` runs on their own data** — confirmed individually on topic 23, on a
   shared screen, not self-reported
2. **At least 35 of 70** on questions 1–7

Question 8 takes no part in that calculation.

## Question 8, and why it is outside the total

It uses only taught syntax on a problem the course never demonstrates: *which subject
separates 11C from 11B by the most?* Three lines for someone who sees it; impossible for
someone who has only memorised shapes.

**It measures problem-solving, which this course does not teach.** Counting it would
punish participants for not learning something nobody taught them. Mark it:

| | |
|---|---|
| **10** | working code |
| **7** | right approach, small error |
| **5** | **a correct plan in a markdown cell, incomplete code** |
| **0** | blank, or no plan |

Report the distribution, never a pass rate. It is the baseline Part 2 will be measured
against.

## What a wrong answer tells you

| What you see | What it means |
|---|---|
| **Q4 and Q5 strong, Q6 and Q7 weak** | The libraries landed; the thinking did not. **This is the expected shape** and is precisely what Part 2 exists to address. Record it; do not treat it as failure |
| **Q5 weak, Q1–Q3 strong** | pandas is being used as a spreadsheet, not joined to the objects. Revisit topic 16 at the start of Part 2 |
| **Q4 missing a title or `savefig`** | Minus 3 each. Charts that cannot leave the notebook are not charts a school can use |
| **Q7 blank across the group** | One day on debugging was not enough. A finding about the programme — record it for the next cohort |
| **Q6 answered with loops** | 3 points. The question is about recursion, and the loop answer is the thing recursion replaces |
| **Q8 above 5 for more than half** | **Strong signal.** The group is ready for algorithmic work, and Part 2 can start where the roadmap says |

## What to report afterwards

Four numbers, agreed with colleagues **before** the sitting rather than argued about after:

1. How many met both halves of the pass criterion
2. The distribution of question 8, separately
3. How many ran `python main.py` on their own school's data
4. How many withdrew, counted separately from those who failed

> `docs/RATIONALE.md` §5a holds the decision rule those numbers feed into. The rule was
> set before the cohort started, and it does not move because the result is disappointing.
