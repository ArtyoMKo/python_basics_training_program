# Python for grade 11 — a course for teachers

The second of two courses for Armenian public-school teachers. It takes a teacher who has
finished the [grade-10 course](../grade10/README.md) and prepares them to teach **grade
11** — state topics 15–22 and 24 of ministry order 1875
([`../shared/GOVERNMENT_ASSIGNMENT.md`](../shared/GOVERNMENT_ASSIGNMENT.md)).

| | |
|---|---|
| **Entry** | the grade-10 course, and nothing beyond it |
| **Format (Part 1)** | 16 sessions × 120 minutes = **32 hours**, 2 per week over 8 weeks ≈ **2 months** |
| **Delivery** | remote, over Google Meet, in groups of **4–8** |
| **Language** | Armenian explains · English codes |
| **Tools** | Anaconda, VS Code, Jupyter — **nothing to install**, and no network for 23 of 24 days |
| **Final deliverable** | a five-file program that reads the teacher's own school file and produces a term report with charts |

## What a participant does not know on session 1

They can write a `for` loop, a dictionary and a function, and can run a four-file program.
**They have never seen a class, an object, a library, a comprehension or a keyword
argument.** None of it is assumed; all of it is taught from zero, practically, the way
the grade-10 course teaches variables and loops.

## The spine

Grade 10's was one class. This one is **the whole school** — and every tool arrives
because the previous way stopped working, in the same session, never the next.

| Day | The task | The long way | The tool, same day |
|---|---|---|---|
| 4 | six reports the head teacher wants | the same filter loop, six times | **comprehensions** |
| 6 | a student is now nine fields | a dict per student, and a typo is silent | **classes** |
| 9 | teachers as well as students | copy the whole class and edit it | **inheritance** |
| 12 | the term's statistics | mean and spread by loop, over 600 numbers | **NumPy** |
| 14 | show the head teacher | a bar chart made of asterisks | **Matplotlib** |
| 16 | the school's own CSV | 22 lines of `split(",")` | **pandas** |
| 19 | a school of unknown depth | a loop per level, and one level too few | **recursion** |

## The two rules that invert from grade 10

| Grade 10 | Here | Why |
|---|---|---|
| standard library only | **`numpy`, `matplotlib`, `pandas`** | state topics 15, 20 and 21 — a teacher has to demonstrate them, and Anaconda already ships all three |
| `class` fails the style check | **classes are the centre of the course** | state topics 18 and 19, 22 pupil-hours |

`pip` is **taught as a topic on topic 20**, not required to follow the course. topics 1–19 run
with the wifi off.

## Where things are

```
grade11/
├── AGENTS.md                 the contract for anyone changing this course
├── docs/
│   ├── BUILD_PLAN.md         the step board — what is built and what is not
│   ├── CURRICULUM.md         16 sessions, 24 topics, every agenda, the time arithmetic
│   ├── OUTLINE.md            what the course is, short            (for administration)
│   ├── RATIONALE.md          why it is built this way, and the risk  (for colleagues)
│   ├── INSTRUCTOR_NOTES.md   pre-flight, pacing, what to cut
│   ├── ROADMAP.md            this course's Part 2 — a vision, not written
│   ├── ANNOUNCEMENT.md       recruitment text                     (Armenian)
│   └── ENROLMENT.md          who to admit, and what to tell them
├── handouts/                 SETUP.md · CHEATSHEET.md · check_setup.py   (Armenian)
├── src/                      ← EDIT HERE. day01…day21, solutions_source, tests/
├── notebooks/ solutions/ tests/    generated — never edit a .ipynb
├── guides/                   topics 22–24, markdown                 (Armenian)
├── project/school_report/    the finished five-file program
├── data/school.csv           generated and engineered
└── tools/                    nbbuild · verify · the three checkers · make_school
```

## Building it

```bash
python tools/nbbuild.py      # rebuild notebooks, solutions and tests from src/
python tools/verify.py       # nothing is done until this passes
```

`verify.py` runs five checks:

| | What it proves |
|---|---|
| agenda arithmetic | every agenda sums to 120; 16 sessions = 1,920 minutes |
| notebooks execute | all 48 — lessons, solutions and both builds of each exam — run cell by cell, with `input()` stubbed and every deliberate-error cell raising exactly what it claims |
| style and language | the language rule, the three allowed libraries, excluded constructs, exercise sections present |
| the sample school | the engineered figures the course prose quotes |
| project end to end | `python main.py` prints 36 students, average 7.0, 12 at risk |

## The sample school

Engineered, not random, because prose throughout quotes it:

```
36 students · 3 classes (11A 11B 11C) · 5 subjects · 180 grades
total 1260 · school average exactly 7.0 · pass mark 4
18 failing grades = 10% · 12 students at risk = one third
Informatics 7.56 highest · Physics 6.28 lowest
```

It carries a header, one blank line and one field with a comma inside it, because day
16's long half has to break on all three. `tools/make_school.py --check` fails if any of
it drifts, and `verify.py` runs that check.

## Status

**Part 1 is built and verified. Nothing has been taught to a cohort.** Part 2 —
algorithmic recursion, complexity, algorithm design, bigger projects — is a vision in
`docs/ROADMAP.md` and runs only if Part 1 meets its success criterion.
