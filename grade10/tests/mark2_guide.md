# Marking guide — Test 2, midpoint (after session 10)

**Instructor-facing. Hand out `tests/participant/test2_midpoint.ipynb`.**

| | |
|---|---|
| **When** | After topic 13, as a separate sitting |
| **Length** | 60–75 minutes |
| **Total** | **50 points**, across 6 questions |
| **Covers** | topics 6–13: lists, `if`/`else`, `elif`, `for`, accumulators, filtering |
| **Variants** | A/B/C per question — each participant gets **one** |

## What this test is for

Everything up to topic 13 is mechanical fluency: can they write and fix basic code with
lists, conditions and loops, unaided? **This is the first point at which the programme's
central claim is testable**, and the most important single result in it is Q4.

Record the help level (`3`–`0`) alongside the score, as in test 1.

## Question by question

| Q | Points | Expected | What a wrong answer tells you |
|---|---|---|---|
| 1 | 8 | `.append()` to **both** lists, then correct one grade by index | Appending to one list only is the two-list fragility the course deliberately exposes on topic 8, which the midpoint already covers. **Not a failure** — note it |
| 2 | 7 | `if grade >= PASS_MARK:` / `else:` | Hardcoding the number instead of using `PASS_MARK` is minor here, but it is the habit `settings.py` depends on at session 16. Mention it individually |
| 3 | 8 | Spots that the chain is in the wrong order and reorders it, strictest first | **The only question with no error message to guide them.** Not spotting it means they cannot yet reason about code that runs and is wrong — the hardest thing for a beginner to accept, and worth re-teaching out loud |
| 4 | 10 | A `for` loop over the register, with the condition inside it | **This is the headline result of the whole test.** A loop means the topic 11 discovery structure worked. Hand-written repetition for every student means it did not |
| 5 | 9 | `total = 0` before the loop, accumulate inside, divide after, `round` | `total = 0` placed *inside* the loop is the classic accumulator bug. Show it once on the board; it recurs at topic 15 |
| 6 | 8 | Empty list, loop, condition, `.append()`, print | Appending the grade rather than the name means they lost track of which list they were indexing. Common, and self-correcting |

## The result that decides what happens next

> **Q4 is the measurement.** If most of the cohort wrote a loop, the "do it the long way,
> then get the tool" structure is producing transfer and the second half of the course can
> run as designed.
>
> If most are still writing one block per student after nine sessions, that is **the
> strongest early evidence against the approach** and must be recorded as such in the
> report — not explained away.

Two other decisions come out of this test:

- **Q5 wrong for several people** → spend ten minutes at the start of topic 14 on where
  `total = 0` goes.
- **Q3 wrong across the room** → revisit the `elif` ordering trap before topic 14, where <!--ref-ok-->
  report logic starts stacking up.

## What to keep for the final report

Per participant: score and help level per question, and the total. Separately, the single
number that matters most: **how many wrote a loop in Q4**.
