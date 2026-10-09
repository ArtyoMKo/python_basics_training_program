# Build plan — the grade-11 course

**Status board for the agent building this course.** It exists so that a session that
loses its context can pick up exactly where the last one stopped. Update the Status column
as each step completes; never mark a step done before `tools/verify.py` passes.

The method, the file layout, the source format, the exercise tiers and the language rule
are **copied from the grade-10 course without change** (`../grade10/AGENTS.md`). What
differs is the entry point, the subject matter, and two rules that invert (§2 below).

---

## 0. What this course is

A teacher who has finished the grade-10 course can write a loop, a dictionary and a
function, and can run a four-file program over their own class list. They have **never
seen a class, an object, a library, a comprehension or a keyword argument.**

This course takes them from there to being able to teach **grade 11**, and to teach the
half of grade 10's second semester the first course did not reach.

| | |
|---|---|
| **Entry** | the grade-10 course, and nothing else |
| **State topics** | **15, 16, 17, 18, 19, 20, 21, 22, 24** — not 23 (git), deferred |
| **Shape** | 24 sessions × 75 min = 30 hours · 3 a week × 8 weeks · remote · groups of 4–8 |
| **Exit** | a teacher can write and explain a class, read a library's output, and produce a report with statistics and a chart from their school's own data |

**Part 2 of this course** — algorithmic recursion, complexity, algorithm design, bigger
projects — is a vision in `ROADMAP.md`, not built, and runs only if Part 1 succeeds.

### The compression, stated honestly

| | Pupil hours | Teacher hours | Ratio |
|---|---|---|---|
| Grade-10 course | topics 1–14 ≈ 118 | 30 | 3.9 : 1 |
| **This course** | topics 15–22, 24 ≈ **110** | 30 | **3.7 : 1** |

The same ratio as a course that works on paper. That is the whole argument for believing
30 hours is enough — not that the material is easier, because it is not.

---

## 1. The spine

Grade 10's spine was **one class**: a register, then a four-file gradebook over it.

This course's spine is **the whole school**. The teacher arrives with a program that
handles one class in dictionaries. The school asks for three classes, five subjects, a
term of grades, and a report with charts. Every tool in this course arrives because that
demand makes the previous way untenable — in the same session, never the next.

```
one class, dictionaries        ← what they bring from grade 10
   │
   ├─ the same function, six slightly different calls    → default and keyword arguments
   ├─ the same filter loop, written six times            → comprehensions
   ├─ a student is now 9 fields, and a typo is silent    → CLASSES
   ├─ Teacher needs everything Student has, plus more    → INHERITANCE
   ├─ statistics over 600 numbers, by loop               → NUMPY
   ├─ a bar chart drawn with print() and asterisks       → MATPLOTLIB
   ├─ the school's CSV parsed by hand, 40 lines          → PANDAS
   └─ a structure whose depth you do not know in advance → RECURSION
   │
the school report tool         ← what they leave with
```

---

## 2. The two rules that invert

Everything in `../grade10/AGENTS.md` holds here **except these**, and both inversions are
deliberate:

| Grade 10 | Here | Why |
|---|---|---|
| **Standard library only.** No third-party import, ever | **Anaconda's bundled packages**: `numpy`, `matplotlib`, `pandas`. Nothing else | They are state topics 15, 20 and 21. A teacher must demonstrate them |
| **No classes.** `class` fails the style check | **Classes are the centre of the course** — days 9–14 | State topics 18 and 19, 22 pupil-hours |

**`pip install` still requires a decision, and the answer is: not to follow the course.**
Anaconda ships `numpy`, `matplotlib` and `pandas` already, so nothing in days 1–20 needs
the network. `pip`, `requirements.txt` and environments are **taught as a topic** on day
21, against one small package, and that is the only session that needs internet. This
keeps the grade-10 promise — *the course runs with the wifi off* — true for 23 of 24 days.

**Still excluded, and this list is load-bearing:**

decorators · generators · context managers of their own · `@property` · `dataclasses` ·
multiple inheritance · abstract base classes · `__slots__` · custom exception classes ·
`sklearn`, `pytorch`, `tensorflow` (**named once on day 24 and never used**) · regex ·
type hints · `async` · testing frameworks · databases · **git** (topic 23, deferred by
decision) · algorithmic recursion — factorial, Fibonacci, the call stack, complexity —
which is **Part 2**, not this course.

Before adding anything to the taught list, answer the grade-10 question in its grade-11
form: **which line of the final school report tool needs it?**

---

## 3. Steps

| # | Step | Produces | Status |
|---|---|---|---|
| **1** | Repository split into `grade10/` + `grade11/` + `shared/`; grade 10 re-verified in its new home | root `README.md`, `AGENTS.md`, this tree | ✅ done |
| **2** | **This plan**, the course contract, and the full day map with agendas | `BUILD_PLAN.md`, `AGENTS.md`, `CURRICULUM.md` | ✅ done — `PLAN.md` outstanding |
| **3** | Tooling: copy `tools/` from grade 10 and invert the two rules in `check_style.py`; new sample data | `tools/*.py` | ✅ done |
| **4** | The sample school — engineered numbers that prose may quote, as `6.5` is quoted in grade 10 | `data/school.csv`, numbers table in `AGENTS.md` | ✅ done |
| **5** | Days 1–8 sources — setup, functions, comprehensions | `src/day01…day08.py` | ☐ |
| **6** | Days 9–14 sources — classes and inheritance | `src/day09…day14.py` | ☐ |
| **7** | Days 15–21 sources — NumPy, Matplotlib, pandas, environments | `src/day15…day21.py` | ☐ |
| **8** | Days 22–24 — recursion, debugging, the project | `src/day22.py`, `guides/day23…day24.md` | ☐ |
| **9** | Solutions, all in one reviewable file | `src/solutions_source.py` | ☐ |
| **10** | Three assessment sittings, grader and participant builds | `src/tests/*.py`, `tests/mark*_guide.md` | ☐ |
| **11** | The reference project — the school report tool | `project/school_report/` | ☐ |
| **12** | Participant-facing documents | `handouts/SETUP.md`, `CHEATSHEET.md`, `docs/ANNOUNCEMENT.md`, `docs/ENROLMENT.md` | ☐ |
| **13** | Colleague-facing documents | `docs/RATIONALE.md`, `docs/OUTLINE.md`, `docs/INSTRUCTOR_NOTES.md`, `docs/ROADMAP.md` | ☐ |
| **14** | Full verification; coverage audit against `../shared/GOVERNMENT_ASSIGNMENT.md` | green `verify.py`, a §7-style audit table | ☐ |
| **15** | Partner document covering both courses | `partners/` | ☐ |

### Rules for working through them

- **Steps 5–8 are the expensive ones.** Build and verify day by day; do not write eight
  days and then run the checker.
- **A step is done when `verify.py` is green**, not when the files exist.
- **Never edit a `.ipynb`.** Edit `src/`, run `tools/nbbuild.py`.
- When a step forces a decision that changes what is taught, **stop and record it** in
  `PLAN.md` §15 rather than deciding silently.
