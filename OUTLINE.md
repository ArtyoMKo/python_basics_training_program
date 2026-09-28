# Course Outline — Python from Zero, for School Teachers

**20 hours** (24 sessions × 50 min) · **3 sessions/week, 8 weeks** · **16 participants**
· public-school teachers, **any subject, no programming background**

> Why we are teaching it this way, and what we are betting on, is in `RATIONALE.md`.
> This document is only what the course *is*.

---

## 1. Idea

Every participant finishes with a small program they actually use: a gradebook that opens
their own class list, shows who has passed, calculates the average, and saves changes back.
One command, their own laptop, no internet, nothing to pay for. **They write it themselves.**

They start from not having Python installed, and in most cases from never having written
a line of code.

The method is **feel the problem, then get the solution**:

| Day | They do this | Day | They get this |
|---|---|---|---|
| 6 | Write 40 variables by hand, then edit all 40 because the grades changed | 10 | **Lists** — the 40 lines become 1 |
| 9 | Edit the number `4` in 25 copy-pasted `if` blocks | 14 | **Loops** — the 125 lines become 4 |
| 17 | Write the same 6-line calculation in 4 places | 18 | **Functions** — one place, one fix |

Nothing is introduced as "good practice". Everything arrives as the thing that stops a pain
they felt three minutes ago. A teacher who has typed 40 variables understands why a list
exists better than one who was given a good definition of it.

**Every example is a classroom** — students, grades, attendance, averages, report lines.
No `foo`, no `x = 5`, no fizzbuzz.

**Armenian prose, English code.** Explanations, comments and example values are Armenian.
Keywords and variable names are English: a teacher who names a variable `անուն` writes
valid Python and can then read no other Python, search for no answer, and copy no example
ever again. The ten English words are taught instead.

## 2. Skills developed

**Programming** — `print` · four types · `input()` · variables and f-strings ·
`if`/`elif`/`else` · lists · `for` and `range` · `while` · dictionaries · functions and
`return` · reading and writing files · modules and running a program from a terminal.

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
missed day is recoverable), `SETUP.md` for Windows and macOS, a printable cheatsheet with
a bilingual glossary, `check_setup.py`, a fictional 12-student sample class, and the
finished reference program.

> **⚠️ One preparation item is not optional.** The Anaconda download is ~1 GB. Sixteen
> people downloading it at once on school wifi will cost a session. **A USB stick with
> offline installers for both platforms is mandatory kit**, and `SETUP.md` goes out three
> days in advance.

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

**The proof it is finished is not that it runs.** On Day 24 participants swap laptops and
run each other's programs **from the README alone, without asking the author anything**.
