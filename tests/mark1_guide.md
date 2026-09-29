# Marking guide — Test 1 (Days 1–6)

**Instructor-facing. Do not hand out.**

These tests exist to tell you whether the method is working, not to grade teachers.
The second column is the point: what a wrong answer *tells you*.

| Q | Expected | What a wrong answer tells you |
|---|---|---|
| 1 | Two `print()` calls with text in quotes | Missing quotes → they have not internalised that text needs them. Re-demonstrate on Day 7, briefly |
| 2 | Four variables, four `type()` calls | Confusing `9` and `"9"` → Day 3 did not land. This *will* cause trouble at Day 22 (reading files) |
| 3 | `print(int(answer) + 2)` → `9` | `"7" + 2` → they have not connected Day 3's `TypeError` to Day 4's `int()`. The most common failure at this stage |
| 4 | `print(f"{student_name} has {student_grade} points")` | Used commas instead of an f-string → acceptable, but note it; f-strings are used in every later day |
| 5 | `student_grade = student_grade + 1` | Wrote `student_grade = 7` → **the important miss.** They have not understood that `=` means "assign", not "equals". This blocks the accumulator on Day 11 |
| 6 | One list, then `len()`, `[0]`, `[-1]` | Five separate variables → Day 6's second half did not land. Worth five minutes at the start of Day 7 |
| 7 | `class_grades[2]` → `10` | `class_grades[3]` → counting from one. Extremely common and harmless *if caught*; it becomes `IndexError` everywhere later |
| 8 | (a) `TypeError` (b) cannot add a number to text | Blank → they may be skipping error messages entirely. Ask directly; fear of red text is the single biggest brake on this audience |

## How to read the results as a whole

- **Q3 and Q5 are the two that matter.** They are the ones later days depend on.
- If **more than a third** of the group misses Q5, do not continue to Day 7 as written.
  Spend the first fifteen minutes of Day 7 on `x = x + 1` with the register, and cut the
  Extra tasks to make room.
- If **most of the group** got Q6 right, the Day 6 discovery structure worked. That is
  the first real evidence for or against the method (`RATIONALE.md` §5).
- **Blank answers are data.** A blank Q8 means something different from a wrong Q8.
  Record which questions were left blank, not just which were wrong.

## What to record

For `RATIONALE.md` §5, keep a simple count per question: correct / wrong / blank, and
how many completed the whole test. Nothing more elaborate — a tally on paper is enough,
and it is what the two-month decision will be made on.
