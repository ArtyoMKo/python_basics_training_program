# AGENTS.md — the grade-11 course

**Read this before changing anything in `grade11/`. It is the authority here.**

The repository root's `AGENTS.md` lists the seven rules both courses share. This file
holds what is true *only* here. Where they disagree, this file wins inside `grade11/`.

`docs/BUILD_PLAN.md` is the build specification and wins any disagreement with this file.
`docs/BUILD_PLAN.md` is the step board — read it to find out what is built and what is not.

---

## What this course is

**The second of two courses for Armenian public-school teachers.** It takes a teacher who
has finished the grade-10 course and prepares them to teach **grade 11** — state topics
15–22 and 24 of ministry order 1875 (`../shared/GOVERNMENT_ASSIGNMENT.md`).

| | |
|---|---|
| **Entry** | the grade-10 course, and **nothing beyond it** |
| **Shape** | 16 sessions × 120 min = **32 hours** · 2 a week × 8 weeks · remote · groups of 4–8 |
| **Spine** | one class in dictionaries → **the whole school**, as objects, with statistics and charts |
| **Excluded** | git (topic 23, deferred) · algorithmic recursion, which is Part 2 |

### What a participant knows on session 1, and what they do not

They can write a `for` loop, a dictionary, a function with `return`, read and write a
file, and run a four-file program. **They have never seen a class, an object, a library,
a comprehension or a keyword argument**, and none of it may be assumed. Those are taught
from zero, practically, exactly as the grade-10 course teaches variables and loops.

> **The mistake that would ruin this course is assuming fluency the grade-10 course did
> not produce.** "They have met functions, so `*args` is a small step" is the shape of
> that mistake. It is not a small step. Teach it as if it were new, because it is.

---

## The two rules that invert from grade 10

| Grade 10 | **Here** |
|---|---|
| Standard library only | **`numpy`, `matplotlib`, `pandas` — the three Anaconda already ships. Nothing else** |
| `class` fails the style check | **Classes are the centre of the course**, topics 6–11 |

**Nothing in topics 1–19 needs the network.** Anaconda bundles all three libraries, so no
participant installs anything to follow the course. `pip`, `requirements.txt` and
environments are *taught as a topic* on topic 20, against one small package — the only
session that needs internet.

Still excluded, deliberately (`docs/BUILD_PLAN.md` §2): decorators · generators · `@property` ·
`dataclasses` · multiple inheritance · abstract base classes · custom exception classes ·
`sklearn`, `pytorch`, `tensorflow` (**named once in session 16, never used**) · regex · type
hints · `async` · testing frameworks · databases · **git** · factorial, Fibonacci, the
call stack and complexity, which are **Part 2**.

Before adding anything, answer: **which line of the final school report tool needs it?**

---

## The build loop

> ### ⛔ `notebooks/`, `solutions/` and `tests/` are GENERATED. Never edit a `.ipynb`.

```bash
python tools/nbbuild.py         # rebuild from src/
python tools/verify.py          # nothing is done until this passes
```

The source format is identical to grade 10's:

```
#%% md                                  a markdown cell  (Armenian)
#%% code                                a code cell      (English)
#%% code expected-error: KeyError       this cell MUST raise KeyError
#%% code interactive: 9; 6; quit        input() is fed these answers, in order
#%% md teacher                          grader-only; dropped from the participant build
```

---

## The seven discovery topics

**Topics 4, 6, 9, 12, 14, 16, 19** — sessions 3, 5, 7, 9, 10, 11, 13. Each gives a real task, lets participants do it the long
way, then hands them the tool that collapses it — **inside one session, never across
two.**

| Day | Task | Long way | Tool, same day |
|---|---|---|---|
| 4 | six reports, six filters | the same 5-line loop, six times | **comprehensions** |
| 6 | a student is now nine fields | a dict per student, and a typo is silent | **classes** |
| 9 | teachers as well as students | copy the whole Student class and edit it | **inheritance** |
| 12 | the term's statistics | mean, spread and extremes by loop, over 180 numbers | **NumPy** |
| 14 | show the head teacher | a bar chart drawn with `print()` and asterisks | **Matplotlib** |
| 16 | the school's own CSV | 40 lines of `split(",")` and `try` | **pandas** |
| 19 | a school of unknown depth | a loop for each level, and one level too few | **recursion** |

**Never split one across two sessions.** If a day runs long, cut its Extra tasks — never
its second half.

---

## Numbers that are load-bearing

The sample school is engineered, and prose throughout the course quotes these values. If
`data/school.csv` changes, **grep for every number that was true before**, then rebuild.

```
36 students  ·  3 classes (11A 11B 11C)  ·  5 subjects  ·  180 grades
grades total 1260  ·  school average exactly 7.0  ·  pass mark 4
18 failing grades = exactly 10%  ·  12 students at risk = exactly one third

subject averages   Informatics 7.56 (highest)   History 7.22   Mathematics 7.03
                   Armenian 6.92                Physics 6.28 (lowest)
class averages     11A 6.98      11B 6.33       11C 7.68
```

`data/school.csv` is **generated** — `python tools/make_school.py` rebuilds it, and
`--check` fails if it no longer matches the figures above. `verify.py` runs that check, so
a silent drift is impossible. The file deliberately contains **a header, one blank line
and one field with a comma inside it**, because topic 16's long half must break on all three.

---

## Mistakes specific to this course

| Mistake | Instead |
|---|---|
| Assuming grade-10 fluency the course did not produce | teach every new syntax as new |
| `import sklearn`, `seaborn`, `scipy`, anything beyond the three | the three Anaconda ships, nothing else |
| A `pip install` needed before topic 20 | topics 1–19 run with the wifi off |
| Teaching recursion with factorial or Fibonacci | recursion here walks a real nested school; the algorithms are Part 2 |
| A class introduced before the dict version has failed | topic 6's long half must break first, visibly |
| Writing "now you see how slow that was" | compare line counts in a table, and say nothing |
| An Armenian class name in a code cell | **transliterate**: `11A`, not `11Ա` — the same decision grade 10 made for `Ani` |
| Editing a `.ipynb` | edit `src/`, run `nbbuild.py` |
