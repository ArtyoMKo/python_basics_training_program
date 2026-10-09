# Curriculum — the grade-11 course

24 sessions × 75 minutes = **30 hours**. Three a week over eight weeks. Remote, in groups
of 4–8. Arithmetic verified by `tools/check_times.py`.

Entry is the grade-10 course and nothing beyond it. See `AGENTS.md` for what that means
in practice, and `BUILD_PLAN.md` for what is built so far.

## The day map

| # | Title | Shape | File | Min |
|---|---|---|---|---|
| 1 | The school, and what we are going to build | Notebook | `notebooks/day01_setup_and_school.ipynb` | 75 |
| 2 | Functions that bend | Notebook | `notebooks/day02_default_arguments.ipynb` | 75 |
| 3 | Sending back more than one answer | Notebook | `notebooks/day03_many_returns.ipynb` | 75 |
| 4 | **Six reports, six loops** | **Discovery** | `notebooks/day04_comprehensions.ipynb` | 75 |
| 5 | Choosing while you build | Notebook | `notebooks/day05_choosing_while_building.ipynb` | 75 |
| 6 | **A student is more than a grade** | **Discovery** | `notebooks/day06_classes.ipynb` | 75 |
| 7 | The calculation moves inside | Notebook | `notebooks/day07_methods.ipynb` | 75 |
| 8 | A class full of students | Notebook | `notebooks/day08_objects_in_objects.ipynb` | 75 |
| 9 | **Teachers as well as students** | **Discovery** | `notebooks/day09_inheritance.ipynb` | 75 |
| 10 | One loop, many kinds | Notebook | `notebooks/day10_overriding.ipynb` | 75 |
| 11 | The register, rewritten | Notebook | `notebooks/day11_school_with_objects.ipynb` | 75 |
| 12 | **The term's statistics** | **Discovery** | `notebooks/day12_numpy.ipynb` | 75 |
| 13 | Whole arrays at once | Notebook | `notebooks/day13_numpy_arrays.ipynb` | 75 |
| 14 | **Show the head teacher** | **Discovery** | `notebooks/day14_matplotlib.ipynb` | 75 |
| 15 | The four charts a school asks for | Notebook | `notebooks/day15_charts.ipynb` | 75 |
| 16 | **The school's own file** | **Discovery** | `notebooks/day16_pandas.ipynb` | 75 |
| 17 | Filter, group, describe | Notebook | `notebooks/day17_pandas_groups.ipynb` | 75 |
| 18 | The term report | Notebook | `notebooks/day18_term_report.ipynb` | 75 |
| 19 | **How deep does it go?** | **Discovery** | `notebooks/day19_recursion.ipynb` | 75 |
| 20 | Where code comes from | Notebook | `notebooks/day20_packages.ipynb` | 75 |
| 21 | Wrong, with no error | Notebook | `notebooks/day21_debugging.ipynb` | 75 |
| 22 | **Five files that each do one thing** | **Transition** | `guides/day22_five_files.md` | 75 |
| 23 | Make it yours | Project | `guides/day23_make_it_yours.md` | 75 |
| 24 | Finish and show | Project | `guides/day24_finish_and_show.md` | 75 |

Seven discovery days — **4, 6, 9, 12, 14, 16, 19**. Each resolves its own difficulty in
its own session. **Never split one.**

## The state curriculum, by day

| State topic | Pupil hours | Days here |
|---|---|---|
| 16 — Խորացված ֆունկցիաներ | 15 | 2, 3, 4, 5 |
| 18 — Դասեր (Class) | 12 | 6, 7, 8, 11 |
| 19 — Ժառանգականություն | 10 | 9, 10, 11 |
| 15 — Մոդուլների ներածություն \| Colab | 15 | 1, 12, 14, 20 |
| 21 — Գրադարաններ և միջավայրեր | 23 | 12, 13, 14, 15, 16, 17, 18, 20 |
| 20 — Մոդուլներ և կրկնություն | 8 | 20, 22 |
| 17 — Ռեկուրսիա | 15 | 19 — **mechanics only**; the algorithms are Part 2 |
| 22 — Սխալների հանգուցալուծում | 7 | 21, and every day's error reading |
| 24 — Ամփոփում | 2 | 24 |
| 23 — Git | 6 | **not taught** — deferred by decision |

## The two agenda shapes

Every day is one of these two. Both sum to 75.

### Standard day

| # | Block | Min |
|---|---|---|
| 1 | Recap, and last time's retrospective question | 5 |
| 2 | **Teach:** the new idea — ends with something running | 12 |
| 3 | **Run together:** the notebook's example cells, cell by cell | 20 |
| 4 | **Do it yourself:** the exercises — Required, then Extra | 33 |
| 5 | Retrospective: where we got to, what comes next | 5 |
| | **Total** | **75** |

### Discovery day

| # | Block | Min |
|---|---|---|
| 1 | Recap | 5 |
| 2 | **Teach:** today's task, and the only way we can do it so far | 7 |
| 3 | **Do it the long way:** the real task, with most of it shipped | 22 |
| 4 | **Teach:** the tool that shortens it | 9 |
| 5 | **Do the same task again**, with the tool. Compare the two | 27 |
| 6 | Retrospective | 5 |
| | **Total** | **75** |

Teaching never exceeds 12 minutes in one block. Hands-on is 53 of 75 on a standard day,
49 of 75 on a discovery day.

> **Never split a discovery day.** If it runs long, cut the Extra tasks — never the
> second half. Ending a session after the long way and before the short way is the worst
> outcome this design can produce.

---

## Day 1 — The school, and what we are going to build

The one session that is mostly not programming. They already have Anaconda and VS Code
from the grade-10 course, so there is no installation — but **three libraries must be
proved present before day 12**, and this is where that happens.

| # | Block | Min |
|---|---|---|
| 1 | Welcome back. A live demo of the finished tool: it reads the school's file, prints the term's statistics, and saves a chart. "In eight weeks this is yours, with your school in it" | 8 |
| 2 | **Hands-on:** `python check_setup.py` — six green lines, including `numpy`, `matplotlib` and `pandas`. Screen-share with anyone who is not green | 18 |
| 3 | Recap of the grade-10 gradebook, running, on screen. **This is the thing we are going to outgrow** | 10 |
| 4 | **Teach:** what the school actually asks for — three classes, five subjects, a term of grades. Why the dictionary version will not stretch that far | 10 |
| 5 | **Hands-on:** open `data/school.csv`, read it with what they already know, print the first five rows | 24 |
| 6 | Retrospective. What is coming, and the promise: **everything hard in this course arrives because you needed it first** | 5 |

## Day 2 — Functions that bend

*Standard shape.* Default arguments, then keyword arguments. One function that prints a
report line, called six ways. `*args` is shown **once**, named, and not drilled —
state topic 16 requires a teacher to recognise it.

## Day 3 — Sending back more than one answer

*Standard shape.* `return a, b`, and unpacking it on the other side. The grade-10 course
used `for name, grade in grades.items():` without the word "tuple"; today the word
arrives, and so does the reason it works.

## Day 4 — Six reports, six loops  ⟵ *discovery*

| # | Block | Min |
|---|---|---|
| 1 | Recap: functions with defaults, and returning two things | 5 |
| 2 | **Teach:** the head teacher wants six lists — passing, failing, top five, each subject. With what we know, that is one loop each. *After the break, a way to write each of them on one line* | 7 |
| 3 | **Do it:** three of the six loops are shipped; write the other three. Then the pass mark changes and all six must be edited | 22 |
| 4 | **Teach:** the list comprehension — `[s for s in students if …]`, read right to left | 9 |
| 5 | **Do the same again:** all six, as comprehensions. Put the two versions side by side and count the lines | 27 |
| 6 | Retrospective | 5 |

## Day 5 — Choosing while you build

*Standard shape.* A comprehension with a condition, the one-line `if`/`else` inside one,
and a dictionary comprehension once. `lambda` arrives **only** as a sort key —
`sorted(students, key=lambda s: s.average)` — which is the single place a teacher will
meet it in the pupils' material.

## Day 6 — A student is more than a grade  ⟵ *discovery*

| # | Block | Min |
|---|---|---|
| 1 | Recap: the register as a dictionary, from the grade-10 course | 5 |
| 2 | **Teach:** a student is now a name, a class, five subject grades, attendance and a note. With what we know, that is a dictionary per student. *After the break, a way to describe a student once and make thirty-six of them* | 7 |
| 3 | **Do it:** build four students as dictionaries. Then misspell one key — and watch it fail silently, with no error, three functions later | 22 |
| 4 | **Teach:** `class Student`, `__init__`, `self`, attributes. Defining is not creating | 9 |
| 5 | **Do the same again:** `Student` objects. Misspell the same thing and read the `AttributeError` that now appears immediately | 27 |
| 6 | Retrospective | 5 |

## Day 7 — The calculation moves inside

*Standard shape.* Methods. The average, the pass/fail decision and the report line were
loose functions taking a dictionary; they become `student.average()`,
`student.has_passed()`, `student.report_line()`. The data and the thing that calculates it
now travel together.

## Day 8 — A class full of students

*Standard shape.* `SchoolClass` holds a list of `Student` objects. Objects inside objects,
and a method that loops over them. The school's three classes exist by the end of the hour.

## Day 9 — Teachers as well as students  ⟵ *discovery*

| # | Block | Min |
|---|---|---|
| 1 | Recap: `Student`, and `SchoolClass` holding a list of them | 5 |
| 2 | **Teach:** the school has teachers too. They have a name, a class and a phone number, like a student — and a subject and a salary, which a student has not. *After the break, a way to say "everything a person has, plus"* | 7 |
| 3 | **Do it:** copy the whole `Student` class, rename it `Teacher`, edit it. Then a surname rule changes and both classes need the same edit | 22 |
| 4 | **Teach:** `class Teacher(Person)` — what is inherited, and `super().__init__()` | 9 |
| 5 | **Do the same again:** `Person`, then `Student(Person)` and `Teacher(Person)`. Make the surname change **once** and watch both move | 27 |
| 6 | Retrospective | 5 |

## Day 10 — One loop, many kinds

*Standard shape.* Overriding a method, and why one loop over a list of mixed `Person`s
prints the right line for each without a single `if`. Polymorphism is **named at the end,
after it has already worked**, never before.

## Day 11 — The register, rewritten

*Standard shape.* No new syntax. The grade-10 gradebook, rebuilt with `Person`,
`Student`, `Teacher` and `SchoolClass`, side by side with the dictionary version. The
consolidation session for the whole object block, and the last one before the midpoint.

## Day 12 — The term's statistics  ⟵ *discovery*

| # | Block | Min |
|---|---|---|
| 1 | Recap: the school, as objects | 5 |
| 2 | **Teach:** the ministry wants the term's figures — mean, highest, lowest, and how spread out the grades are, per subject and per class. That is 600 numbers. *After the break, a tool that does all four in four lines* | 7 |
| 3 | **Do it:** mean and extremes by loop, which works. Then the spread, by hand, which is where it stops being reasonable | 22 |
| 4 | **Teach:** `import numpy as np`, the array, and `.mean() .min() .max() .std()` | 9 |
| 5 | **Do the same again:** every figure, per subject and per class. Compare the two versions | 27 |
| 6 | Retrospective. **The first `import` of something we did not write** | 5 |

## Day 13 — Whole arrays at once

*Standard shape.* Creating arrays, indexing and slicing them, arithmetic on a whole array
at once, and a boolean mask — `grades[grades < PASS_MARK]`. The moment a teacher stops
writing the loop at all.

## Day 14 — Show the head teacher  ⟵ *discovery*

| # | Block | Min |
|---|---|---|
| 1 | Recap: arrays, and statistics in one line | 5 |
| 2 | **Teach:** the figures have to be shown at a staff meeting, not read out. *After the break, a tool that draws them* | 7 |
| 3 | **Do it:** a bar chart with `print()` and asterisks, scaled by hand. It works, and it cannot go in a report | 22 |
| 4 | **Teach:** `import matplotlib.pyplot as plt`, `plt.bar()`, labels, `plt.savefig()` | 9 |
| 5 | **Do the same again:** the same chart, drawn. Then save it as a PNG and open the file | 27 |
| 6 | Retrospective | 5 |

## Day 15 — The four charts a school asks for

*Standard shape.* Bar for subject averages, line for a term's progress, histogram for the
spread of one class, and a grouped bar comparing three classes. Titles and axis labels in
Armenian — **the only place in the course where Armenian text appears inside a code
cell's output**, and the `encoding` reason it needs care.

## Day 16 — The school's own file  ⟵ *discovery*

| # | Block | Min |
|---|---|---|
| 1 | Recap: charts, saved to disk | 5 |
| 2 | **Teach:** the school's real file has 180 rows, a header, blank lines and two commas inside a name field. *After the break, a tool that reads it in one line* | 7 |
| 3 | **Do it:** parse it with `split(",")`. Handle the header, the blanks, then the quoted name — and find the row that is still wrong | 22 |
| 4 | **Teach:** `import pandas as pd`, `pd.read_csv()`, `.head()`, `.shape`, `.columns` | 9 |
| 5 | **Do the same again:** one line, and the same five checks. Compare | 27 |
| 6 | Retrospective | 5 |

## Day 17 — Filter, group, describe

*Standard shape.* Selecting a column, filtering rows by a condition, `.groupby()` for
per-class and per-subject figures, and `.describe()`. The dataframe is not taught as a
data structure — it is taught as **the register, which you already understand**.

## Day 18 — The term report

*Standard shape.* No new library. pandas and Matplotlib together: read the file, group it,
chart the result, save both the table and the picture. The session that proves the two
tools are one workflow.

## Day 19 — How deep does it go?  ⟵ *discovery*

| # | Block | Min |
|---|---|---|
| 1 | Recap: the term report, from file to chart | 5 |
| 2 | **Teach:** the ministry's file nests — school, then streams, then classes, then groups, and not every branch goes the same depth. We need every student in it. *After the break, a way to write that once* | 7 |
| 3 | **Do it:** a loop inside a loop inside a loop. It works — until the file arrives with one level more | 22 |
| 4 | **Teach:** a function that calls itself. The base case first, always. Why the depth no longer appears in the code | 9 |
| 5 | **Do the same again:** one recursive function, any depth. Then add a level to the file and change nothing | 27 |
| 6 | Retrospective. **Factorial and Fibonacci are not mentioned. They are Part 2** | 5 |

## Day 20 — Where code comes from

*Standard shape.* `import` properly: our own modules, the standard library, and the three
installed ones. Then `pip`, `requirements.txt` and what a virtual environment is for —
against one small package, installed live. **The only session that needs internet.**
Google Colab is shown at the end, because the pupils' curriculum names it sixteen times.

## Day 21 — Wrong, with no error

*Standard shape.* Debugging as its own topic — state topic 22. Reading a traceback from
the bottom up, VS Code's debugger, a breakpoint, stepping, and inspecting a variable
mid-run. The worked example is a function that returns a wrong average, silently.

## Day 22 — Five files that each do one thing  ⟵ *transition*

| # | Block | Min |
|---|---|---|
| 1 | Recap: everything the notebook can now do, on screen | 5 |
| 2 | **Teach:** five files, one job each, drawn on screen with the arrows between them | 12 |
| 3 | **Hands-on:** `settings.py` and `people.py` — the classes, moved out of the notebook | 18 |
| 4 | **Hands-on:** `loading.py` (pandas) and `charts.py` (Matplotlib) | 18 |
| 5 | **Hands-on:** `main.py`. **Run `python main.py` for the first time** | 16 |
| 6 | Retrospective. **The instructor confirms `python main.py` individually for every participant, on a shared screen, before they leave** | 6 |

## Day 23 — Make it yours

| # | Block | Min |
|---|---|---|
| 1 | Recap: everyone's `python main.py` runs on the sample school | 5 |
| 2 | **Teach:** four features you could add, and the one question that decides which file the code goes in | 12 |
| 3 | **Hands-on:** your own school's data in, and build the feature you chose. The instructor moves between shared screens; nobody is given code | 50 |
| 4 | Retrospective: what you chose and why | 8 |

## Day 24 — Finish and show

| # | Block | Min |
|---|---|---|
| 1 | Recap | 3 |
| 2 | **Hands-on:** write your `README.md` and your `requirements.txt` | 15 |
| 3 | **Hands-on:** send your folder to a colleague, who runs it **from your README alone** and reports back on the call | 18 |
| 4 | **Showcase:** 90 seconds each — your chart, one thing that broke, one thing you would add | 20 |
| 5 | The libraries we only name: `sklearn`, `pytorch`, `tensorflow`. What they are, why they are in the pupils' topic 21, and why you do not need them to teach it | 12 |
| 6 | Close, and what Part 2 would be | 7 |

---

## Time check

```
Days  1- 6   450      Days 13-18   450
Days  7-12   450      Days 19-24   450
                    ---------------------
                      1,800 minutes  =  30 hours  ✓
```

Notebook phase: Days 1–21 (1,575 min / 26 h 15).
Transition: Day 22 (75 min).
Project: Days 23–24 (150 min / 2 h 30).

## Assessment

**Three sittings**, mirroring the grade-10 course. They are **separate sittings, not
session time** — the 24 teaching sessions remain 30 hours exactly.

| | Test | When | Length | Covers |
|---|---|---|---|---|
| 1 | Initial diagnostic | **Before day 1** | 45–60 min | What the grade-10 course left them with. Nothing from this course |
| 2 | Midpoint | **After day 14** | 60–75 min | Days 2–14: functions, comprehensions, classes, inheritance |
| 3 | Final practical | **Day 24** | 90–120 min | Days 15–24: libraries, charts, data, the project |

- **Each question has variants A, B and C**, equivalent in difficulty.
- **Two versions of every test are generated** — `tests/<name>.ipynb` for the grader, with
  the rubric, and `tests/participant/<name>.ipynb` with questions only.
- **Record a help level with every score** — `3` independent, `2` after one hint, `1` with
  step-by-step help, `0` did not finish.
- **Scores diagnose the programme, not the teachers**, and participants are told so.

**The diagnostic matters more here than it did in grade 10.** It is the only measurement
of what the first course actually produced, taken before this one can affect it.

## Week map

| Week | Days | Arc | Assessment |
|---|---|---|---|
| 1 | 1–3 | My functions bend to what is asked of them | *(diagnostic sat before day 1)* |
| 2 | 4–6 | One line instead of six, and a student is a thing | |
| 3 | 7–9 | The school is objects, and they share what they have in common | |
| 4 | 10–12 | One loop for every kind of person, and figures in four lines | |
| 5 | 13–15 | I can measure a term and draw it | **Midpoint**, sat after day 14 |
| 6 | 16–18 | The school's own file goes in, a report comes out | |
| 7 | 19–21 | Any depth, and I can find out why it is wrong | |
| 8 | 22–24 | It is a program now, it runs on my school, and I showed it | **Final practical**, sat on day 24 |
