# Marking guide — Test 3, final practical (topic 24)

**Instructor-facing. Hand out `tests/participant/test3_final_practical.ipynb`.**

| | |
|---|---|
| **When** | Topic 24, as a separate sitting |
| **Length** | 90–120 minutes |
| **Total** | **70 points** across questions 1–7, **plus question 8 marked separately** |
| **Covers** | topics 14–24: functions, `return`, dictionaries, files, the four-file program |
| **Variants** | A/B/C for questions 1–7. **Question 8 is the same for everyone** |

**This test is marked in two parts, and the second one matters more.**

> ### This assessment decides who continues to Part 2
>
> Unlike the first two, it has a consequence for the individual. The bar is
> **a working `python main.py` at session 14 and at least half of the 70 points on questions
> 1–7** (`docs/RATIONALE.md` §5a). **Question 8 does not count towards it.**
>
> Mark questions 1–7 with that in mind: this is the one place in the programme where
> consistency between markers matters. Where a borderline answer could go either way,
> **record why you decided**, because a teacher offered Part 1 again deserves a reason
> better than a number.

---

## Part one — questions 1 to 7 (70 points)

| Q | Points | Expected | What a wrong answer tells you |
|---|---|---|---|
| 1 | 8 | Names which file holds `PASS_MARK`, which saves, and why the calculations file does not import the storage file | **The "why" is the one that matters.** If they can answer it, the four-file structure was understood rather than copied. If most cannot, the transition was mechanical and should be reported that way |
| 2 | 12 | A function that computes **and returns** the average from a dictionary's values | Printing instead of returning means `return` never landed — the clearest single failure the course can produce, because the whole project rests on it |
| 3 | 12 | A function that loops a dictionary, applies the pass mark, and **returns a list** | Printing the names instead of returning them is the same miss as Q2 and confirms it |
| 4 | 10 | `line.split(",")`, then `int()` on the second part | Forgetting `int()` after eight weeks means the topic 3–4 type lesson never fully closed. Record it honestly |
| 5 | 8 | Notices the bad row and skips it without stopping the program | Letting the program crash means the validation habit did not form. It is in the project menu, so they have met it repeatedly |
| 6 | 15 | A working feature with the calculation in the right file and the printing in another | The heaviest question. Putting everything in one place still earns most of the marks — the separation is the stretch |
| 7 | 5 | Explains that without saving, changes vanish when the program closes | Short and almost always correct by topic 24 |

---

## Part two — question 8, the transfer question (10 points, **reported separately**)

> *Find the student whose grade is closest to the class average.*

**This is the closest thing the programme has to a measurement of its own hypothesis**
(`docs/RATIONALE.md` §5). It uses no syntax the course did not teach, and the course never
demonstrates it. The question asks for a plain-words plan **before** any code.

**Do not add these 10 points to the 70.** Report them separately, and never as a pass rate.

### Record four things, not one

| Record | Why it matters |
|---|---|
| Did they write the plain-words plan at all? | Attempting a plan is itself evidence of a problem-solving posture |
| Was the plan a **correct approach**, even if the code failed? | Separates "cannot think about the problem" from "cannot yet type it". Completely different findings |
| Did the code work? | The weakest of the four signals, and the easiest to count |
| **Where did they stop, in their own words?** | The most useful qualitative data in the entire programme |

### How to interpret it

| Pattern | What it means for the two-month decision |
|---|---|
| Plan correct, code works | The bet paid off: fluency freed attention for the problem |
| **Plan correct, code incomplete** | **The most important result, and a positive one.** They can reason about a problem; the remaining gap is practice, which is what the next course provides |
| Plan vague, code attempted anyway | Mechanical fluency without problem-solving — the central risk, realised |
| Nothing attempted, or "we did not do this in class" | The strongest negative signal. The course taught recipes, not capability. **Record the exact wording** |

> **A cohort that mostly produces the second pattern is a success**, even though most of
> the code will not run. Marking it as "30% correct" would be the single most misleading
> number this programme could publish.

---

## What goes to the review meeting

Five numbers decide the two-month direction:

1. Test 1 → test 3 change, per participant, with help levels
2. Test 2 Q4 — how many wrote a loop
3. session 14 — how many left with a working `python main.py`
4. Topic 24 — how many programs a colleague ran unaided
5. **Question 8, in the four columns above**, with the participants' own words

Numbers 1–4 say whether the course ran well. **Number 5 says whether the theory was
right.**
