# Marking guide — Test 2 (Days 7–12)

**Instructor-facing. Do not hand out.**

| Q | Expected | What a wrong answer tells you |
|---|---|---|
| 1 | `.append()` on both lists, then `len()` | Appended to one list only → they have not felt the two-list fragility. Good: Day 14 is built on exactly this, so it will land |
| 2 | `if grade >= PASS_MARK:` / `else:` | Hardcoded `4` instead of `PASS_MARK` → minor, but mention it; `settings.py` on Day 21 depends on this habit |
| 3 | Four-branch `elif`, strictest first, tested on four values | Chain in the wrong order → they did not absorb Day 9's silent-failure warning. **Worth repeating out loud**, because it fails without an error |
| 4 | `for student_name in student_names:` | Still indexing `[0]`, `[1]`, `[2]` → Day 10's second half did not land. This is the single most important miss on this test |
| 5 | `for position in range(len(...))` with both lists | Only one list used → they cannot yet combine two sequences. Day 14 fixes this permanently; reassure them |
| 6 | Accumulator, then `total / len(...)`, rounded | `total = 0` placed *inside* the loop → the classic accumulator bug. Show it once on the board; it recurs on Day 16 |
| 7 | Counter with `if grade < PASS_MARK` | Counted everyone → the `if` is missing inside the loop. Usually a structure problem, not a logic one |
| 8 | Empty list, loop, `if`, `.append()` | Appended the grade instead of the name → they lost track of which list they were indexing. Common and self-correcting |
| 9 | "Because the first true condition wins, and `10 >= 4` is true" | Cannot explain it → the most valuable thing to re-teach from this test. A wrong answer with no error is the hardest thing for a beginner to accept |

## How to read the results as a whole

- **Q4 is the headline.** If most of the group wrote a loop, the Day 10 discovery
  structure worked and the method is doing what it claims. If most are still indexing by
  hand, that is the strongest early evidence **against** the approach and should be
  recorded as such.
- **Q6's misplaced `total = 0`** is a structural misunderstanding, not carelessness. Ten
  minutes at the start of Day 13 is well spent if several people hit it.
- **Q9 measures something no other question does:** whether they can reason about code
  that runs and is wrong. That skill is what the whole programme is betting on.

## What to record

Per question: correct / wrong / blank, plus completion rate. Compare Q4 here with Q6 on
Test 1 — together they say whether "feel it, then get the tool" is producing transfer or
just producing recognition.
