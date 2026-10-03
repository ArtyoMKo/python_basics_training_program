# Marking guide — Test 1, initial diagnostic (before day 1)

**Instructor-facing. Never hand this out, and never hand out `tests/test1_diagnostic.ipynb`
either — give participants `tests/participant/test1_diagnostic.ipynb`.**

| | |
|---|---|
| **When** | Before day 1, as a separate sitting |
| **Length** | 45–60 minutes |
| **Total** | **44 points**, across 6 questions |
| **Variants** | A/B/C per question — each participant gets **one**, assigned by the platform |
| **Self-assessment** | 4 statements at the end, scored 1–5. **Not added to the total** |

## What this test is for

**It is not a Python exam.** Nobody has been taught anything yet. It measures baseline
digital confidence, data reasoning, and how much support each person will need.

It also gives the programme something it would otherwise lack: **a before-measurement**.
Everything after this is change, not just an endpoint — see `RATIONALE.md` §5.

## Record two numbers per question, not one

Alongside the score, record the **help level**, exactly as the test's own rules state:

| Help level | Meaning |
|---|---|
| `3` | Worked it out independently |
| `2` | Completed after one hint |
| `1` | Completed with step-by-step help |
| `0` | Did not finish |

**The help level is more useful than the score on this test.** Two participants can both
reach 30/44; the one who needed step-by-step help on four questions is a different
teaching problem from the one who worked alone and ran out of time.

## Question by question

| Q | Points | Expected | What a weak answer tells you |
|---|---|---|---|
| 1 | 6 | They find the cell, change one value, run it | Cannot operate the editor at all. **This is the single most important signal in the test** — it predicts a hard day 1 and tells you who to sit near the front |
| 2 | 8 | Reads a value out of a small table and applies the stated rule | Difficulty here is about reading structured data, not about code. Expect the register work on days 6–7 to need extra time |
| 3 | 8 | Applies a threshold rule to three numbers by hand | This is conditional thinking with no Python in it. A participant who struggles here will struggle on days 8–9, and that is worth knowing six sessions early |
| 4 | 6 | Separates text from whole number from decimal | Predicts trouble on day 3 and, much later, on day 22 when text from a file has to become a number |
| 5 | 8 | Explains in their own words what a repeated instruction does | Measures whether the idea of repetition is already there. Strong answers here mean day 10 will land easily |
| 6 | 8 | Notices that the data is inconsistent and asks a clarifying question | The most advanced thing on the test. Not noticing is entirely normal and costs nothing later |

## How to read the cohort as a whole

- **Q1 at help level 0 or 1 for several people** → add a second helper to day 1, or run an
  optional setup clinic beforehand. Day 1 is the highest-risk session in the programme and
  this is your advance warning.
- **Q3 weak across the room** → do not shorten day 9. The `elif` ordering trap will need
  the full session.
- **A wide spread** → plan the pairing from day 3 deliberately, rather than letting it
  happen.
- **Everyone scoring high** → the cohort is stronger than the course assumes. Say so in
  the report; it changes how the final result should be read.

## What to keep for the final report

Per participant: score per question, help level per question, total, and the four
self-assessment numbers. The self-assessment is repeated nowhere else, so it is only
useful if it is kept — the interesting comparison is **confidence before against capability
after**.
