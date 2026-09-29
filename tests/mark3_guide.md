# Marking guide — Test 3 (Days 13–18)

**Instructor-facing. Do not hand out.**

| Q | Expected | What a wrong answer tells you |
|---|---|---|
| 1 | `class_grades["Nare"]` | Looped to find it → works, but they have not seen that a dictionary removes the search. Mention it; do not mark it wrong |
| 2 | Assignment, reassignment, `del` | Used `.append()` → they are mixing lists and dictionaries. Worth five minutes; it will break Day 22 |
| 3 | `if "Vahe" in class_grades:` / `else:` | Program stops with `KeyError` → they did not guard the lookup. **This exact pattern is in `storage.py`**; flag it before Day 21 |
| 4 | `for name, grade in class_grades.items():` | Used `.keys()` then looked up each value → acceptable; note it but do not correct in front of the room |
| 5 | Counter with `if` inside an `.items()` loop | — |
| 6 | `def average_of(grades):` … `return round(..., 1)` | Used `print` instead of `return` → **the important miss.** Day 18's whole point. The four-file project is impossible without it |
| 7 | `def has_passed(grade): return grade >= PASS_MARK` | Wrote `if ...: return True else: return False` → correct, just longer. Do not mark down; mention the shorter form once |
| 8 | Empty list, loop, `if`, `.append()`, `return` | Printed the list instead of returning it → same miss as Q6, and it confirms it |
| 9 | Loop with `break` on `"quit"` and `.isdigit()` guard | Crashed on `"nine"` → the validation habit has not formed. It is in the project menu, so it will be met again |
| 10 | "One prints and gives you nothing back; the other returns a value you can compare" | Cannot articulate it → re-teach before Day 20. **Do not start the transition until this is understood by most of the room** |

## How to read the results as a whole

- **Q6, Q8 and Q10 are one question asked three ways:** do they understand `return`?
  If the group fails all three, **Day 19 should be spent on `return`, not on
  consolidation.** That is a legitimate and planned use of Day 19.
- Q3 is the direct rehearsal for `storage.py`. A failure here predicts a hard Day 22.
- This is the last test before the transition. It is the last cheap chance to find out
  that something fundamental is missing.

## What to record

Per question: correct / wrong / blank, plus completion. Then one judgement in a sentence:
**is this group ready for `.py` files?** If the honest answer is no, say so in the notes
now — Day 21 is where that becomes visible to everyone, including them.
