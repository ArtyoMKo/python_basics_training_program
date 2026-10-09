# Assessments

Three sittings, designed with our partner colleague and integrated into the course.

| | Test | When | Length | Points | Covers |
|---|---|---|---|---|---|
| 1 | Initial diagnostic | **Before session 1** | 45–60 min | 44 | Nothing — it measures the baseline |
| 2 | Midpoint | **After session 10** | 60–75 min | 50 | Topics 6–13: data types, conditions, loops |
| 3 | Final practical | **Session 18** | 90–120 min | 70 **+ 10 reported separately** | topics 14–24: functions, dictionaries, files, the project |

**These are separate sittings, not session time.** The 18 teaching sessions remain 22½
hours exactly; the assessments add roughly 3½ hours on top.

## Two versions of every test — hand out the right one

```
tests/<name>.ipynb              the grader's copy: questions + rubric + points
tests/participant/<name>.ipynb  what the platform hands out: questions only
```

Both are **generated** by `python tools/nbbuild.py` from `src/tests/`. Cells marked
`#%% md teacher` in the source appear only in the grader's copy, so a participant cannot
be handed the rubric by accident. Never edit the `.ipynb` files.

## How they work

- **Each question has variants A, B, C**, equivalent in difficulty and points. The
  platform gives each participant **one**.
- **Record a help level with every score**: `3` independent, `2` after one hint,
  `1` with step-by-step help, `0` did not finish. On test 1 the help level is more
  informative than the score.
- **The first two diagnose the programme, not the teachers.** They exist to show where to
  slow down and whether the method is working. Participants are told this.
- **The third is also a gate.** It decides who continues to Part 2, on the bar in
  `docs/RATIONALE.md` §5a — a working `python main.py` at session 16 plus at least half of
  questions 1–7. **Question 8 does not gate.** Participants are told this *before the
  course starts*, not when the paper is handed out.
- Only the course cheatsheet is open. No internet, no AI, no asking a neighbour.

## The marking guides

`mark1_guide.md`, `mark2_guide.md`, `mark3_guide.md` — instructor only.

Their second column is the point: not whether the answer was right, but **what a wrong
answer tells you**, and what to change in the next session because of it. Three results
change what happens next:

| Result | Consequence |
|---|---|
| Test 1 Q1 at help level 0–1 for several people | Add a helper to session 1, or run a setup clinic first |
| **Test 2 Q4 — did they write a loop?** | The first real evidence for or against the whole method |
| Test 3 Q2/Q3 — printing instead of returning | `return` never landed, and the project rests on it |

## Question 8 of the final test

The transfer question: *find the student whose grade is closest to the class average.* No
untaught syntax, never demonstrated. It is marked separately, never reported as a pass
rate, and **a correct plan with incomplete code counts as a success**. See
`mark3_guide.md` and `docs/RATIONALE.md` §5.
