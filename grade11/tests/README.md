# Assessments — the grade-11 course

Three sittings. They are **separate from the 24 teaching sessions**, which remain 30
hours exactly, and add roughly 3½ hours on top.

| | Test | When | Length | Points |
|---|---|---|---|---|
| 1 | `test1_diagnostic` | **Before day 1** | 45–60 min | 40 |
| 2 | `test2_midpoint` | **After day 11** | 60–75 min | 50 |
| 3 | `test3_final_practical` | **Day 24** | 90–120 min | 70 **+ 10 reported separately** |

## Two builds of every test

| File | Who gets it |
|---|---|
| `tests/<name>.ipynb` | **the grader.** Rubric, points, and what each question measures |
| `tests/participant/<name>.ipynb` | **the participant.** Questions only |

Both are generated from `src/tests/<name>.py` by `tools/nbbuild.py`. Cells marked
`#%% md teacher` are removed entirely from the participant build.

> **Handing out the grader's copy would give away what each question is worth and what
> it is looking for.** Check which file you are sending.

## Variants

Every question has variants **A, B and C**, equivalent in difficulty and points. The exam
platform gives each participant **one**. Where a question has no variants the heading says
so — those are the ones where a single task is the measurement.

## Record a help level with every score

`3` independent · `2` after one hint · `1` with step-by-step help · `0` did not finish.

On the diagnostic this matters more than the score. Two participants scoring 25 — one
unaided, one after six hints — are at completely different starting points, and the
score alone hides that.

## What the scores are for

**They diagnose the programme, not the teachers**, and participants are told so out loud
before the first sitting. Each test ships a marking guide — `mark1_guide.md`,
`mark2_guide.md`, `mark3_guide.md` — saying what a wrong answer tells the instructor and
what to change in the next session because of it.

## The transfer question

Question 8 of the final practical uses only taught syntax on a problem the course never
demonstrates. It is **never counted towards the pass rate** and is reported separately.
A correct plan with incomplete code is a success. See `docs/RATIONALE.md` §5.
