# Python from Zero — a course for school teachers

A 24-session introduction to Python for public-school teachers with **no programming
background**, built to the rules in `PLAN.md` and the house style in
`../tumo_month_workshop/METHODOLOGY.md`.

| | |
|---|---|
| **Participants** | Public-school teachers, any subject. No prior programming. |
| **Format** | 24 sessions × 50 minutes = **20 hours exactly**, 3 per week over 8 weeks |
| **Language** | **Armenian** explanations; **English** everything inside a code cell |
| **Tools** | Anaconda (Python) + VS Code. Two installs on Day 1, nothing after |
| **Dependencies** | **Standard library only.** No `pip`, no venv, no network, no accounts, no cost |
| **Final deliverable** | A working `python main.py` gradebook over the teacher's own class list |

## The idea

Teachers are given a real classroom task, solve it with what they already know, and then —
**in the same session** — meet the tool that collapses it.

| Day | The task | The long way | The tool, same day |
|---|---|---|---|
| 6 | A register for the whole class | one variable per student | **lists** |
| 10 | Mark the whole class | one `if` block per student | **`for` loops** |
| 14 | Find one student's grade | two parallel lists and a position | **dictionaries** |
| 17 | An average on every report card | the same six lines, four times | **functions** |
| 22 | Keep the register after closing | retyping it every time | **files** |

Nothing is introduced as "good practice", and **the course never tells a participant that
the long way was there to make a point** — the task is genuine on its own terms. The full
plan of record is §4 of `PLAN.md`.

Every example is a classroom: students, grades, attendance, averages, report lines. No
`foo`, no `x = 5`, no shopping baskets.

> **Picking this up with a coding agent (Codex, Cursor, Claude Code)?**
> Point it at **`AGENTS.md`** — the contract for agents working here, and the single
> source of truth. `CLAUDE.md`, `.cursorrules` and `.cursor/rules/` all point there and
> carry no rules of their own, so they cannot drift apart.

```
public_school_python/
├── AGENTS.md               <- contract for coding agents  ** agents read this first **
├── PLAN.md                 <- the build specification     ** humans read this first **
├── CURRICULUM.md           <- 24 day agendas, time math, deliverables
├── RATIONALE.md            <- why this method, the risk, the experiment  ** for colleagues **
├── OUTLINE.md              <- what the course is: 4-part outline, short
├── SETUP.md                <- installation, Windows and macOS   (Armenian)
├── CHEATSHEET.md           <- printable reference + the bilingual glossary  (Armenian)
├── INSTRUCTOR_NOTES.md     <- pre-flight, pacing, risks, what to cut
├── ANNOUNCEMENT.md         <- recruitment text for teachers   (Armenian)
├── check_setup.py          <- six checks, run on Day 1
├── notebooks/              <- Days 1-19, one per day  + sample_class.csv
├── solutions/              <- Days 2-19, handed out AFTER each session
├── tests/                  <- 4 fortnightly tests + instructor marking guides
├── guides/                 <- Days 20-24, markdown, read beside the code
├── project/gradebook/      <- the finished reference program
├── src/                    <- notebook SOURCES (see below)
└── tools/                  <- verification scripts
```

## Notebooks are generated — edit `src/`, not `notebooks/`

Nineteen notebooks are nineteen large JSON files, and editing Armenian prose inside JSON
string arrays is unreviewable. So the source of truth is a readable text file per day, and
`notebooks/`, `solutions/` and `tests/` are built from it.

**The whole workflow is two commands:**

```bash
python tools/nbbuild.py     # rebuild notebooks, solutions and tests from src/
python tools/verify.py      # four checks; nothing is done until this passes
```

`nbbuild.py day07` rebuilds one notebook while iterating. The build is idempotent, so
`git status` after a rebuild shows exactly what you changed.

Cell markers: `#%% md`, `#%% code`, `#%% code expected-error: TypeError`,
`#%% code interactive: 9`. The last two become cell metadata, not text the participant
sees.

## Verification

`python tools/verify.py` runs four checks:

| | What it proves |
|---|---|
| agenda arithmetic | every agenda sums to 50; 24 days = 1,200 minutes |
| notebooks execute | all 41 notebooks — lessons, solutions and tests — run cell by cell in order, with `input()` stubbed and every **break-it-on-purpose** cell raising exactly the error it claims. A demo that stops failing is a bug |
| style and language | no Armenian inside any code cell, standard library only, no excluded constructs |
| project end to end | `python main.py` prints 12 students, average 6.5, 2 failing |

## Current state

| Check | Result |
|---|---|
| Agenda arithmetic | ✅ 8 agenda tables, 24 days, 1,200 minutes |
| Notebook execution | ✅ 41 notebooks (19 lessons + 18 solutions + 4 tests), every cell, in order |
| Deliberate errors | ✅ 9 cells raise exactly the error they claim |
| Solutions | ✅ 18 notebooks, every cell runs |
| Tests | ✅ 4 tests + 4 marking guides; every cell runs |
| Project | ✅ `python main.py` end to end; 4 failure paths give one sentence each |
| Style | ✅ stdlib only, no excluded constructs, every identifier English |
| Language rule | ✅ no Armenian anywhere inside a code cell — verified by script |
| **Armenian terminology** | ⏳ **awaiting native-speaker review** (Decision D9) |
| **Fresh-laptop install test** | ⏳ **not yet run** — see `INSTRUCTOR_NOTES.md` §1 |

The last two are stated plainly rather than assumed. Neither can be verified from here.
