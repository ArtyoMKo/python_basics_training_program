# Build Plan — Python from Zero, for School Teachers

**What this is:** the complete build specification for a new training programme in
`public_school_python/`. It plays the same role for this course that `METHODOLOGY.md`
plays for the TUMO workshops: read it fully before writing any material, and build
against it rather than against memory of this conversation.

**Relationship to `METHODOLOGY.md`:** that document is the house style and is still
binding — the spiral structure, "run it first, name it after", straw-man-then-improve,
measured claims, callout vocabulary, verification discipline, definition of done. This
plan states the **course-specific rules** and, where it **overrides** the methodology,
says so explicitly and gives the reason. Overrides are collected in §14.

**Status:** draft v3. **Every decision is closed** (§15) and the build can start.

| | Decision | Where it lands |
|---|---|---|
| **Language** | Armenian prose, English code | §7.7 |
| **Python** | Anaconda, `base` environment, never activated by hand | §9.1 |
| **Editor** | **VS Code, from Day 1 to Day 24. One tool, all course.** | §9.1 |
| **Grades** | 1–10 scale, pass mark 4 | §6.2 |
| **Repository** | `git@github.com:AIrtyoMKo/python_basics_training_program.git` | §9.3 |

---

## 0. The simplicity rule

The instruction governing this whole build: **keep it as simple as possible.** Where two
designs both work, take the one with fewer moving parts, even when the other is better
engineering. Concretely, this course has:

| One | Not |
|---|---|
| One editor — VS Code — from Day 1 to Day 24 | Jupyter in a browser, then an editor later |
| One Python — Anaconda's `base` | venv, conda environments, activation steps |
| One terminal — the one inside VS Code | Anaconda Prompt, PowerShell, Terminal.app |
| One folder — `python_course/` in Documents | A folder per day, a folder per phase |
| One idea per day, named in the file name | Two related things "while we're here" |
| One new built-in per concept | The three ways Python can do it |
| Four files in the final project | Five, or a package |
| Zero installs after Day 1 | `pip install` anything, ever |
| One language per place — Armenian explains, English codes | Armenian inside a code cell |

**When reviewing any artefact, the first question is: what can be removed?** A teacher who
never programmed does not need the second-best way to do something. They need one way that
works, that they can remember on a Tuesday, without notes.

---

## 1. The course in one paragraph

Public-school teachers, with no programming background, learn Python from installing it to
writing a small program they actually use. Twenty-four 50-minute sessions over two months.
Every example is about a classroom — students, grades, attendance, averages, reports —
and the course ends with each participant running a gradebook program over their own
(anonymised) class list, from a terminal, on their own laptop.

The teaching engine is **do it the long way, then learn the short way — in the same
session**. Participants are given a real classroom task, solve it with what they already
know, and then, twenty minutes later, meet the tool that collapses it. Nothing is
introduced as "good practice"; everything arrives as the thing that shortens work they
have just finished doing. The task is always genuine — a register, a pass list, a report
card — and the course never tells a participant that the long way was there to make a
point.

---

## 2. Audience and constraints

| | |
|---|---|
| **Participants** | Public-school teachers. Any subject. |
| **Prior programming** | **None assumed.** Not "basic Python" — none. Some will not know what a file extension is. |
| **Prior computer use** | Everyday: email, a browser, Word, a school information system. Comfortable typing. |
| **Delivery** | **Remote**, over Google Meet with screen sharing. Not on site. |
| **Machines** | **Their own laptop**, which they must have for the whole course. Mixed Windows and macOS. Possibly no admin rights. Checked at enrolment (`ENROLMENT.md`). See §12 risks. |
| **Language** | Materials in **Armenian**; code, keywords and identifiers in English (§7.7) |
| **Format** | 24 sessions × **75 minutes** = 1,800 minutes = 30 hours. *Session plans are still written to 50 minutes — see the note below.* |
| **Schedule** | 3 sessions per week × 8 weeks. After the cohort adapts, possibly 2 a week, or 3 of 50 minutes |
| **Group size** | **4–8**, one instructor. Fewer than 4 and they cannot discuss; more than 8 and remote teaching stops working |
| **Part** | Part 1 of 6 months. Part 2 is outlined in `ROADMAP.md` and runs only if Part 1 succeeds |
| **Between sessions** | ~2 days. One optional 10-minute practice task per day; nothing required. |
| **Final deliverable** | A working `python main.py` gradebook over the participant's own class list |

### What this audience changes, compared with the TUMO courses

| TUMO workshop | This course | Consequence |
|---|---|---|
| 13–18, already program | Adults, never programmed | Python **is** the subject, not the medium |
| 16 identical lab Macs prepared by IT | Mixed personal Windows/Mac laptops | Installation is Day 1's entire content, and is the single biggest risk |
| 120-minute lessons | **50-minute** lessons | One idea per session, and the agenda has no slack |
| External paid API, keys, vendor abstraction | **Standard library only** | No `pip`, no venv, no `requirements.txt`, no keys, no network, no cost |
| Materials in English for English-schooled teens | **Armenian prose, English code** | A beginner cannot learn a spoken language and a programming language at once |
| Fast students get an extra challenge | Fear, not boredom, is the failure mode | Every session must be completable by the slowest person; extras are genuinely optional |

**Vocabulary rule, because the word collides.** In this course the participants *are*
teachers. So:

- **participant** — the person taking the course (never "student" — that word is reserved)
- **student** — a child in the participant's own class, i.e. the data in every example
- **instructor** — the person delivering the course

This applies to file names too: instructor-facing notes are `INSTRUCTOR_NOTES.md`, not
`TEACHER_NOTES.md`.

---

## 3. Course architecture

### Three phases

| Phase | Days | Tool | Purpose |
|---|---|---|---|
| **Notebook** | 1–19 | Jupyter notebooks, one per day | Learn the language, cell by cell |
| **Transition** | 20–21 | VS Code, `.py` files, terminal | Reorganise working code into a real program |
| **Project** | 22–24 | VS Code + terminal | Own data, own feature, finish and show |

Two days for the transition rather than the methodology's one, because 50 minutes cannot
hold both "here is what a `.py` file is" and "here are four modules". Day 20 is one file;
Day 21 is the split. **Neither may be cut** (§13).

### Time budget

- 24 × 50 = **1,200 minutes**. Hard ceiling.
- Every day's agenda sums to **exactly 50**, verified by script (§11.1).
- If content does not fit, **cut a topic**. Never compress one, never run over — these are
  working adults and 50 minutes is 50 minutes.

> ### ⏳ Session length is changing, and the plans have not caught up
>
> Sessions will run **75 minutes**, decided after the colleagues' meeting. **Every agenda
> in `CURRICULUM.md` is still written to 50 minutes** and `check_times.py` still verifies
> against 50.
>
> Rebuilding the 24 agendas to 75 minutes is the next piece of work. The extra 25 minutes
> per session is **not** for more teaching — the 12-minute ceiling stands — it goes to
> hands-on work and to the second half of the discovery days, which is where the method
> actually lives.
>
> Until that rebuild happens, **treat the minute counts below as proportions, not
> absolutes**.

### The standard 50-minute shape

Every day in the notebook phase uses this agenda unless stated otherwise:

| # | Activity | Min |
|---|---|---|
| 1 | Recap, and last time's retrospective question | 5 |
| 2 | **Teach:** the new idea — ends with something running | 12 |
| 3 | **Run together:** the notebook's example cells, cell by cell | 15 |
| 4 | **Do it yourself:** the exercises | 15 |
| 5 | Retrospective: where we got to, what breaks next | 3 |
| | **Total** | **50** |

**Hands-on is 30 of 50 minutes — 60%.** That is the floor, not the target. Activity 2 is
capped at 12 minutes and may never exceed 15 in any variant agenda. This is the rule the
review should check first: *if a day talks for more than 15 minutes, it is wrong.*

### The discovery shape

Days 6, 10, 14, 17 and 22 — where a tool arrives to replace work done the same session —
use this instead:

| # | Activity | Min |
|---|---|---|
| 1 | Recap | 5 |
| 2 | **Teach:** today's task, and the only way we can do it so far | 7 |
| 3 | **Do it the long way:** the real task, with shipped boilerplate | 13 |
| 4 | **Teach:** the tool that shortens it | 9 |
| 5 | **Do the same task again**, with the tool. Compare | 13 |
| 6 | Retrospective | 3 |
| | **Total** | **50** |

Teaching is 16 minutes but **split into two blocks of 7 and 9** — neither approaches the
15-minute ceiling, and the second one lands on a participant who now wants it. Hands-on
is 26 of 50.

Days 1, 20, 21, 23 and 24 have bespoke agendas (installation, the transition, the build
day and the showcase). Each still sums to 50.

### Per-day deliverable

Every day ends with one concrete thing the participant **has**, not understands. Written
in the curriculum as:

> **📦 By the end of today you have:** a notebook that prints your own class register,
> with one deliberate mistake you made on purpose and then fixed.

### Spiral: each day makes the previous day insufficient

This is the backbone and §4 sets it out in full.

---

## 4. Discovery days — the plan of record

Every concept arrives as relief from work the participant has just done **in the same
session**. This table is the course; build against it.

| Day | The real task they are given | The laborious way they do it first | The tool that arrives, same day |
|---|---|---|---|
| **6** | Build a register that holds the whole class | One variable per student, ~30 of them | **Lists** |
| **10** | Mark the whole class pass/fail | One `if`/`else` block per student | **`for` loops** |
| **14** | Look up one student's grade by name | Two parallel lists and a position counter | **Dictionaries** |
| **17** | Put an average on every report card | The same six lines written four times | **Functions** |
| **22** | Keep the register after closing the program | Retyping it every time | **Files** |
| **20–21** | Give the program to a colleague | Explaining which cells to run in what order | **`.py` files and the terminal** |

### 4.1 Same session, always

**The laborious version and its replacement happen in the same 50 minutes.** A participant
never goes home having only done the slow thing. They go home having done the slow thing
*and* seen it collapse.

This is the shape (§3 has the minute-by-minute agenda):

```
a real task  →  do it the only way you currently can  →  notice it is slow
             →  learn the tool  →  do the same task again  →  see the difference
```

Leaving the laborious half hanging until the next session is **forbidden**. Adults do not
return to a course that wasted their evening.

### 4.2 The task is real; the tedium is never named

This is the rule most likely to be broken by accident, so it is stated bluntly.

**A participant must never be told they are doing something in order to suffer.** They are
building a class register because a teacher needs a class register. That is the whole
reason, and it is a true one.

| ❌ Never write this | ✅ Write this |
|---|---|
| "Today is a pain day." | "Today we build a register for the whole class." |
| "Write forty variables so you feel how bad it is." | "We need somewhere to keep each student's name and score." |
| "This is deliberately tedious." | *(say nothing — just give the task)* |
| "Notice how awful that was." | "That worked. It took a while, though — and there is a shorter way." |

The task is grounded in something the participant actually does: a register, a pass list,
a report card, a saved file. If a task cannot be justified to a teacher on its own terms,
**it does not belong in the course**, no matter how well it sets up the next concept.

### 4.3 Reassure forward, every single time

Before and during any stretch of repetitive typing, the notebook says — plainly and
without drama — that a shorter way is coming and names when.

> **Այս ձևը աշխատում է, բայց երկար է։ Դասի երկրորդ կեսին կսովորենք մի բան, որը սա
> դարձնում է մի քանի տող։**
> *(This way works, but it is long. In the second half of today we will learn something
> that turns this into a few lines.)*

Placed **before** the long task, not after it. A participant who knows a shortcut is
twenty minutes away types the long version willingly; one who does not starts wondering
whether the course knows what it is doing.

Where minor friction does cross a session boundary — printing a list item by item on
Day 7, say — the same reassurance names the day: *"Day 10 makes this three lines."*

### 4.4 Sizing the laborious half

Typing thirty variables takes longer than the lesson allows. So:

> **The boilerplate rule.** The notebook **ships** most of the repetitive code already
> written — twenty or so entries — and the participant's job is to **extend it by a few
> and then change it**. Editing thirty things takes four minutes and teaches the same
> lesson as typing them.

Never ask a participant to type more than ten repetitive lines.

## 5. What we teach, and what we deliberately do not

### The spine, in the order it is taught

`print` → types → variables → `if`/`else` → **lists** → `for` → **dictionaries** →
functions → files → modules

Lists and dictionaries are not in the requested order but are required by it: "collect all
of these variables in one object" and "navigate in a dict or list" *is* the collection
topic. They are placed where the pain lands — lists after conditions, dictionaries after
loops — so the requested order (`print → types → variables → conditions → loops →
functions`) is preserved exactly, with collections interleaved as the relief.

### Taught

| Topic | Days | Depth |
|---|---|---|
| `print` | 1–2 | Several values, quotes inside quotes, blank lines |
| Comments | 2 | `#`, and why |
| Types `str int float bool` | 3 | `type()`, and what breaks when they are mixed |
| Conversion, `input()` | 4 | `int()`, `str()`, and "input always gives you text" |
| Variables, f-strings | 5–6 | Naming, reassignment, `f"{name}: {grade}"` |
| `if` / `else` / `elif` | 7–9 | Comparisons, `and` / `or` / `not`, indentation |
| Lists | 10–11 | Index from 0, `len`, `append`, `remove`, `in`, `sort`, `[a:b]` |
| `for` | 12–14 | Over a list, `range`, totals, counters, filtering into a new list |
| `while` | 15 | Repeat until told to stop; validating input; stopping a runaway loop |
| Dictionaries | 16–17 | `name → value`, lookup, add, update, `.items()`, dict of lists |
| Functions | 18–19 | `def`, parameters, `return`, one default argument |
| Files | 22 | Read and write a text/CSV file; `FileNotFoundError` handled once |
| Modules & imports | 20–21 | `import`, `if __name__ == "__main__":`, four files |
| Reading errors | every day | See §6.5 |

### Not taught — and this list is as important as the one above

Classes and objects · exceptions beyond one `try`/`except` in `main.py` · list
comprehensions (cheatsheet only, never required, never in shipped code) · `lambda`,
`map`, `filter` · generators · recursion · tuples and sets as concepts · `pip`, virtual
environments, third-party packages · regular expressions · type hints · `async` · `git` ·
testing frameworks · databases · anything with a decorator · `*args` / `**kwargs` ·
`enumerate` **as a concept** (it appears twice, as a copyable recipe for numbering a
printed list, and is never examined).

**Tuple unpacking is used without the word.** `for name, grade in grades.items():` is
taught as "two names at once, because each entry has two parts". A teacher does not need
the word "tuple" to write a report card.

Every exclusion above is a thing that would cost 15 minutes and buy a teacher nothing in
the programme they are going to write. If the review wants one added back, the question to
answer is: *which line of the final gradebook needs it?*

---

## 6. Pedagogical rules

`METHODOLOGY.md` §2 applies in full. These are the additions and sharpenings for absolute
beginners.

### 6.1 Talk for twelve minutes, then stop

The cap is in the agenda (§3) and is the first thing to check in review. "Variables" gets
twelve minutes of explanation and then thirty-three minutes of typing. A participant who
has typed `grade_anna = 9` forty times understands variables better than one who heard a
good definition.

### 6.2 Every example is a classroom

No `foo`, no `x = 5`, no shopping baskets, no bank accounts, no fizzbuzz. The running data
is a class: names, grades, attendance, subjects, averages, pass marks, report lines. A
participant should be able to look at any cell in any notebook and see their Tuesday
morning in it.

The shipped sample class is **fictional** and small (12 students). Participants swap in
their own from Day 22 — see the privacy rule in §12.

**The grading scale is 1–10, and the pass mark is 4.** Fixed, everywhere, in every cell.
It is written **once**, as `PASS_MARK = 4`, from Day 9 onward, and lives in `settings.py`
in the project. Two rules follow from it:

- Nothing in shipped code writes `4` as a bare number after Day 9. The whole point of
  Day 9 is that the number lives in one place.
- Grades are **whole numbers** in every example until Day 13, where an average produces
  `7.6` and `float` stops being an abstract idea from Day 3.

Participants change `PASS_MARK` to their own school's value on Day 9 if it differs, and
that edit is itself the exercise.

### 6.3 One idea per day, and it is named in the file name

`day12_for_loops.ipynb`. If a day needs two nouns in its name, it is two days.

### 6.4 Compare the two versions, in writing

A discovery day ends by putting the two versions side by side, as a table of facts. No
commentary on how it felt:

> | | Separate variables | List |
> |---|---|---|
> | 20 students | 40 lines | **2 lines** |
> | "how many?" | count by hand | `len(...)` |
> | 300 students | 600 lines | **2 lines** |

Where minor friction genuinely does cross a session boundary, **name the day it ends**
(§4.3). Never hint, never say "we'll see a better way later" — say which day.

### 6.5 Break it on purpose — one cell per notebook

Every notebook contains exactly one cell that **is meant to fail**, with the error named
in the comment above it and read together afterwards. Beginners lose more time to fear of
red text than to any concept in this course.

Rota, so each common error is met deliberately at least once:

| Error | Broken on purpose in |
|---|---|
| `SyntaxError` (missing quote, missing bracket, missing `:`) | Days 2, 7 |
| `NameError` | Day 5 |
| `TypeError` (`"2" + 2`) | Day 3 |
| `ValueError` (`int("nine")`) | Day 4 |
| `IndentationError` | Day 7 |
| `IndexError` | Day 10 |
| `KeyError` | Day 16 |
| `FileNotFoundError` | Day 22 |
| `ModuleNotFoundError` / wrong folder | Day 20 |

Each is followed by a short markdown cell with the same three-part shape: **what the
message says · what it actually means · the two most likely causes.**

### 6.6 Predict before running

Where output is surprising — integer vs float division, `"9" > "10"`, a loop variable
after the loop ends — the notebook asks for a written guess first. Two or three per
course, not per day; it costs time and should be spent where the answer is genuinely
counter-intuitive.

### 6.7 Every participant's output is different

From Day 5 onward every exercise uses **their own** subject, class size and pass mark.
Sixteen identical gradebooks is a failed course. The shipped sample exists so that nobody
is blocked, not so that everybody uses it.

### 6.8 Nothing requires the internet

After Day 1, every notebook runs with the wifi off. No API keys, no accounts, no
downloads, no `pip install`. This is a deliberate architectural decision (§14, override O2)
and it removes the failure mode that costs the TUMO course its riskiest hour.

---

## 7. Notebook conventions

`METHODOLOGY.md` §4 applies. Specifics for this course:

### Cell rhythm

```
1.  Title block            # Day N — Title  /  ### Python from Zero · Day N of 24
                           two-sentence intro, then "## TODAY:" with 3–4 bullets
2.  Recap callout          blue 🔄 — what we had at the end of last time (Day 2+)
3.  Kernel/how-to-run box  red — Days 1 and 2 only
4.  …alternating           short markdown explainer → one small code cell
5.  "🧨 Let's break it"    the deliberate error cell (§6.5) + its explanation
6.  ## 🎯 Exercises        3–5, worked first item each (§7.3)
7.  ## Where we got to     3–5 bullets
8.  ## Next time           one sentence; names the day number if it fixes something
9.  ## Two-minute practice optional, genuinely two minutes
```

Sections 7–9 together are the **retrospective** and are mandatory on every notebook.

### Size targets

| | Target | Why |
|---|---|---|
| Cells per notebook | 18–26 | 15 minutes of running together, ~35 s per cell |
| Median code cell | **≤ 200 characters** | Smaller than the TUMO courses' 250 — this audience reads every character |
| Longest code cell | ≤ 15 lines, excluding shipped boilerplate | |
| Markdown : code | ~1 : 1 | |
| New built-in functions per day | ≤ 4 | |

A bare variable name on the last line to display it is used constantly, and is explained
once, on Day 5, as a notebook trick rather than Python.

### 7.3 Exercise format

Three to five per notebook. **Every exercise shows the first item already done**, exactly
as requested:

```python
# Exercise 2 — write out your own class.
# Here is the first one. Add nine more, with your real students' first names only.

student_01 = "Anna"

# your turn:
```

- **Three tiers, and the third is not optional to write.**

| Tier | How many | Sized for |
|---|---|---|
| **Պարտադիր** (Required) | 3–4 | Everyone, inside the allotted minutes |
| **Լրացուցիչ** (Extra) | **3–4** | The participant who finished Required with 8 minutes left |
| **Մարտահրավեր** (Challenge) | 1–2 | The fastest one or two in the room |

- **Every notebook ships at least three Extra tasks.** In a group of 4–8, at least one
  or two will finish Required work early in every single session. "Help someone else" is
  a fine answer once; it is not a plan for eight weeks. Running out of work is how a
  competent participant concludes the course is beneath them.
- Extra tasks use **only what the course has already taught** — they are wider, not
  further ahead. A Challenge may combine two earlier days.
- Never a blank cell. Always a skeleton with a comment saying what goes where.
- Exercise 1 of every notebook is a two-minute confidence win.
- The last Required exercise produces the day's deliverable (§3).

### 7.4 Solutions

`solutions/dayNN.ipynb` — every Required exercise solved, with one comment per solution
saying *why*, not *what*. Handed out **after** each session, not with the notebook.
Participants who miss a session need to be able to catch up alone; this is the artefact
that lets them.

### 7.5 Callouts

Same fixed vocabulary and inline-styled `<div>` template as `METHODOLOGY.md` §4, with one
addition and one change:

| Colour | Emoji + heading | Use |
|---|---|---|
| `#900` red | 🎯 Exercises | The required work |
| `#900` red | 🧨 Let's break it on purpose | **New for this course** — the deliberate error |
| `#181` green | 🏫 In your classroom | Where today's idea shows up in real school work — replaces "🌍 real world" |
| `#f71` orange | 🚀 If you finished early | Genuinely optional |
| `#06c` blue | 🔄 Where we were | The recap, and just-in-time syntax reminders |

### 7.6 `input()` is rationed

`input()` blocks a notebook and cannot be executed headlessly, which fights the
verification discipline (§11.2). Rules:

- Taught on Day 4, used in exercises on Days 4, 15 and in the project.
- **Any cell containing `input()` is tagged `interactive` in its source marker**, so the
  verification runner can feed it a scripted answer. The tag becomes **cell metadata**,
  never a visible comment — a participant should not see `# interactive` in their notebook.
- Shipped example cells never *depend* on `input()` for a later cell's variables. Where a
  value is needed downstream, the notebook assigns it directly and mentions that `input()`
  would do the same thing.

### 7.7 Armenian descriptions, English everything-else — the exact split

The rule in one line: **Armenian appears only in markdown. Every character inside a code
cell is English.**

| Element | Language |
|---|---|
| Markdown cells, callouts, exercise instructions, retrospectives | **Armenian** |
| Guides (`guides/*.md`), `SETUP.md`, `CHEATSHEET.md`, `ANNOUNCEMENT.md` prose | **Armenian** |
| Keywords, built-ins, method names | English |
| Variable and function names | English |
| **Comments inside code cells** | **English** |
| **String values** — `print("...")`, example names, menu text | **English** |
| **Docstrings** | **English** |
| Output the program prints at runtime | **English** |
| File and folder names | English, lowercase |
| `PLAN.md`, `CURRICULUM.md`, `OUTLINE.md`, `RATIONALE.md`, `INSTRUCTOR_NOTES.md`, `tools/` | English |

**Why the line is drawn at the cell boundary.** A participant reads the explanation in
their own language and then types code that looks exactly like every other piece of Python
in the world. Anything they can copy from this course into a real project, or search for
when stuck, is already in the form the rest of the world uses. Armenian inside a code cell
would make the course a dialect.

**Example names are transliterated Armenian**, so the data stays familiar without leaving
Latin script: `Ani`, `Davit`, `Nare`, `Aram`, `Mariam`, `Tigran`, `Lilit`, `Gor`,
`Anahit`, `Hayk`, `Sona`, `Vahe`. A teacher recognises their own classroom; Python sees
plain ASCII.

**`encoding="utf-8"` keeps its motivation.** The shipped sample data is Latin, but on
Day 22 participants type their *own* class list, and many will use Armenian names there.
That is where the encoding argument is demonstrated and where it earns its place.

**Error messages are English and always will be.** §6.5's deliberate-error cells therefore
have a second job: teaching a participant to read an English error message. The explanation
above each one is Armenian; the message it explains is not.

**The bilingual glossary is still a deliverable.** `CHEATSHEET.md` §1 maps ~40 terms —
*variable · փոփոխական*, *list · ցուցակ* — because the instructor and the markdown talk
about these concepts in Armenian even though the code never does.

### 7.8 Assessment — three sittings

**Three assessments, designed with our partner colleague**, replacing an earlier design
of four take-home tests. They are **separate sittings, not session time**: the 24 teaching
sessions stay at 20 hours exactly and the assessments add roughly 3½ hours.

| Test | When | Length | Points | Covers |
|---|---|---|---|---|
| `test1_diagnostic` | **Before day 1** | 45–60 min | 44 | nothing — the baseline |
| `test2_midpoint` | **After day 12** | 60–75 min | 50 | days 6–12 |
| `test3_final_practical` | **Day 24** | 90–120 min | 70 + 10 separate | days 14–24 |

Rules that make them worth setting:

- **Every question has variants A, B, C**, equivalent in difficulty and points; the
  platform gives each participant one. Question 8 of the final test is the exception —
  the same for everyone.
- **Two notebooks are generated from each source.** `#%% md teacher` cells carry the
  rubric and appear only in `tests/<name>.ipynb`; `tests/participant/<name>.ipynb` has
  questions only. **Never hand out the grader's copy** — it states what each question
  measures and what it is worth.
- **Every score is recorded with a help level**: `3` independent, `2` after one hint,
  `1` step-by-step, `0` did not finish. On the diagnostic the help level carries more
  information than the score.
- **Scores diagnose the programme, not the teachers**, and the materials say so. The
  earlier design refused to score at all; scoring plus the explicit framing keeps the
  diagnostic value while gaining a measurable before-and-after.
- **Every question is a classroom task**, never a puzzle, and nothing untaught appears —
  except question 8, which is untaught by design.
- **A marking guide ships with each test** (`tests/markN_guide.md`): expected answer, and
  *what a wrong answer tells the instructor*. That second column is the point.

**The diagnostic is what makes the experiment measurable.** Without a before-measurement
the programme can only report an endpoint; with one it reports change. It is also an
early warning: a participant who cannot run a cell at help level 3 predicts a hard day 1.

**Question 8 of the final test carries the transfer question** — one small task using
only taught syntax that the course never demonstrates, marked separately and never
reported as a pass rate (§ `RATIONALE.md` 5).

## 8. Code style for this audience## 8. Code style for this audience

`METHODOLOGY.md` §6 applies; these override or sharpen it.

| Rule | This course |
|---|---|
| Names | Full words, no abbreviations: `class_average`, not `avg`. `student_name`, not `s`. |
| Loop variables | `for student_name in student_names:` — never `for i in`, except `for position in range(...)` |
| Quotes | Double quotes everywhere, without exception. One rule is easier than one convention. |
| Strings into output | f-strings only. `.format()` and `%` never appear. |
| Comparison chains | `if grade >= 9 and attendance >= 80:` — parentheses only where genuinely needed |
| Line length | ≤ 80 characters, so it fits a projector at a readable font size |
| Blank lines | One between logical steps inside a cell; beginners read whitespace as structure |
| Comment density, notebooks | One comment above each code cell saying **why**; inline comments only on the line that surprises |
| Comment density, `project/` | `settings.py` ~50% (it is a teaching surface); other modules 15–25% |
| Docstrings | One line, plain language, in every project function: `"""Return the average of a list of grades."""` |
| `try` / `except` | Exactly one, in `main.py`, around the menu loop. Nowhere else. Day 22's `FileNotFoundError` is handled with an `if` on whether the file exists, not an exception. |
| Emoji in output | `✅` and `❌` in check scripts only; never inside teaching code |

### The project's four files

Each explainable in one sentence, stated in the project README as a table:

```
settings.py    Every number you might want to change.     (no logic — the Day 9 lesson, as a file)
storage.py     Load the class from a file, save it back.  (knows nothing about grades)
grades.py      The calculations: average, highest, pass.  (knows nothing about files)
main.py        Ask the teacher what they want, and print. (does no calculating of its own)
```

**Four, not five.** An earlier draft had a separate `report.py` for printing. Printing is
two `print()` calls in a loop and does not need its own file; folding it into `main.py`
removes a file, an import and five minutes of explanation from a 50-minute day. This is
§0 applied.

**Dependency arrows point one way:** `main` → `grades`, `storage` → `settings`.
`grades.py` must not import `storage.py`. The reason is stated to participants in Day 21's
guide: *you can test your average calculation without having a file at all.*

`settings.py` is the pedagogical payoff of Day 9 — one place to change the pass mark —
and the plan should keep that connection explicit in both the guide and the file's own
comments.

---

## 9. The document set

```
public_school_python/
├── PLAN.md                     <- this document
├── README.md                   <- index; what this is; how to run it
├── OUTLINE.md                  <- 4-part outline: idea / skills / requirements / outcome
├── CURRICULUM.md               <- 24 day agendas, time math, deliverables
├── SETUP.md                    <- Anaconda install, Windows AND macOS, screenshots-in-words
├── INSTRUCTOR_NOTES.md         <- pre-flight, pacing, what to cut, the risk register
├── CHEATSHEET.md               <- printable, 4 pages; opens with the bilingual glossary (§7.7)
├── RATIONALE.md                <- why this method, the risk, the experiment (for colleagues)
├── ANNOUNCEMENT.md             <- recruitment text, written for teachers
├── check_setup.py              <- 6 checks, run on Day 1
├── notebooks/                  <- GENERATED -- do not edit by hand
│   ├── day01_first_program.ipynb … day19_return.ipynb             (19)
│   └── sample_class.csv        <- the fictional 12-student class
├── src/                        <- notebook SOURCES, the thing you edit
│   ├── day01_first_program.py … day19_return.py                   (19)
│   ├── solutions_source.py     <- all solutions in one reviewable file
│   └── solutions/              <- split per day by the build step
├── solutions/
│   └── day02.ipynb … day19.ipynb                                  (18)
├── tests/                      <- assessment (§7.8) -- GENERATED
│   ├── test1_diagnostic.ipynb … test3_final_practical.ipynb       (3, grader's copy)
│   ├── participant/            <- the same three, rubric stripped (3)
│   ├── mark1_guide.md … mark3_guide.md   <- instructor only       (3)
│   └── README.md               <- how the three sittings work
├── guides/
│   ├── day20_leaving_the_notebook.md
│   ├── day21_four_files.md
│   ├── day22_your_own_class.md
│   ├── day23_make_it_yours.md
│   └── day24_finish_and_show.md
├── project/
│   └── gradebook/              <- the finished reference program
│       ├── settings.py  storage.py  grades.py  main.py
│       ├── data/sample_class.csv
│       └── README.md
└── tools/                      <- build and verification, not participant-facing
    ├── nbbuild.py              <- src/*.py  ->  notebooks/*.ipynb
    ├── run_all_notebooks.py
    ├── check_times.py
    └── check_style.py
```

### 9.2b Why notebooks are generated

Nineteen notebooks are nineteen large JSON files, and editing Armenian prose inside JSON
string arrays is unreviewable — a multi-step review of the wording would be impossible.
So the source of truth is a readable text file per day in `src/`, and `tools/nbbuild.py`
generates the `.ipynb`.

**This does not violate §0.** The simplicity rule governs what the *participant* touches:
they open one folder, in one editor, with one Python. The build system is ours, and no
participant ever sees it.

### 9.3 Repository

Its own git repository, separate from `tumo_month_workshop`:

```
git@github.com:AIrtyoMKo/python_basics_training_program.git
```

`.gitignore` covers `.ipynb_checkpoints/`, `__pycache__/`, `.DS_Store`, `.vscode/` and
`project/gradebook/data/my_class.csv` — the last one so a participant who clones this
cannot accidentally commit a real class list (§12).

**Notebooks are committed with their outputs cleared.** Outputs make every diff unreadable
and, once the sample class changes, actively misleading. The verification runner (§11.2)
regenerates them; nothing depends on a stored output.

**Format follows phase**, per the methodology: notebooks for Days 1–19, markdown guides
for Days 20–24 because participants are editing `.py` files with the guide open in VS Code's
preview pane beside them. Day 20 gets no notebook **on purpose** — the lesson is leaving the
notebook.

### 9.1 The toolchain — Anaconda for Python, VS Code for everything else

**Two installs on Day 1, and nothing ever again.**

| What | Which | Used for |
|---|---|---|
| Python | **Anaconda**, `base` environment | Days 1–24. Never activated by hand, never a second environment |
| Editor | **VS Code** + two extensions (Python, Jupyter) | Days 1–24. Notebooks *and* `.py` files, in the same window |
| Terminal | **VS Code's built-in terminal** (`Ctrl+`` ` ``) | Days 20–24 |

**One editor for the whole course is the simplification that matters most.** VS Code opens
`.ipynb` files natively, so Days 1–19 happen in it; Days 20–24 open a `.py` file in the
same window, in the same folder, with the same sidebar. **Day 20 therefore introduces two
new things — a `.py` file and a terminal — instead of three.** Participants never learn a
second program's menus, and never wonder which tool they were supposed to be in.

**Why Anaconda rather than python.org.** It installs Python, Jupyter and everything the
notebooks need in one go, and on Windows it avoids the `Add python.exe to PATH` checkbox
that beginners miss and then lose an hour to. Its cost is a ~1 GB download, which §12
treats as the main Day-1 risk.

**The environment question is answered by not asking it.** Everyone works in Anaconda's
`base` environment. No `conda create`, no `conda activate`, no "which environment am I in".
This is free here because the course imports nothing outside the standard library (§5), and
it removes the failure that opens every session of the TUMO course with "but it worked last
time".

**Anaconda's 300 bundled packages are not a licence to use them.** `pandas` would make
Day 13 a one-liner and teach a teacher nothing about loops. The standard-library-only rule
in §5 stands, and `tools/check_style.py` enforces it by grepping every import.

**The two things VS Code will do to us, and the answer to each:**

| | Answer |
|---|---|
| **The kernel picker.** Every notebook asks which Python to use; pick the wrong one and packages "aren't installed" | There is only **one** choice in the list — Anaconda's `base`. `SETUP.md` shows it in words, Day 1 and Day 2 have a red callout about it, and `check_setup.py` reports which Python is actually running |
| **The built-in terminal may open without conda on it** (Windows PowerShell) | The Python extension activates the interpreter in new terminals by default, so this usually just works. If it doesn't: `SETUP.md`'s fallback is one line — set the default terminal to Command Prompt. Named in `INSTRUCTOR_NOTES.md` as a thing to test on a school laptop before Day 1 |

**If VS Code is blocked by school IT**, the fallback is JupyterLab from Anaconda Navigator
for Days 1–19 and pairing with a colleague for Days 20–24. Documented in
`INSTRUCTOR_NOTES.md`, not in the participant materials — a fallback in the main text is a
fork in the road for everyone.

### 9.2 `SETUP.md` is a first-class deliverable here

In the TUMO course setup is a 15-minute appendix because IT prepared the machines. Here it
is Day 1's entire content and the largest single risk to the programme. It must:

- Cover **Windows and macOS** in separate, complete, non-interleaved sections. A
  participant should never read a step that is not for their machine.
- Be **six steps**, numbered, with a ✅ check after each: install Anaconda → install
  VS Code → install the two extensions → make the `python_course` folder → open it in
  VS Code → run `check_setup.py`.
- Name what they will see on screen, in words, at every step — "a green button saying
  *Download*", "a box on the left with five icons; the top one looks like two sheets of
  paper".
- State the real numbers up front: **the download is about 1 GB and the install needs about
  5 GB free**, and on a school wifi it can take 30 minutes. A participant who knows that in
  advance waits; one who doesn't assumes it has frozen.
- Tell them to install with the **default options** and change nothing. Anaconda's installer
  asks two questions that beginners get wrong; both defaults are correct.
- Have a fallback path for **no admin rights** — Anaconda and VS Code both install
  per-user ("Just Me") and usually succeed without admin. If they are blocked outright, the
  fallback is in `INSTRUCTOR_NOTES.md`, not here.
- End with `check_setup.py` printing six green lines, run from inside VS Code on Day 1.
- Be handed out **at least three days before** Day 1, with the note that trying it at home
  is welcome and failing at it is expected and is exactly what Day 1 is for.

---

## 10. The 24-day map

**D** = discovery day (the tool arrives the same session). **TR** = transition, **PR** = project.

| Day | Title | Phase | New idea | 📦 Deliverable |
|---|---|---|---|---|
| 1 | Install everything and run your first line | NB | JupyterLab in VS Code, a cell, Shift+Enter | `check_setup.py` green; a notebook printing their name |
| 2 | Printing properly | NB | `print`, quotes, comments | A four-line register header |
| 3 | Four kinds of value | NB | `str` `int` `float` `bool`, `type()` | A cell showing each type and what `"2" + 2` does |
| 4 | Changing type, and asking a question | NB | `int()`, `str()`, `input()` | A cell that takes a grade and prints it plus one |
| 5 | Giving a value a name | NB | variables, f-strings | One student's row printed from named values |
| **6** | **A register for the whole class** | **D** | many variables → **lists** | Their class as one list, plus the count |
| 7 | Working with the register | NB | `append` `remove` `in` `sort` `[a:b]` | A sorted class list, one student added, one removed |
| 8 | The first decision | NB | `if`/`else`, comparisons, indentation | Pass/fail for one grade, on their own pass mark |
| 9 | More than two outcomes | NB | `elif`, `and`/`or`/`not` | A grade banded into four levels |
| **10** | **Marking the whole class** | **D** | one `if` block per student → **`for` loops** | The whole register marked, in four lines |
| 11 | Counting and totalling | NB | `range`, accumulator, average | Their own class average, computed |
| 12 | Loops that decide | NB | loop + `if`, building a new list | Who failed, how many passed, the highest grade |
| 13 | Entering grades one by one | NB | `while`, `break`, validating input | A loop that collects grades until they type `quit` |
| **14** | **Finding one student** | **D** | two parallel lists → **dictionaries** | Their class as `name → grade` |
| 15 | Reports from the register | NB | `.items()`, two loop variables | A printed line per student, from the dictionary |
| 16 | Several grades per student | NB | a dictionary of lists | A report card per student with three grades each |
| **17** | **An average on every card** | **D** | the same six lines, four times → **functions** | The calculation as a function, called four times |
| 18 | Sending an answer back | NB | `return`, default parameter | Four grade functions that return values |
| 19 | The register, assembled | NB | consolidation — no new syntax | The complete register program, in one notebook |
| 20 | Leaving the notebook | **TR** | a `.py` file, the terminal, `__main__` | `python grades.py` runs in a terminal |
| 21 | Four files that each do one thing | **TR** | `import`, modules | **A working `python main.py`** — confirmed individually |
| **22** | **Keeping it after you close it** | **D** | retyping every time → **files** | Their own class in `data/my_class.csv`, loaded and saved |
| 23 | Make it yours | PR | designing a small feature | One self-designed feature working |
| 24 | Finish and show | PR | README, the fresh-laptop test, demoing | A 90-second demo; a README a colleague can follow |

```
Notebook phase   Days  1–19   950 min   15 h 50
Transition       Days 20–21   100 min    1 h 40
Project          Days 22–24   150 min    2 h 30
                            ----------------------
                             1,200 min  = 20 h  ✓
```

**Assessments** before Day 1, after Day 12 and on Day 24 (§7.8) — separate sittings, so the agendas are unaffected.

### Week map (3 sessions/week × 8 weeks)

| Week | Days | Arc | Assessment |
|---|---|---|---|
| 1 | 1–3 | It runs on my laptop, and I know what a value is | *(diagnostic sat before day 1)* |
| 2 | 4–6 | I can name things, and keep a whole class in one list | |
| 3 | 7–9 | The computer can decide | |
| 4 | 10–12 | One loop marks thirty students | **Midpoint** |
| 5 | 13–15 | I can find any student by name | |
| 6 | 16–18 | I write the calculation once and use it everywhere | |
| 7 | 19–21 | It is a program now, not a notebook | |
| 8 | 22–24 | It has my class in it, it saves, and I showed it to someone | **Final practical** |

## 11. Verification discipline

Non-negotiable, per `METHODOLOGY.md` §9. Nothing is reported complete until these pass.

### 11.1 Time arithmetic, by script

`tools/check_times.py` parses every agenda table in `CURRICULUM.md`, asserts each sums to
50 and the grand total is 1,200. Re-run after **every** curriculum edit.

### 11.2 Execute every notebook cell, in order

`tools/run_all_notebooks.py`: fresh kernel per notebook, cells in order, catch per cell,
report which failed. Two course-specific wrinkles:

- **`input()` is stubbed.** Cells marked `# interactive` get a scripted answer fed in. The
  runner asserts that the answers it feeds produce the output the notebook claims.
- **Deliberate-failure cells (§6.5) are expected to fail.** They are tagged
  `expected-error: KeyError` in the source, which becomes cell metadata; the runner
  asserts the cell raises **that specific** error. A break-it cell that stops raising is a bug in the notebook.

There is no external API in this course, so `METHODOLOGY.md` §9.2's stubbing requirement
is satisfied trivially — but §9.4's failure-path requirement is not, see 11.4.

### 11.3 Assert outputs, not just "it ran"

Every claim a notebook makes about output is checked: if a markdown cell says the average
is `7.4`, the runner asserts the computed value is `7.4`. This is where stale numbers get
caught after the sample class changes.

### 11.4 Every failure path gives one actionable sentence

For `check_setup.py` and the project: Python not on PATH, wrong Python version, notebook
run out of order, missing data file, empty data file, a grade that is not a number, a
non-existent student name. Each produces one sentence a teacher can act on. **A traceback
is never acceptable as participant-facing output.**

### 11.5 The fresh-laptop test

Before Day 1 is final: a machine that has never had Python on it, following `SETUP.md`
literally, with nothing else open. Once on Windows, once on macOS. Time it, and put the
real number in `INSTRUCTOR_NOTES.md`.

Three things to confirm specifically, because they are the ones that bite:

1. VS Code offers **exactly one** kernel, and its name matches what `SETUP.md` says.
2. `Ctrl+`` ` `` opens a terminal in which `python --version` works, with no conda
   activation typed by hand — **on Windows**.
3. `check_setup.py` runs green from inside VS Code, not just from a terminal.

### 11.6 Sweep for stale claims

After any change to the sample class, the pass mark or the project structure, grep for
every number and file name that was true before it.

---

## 12. Risks

| Risk | Likelihood | Cost | Mitigation |
|---|---|---|---|
| **The ~1 GB Anaconda download** | Medium — lower than in a room, since each teacher downloads at home | Day 1 | `SETUP.md` sent 3 days early **with a reply required** confirming `check_setup.py` is green. No reply means not attempted |
| **No instructor present to fix a stuck machine** | **High** — this is what remote delivery costs | Any session | All screens shared through hands-on work (Meet shows every participant's at once); check in on each person **by name**; groups capped at 8 so that is possible |
| Not enough disk space (Anaconda needs ~5 GB) | Medium | Blocks one participant entirely | Stated in `SETUP.md` as a checkable number *before* they start; asked on the enrolment form |
| No admin rights on school laptops | Medium | Blocks installation | Both installers offer a per-user ("Just Me") install; `SETUP.md` selects it explicitly. If blocked outright, the fallback is in `INSTRUCTOR_NOTES.md` |
| **VS Code's kernel picker** — "Select Kernel", or packages that "aren't installed" | **High** | 10 min per person, repeatedly | There is only one kernel in the list. Red callout on Days 1 and 2; `check_setup.py` prints which Python is running; `INSTRUCTOR_NOTES.md` lists it as the #1 thing to check before answering any other question |
| The VS Code terminal opens without conda on Windows | Medium | Day 20, for some people | Usually handled by the Python extension. One-line fallback in `SETUP.md`; must be tested on a real school laptop before Day 1 (§11.5) |
| A participant also installs Python from python.org | Medium | Two Pythons, confusing errors | `SETUP.md` says plainly: Anaconda and VS Code, nothing else. `check_setup.py` reports which Python is running |
| Mixed pace — some finish in 5 min, some not at all | Certain | Room stalls | Required vs Extra exercises; solutions handed out after each day; fast finishers paired with slow ones from Day 3 |
| Missing a session (2 days apart, working adults) | High | Falls behind permanently | Every notebook is self-contained and re-declares what it needs; solutions published after each day; §13 catch-up rule |
| **Real student data in the exercises** | Medium | A genuine privacy problem | Stated plainly on Day 5, *before* they choose their data: **first names or initials only, no surnames, no real grades, no ID numbers.** Repeated on Day 22 where they load a real file. The shipped sample class is fictional. |
| Fear of the terminal at Day 20 | High | Loses the transition | Day 20 does exactly two things in a terminal: `cd` and `python file.py`. Nothing else, all course. |
| Instructor talks past 15 minutes | High | The course stops being practical | The agenda is printed in `INSTRUCTOR_NOTES.md` with the cap stated per day |
| **Inconsistent Armenian terminology across 19 notebooks** | High if unmanaged | Quiet, cumulative confusion | The glossary (§7.7) is fixed in Build Block 1, reviewed by a native speaker in Block 2, and `tools/check_style.py` greps for off-glossary terms |

---

## 13. What to cut if time runs out

Cut, never compress. In this order:

1. Day 13 `while` loops — the project menu ships written and can be explained in two
   minutes on Day 21. This is the one genuinely removable day.
2. Day 16's dict-of-lists (several grades per student) — the project works with one grade.
3. Day 19's consolidation day, if the room is already ahead.
4. Day 23's own-feature work — it can become optional homework.

**Never cut:** the five discovery days (6, 10, 14, 17, 22) — each is a concept *and* its
motivation in one session, so cutting one costs both. Nor Days 20–21 (the transition) or
Day 24 (finishing something is the point).

**Never split a discovery day across two sessions.** If Day 10 runs out of time, cut its
Extra tasks — never its second half. A session that ends after the long way and before the
short way is the single worst outcome the design can produce.

**Catch-up rule for a missed session:** the solutions notebook for that day, plus the next
day's recap callout, must be enough. Build each notebook so this is true.

---

## 14. Where this plan overrides `METHODOLOGY.md`

| # | Methodology says | Here | Why |
|---|---|---|---|
| O1 | Transition is exactly one lesson | Two (Days 20–21) | 50-minute sessions; one cannot hold both "what a `.py` file is" and a five-module split |
| O2 | Provider-agnostic pattern is the architectural spine (§7) | **Dropped entirely** | No external service exists in this course. Its replacement as the "one clean abstraction" is `settings.py` — one place for every number — which is the Day 9 lesson made structural |
| O3 | "Age-appropriate complexity: students already program" | Absolute beginners | Python is the subject, not the medium; §5's exclusion list is far longer |
| O4 | Python is not taught; a cheatsheet is handed out | Python **is** the course; the cheatsheet is a printable summary that grows with it | Inverted audience |
| O5 | 1–2 exercise callouts per lesson | 3–5 short ones | 50-minute sessions need smaller units of work |
| O6 | "🌍 Where you'll see this in the real world" | "🏫 In your classroom" | The real world in question is a school |
| O7 | Stub the external API (§9.2) | Stub `input()`; assert deliberate errors | Same discipline, different external dependency |
| O8 | `TEACHER_NOTES.md` | `INSTRUCTOR_NOTES.md` | "Teacher" means the participant here |
| O9 | venv + `pip install -r requirements.txt` | **Anaconda**, `base` environment, no activation step | No `pip`, no venv, no "did you `source` it?" — the line that opens every TUMO session |
| O10 | All materials in English | Armenian prose, English code | §7.7 |

Everything else in `METHODOLOGY.md` — the spiral, straw-man-first, run-it-then-name-it,
measured claims, callout HTML, verbose naming, one `try` at the edge, numbers not
adjectives, the definition of done — applies unchanged.

---

## 15. Decisions — all closed

| # | Decision | Answer | Written into |
|---|---|---|---|
| **D1** | Language of materials | Armenian prose, comments and string values; English identifiers and keywords | §2, §7.7 |
| **D2** | Python distribution | **Anaconda**, `base` environment, never activated by hand | §9.1 |
| **D3** | Grading scale | **1–10, pass mark 4**, written once as `PASS_MARK = 4` from Day 9 | §6.2, §8 |
| **D4** | Where participants keep their work | Their own laptop, one folder: `Documents/python_course/`. Same folder all 24 days | §9.2 |
| **D5** | Practice between sessions | Yes — one ~10-minute task per day, **explicitly optional**, and the next day never assumes it was done | §7, §3 |
| **D6** | Group size | **4–8, one instructor.** Fewer than 4 and they cannot discuss; more than 8 and the instructor cannot check on everyone remotely | §2, §12 |
| **D11** | Delivery | **Remote**, over Google Meet with screen sharing. Each teacher needs their own laptop and a connection that holds a 75-minute call | §2, §12, `ENROLMENT.md` |
| **D12** | Session length | **75 minutes**, 3 a week. May become 2 a week or 3 × 50 after the cohort adapts. **Agendas not yet rebuilt** | §3 |
| **D13** | Success criterion | **>90% can code** = success · **<50%** = failure · between = adjust and repeat | `RATIONALE.md` §5a |
| **D7** | Recruitment document | `ANNOUNCEMENT.md`, written **for teachers**. A one-page summary for school administration only if asked for | §9 |
| **D8** | Version control | Own repository: `git@github.com:AIrtyoMKo/python_basics_training_program.git` | §9.3 |
| **D9** | Armenian terminology review | The glossary is produced in Block 1 and **reviewed by you later**; the build continues meanwhile. Terminology is confined to the glossary file so a later change is one edit plus a scripted sweep, not a rewrite | §7.7, §11.6 |
| **D10** | Editor | **VS Code**, Days 1–24, notebooks and `.py` files in the same window | §9.1 |

**Note on D9.** Because the glossary is reviewed after the notebooks are drafted, every
Armenian term in every notebook must come from `CHEATSHEET.md`'s glossary table and nowhere
else, and `tools/check_style.py` must verify that. That is what makes a late terminology
correction a find-and-replace instead of a re-read of 19 files.

---

## 16. Build order and review checkpoints

Five blocks. Each ends with something reviewable, and nothing downstream starts until the
review closes — this is what keeps a wrong decision from propagating into 19 notebooks.

| Block | Produces | Review question |
|---|---|---|
| **0 · Decisions** | All closed (§15); repository initialised with `.gitignore` | — |
| **1 · Skeleton** | `CURRICULUM.md` (24 agendas, times verified), `OUTLINE.md`, `README.md`, the **bilingual glossary**, the sample class data | Is the day map right? Is the pain spiral right? **Is the Armenian terminology right?** Is anything taught that shouldn't be? |
| **2 · Day 1 vertical slice** | `SETUP.md`, `check_setup.py`, `day01`, `day02`, `solutions/day02` | Is this the right level, tone, pace and length for a teacher who has never programmed — **and is the Armenian prose right?** **This is the most important review of the project.** Get it wrong here and 19 notebooks inherit it |
| **3 · Notebook phase** | Days 3–19 + solutions + Tests 1–3, in four batches (3–6, 7–10, 11–14, 15–19) | Per batch: is the task believable? Does the tool land in the same session? Does each day fit 50 minutes? Are there enough Extra tasks? |
| **4 · Transition + project** | Guides 20–24, `project/gradebook/`, `CHEATSHEET.md` | Can a participant who followed the notebooks actually do this? |
| **5 · Verification & handover** | All of §11 passing, `INSTRUCTOR_NOTES.md`, the fresh-laptop test results | Definition of done (§17) |

Block 2 is deliberately small. Two notebooks is enough to argue about tone, density,
exercise size and the retrospective format — and cheap to throw away.

---

## 17. Definition of done

- [ ] Every day's agenda sums to exactly 50, and the total to 1,200 — **verified by script**
- [ ] Every day has a concrete deliverable and participant-facing material
- [ ] Every notebook cell executes in order, with `input()` stubbed
- [ ] Every deliberate-failure cell raises the exact error it claims
- [ ] Every numeric claim in markdown matches what the code actually produces
- [ ] Every Required exercise has a solution in `solutions/`
- [ ] Every notebook has at least 3 Extra tasks and 1 Challenge (§7.3)
- [ ] Every notebook has the three retrospective sections
- [ ] Every discovery day resolves its own laborious half **in the same notebook** (§4.1)
- [ ] No notebook tells a participant the long way was there to make a point (§4.2)
- [ ] Every stretch of repetitive work is preceded by the forward reassurance (§4.3)
- [ ] All three assessments, both versions, and their marking guides exist and run
- [ ] No `teacher` cell leaks into `tests/participant/`
- [ ] No notebook after Day 1 needs the internet
- [ ] Nothing outside the standard library is imported anywhere — including Anaconda's own bundled packages
- [ ] `project/gradebook/` runs end to end from a clean folder
- [ ] Every failure path produces one actionable sentence; no participant-facing traceback
- [ ] `check_setup.py` passes on a fresh Windows machine and a fresh macOS machine, timed
- [ ] `SETUP.md` verified by following it literally on a machine with no Python (§11.5)
- [ ] Every Armenian term matches the glossary — **verified by script**, not by eye
- [ ] **No Armenian anywhere inside a code cell** — verified by script (§7.7)
- [ ] The exclusion list in §5 holds — grep the notebooks for `class `, `lambda`, `import ` of anything third-party, and comprehensions
- [ ] Anything that could not be verified is **stated plainly**, with how to verify it
