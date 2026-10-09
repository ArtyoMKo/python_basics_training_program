# Python from Zero — a course for school teachers

A 24-session introduction to Python for public-school teachers with **no programming
background**, built to the rules in `docs/PLAN.md` and the house style in
`../tumo_month_workshop/METHODOLOGY.md`.

| | |
|---|---|
| **Participants** | Public-school teachers, any subject. No prior programming. **Groups of 4–8** |
| **Delivery** | **Remote**, over Google Meet with screen sharing |
| **Structure** | **Two parts.** **Part 1 — coding skills — 2 months** (this repository). **Part 2 — algorithmic tasks and theory — 4 months**, outlined in `docs/ROADMAP.md`, runs only if Part 1 succeeds |
| **Format (Part 1)** | 16 sessions × 120 minutes = **32 hours**, 2 per week over 8 weeks ≈ **2 months** |
| **Language** | **Armenian** explanations; **English** everything inside a code cell |
| **Tools** | Anaconda (Python) + VS Code. Two installs on session 1, nothing after |
| **Dependencies** | **Standard library only.** No `pip`, no venv, no network, no accounts, no cost |
| **Final deliverable** | A working `python main.py` gradebook over the teacher's own class list |

## The idea

Teachers are given a real classroom task, solve it with what they already know, and then —
**in the same session** — meet the tool that collapses it.

| Day | The task | The long way | The tool, same day |
|---|---|---|---|
| 6 | A register for the whole class | one variable per student | **lists** |
| 8 | Find one student's grade | two parallel lists, read by hand | **dictionaries** |
| 11 | Mark the whole class | one `if` block per student | **`for` loops** |
| 17 | An average on every report card | the same six lines, four times | **functions** |
| 22 | Keep the register after closing | retyping it every time | **files** |

Nothing is introduced as "good practice", and **the course never tells a participant that
the long way was there to make a point** — the task is genuine on its own terms. The full
plan of record is §4 of `docs/PLAN.md`.

Every example is a classroom: students, grades, attendance, averages, report lines. No
`foo`, no `x = 5`, no shopping baskets.

> **Picking this up with a coding agent (Codex, Cursor, Claude Code)?**
> Point it at **`AGENTS.md`** — the contract for agents working here, and the single
> source of truth. `CLAUDE.md`, `.cursorrules` and `.cursor/rules/` all point there and
> carry no rules of their own, so they cannot drift apart.

```
public_school_python/
├── README.md               <- you are here
├── AGENTS.md               <- contract for coding agents  ** agents read this first **
│                              (CLAUDE.md, .cursorrules and .cursor/ all point here)
│
├── docs/                   <- all programme documentation
│   ├── PLAN.md                 the build specification   ** humans read this first **
│   ├── CURRICULUM.md           16 sessions, 24 topics, agendas, time math
│   ├── RATIONALE.md            why this method, the risk, and the decision rule
│   ├── ROADMAP.md              the six-month arc: Part 1 built, Part 2 outlined
│   ├── OUTLINE.md              what the course is, short
│   ├── INSTRUCTOR_NOTES.md     pre-flight, pacing, risks, what to cut
│   ├── ENROLMENT.md            the questionnaire sent before a group is formed
│   ├── ANNOUNCEMENT.md         recruitment text, for teachers      (Armenian)
│   └── GOVERNMENT_ASSIGNMENT.md  the state curriculum we prepare teachers for
│
├── handouts/               <- what a participant is given
│   ├── SETUP.md                installation, Windows and macOS     (Armenian)
│   ├── CHEATSHEET.md           printable reference + glossary      (Armenian)
│   └── check_setup.py          six checks, run on session 1
│
├── notebooks/              <- Topics 1-19  (GENERATED)  + sample_class.csv
├── solutions/              <- Topics 2-19, handed out after each session  (GENERATED)
├── guides/                 <- Topics 20-24, markdown, read beside the code
├── tests/                  <- 3 assessments: grader's copy, participant/, marking guides
├── project/gradebook/      <- the finished reference program
├── src/                    <- notebook SOURCES, the thing you edit
└── tools/                  <- builder, verifier and the three checkers
```

> **Root holds only `README.md` and the agent files.** Everything else is foldered by
> audience: `docs/` for the programme, `handouts/` for what a participant receives.
>
> **One rule that is easy to get backwards:** participants receive a *flat folder*, so
> material inside `notebooks/`, `guides/` and `handouts/` refers to files **by bare
> name**. Everything else uses full repo paths.

## Notebooks are generated — edit `src/`, not `notebooks/`

Nineteen notebooks are nineteen large JSON files, and editing Armenian prose inside JSON
string arrays is unreviewable. So the source of truth is a readable text file per day, and
`notebooks/`, `solutions/` and `tests/` are built from it.

**The whole workflow is two commands:**

```bash
python tools/nbbuild.py     # rebuild notebooks, solutions and tests from src/
python tools/verify.py      # four checks; nothing is done until this passes
```

`nbbuild.py day07` rebuilds one notebook while iterating.

The partner dossier is generated too:

```bash
# The partner dossier covers BOTH courses and is built from the repository root:
#   cd .. && python tools/build_partner_docx.py
```

The change log is a **single page in plain language for a non-technical reader** — what
changed, and why it matters, with no programming vocabulary at all. Its baseline is set by
`BASELINE_COMMIT` in the generator, and **its claims about that older version are read
back from git**, not written from memory: a change log that describes the past from memory
is exactly how one misleads.

It **restates** facts rather than linking to them, so it is the one document that can
drift. The build verifies every figure it quotes against the repository — day count,
total minutes, material counts, the sample-class numbers, the five discovery days — and
refuses to write the file if any of them disagree. The build is idempotent, so
`git status` after a rebuild shows exactly what you changed.

Cell markers: `#%% md`, `#%% code`, `#%% code expected-error: TypeError`,
`#%% code interactive: 9`, and `#%% md teacher`. The last three become cell metadata, not
text the participant sees — and `teacher` cells are dropped entirely from the participant
copy of each assessment, so the rubric cannot be handed out by accident.

## Verification

`python tools/verify.py` runs four checks:

| | What it proves |
|---|---|
| agenda arithmetic | every agenda sums to 120; 16 sessions = 1,920 minutes |
| notebooks execute | all 43 notebooks — lessons, solutions and both versions of each assessment — run cell by cell in order, with `input()` stubbed and every **break-it-on-purpose** cell raising exactly the error it claims. A demo that stops failing is a bug |
| style and language | no Armenian inside any code cell, standard library only, no excluded constructs |
| project end to end | `python main.py` prints 12 students, average 6.5, 2 failing |

## Current state

| Check | Result |
|---|---|
| Agenda arithmetic | ✅ 11 agenda tables, 16 sessions, 1,920 minutes = 32 hours |
| Notebook execution | ✅ 43 notebooks (19 lessons + 18 solutions + 3 assessments × 2 versions), every cell, in order |
| Deliberate errors | ✅ 9 cells raise exactly the error they claim |
| Solutions | ✅ 18 notebooks, every cell runs |
| Assessments | ✅ 3 sittings × 2 versions + 3 marking guides; every cell runs |
| Project | ✅ `python main.py` end to end; 4 failure paths give one sentence each |
| Style | ✅ stdlib only, no excluded constructs, every identifier English |
| Language rule | ✅ no Armenian anywhere inside a code cell — verified by script |
| **Armenian terminology** | ⏳ **awaiting native-speaker review** (Decision D9) |
| Session length | ✅ 16 × 120 min = **32 hours**, every agenda verified |
| Topic order | ✅ materials rebuilt — data types precede conditions and loops |
| **Fresh-laptop install test** | ⏳ **not yet run** — see `docs/INSTRUCTOR_NOTES.md` §1 |

The last two are stated plainly rather than assumed. Neither can be verified from here.
