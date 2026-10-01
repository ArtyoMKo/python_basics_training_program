# AGENTS.md — contract for coding agents working on this repository

**Read this before changing anything. It is short on purpose; everything here is a rule
that is cheap to break by accident and expensive to fix.**

This file is the single source of truth for agents. `CLAUDE.md`, `.cursorrules` and
`.cursor/rules/` all point here and contain no rules of their own, so there is nothing to
keep in sync.

---

## What this repository is

A **24-session Python course for Armenian public-school teachers with no programming
background.** 24 × 50 minutes = 20 hours exactly. Materials are in Armenian; code is in
English. The course ends with each participant running a four-file gradebook program over
their own class list.

It is not a library and has no users other than teachers in a classroom. "Working" means
*a teacher can follow it in 50 minutes*, not *the code runs*.

---

## Read in this order

| # | File | What it gives you |
|---|---|---|
| 1 | **this file** | the rules you must not break |
| 2 | `PLAN.md` | the full build specification — §4 (discovery days), §5 (what is taught and excluded), §7 (notebook conventions) |
| 3 | `CURRICULUM.md` | the 24-day map and every agenda |
| 4 | `RATIONALE.md` | *why* the course is built this way, and what it is risking |

`PLAN.md` wins any disagreement with this file. If you find a contradiction, fix it and
say so.

---

## The build loop — get this wrong and your work is lost

> ### ⛔ `notebooks/`, `solutions/` and `tests/` are GENERATED. Never edit a `.ipynb`.
>
> They are rebuilt from `src/` and your edits will be silently overwritten.

**Two commands. That is the whole workflow.**

```bash
vim src/day10_for_loops.py      # 1. edit the SOURCE

python tools/nbbuild.py         # 2. rebuild   (notebooks + solutions + tests)
python tools/verify.py          # 3. verify    (nothing is done until this passes)
```

`python tools/nbbuild.py day10` rebuilds one notebook when you are iterating.

`verify.py` runs four checks and prints what failed:

| | What it proves |
|---|---|
| agenda arithmetic | every agenda sums to 50; 24 days = 1,200 minutes |
| notebooks execute | all 41 notebooks — lessons, solutions **and** tests — run cell by cell, in order, with `input()` stubbed and every deliberate-error cell raising exactly the error it claims |
| style and language | the language rule, standard library only, excluded constructs, exercise sections present |
| project end to end | `python main.py` prints 12 students, average 6.5, 2 failing |

### The source format

```
#%% md                                  a markdown cell  (Armenian)
#%% code                                a code cell      (English)
#%% code expected-error: TypeError      this cell MUST raise TypeError
#%% code interactive: 9; 6; quit        input() is fed these answers, in order
```

The last two become **cell metadata**, never visible text. A participant must never see
`# interactive` in their notebook.

**The 18 solutions live in one source file**, `src/solutions_source.py`, split per day at
build time — so a reviewer reads them in one pass instead of opening eighteen files.
Cells there are marked `#%% day07 code`.

## The seven rules

### 1. Armenian explains. English codes. No exceptions.

| Where | Language |
|---|---|
| Markdown cells, callouts, exercise instructions, `guides/*.md`, `SETUP.md`, `CHEATSHEET.md` | **Armenian** |
| **Everything inside a code cell** — identifiers, comments, docstrings, string values, printed output | **English** |
| `PLAN.md`, `CURRICULUM.md`, `RATIONALE.md`, `INSTRUCTOR_NOTES.md`, `tools/`, this file | English |

Example names are **transliterated Armenian**: `Ani`, `Davit`, `Nare`, `Aram`, `Mariam`,
`Tigran`, `Lilit`, `Gor`, `Anahit`, `Hayk`, `Sona`, `Vahe`. Familiar data, copyable code.

*Enforced by `check_style.py`: zero Armenian characters inside any code cell.*

### 2. A laborious task and its replacement happen in the SAME session.

Five **discovery days** — 6, 10, 14, 17, 22 — each give a real task, let participants solve
it the long way, then hand them the tool that collapses it, inside one 50 minutes.

| Day | Task | Long way | Tool, same day |
|---|---|---|---|
| 6 | a register for the whole class | one variable per student | **lists** |
| 10 | mark the whole class | one `if` block per student | **`for` loops** |
| 14 | find one student by name | two parallel lists | **dictionaries** |
| 17 | an average on every report card | the same 6 lines, 4 times | **functions** |
| 22 | keep the register after closing it | retyping it | **files** |

**Never split one across two sessions.** Ending a session after the long way and before
the short way is the worst outcome this design can produce. If a day runs long, cut its
Extra tasks — never its second half.

### 3. The task is real. The tedium is never named.

A participant is **never** told they are doing something in order to suffer, or that the
long way was there to make a point.

| ❌ Never write | ✅ Write |
|---|---|
| "Today is a pain day." | "Today we build a register for the whole class." |
| "Write 30 variables so you feel how bad it is." | "We need somewhere to keep each student's name and score." |
| "Notice how awful that was." | *(a table comparing line counts, and nothing else)* |

Before any stretch of repetitive typing, the notebook **promises the shortcut in writing
and names when it arrives** (`PLAN.md` §4.3). Keeping that promise is what makes the long
half acceptable.

### 4. Time is a hard ceiling.

Every agenda sums to **exactly 50**. Teaching never exceeds **12 minutes** in one block.
Hands-on is ≥ 26 of 50. If content does not fit, **cut a topic — never compress one**.

*Enforced by `check_times.py`.*

### 5. Standard library only.

No `pip`, no venv, no third-party imports — **including Anaconda's 300 bundled packages**.
`pandas` would make Day 11 a one-liner and teach a teacher nothing about loops.

Also excluded, deliberately (`PLAN.md` §5): classes, exceptions beyond one `try` in
`main.py`, comprehensions, `lambda`, generators, recursion, regex, type hints, `async`,
decorators, `*args`.

Before adding anything to this list, answer: **which line of the final gradebook needs it?**

*Enforced by `check_style.py`.*

### 6. Three exercise tiers, every notebook.

| Tier | Count | For |
|---|---|---|
| **Պարտադիր** (Required) | 3–4 | everyone, inside the allotted minutes |
| **Լրացուցիչ** (Extra) | **3–4** | whoever finishes Required with 8 minutes left |
| **Մարտահրավեր** (Challenge) | 1–2 | the fastest one or two in the room |

In a room of sixteen adults, three or four finish early **every session**. Extra tasks are
not optional to write. They use only what has already been taught — wider, not further ahead.

Never a blank cell: always a skeleton with a comment saying what goes where.

### 7. Every example is a classroom.

Students, grades, attendance, averages, report lines. **No `foo`, no `x = 5`, no shopping
baskets, no fizzbuzz.** A participant should see their Tuesday morning in any cell.

The grading scale is **1–10, pass mark 4**, written once as `PASS_MARK = 4` from Day 8.

---

## Numbers that are load-bearing

The sample class is engineered, and **prose throughout the course quotes these values**:

```
12 students · grades sum to 78 · average exactly 6.5
2 failing (Aram 3, Hayk 2) · highest Nare 10 · 10 pass
```

**If you change `notebooks/sample_class.csv`, you must grep for every number that was true
before** (`PLAN.md` §11.6). `6.5` in particular is quoted in Day 11 as the moment `float`
stops being abstract.

---

## File map

```
PLAN.md                 the build spec           ← the authority
CURRICULUM.md           24 agendas, time math
RATIONALE.md            why this method, the risk, the experiment   (for colleagues)
OUTLINE.md              what the course is, short                   (for administration)
INSTRUCTOR_NOTES.md     pre-flight, pacing, risks, what to cut
SETUP.md                installation, Windows + macOS               (Armenian)
CHEATSHEET.md           printable reference + bilingual glossary    (Armenian)
ANNOUNCEMENT.md         recruitment text                            (Armenian)
check_setup.py          six checks a participant runs on Day 1

src/                    ← EDIT HERE
  day01…day19.py          notebook sources
  solutions_source.py     all 18 solutions in one reviewable file
  tests/                  the four test sources
notebooks/              generated .ipynb — do not edit
solutions/              generated .ipynb — do not edit
tests/                  generated .ipynb + mark1–4_guide.md (hand-written, instructor only)
guides/                 Days 20–24, markdown, read beside the code  (Armenian)
project/gradebook/      the finished reference program (4 files)
tools/                  nbbuild.py + the three checkers
```

---

## Mistakes specific to this repository

| Mistake | What happens | Instead |
|---|---|---|
| Editing a `.ipynb` directly | silently overwritten on next build | edit `src/`, run `nbbuild.py` |
| Armenian in a code comment or string | `check_style.py` fails | Armenian in markdown only |
| Adding a topic without removing one | an agenda stops summing to 50 | cut something; say what you cut |
| Importing `pandas`/`numpy` "just for this" | `check_style.py` fails | standard library only |
| Writing "now you see how slow that was" | breaks rule 3 | compare line counts in a table |
| Planting a problem to solve next session | breaks rule 2 | resolve it in the same notebook |
| Committing notebooks with outputs | unreadable diffs, stale numbers | outputs stay cleared |
| Changing the sample class casually | silently falsifies prose in several days | grep every quoted number |
| Marking a deliberate-error cell as a bug | it is a teaching device | `expected-error:` cells must raise |

---

## Commands

```bash
python tools/nbbuild.py              # rebuild everything from src/
python tools/nbbuild.py day10        # rebuild one notebook

python tools/verify.py               # all four checks — nothing is done until this passes

# the individual checkers, if you want one in isolation
python tools/check_times.py
python tools/run_all_notebooks.py    # add a day name to run just one
python tools/check_style.py

cd project/gradebook && python main.py    # drive the finished program by hand
```

The build is **idempotent**: running `nbbuild.py` on an unchanged `src/` leaves every
generated file byte-identical, so `git status` after a rebuild tells you exactly what you
changed.

## Open items — do not report these as done

Both are stated plainly in `README.md` and `INSTRUCTOR_NOTES.md`. **Do not quietly close
them.**

1. **The Armenian terminology has not been reviewed by a native speaker.** Every Armenian
   technical term must come from the glossary in `CHEATSHEET.md` §1 and nowhere else —
   that is what makes a later correction a find-and-replace rather than a re-read of
   nineteen files. Terms marked ⚠ are the least certain.
2. **`SETUP.md` has never been tested on a clean machine.** `INSTRUCTOR_NOTES.md` §1 lists
   the three things to confirm; the riskiest is whether VS Code's built-in terminal opens
   with conda active on Windows.

Anything else you cannot verify, **say so plainly and give the command to verify it**.
Do not report completion on unexecuted material.
