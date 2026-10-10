# Curriculum — the grade-11 course

**18 sessions × 75 minutes = 22 hours 30 minutes.** Two a week over nine weeks. **Fully remote** — every
session, without exception — in groups of 4–8. Arithmetic verified by `tools/check_times.py`.

Entry is the grade-10 course and nothing beyond it. See `AGENTS.md` for what that means
in practice, and `BUILD_PLAN.md` for what is built.

> **The course teaches 24 topics across 18 sessions.** A topic is one notebook and one
> idea. A session is 75 minutes in a room. Seven of the eighteen hold one discovery arc,
> four hold one topic with its practice in the room, and six hold two topics — and on
> four of those six the practice moves to homework.

## The session map

| # | Session | Topics | Shape | Min |
|---|---|---|---|---|
| 1 | The school, and functions that bend | 1–2 | Setup | 75 |
| 2 | Sending back more than one answer | 3 | Single | 75 |
| 3 | **Six reports, six loops** | 4 | **Discovery** | 75 |
| 4 | Choosing while you build | 5 | Single | 75 |
| 5 | **A student is more than a grade** | 6 | **Discovery** | 75 |
| 6 | The calculation moves inside, and a class full of students | 7–8 | Paired | 75 |
| 7 | **Teachers as well as students** | 9 | **Discovery** | 75 |
| 8 | One loop many kinds, and the register rewritten | 10–11 | Paired | 75 |
| 9 | **The term's statistics** | 12 | **Discovery** | 75 |
| 10 | Whole arrays at once | 13 | Single | 75 |
| 11 | **Show the head teacher** | 14 | **Discovery** | 75 |
| 12 | The four charts a school asks for | 15 | Single | 75 |
| 13 | **The school's own file** | 16 | **Discovery** | 75 |
| 14 | Filter, group, describe — and the term report | 17–18 | Paired | 75 |
| 15 | **How deep does it go?** | 19 | **Discovery** | 75 |
| 16 | Where code comes from, and wrong with no error | 20–21 | Paired | 75 |
| 17 | Five files that each do one thing | 22 | Transition | 75 |
| 18 | Make it yours, and show it | 23–24 | Project | 75 |

Seven discovery sessions — **3, 5, 7, 9, 11, 13, 15**. Each holds one topic and resolves
its own difficulty inside its own session. **Never split one.**

> **The "discovery + consolidation" shape is gone.** At 120 minutes a session could hold <!--history-->
> an arc and the topic that widens it; at 75 it cannot, so topics 13 and 15 have sessions
> of their own again — with their practice back in the room, which is better than they
> had on the previous schedule.

## The state curriculum, by session

| State topic | Pupil hours | Topics here | Sessions |
|---|---|---|---|
| 16 — Խորացված ֆունկցիաներ | 15 | 2, 3, 4, 5 | 1–4 |
| 18 — Դասեր (Class) | 12 | 6, 7, 8, 11 | 5, 6, 8 |
| 19 — Ժառանգականություն | 10 | 9, 10, 11 | 7, 8 |
| 15 — Մոդուլների ներածություն \| Colab | 15 | 1, 12, 14, 20 | 1, 9, 11, 16 |
| 21 — Գրադարաններ և միջավայրեր | 23 | 12–18, 20 | 9–14, 16 |
| 20 — Մոդուլներ և կրկնություն | 8 | 20, 22 | 16, 17 |
| 17 — Ռեկուրսիա | 15 | 19 | 15 — **mechanics only**; the algorithms are Part 2 |
| 22 — Սխալների հանգուցալուծում | 7 | 21, and every topic's error reading | 16 |
| 24 — Ամփոփում | 2 | 24 | 18 |
| 23 — Git | 6 | — | **not taught** — deferred by decision |

The full audit, construct by construct, is in `../shared/GOVERNMENT_ASSIGNMENT.md` §8.

## The three agenda shapes

All three sum to 75.

### Single session — one topic, practice in the room

| # | Block | Min |
|---|---|---|
| 1 | Recap, and last session's homework | 5 |
| 2 | **Teach:** the new idea — ends with something running | 12 |
| 3 | **Run together:** the notebook's example cells, cell by cell | 20 |
| 4 | **Do it yourself:** the exercises — Required, then Extra | 33 |
| 5 | Retrospective | 5 |
| | **Total** | **75** |

### Discovery session — one topic, one arc

| # | Block | Min |
|---|---|---|
| 1 | Recap, and last session's homework | 5 |
| 2 | **Teach:** today's task, and the only way we can do it so far | 7 |
| 3 | **Do it the long way:** the real task, with most of it shipped | 22 |
| 4 | **Teach:** the tool that shortens it | 9 |
| 5 | **Do the same task again**, with the tool. Compare the two | 27 |
| 6 | Retrospective | 5 |
| | **Total** | **75** |

### Paired session — two topics, practice at home

| # | Block | Min |
|---|---|---|
| 1 | Recap, and last session's homework | 5 |
| 2 | **Teach:** the first idea | 12 |
| 3 | **Run together:** the first notebook's example cells | 16 |
| 4 | **Teach:** the second idea | 12 |
| 5 | **Run together:** the second notebook's example cells | 16 |
| 6 | **Do it yourself:** as far as you get in both notebooks | 9 |
| 7 | Retrospective, and what to finish at home | 5 |
| | **Total** | **75** |

> **The paired session is the compromise this schedule forces, and it is stated here
> rather than hidden.** Hands-on is **41 of 75** against 53 on a single session. **Four** sessions use this agenda — 6, 8, 14 and 16 — and two more hold two topics under
> a bespoke agenda (1 and 18). **None of the six is a discovery session** — the arcs
> always keep their full 75 minutes.

Teaching never exceeds **12 minutes** in one block; a paired session is two blocks of 12,
not one of 24. Hands-on is **53 of 75** on a single session, **49** on a discovery
session, **41** on a paired one.

---

## Session agendas that differ from the shapes

### Session 1 — The school, and functions that bend · *topics 1–2*

| # | Activity | Min |
|---|---|---|
| 1 | Welcome back. A live demo of the finished tool: it reads the school's file, prints the term's statistics, and saves a chart | 5 |
| 2 | **Hands-on:** `python check_setup.py` — six green lines, including `numpy`, `matplotlib` and `pandas` | 14 |
| 3 | Recap of the grade-10 gradebook, and what the school actually asks for — three classes, five subjects, a term of grades | 10 |
| 4 | **Hands-on:** open `school.csv`, read it with what they already know, print the first rows and the school average | 16 |
| 5 | **Teach:** default arguments, then keyword arguments | 12 |
| 6 | **Run together:** topic 2's cells, including the deliberate `TypeError` | 13 |
| 7 | Retrospective. The promise: **everything hard in this course arrives because you needed it first** | 5 |
| | **Total** | **75** |

### Session 17 — Five files that each do one thing · *topic 22 · transition*

| # | Activity | Min |
|---|---|---|
| 1 | Recap: everything the notebook can now do, on screen | 5 |
| 2 | **Teach:** five files, one job each, drawn on screen with the arrows between them | 12 |
| 3 | **Hands-on:** `settings.py`, then `people.py` — the classes, moved out of the notebook | 18 |
| 4 | **Hands-on:** `loading.py`, with the checks that refuse a bad file | 16 |
| 5 | **Hands-on:** `charts.py`, then `main.py`. **Run `python main.py` for the first time** | 14 |
| 6 | Retrospective. **The instructor confirms `python main.py` individually for every participant, on a shared screen, before they leave** | 10 |
| | **Total** | **75** |

### Session 18 — Make it yours, and show it · *topics 23–24 · project*

| # | Activity | Min |
|---|---|---|
| 1 | Recap: everyone's `python main.py` runs on the sample school | 3 |
| 2 | **Hands-on:** your own school's file in, and the font fix if the names do not render | 12 |
| 3 | **Teach:** four features you could add, and the one question that decides which file the code goes in | 10 |
| 4 | **Hands-on:** build the one you chose. The instructor moves between shared screens; nobody is given code | 22 |
| 5 | **Hands-on:** write your `README.md` and `requirements.txt`, then send your folder to a colleague who runs it from your README alone | 18 |
| 6 | **Showcase**, the libraries we only name, and what Part 2 would be | 10 |
| | **Total** | **75** |

---

# The 24 topics

## Topic 1 — The school, and what we are going to build

The one session that is mostly not programming. They already have Anaconda and VS Code
from the grade-10 course, so there is no installation — but **three libraries must be
proved present before session 9**, and this is where that happens.

## Topic 2 — Functions that bend

Default arguments, then keyword arguments. One function that prints a
report line, called six ways. `*args` is shown **once**, named, and not drilled —
state topic 16 requires a teacher to recognise it.

## Topic 3 — Sending back more than one answer

`return a, b`, and unpacking it on the other side. The grade-10 course
used `for name, grade in grades.items():` without the word "tuple"; today the word
arrives, and so does the reason it works.

## Topic 4 — Six reports, six loops  ⟵ *discovery*

**The real task:** the head teacher wants six lists out of one register — who passed,
who failed, the top five, each subject. With what the participant knows, that is one loop
each, and when the pass mark changes all six must be edited.

**The tool, the same session:** the list comprehension. The notebook promises it in
writing before the long stretch begins, and ends with the two versions side by side and a
count of the lines.

## Topic 5 — Choosing while you build

A comprehension with a condition, the one-line `if`/`else` inside one,
and a dictionary comprehension once. `lambda` arrives **only** as a sort key —
`sorted(students, key=lambda s: s.average)` — which is the single place a teacher will
meet it in the pupils' material.

## Topic 6 — A student is more than a grade  ⟵ *discovery*

**The real task:** a student is no longer a name and a grade. They are a name, a class,
five subject marks, attendance and a note — nine fields. With what the participant knows,
that is a dictionary per student.

**What breaks:** one key is misspelled `clas`, and `average_of()` and `failed_subjects()`
both run happily over it. The `KeyError` arrives thirty lines later, in the grouping code,
naming neither the student nor the line that caused it.

**The tool, the same session:** `class Student`, `__init__`, `self`. The same typo as a
keyword argument raises on the spot and names it. **That contrast is the argument for
objects**, and it is made by running code rather than by assertion.

## Topic 7 — The calculation moves inside

Methods. The average, the pass/fail decision and the report line were
loose functions taking a dictionary; they become `student.average()`,
`student.has_passed()`, `student.report_line()`. The data and the thing that calculates it
now travel together.

## Topic 8 — A class full of students

`SchoolClass` holds a list of `Student` objects. Objects inside objects,
and a method that loops over them. The school's three classes exist by the end of the hour.

## Topic 9 — Teachers as well as students  ⟵ *discovery*

**The real task:** the school has teachers too — a name, a class and a phone number like
a student, plus a subject and a salary. With what the participant knows, that is copying
the whole `Student` class and editing it. Then a surname rule changes and both need the
same edit.

**The tool, the same session:** `class Teacher(Person)` and `super().__init__()`. The
surname change is made once and both classes move.

## Topic 10 — One loop, many kinds

Overriding a method, and why one loop over a list of mixed `Person`s
prints the right line for each without a single `if`. Polymorphism is **named at the end,
after it has already worked**, never before.

## Topic 11 — The register, rewritten

No new syntax. The grade-10 gradebook, rebuilt with `Person`,
`Student`, `Teacher` and `SchoolClass`, side by side with the dictionary version.

> **The consolidation session for the whole object block, and the last before the
> midpoint**, which is sat after this day. The block boundary is deliberate: everything
> the midpoint asks about has been taught by now, and nothing after it is a library.

## Topic 12 — The term's statistics  ⟵ *discovery*

**The real task:** the ministry wants the term's figures — mean, highest, lowest, and how
spread out the marks are, per subject and per class. The mean and the extremes go fine by
loop. The spread does not: the formula is written out by hand, and that is where it stops
being reasonable.

**The tool, the same session:** `import numpy as np`, and `.mean() .min() .max() .std()`.
**The first import of something the course did not write**, and it arrives as relief from
work already done.

## Topic 13 — Whole arrays at once

Creating arrays, indexing and slicing them, arithmetic on a whole array
at once, and a boolean mask — `grades[grades < PASS_MARK]`. The moment a teacher stops
writing the loop at all.

## Topic 14 — Show the head teacher  ⟵ *discovery*

**The real task:** the figures have to be shown at a staff meeting, not read out. With
what the participant knows, that is a bar chart drawn with `print()` and asterisks, scaled
by hand. It works, and it cannot go in a report.

**The tool, the same session:** `matplotlib.pyplot`, `plt.bar()`, and `plt.savefig()` —
after which the file opens on their own desktop.

## Topic 15 — The four charts a school asks for

Bar for subject averages, histogram for the spread of one class, a line
for the grade distribution, and a grouped bar comparing three classes across five subjects.

> The sample school holds one term, not several, so there is no honest progress-over-time
> chart to draw from it. A line chart that invented one would teach the wrong habit.

> **The sample data is transliterated — `11A`, not `11Ա`** — the same decision grade 10
> made when it named its students `Ani` rather than `Անի`, so the language rule holds
> everywhere without an exception.
>
> **The Armenian font problem is still taught here**, because on topic 23 participants load
> *their own* school's file and the names in it will be Armenian. The session shows the
> missing-glyph box, and the one line that fixes it, against a name typed in the markdown
> and pasted in by the participant — never shipped inside a code cell.

## Topic 16 — The school's own file  ⟵ *discovery*

**The real task:** the school's own file has 180 rows, a header, a blank line and a comma
inside one field. Parsing it with `split(",")` takes twenty-two lines, and the row with
the comma is still wrong afterwards.

**The tool, the same session:** `pd.read_csv()`. One line, and it handles all three. This
is the session that pays off the near-miss flagged on topic 1.

## Topic 17 — Filter, group, describe

Selecting a column, filtering rows by a condition, `.groupby()` for
per-class and per-subject figures, and `.describe()`. The dataframe is not taught as a
data structure — it is taught as **the register, which you already understand**.

## Topic 18 — The term report

No new library. pandas and Matplotlib together: read the file, group it,
chart the result, save both the table and the picture. The session that proves the two
tools are one workflow.

## Topic 19 — How deep does it go?  ⟵ *discovery*

**The real task:** the ministry's file nests — school, then streams, then classes, then
groups — and not every branch goes the same depth. A loop per level works until the file
arrives with one level more.

**The tool, the same session:** a function that calls itself. The base case first, always,
and the depth stops appearing in the code at all.

> **Factorial and Fibonacci are not mentioned.** They are Part 2, and `check_style.py`
> fails a build that names either.

## Topic 20 — Where code comes from

`import` properly: our own modules, the standard library, and the three
installed ones. Then `pip`, `requirements.txt` and what a virtual environment is for —
against one small package, installed live. **The only session that needs internet.**
Google Colab is shown at the end, because the pupils' curriculum names it sixteen times.

## Topic 21 — Wrong, with no error

Debugging as its own topic — state topic 22. Reading a traceback from
the bottom up, VS Code's debugger, a breakpoint, stepping, and inspecting a variable
mid-run. The worked example is a function that returns a wrong average, silently.

## Topic 22 — Five files that each do one thing  ⟵ *transition*

**Concepts:** modules · one job per file · an entry point

The session that turns a notebook into a program. The classes, the file reading, the
charts and the entry point become five files, and the session does not end until
**`python main.py` has run for every participant individually, on a shared screen**.

**Neither half may be cut.**

## Topic 23 — Make it yours

**Concepts:** your own data · one feature of your own design

Their own school's file goes in — which is where the Armenian font problem becomes real
rather than hypothetical — and each participant adds **one** feature they chose. Nobody is
given code; the instructor moves between shared screens and asks questions.

## Topic 24 — Finish and show

**Concepts:** a program someone else can run · what comes next

A `README.md` and a `requirements.txt`, then a colleague runs the folder **from that
README alone** and reports back. Then ninety seconds each: what it does, one thing that
broke, one thing they would add.

The session closes on the libraries the pupils' topic 21 names but this course never uses,
with what each one is and why a grade-11 teacher does not need it — because pupils will
ask, and "that is difficult" is the wrong answer.

---

## Time check

```
Sessions  1- 6   450      Sessions 13-18   450
Sessions  7-12   450
                        ---------------------
                          1,350 minutes  =  22 h 30  ✓
```

Notebook phase: sessions 1–16, topics 1–21 (1,200 min / 20 h).
Transition: session 17, topic 22 (75 min).
Project: session 18, topics 23–24 (75 min).

> **This schedule has the least contact time of any the programme has used** — 22½ hours
> against 30 for three sessions a week and 32 for two of two hours. Nothing was cut: all <!--history-->
> 24 topics survive, and the practice that no longer fits in the room is set as homework.
> **That makes homework load-bearing here in a way it was not before**, and the risk is
> stated plainly in `RATIONALE.md`.

## Homework

**Homework is the practice that no longer fits, not new work.** Every notebook carries ten
tasks in three tiers. What changes with this schedule is how much of that a participant
reaches in the room.

| Session shape | What is set | Roughly |
|---|---|---|
| **Single** | the Extra tier, if Required was finished in the room | 15–20 min |
| **Discovery** | the Extra tier of that notebook | 15–20 min |
| **Paired** | the **Required** tier of both notebooks — and nothing else | 30–40 min |
| **Setup** (session 1) | topic 2's Required tier | 15–20 min |
| **Transition, project** | nothing. Both are hands-on throughout | — |

**Homework is the same work as the session, in the same place.** It is never a different
kind of task, never a longer one, and never a new idea:

- Every task is **already printed in the notebook** the session used, in the same three
  tiers, with the same skeleton-and-comment shape as the tasks done in the room.
- **The Extra tier is never set on top of the Required tier.** On a paired session the
  Required tier is the whole of it; Extra stays available and is not asked for.
- **No Challenge task is ever homework.**
- **Nothing new is introduced at home.** Homework uses only what that session taught.
- **The next session opens by checking it**, and every agenda has that block.

> **A participant who does no homework will not finish this version of the course.**
> **Say so at enrolment**, not in week three.

## Assessment

**Three sittings.** They are **separate from the 18 teaching sessions**, which remain
22½ hours exactly.

| | Test | When | Length | Covers |
|---|---|---|---|---|
| 1 | Initial diagnostic | **Before session 1** | 45–60 min | What the grade-10 course left them with. Nothing from this course |
| 2 | Midpoint | **After session 8** | 60–75 min | Topics 2–11: functions, comprehensions, classes, inheritance |
| 3 | Final practical | **Session 18** | 90–120 min | Topics 12–24: libraries, charts, data, recursion, the project |

- **Each question has variants A, B and C**, equivalent in difficulty.
- **Two versions of every test are generated** — `tests/<name>.ipynb` for the grader, with
  the rubric, and `tests/participant/<name>.ipynb` with questions only.
- **Record a help level with every score** — `3` independent, `2` after one hint, `1` with
  step-by-step help, `0` did not finish.
- **Scores diagnose the programme, not the teachers**, and participants are told so.

**The diagnostic matters more here than it did in grade 10.** It is the only measurement
of what the first course actually produced, taken before this one can affect it.

## Week map

| Week | Sessions | Topics | Arc | Assessment |
|---|---|---|---|---|
| 1 | 1–2 | 1–3 | My functions bend to what is asked of them | *(diagnostic sat before session 1)* |
| 2 | 3–4 | 4–5 | One line instead of six | |
| 3 | 5–6 | 6–8 | A student is a thing, and the school is objects | |
| 4 | 7–8 | 9–11 | They share what they have in common | **Midpoint**, sat after session 8 |
| 5 | 9–10 | 12–13 | I can measure a term | |
| 6 | 11–12 | 14–15 | I can draw it | |
| 7 | 13–14 | 16–18 | The school's own file goes in, a report comes out | |
| 8 | 15–16 | 19–21 | Any depth, and I can find out why it is wrong | |
| 9 | 17–18 | 22–24 | It is a program now, it runs on my school, and I showed it | **Final practical**, sat in session 18 |
