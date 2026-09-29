# Marking guide — Test 4 (Days 19–24)

**Instructor-facing. Do not hand out.**

**This test is marked in two separate parts, and the second one matters more.**

## Part one — Questions 1–7

| Q | Expected | What a wrong answer tells you |
|---|---|---|
| 1 | Function that computes and **returns** the average | Printed instead of returned → `return` never landed. Record it: it is the clearest single failure of the notebook phase |
| 2 | `def has_passed(grade, pass_mark=PASS_MARK)`, called both ways | Default parameter omitted → minor; it appears in the project but they can read it |
| 3 | A printing function that calls `has_passed` inside | Recomputed the comparison inline → they can write functions but not yet compose them. Normal at 20 hours |
| 4 | `line.split(",")`, then `int(parts[1])` | Forgot `int()` → the Day 3/4 type lesson still incomplete after eight weeks. Worth noting honestly |
| 5 | Loop over `lines[1:]`, split, build the dictionary | Included the header row → they did not think about the data, only the code. Very common and worth one sentence of feedback |
| 6 | (a) `settings.py` (b) `storage.py` (c) `grades.py` (d) so you can test calculations without a file (e) `cd` and `python file.py` | **(d) is the one that matters.** If they can answer it, the four-file structure was understood rather than copied. If most cannot, the transition was mechanical |
| 7 | `KeyError`; the key is not in the dictionary; fix with `in` | — |

## Part two — Question 8: the transfer question

**Mark this separately and record it separately. It is the closest thing the programme
has to a measurement of its own hypothesis** (`RATIONALE.md` §5).

The task — *find the student whose grade is closest to the class average* — uses **no
syntax the course did not teach** and **was never demonstrated**. It needs: compute the
average, then loop comparing distances.

Record **four things**, not one:

| Record | Why |
|---|---|
| Did they **write the plain-words approach** before the code? | The question explicitly asks for it. Attempting the plan at all is evidence of a problem-solving posture |
| Did the plan describe a **correct approach**, even if the code failed? | This separates "cannot think about the problem" from "cannot yet type it". They are completely different findings |
| Did the code **work**? | The weakest of the four signals, but the easiest to count |
| **Where did they stop**, in their own words? | The most useful qualitative data in the entire programme |

### How to interpret it

| Pattern | What it means for the decision |
|---|---|
| Plan correct, code works | The bet paid off. Coding fluency freed attention for the problem |
| **Plan correct, code incomplete** | **The most important result, and a positive one.** They can now reason about a problem; the remaining gap is practice, which is exactly what the next course would give |
| Plan vague, code attempted anyway | Mechanical fluency without problem-solving. The bet's central risk, realised |
| Nothing attempted, or "we did not do this in class" | The strongest negative signal. Record the exact wording — it says the course taught recipes, not capability |

A group that mostly produces the **second** pattern is a success, even though most of the
code will not run. Do not report Question 8 as a pass rate.

## What to record overall

Part one: per question correct / wrong / blank. Part two: the four columns above, per
participant, plus their own words about where they stopped.

Take this, the four completion rates, the Day 21 `python main.py` count and the Day 24
fresh-laptop result to the review meeting. Those five numbers are the two-month decision.
