# Course Outline — Python from Zero, for School Teachers

**Part 1 of a six-month programme** · 24 sessions · **3 sessions a week, 8 weeks** ·
**groups of 4–8** · **delivered remotely** · public-school teachers, **any subject, no
programming background**

> Why we are teaching it this way, and what we are betting on, is in `RATIONALE.md`,
> including the decision rule this part will be judged by (§5a). The second part of the
> programme is outlined in `ROADMAP.md`. This document is only what Part 1 *is*.

> **Two things are still settling.** Sessions start at **75 minutes**; after the cohort
> has adapted we may move to two a week, or to three of 50 minutes. And the tools are
> **Anaconda, Jupyter and VS Code**, with Google Colab and Thonny under discussion as a
> lighter alternative. Both are flagged where they appear below.

---

## 1. Idea

Every participant finishes with a small program they actually use: a gradebook that opens
their own class list, shows who has passed, calculates the average, and saves changes back.
One command, their own laptop, no internet, nothing to pay for. **They write it themselves.**

They start from not having Python installed, and in most cases from never having written
a line of code.

The method is **do it the long way, then learn the short way — in the same session**:

| Day | The real task | The long way they do it first | The tool, same day |
|---|---|---|---|
| 6 | A register for the whole class | one variable per student | **lists** |
| 8 | Find one student's grade by name | two parallel lists, read by hand | **dictionaries** |
| 11 | Mark the whole class pass/fail | one `if` block per student | **`for` loops** |
| 17 | An average on every report card | the same 6 lines, 4 times | **functions** |
| 22 | Keep the register after closing it | retyping it every time | **files** |

Nothing is introduced as "good practice". Everything arrives as the thing that shortens
work just finished. A teacher who has written out a whole register by hand understands why
a list exists better than one who was given a good definition of it.

**The task is always genuine, and the course never says the long way was a lesson.** They
are building a register because a teacher needs a register. The laborious half and its
replacement are never split across two sessions.

**Every example is a classroom** — students, grades, attendance, averages, report lines.
No `foo`, no `x = 5`, no fizzbuzz.

**Armenian prose, English code.** Explanations, comments and example values are Armenian.
Keywords and variable names are English: a teacher who names a variable `անուն` writes
valid Python and can then read no other Python, search for no answer, and copy no example
ever again. The ten English words are taught instead.

## 2. Skills developed

**Programming** — `print` · four types · `input()` · variables and f-strings · lists ·
**tuples and sets** · dictionaries · `if`/`elif`/`else` · `for` and `range` · `while` ·
functions and `return` · reading and writing files · modules and running a program from a
terminal.

Part 1 covers topics 1–15 of the 24 in the state curriculum our teachers must deliver
(`docs/GOVERNMENT_ASSIGNMENT.md`); `ROADMAP.md` shows where the rest lands.

**Habits that outlast the syntax**
- If a number appears more than once, give it a name
- If code appears more than once, give it a name
- When a result is wrong, ask *which half* is wrong — the calculation or the display
- An error message is a sentence telling you what to fix, not a judgement

**Deliberately not taught:** classes, exceptions, comprehensions, `lambda`, recursion,
`pip`, virtual environments, third-party packages, regular expressions, web frameworks.
Each would cost 15 minutes and buy a teacher nothing in the program they are going to write.

## 3. What is required

**Per participant:** a Windows or macOS laptop with **~5 GB free** and permission to
install software. Anaconda + VS Code — two installs on Day 1, nothing after. No GPU, no
accounts, no API keys, **no internet after Day 1**. **Cost: zero.**

**Provided:** 19 notebooks, 5 guides, 18 solutions (handed out after each session so a
missed day is recoverable), **3 assessment sittings** — a diagnostic before day 1, a midpoint after day 13 and a
final practical on day 24 — each in a grader's and a participant version, with
instructor marking guides, `SETUP.md` for Windows and macOS, a printable cheatsheet with a bilingual
glossary, `check_setup.py`, a fictional 12-student sample class, and the finished
reference program.

Every notebook carries **three tiers of exercise** — Required, Extra and Challenge — so
that the three or four participants who finish early in every session always have
somewhere to go.

> **⚠️ One preparation item is not optional.** The Anaconda download is ~1 GB. Remotely
> each teacher downloads at home, which removes the worst version of this risk — but it
> also removes the instructor who could fix it. **`SETUP.md` goes out at least three days
> early, and a reply is required** confirming `check_setup.py` printed six green lines.
> No reply means it was not attempted.

## 4. Outcome

A runnable local program in the participant's own folder:

```
main.py        asks the teacher what they want, and prints
settings.py    every number you might want to change
storage.py     reads the class from a file, writes it back
grades.py      the calculations: average, highest, pass or fail
data/my_class.csv
```

`python main.py` opens their class, shows who passed, lists who did not, corrects a grade,
saves.

**Every participant's program is different** — their own subject, class, pass mark, and on
Day 23 one feature of their own design. Sixteen identical gradebooks would be a failed
course.

**The proof it is finished is not that it runs.** On Day 24 participants send their
folder to a colleague, who runs it **from the README alone, without asking the author
anything**.

**Part 1 is judged on one question: can they code?** The threshold, and what counts as
evidence, is in `RATIONALE.md` §5a.
