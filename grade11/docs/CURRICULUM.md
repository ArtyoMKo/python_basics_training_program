# Curriculum — the grade-11 course

**16 sessions × 120 minutes = 32 hours.** Two a week over eight weeks. Remote, in groups
of 4–8. Arithmetic verified by `tools/check_times.py`.

Entry is the grade-10 course and nothing beyond it. See `AGENTS.md` for what that means
in practice, and `BUILD_PLAN.md` for what is built.

> **The course teaches 24 topics across 16 sessions.** A topic is one notebook and one
> idea. A session is two hours in a room. Most sessions hold two topics; the discovery
> sessions hold one — or one plus the topic that consolidates it, which is never the
> discovery arc itself.

## The session map

| # | Session | Topics | Shape | Min |
|---|---|---|---|---|
| 1 | The school, and functions that bend | 1–2 | Setup | 120 |
| 2 | Sending back more than one answer | 3 | Single | 120 |
| 3 | **Six reports, six loops** | 4 | **Discovery** | 120 |
| 4 | Choosing while you build | 5 | Single | 120 |
| 5 | **A student is more than a grade** | 6 | **Discovery** | 120 |
| 6 | The calculation moves inside, and a class full of students | 7–8 | Paired | 120 |
| 7 | **Teachers as well as students** | 9 | **Discovery** | 120 |
| 8 | One loop many kinds, and the register rewritten | 10–11 | Paired | 120 |
| 9 | **The term's statistics**, then whole arrays at once | 12–13 | **Discovery +** | 120 |
| 10 | **Show the head teacher**, then the four charts | 14–15 | **Discovery +** | 120 |
| 11 | **The school's own file** | 16 | **Discovery** | 120 |
| 12 | Filter, group, describe — and the term report | 17–18 | Paired | 120 |
| 13 | **How deep does it go?** | 19 | **Discovery** | 120 |
| 14 | Where code comes from, and wrong with no error | 20–21 | Paired | 120 |
| 15 | Five files that each do one thing | 22 | Transition | 120 |
| 16 | Make it yours, and show it | 23–24 | Project | 120 |

Seven discovery sessions — **3, 5, 7, 9, 10, 11, 13**. Each resolves its own difficulty
inside its own session. **Never split one.**

## The state curriculum, by session

| State topic | Pupil hours | Topics here | Sessions |
|---|---|---|---|
| 16 — Խորացված ֆունկցիաներ | 15 | 2, 3, 4, 5 | 1–4 |
| 18 — Դասեր (Class) | 12 | 6, 7, 8, 11 | 5, 6, 8 |
| 19 — Ժառանգականություն | 10 | 9, 10, 11 | 7, 8 |
| 15 — Մոդուլների ներածություն \| Colab | 15 | 1, 12, 14, 20 | 1, 9, 10, 14 |
| 21 — Գրադարաններ և միջավայրեր | 23 | 12–18, 20 | 9–12, 14 |
| 20 — Մոդուլներ և կրկնություն | 8 | 20, 22 | 14, 15 |
| 17 — Ռեկուրսիա | 15 | 19 | 13 — **mechanics only**; the algorithms are Part 2 |
| 22 — Սխալների հանգուցալուծում | 7 | 21, and every topic's error reading | 14 |
| 24 — Ամփոփում | 2 | 24 | 16 |
| 23 — Git | 6 | — | **not taught** — deferred by decision |

The full audit, construct by construct, is in `../shared/GOVERNMENT_ASSIGNMENT.md` §8.

## The agenda shapes

All five sum to 120.

### Paired session — two topics

| # | Block | Min |
|---|---|---|
| 1 | Recap, and last session's homework | 8 |
| 2 | **Teach:** the first idea — ends with something running | 12 |
| 3 | **Run together:** the first notebook's example cells | 18 |
| 4 | **Do it yourself:** the first notebook's Required tasks | 22 |
| 5 | **Teach:** the second idea | 12 |
| 6 | **Run together:** the second notebook's example cells | 18 |
| 7 | **Do it yourself:** the second notebook's Required tasks | 25 |
| 8 | Retrospective, and what to finish at home | 5 |
| | **Total** | **120** |

### Single session — one topic, in depth

| # | Block | Min |
|---|---|---|
| 1 | Recap, and last session's homework | 8 |
| 2 | **Teach:** the new idea | 12 |
| 3 | **Run together:** the notebook's example cells, cell by cell | 25 |
| 4 | **Do it yourself:** Required | 35 |
| 5 | **Do it yourself:** Extra — in the session, not at home | 32 |
| 6 | Retrospective | 8 |
| | **Total** | **120** |

### Discovery session — one topic, one arc

| # | Block | Min |
|---|---|---|
| 1 | Recap, and last session's homework | 6 |
| 2 | **Teach:** today's task, and the only way we can do it so far | 10 |
| 3 | **Do it the long way:** the real task, with most of it shipped | 32 |
| 4 | **Teach:** the tool that shortens it | 12 |
| 5 | **Do the same task again**, with the tool. Compare the two | 50 |
| 6 | Retrospective | 10 |
| | **Total** | **120** |

### Discovery + consolidation — sessions 9 and 10

Used **only** where the topic that follows a discovery is that same tool applied wider:
NumPy's arrays after NumPy, the four charts after Matplotlib.

| # | Block | Min |
|---|---|---|
| 1 | Recap, and last session's homework | 5 |
| 2 | **Teach:** today's task, and the only way we can do it so far | 8 |
| 3 | **Do it the long way** | 25 |
| 4 | **Teach:** the tool that shortens it | 10 |
| 5 | **Do the same task again**, with the tool | 33 |
| 6 | **Teach:** the same tool, wider | 10 |
| 7 | **Run together:** the second notebook's example cells | 12 |
| 8 | **Do it yourself:** the second notebook's Required tasks | 12 |
| 9 | Retrospective, and what to finish at home | 5 |
| | **Total** | **120** |

> **The discovery arc gets 76 of those minutes. On the old schedule the arc was 65** —
> blocks 2 to 5 of a 75-minute discovery day. So the arc gained eleven minutes; it was
> not compressed.
>
> **What the second topic loses is real, and is stated here rather than buried.** It had
> 65 minutes as a standalone day and has 34 here: the guided walkthrough of its example
> cells survives at 12 minutes, and the rest of its Required tier moves to homework
> along with its Extra tier. That is the price of keeping two discovery arcs whole in a
> sixteen-session course, and it is paid by the two topics — 13 and 15 — that are the
> *same tool applied wider*, never by a topic that introduces something new.

### Transition and project — sessions 15 and 16

Given in full below; they do not follow a shape.

### Setup, transition and project — sessions 1, 15 and 16

Given in full below; they do not follow a shape.

Teaching never exceeds **12 minutes** in one block — a paired session is two blocks of
12, not one of 24. Hands-on is **83 of 120** on a paired session, **92** on a single,
**82** on a discovery session, **82** on a discovery + consolidation and **81** on
session 1, whose first half is an installation check. Never below 67%.

> **Never split a discovery session.** If it runs long, cut the Extra tasks — never the
> second half.

---

## Session agendas that differ from the shapes

### Session 1 — The school, and functions that bend · *topics 1–2*

| # | Activity | Min |
|---|---|---|
| 1 | Welcome back. A live demo of the finished tool: it reads the school's file, prints the term's statistics, and saves a chart | 8 |
| 2 | **Hands-on:** `python check_setup.py` — six green lines, including `numpy`, `matplotlib` and `pandas`. Screen-share with anyone who is not green | 16 |
| 3 | Recap of the grade-10 gradebook, running, on screen. **This is the thing we are going to outgrow** | 8 |
| 4 | **Teach:** what the school actually asks for — three classes, five subjects, a term of grades | 6 |
| 5 | **Hands-on:** open `school.csv`, read it with what they already know, print the first rows and the school average | 22 |
| 6 | **Teach:** default arguments, then keyword arguments | 12 |
| 7 | **Run together:** topic 2's cells, including the deliberate `TypeError` | 18 |
| 8 | **Do it yourself:** topic 2's Required tasks | 25 |
| 9 | Retrospective. The promise: **everything hard in this course arrives because you needed it first** | 5 |
| | **Total** | **120** |

### Session 3 — Six reports, six loops · *topic 4 · discovery*

| # | Activity | Min |
|---|---|---|
| 1 | Recap: functions with defaults, and returning two things | 6 |
| 2 | **Teach:** the head teacher wants six lists from one register. With what we know, that is one loop each. *After the break, a way to write each of them on one line* | 10 |
| 3 | **Do it:** three of the six loops are shipped; write the other three. Then the pass mark changes and all six must be edited | 32 |
| 4 | **Teach:** the list comprehension — `[s for s in students if …]`, read right to left | 12 |
| 5 | **Do the same again:** all six, as comprehensions. Put the two versions side by side and count the lines | 50 |
| 6 | Retrospective | 10 |
| | **Total** | **120** |

### Session 5 — A student is more than a grade · *topic 6 · discovery*

| # | Activity | Min |
|---|---|---|
| 1 | Recap: the register as a dictionary | 6 |
| 2 | **Teach:** a student is now a name, a class, five subject grades, attendance and a note. With what we know, that is a dictionary per student. *After the break, a way to describe a student once and make thirty-six of them* | 10 |
| 3 | **Do it:** build four students as dictionaries. Then misspell one key — and watch it fail silently, with no error, three functions later | 32 |
| 4 | **Teach:** `class Student`, `__init__`, `self`, attributes. Defining is not creating | 12 |
| 5 | **Do the same again:** `Student` objects. Misspell the same thing and read the error that now appears immediately | 50 |
| 6 | Retrospective | 10 |
| | **Total** | **120** |

### Session 7 — Teachers as well as students · *topic 9 · discovery*

| # | Activity | Min |
|---|---|---|
| 1 | Recap: `Student`, and `SchoolClass` holding a list of them | 6 |
| 2 | **Teach:** the school has teachers too. They have a name, a class and a phone number, like a student — and a subject and a salary, which a student has not. *After the break, a way to say "everything a person has, plus"* | 10 |
| 3 | **Do it:** copy the whole `Student` class, rename it `Teacher`, edit it. Then a surname rule changes and both classes need the same edit | 32 |
| 4 | **Teach:** `class Teacher(Person)` — what is inherited, and `super().__init__()` | 12 |
| 5 | **Do the same again:** `Person`, then `Student(Person)` and `Teacher(Person)`. Make the surname change **once** and watch both move | 50 |
| 6 | Retrospective | 10 |
| | **Total** | **120** |

### Session 9 — The term's statistics, then whole arrays · *topics 12–13 · discovery +*

| # | Activity | Min |
|---|---|---|
| 1 | Recap: the school, as objects | 5 |
| 2 | **Teach:** the ministry wants the term's figures — mean, highest, lowest, and how spread out the grades are. That is 180 numbers, five subjects, three classes. *After the break, a tool that does all four in four lines* | 8 |
| 3 | **Do it:** mean and extremes by loop, which works. Then the spread, by hand, which is where it stops being reasonable | 25 |
| 4 | **Teach:** `import numpy as np`, the array, and `.mean() .min() .max() .std()` | 10 |
| 5 | **Do the same again:** every figure, per subject and per class. Compare the two versions. **The first `import` of something we did not write** | 35 |
| 6 | **Teach:** the same tool, wider — whole-array arithmetic, boolean masks, `axis` | 10 |
| 7 | **Do it yourself:** topic 13's Required tasks | 22 |
| 8 | Retrospective, and what to finish at home | 5 |
| | **Total** | **120** |

### Session 10 — Show the head teacher, then the four charts · *topics 14–15 · discovery +*

| # | Activity | Min |
|---|---|---|
| 1 | Recap: arrays, and statistics in one line | 5 |
| 2 | **Teach:** the figures have to be shown at a staff meeting, not read out. *After the break, a tool that draws them* | 8 |
| 3 | **Do it:** a bar chart with `print()` and asterisks, scaled by hand. It works, and it cannot go in a report | 25 |
| 4 | **Teach:** `import matplotlib.pyplot as plt`, `plt.bar()`, labels, `plt.savefig()` | 10 |
| 5 | **Do the same again:** the same chart, drawn. Then save it as a PNG and open the file | 35 |
| 6 | **Teach:** the other three charts — histogram, line, grouped bar — and when each is the right one | 10 |
| 7 | **Do it yourself:** topic 15's Required tasks | 22 |
| 8 | Retrospective, and what to finish at home | 5 |
| | **Total** | **120** |

### Session 11 — The school's own file · *topic 16 · discovery*

| # | Activity | Min |
|---|---|---|
| 1 | Recap: charts, saved to disk | 6 |
| 2 | **Teach:** the school's real file has 180 rows, a header, a blank line and a comma inside one field. *After the break, a tool that reads it in one line* | 10 |
| 3 | **Do it:** parse it with `split(",")`. Handle the header, the blank, then the quoted note — and find the row that is still wrong | 32 |
| 4 | **Teach:** `import pandas as pd`, `pd.read_csv()`, `.head()`, `.shape`, `.columns` | 12 |
| 5 | **Do the same again:** one line, and the same five checks. Compare | 50 |
| 6 | Retrospective | 10 |
| | **Total** | **120** |

### Session 13 — How deep does it go? · *topic 19 · discovery*

| # | Activity | Min |
|---|---|---|
| 1 | Recap: the term report, from file to chart | 6 |
| 2 | **Teach:** the ministry's file nests — school, then streams, then classes, then groups — and not every branch goes the same depth. We need every student in it. *After the break, a way to write that once* | 10 |
| 3 | **Do it:** a loop inside a loop inside a loop. It works — until the file arrives with one level more | 32 |
| 4 | **Teach:** a function that calls itself. The base case first, always. Why the depth no longer appears in the code | 12 |
| 5 | **Do the same again:** one recursive function, any depth. Then add a level to the file and change nothing | 50 |
| 6 | Retrospective. **Factorial and Fibonacci are not mentioned. They are Part 2** | 10 |
| | **Total** | **120** |

### Session 15 — Five files that each do one thing · *topic 22 · transition*

| # | Activity | Min |
|---|---|---|
| 1 | Recap, and last session's homework: everything the notebook can now do | 6 |
| 2 | **Teach:** five files, one job each, drawn on screen with the arrows between them | 12 |
| 3 | **Hands-on:** `settings.py`, then `people.py` — the classes, moved out of the notebook | 28 |
| 4 | **Hands-on:** `loading.py`, with the checks that refuse a bad file | 24 |
| 5 | **Hands-on:** `charts.py` | 20 |
| 6 | **Hands-on:** `main.py`. **Run `python main.py` for the first time** | 22 |
| 7 | Retrospective. **The instructor confirms `python main.py` individually for every participant, on a shared screen, before they leave** | 8 |
| | **Total** | **120** |

### Session 16 — Make it yours, and show it · *topics 23–24 · project*

| # | Activity | Min |
|---|---|---|
| 1 | Recap: everyone's `python main.py` runs on the sample school | 3 |
| 2 | **Hands-on:** your own school's file in, and the font fix if the names do not render | 20 |
| 3 | **Teach:** four features you could add, and the one question that decides which file the code goes in | 12 |
| 4 | **Hands-on:** build the one you chose. The instructor moves between shared screens; nobody is given code | 30 |
| 5 | **Hands-on:** write your `README.md` and `requirements.txt`, then send your folder to a colleague who runs it **from your README alone** | 25 |
| 6 | **Showcase:** 90 seconds each — your chart, one thing that broke, one thing you would add | 18 |
| 7 | The libraries we only name, where to go next, and what Part 2 would be | 12 |
| | **Total** | **120** |

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

## Topic 5 — Choosing while you build

A comprehension with a condition, the one-line `if`/`else` inside one,
and a dictionary comprehension once. `lambda` arrives **only** as a sort key —
`sorted(students, key=lambda s: s.average)` — which is the single place a teacher will
meet it in the pupils' material.

## Topic 6 — A student is more than a grade  ⟵ *discovery*

## Topic 7 — The calculation moves inside

Methods. The average, the pass/fail decision and the report line were
loose functions taking a dictionary; they become `student.average()`,
`student.has_passed()`, `student.report_line()`. The data and the thing that calculates it
now travel together.

## Topic 8 — A class full of students

`SchoolClass` holds a list of `Student` objects. Objects inside objects,
and a method that loops over them. The school's three classes exist by the end of the hour.

## Topic 9 — Teachers as well as students  ⟵ *discovery*

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

## Topic 13 — Whole arrays at once

Creating arrays, indexing and slicing them, arithmetic on a whole array
at once, and a boolean mask — `grades[grades < PASS_MARK]`. The moment a teacher stops
writing the loop at all.

## Topic 14 — Show the head teacher  ⟵ *discovery*

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

## Topic 17 — Filter, group, describe

Selecting a column, filtering rows by a condition, `.groupby()` for
per-class and per-subject figures, and `.describe()`. The dataframe is not taught as a
data structure — it is taught as **the register, which you already understand**.

## Topic 18 — The term report

No new library. pandas and Matplotlib together: read the file, group it,
chart the result, save both the table and the picture. The session that proves the two
tools are one workflow.

## Topic 19 — How deep does it go?  ⟵ *discovery*

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

## Topic 23 — Make it yours

## Topic 24 — Finish and show

---

---

## Time check

```
Sessions  1- 4   480      Sessions  9-12   480
Sessions  5- 8   480      Sessions 13-16   480
                        ---------------------
                          1,920 minutes  =  32 hours  ✓
```

Notebook phase: sessions 1–14, topics 1–21 (1,680 min / 28 h).
Transition: session 15, topic 22 (120 min).
Project: session 16, topics 23–24 (120 min).

> **The move from three 120-minute sessions a week to two of 120 added two hours of
> contact time**, not removed any. What it removed is the third touchpoint in a week —
> and that is what homework replaces.

## Homework

**Homework is the practice that did not fit, not new work.** Every notebook already
carries ten tasks in three tiers; a paired session reaches the Required tier of both
notebooks and little more.

| Session shape | What is set | Roughly |
|---|---|---|
| **Setup** (session 1) | the second notebook's Required tasks not reached in the room | 20–30 min |
| **Paired** | the Required tasks of **either** notebook you did not reach, then the Extra tier of the **second** notebook only | 30–45 min |
| **Single** | nothing. The Extra tier is done **in the session** | — |
| **Discovery** | the Extra tier of that notebook | 20–30 min |
| **Discovery + consolidation** | the **second** notebook only: the Required tasks not reached in the room, then its Extra tier | 35–45 min |
| **Transition, project** | nothing. Both are hands-on throughout | — |

Rules this follows:

- **No task was written for homework.** Every one already existed and a three-a-week
  schedule had time for it in the room.
- **A paired session sets one Extra tier, not two.** Ten tasks cold is an evening's work
  and not what this schedule intends.
- **Required tasks are never homework by design** — only by overflow, and the next
  session's first block is where they are checked.
- **Nothing new is introduced at home.** Homework uses only what the session taught.
- **A participant who does no homework still finishes the course.** They will be slower,
  and the instructor will see it in the recap block.

## Assessment

**Three sittings.** They are **separate from the 16 teaching sessions**, which remain 32
hours exactly.

| | Test | When | Length | Covers |
|---|---|---|---|---|
| 1 | Initial diagnostic | **Before session 1** | 45–60 min | What the grade-10 course left them with. Nothing from this course |
| 2 | Midpoint | **After session 8** | 60–75 min | Topics 2–11: functions, comprehensions, classes, inheritance |
| 3 | Final practical | **Session 16** | 90–120 min | Topics 12–24: libraries, charts, data, recursion, the project |

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
| 5 | 9–10 | 12–15 | I can measure a term and draw it | |
| 6 | 11–12 | 16–18 | The school's own file goes in, a report comes out | |
| 7 | 13–14 | 19–21 | Any depth, and I can find out why it is wrong | |
| 8 | 15–16 | 22–24 | It is a program now, it runs on my school, and I showed it | **Final practical**, sat in session 16 |
