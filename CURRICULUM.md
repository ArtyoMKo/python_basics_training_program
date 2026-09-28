# Curriculum — Python from Zero, for School Teachers

**24 days × 50 minutes = 1,200 minutes = 20 hours exactly.**

Every agenda below sums to 50. The grand total is checked by `tools/check_times.py`.

| # | Day | Phase | What the participant opens | Min |
|---|---|---|---|---|
| 1 | Install everything and run your first line | Notebook | `notebooks/day01_first_program.ipynb` | 50 |
| 2 | Printing properly | Notebook | `notebooks/day02_printing.ipynb` | 50 |
| 3 | Four kinds of value | Notebook | `notebooks/day03_types.ipynb` | 50 |
| 4 | Changing type, and asking a question | Notebook | `notebooks/day04_convert_input.ipynb` | 50 |
| 5 | Giving a value a name | Notebook | `notebooks/day05_variables.ipynb` | 50 |
| 6 | **One hundred variables** | Notebook | `notebooks/day06_hundred_variables.ipynb` | 50 |
| 7 | The first decision | Notebook | `notebooks/day07_if_else.ipynb` | 50 |
| 8 | More than two outcomes | Notebook | `notebooks/day08_elif_and_or.ipynb` | 50 |
| 9 | **One hundred ifs** | Notebook | `notebooks/day09_hundred_ifs.ipynb` | 50 |
| 10 | One name for many values | Notebook | `notebooks/day10_lists.ipynb` | 50 |
| 11 | Working with a list | Notebook | `notebooks/day11_list_methods.ipynb` | 50 |
| 12 | Doing it to everyone | Notebook | `notebooks/day12_for_loops.ipynb` | 50 |
| 13 | Counting and totalling | Notebook | `notebooks/day13_range_totals.ipynb` | 50 |
| 14 | Loops that decide | Notebook | `notebooks/day14_loops_and_ifs.ipynb` | 50 |
| 15 | Repeating until you say stop | Notebook | `notebooks/day15_while.ipynb` | 50 |
| 16 | Which grade belongs to whom | Notebook | `notebooks/day16_dictionaries.ipynb` | 50 |
| 17 | Reports from a dictionary | Notebook | `notebooks/day17_dict_reports.ipynb` | 50 |
| 18 | Writing it once | Notebook | `notebooks/day18_functions.ipynb` | 50 |
| 19 | Sending an answer back | Notebook | `notebooks/day19_return.ipynb` | 50 |
| 20 | Leaving the notebook | **Transition** | `guides/day20_leaving_the_notebook.md` | 50 |
| 21 | Four files that each do one thing | **Transition** | `guides/day21_four_files.md` | 50 |
| 22 | Your own class, saved | Project | `guides/day22_your_own_class.md` | 50 |
| 23 | Make it yours | Project | `guides/day23_make_it_yours.md` | 50 |
| 24 | Finish and show | Project | `guides/day24_finish_and_show.md` | 50 |
| | | | **Total** | **1,200 min = 20 h** |

> **Nineteen notebooks, then five markdown guides.** Days 1–19 are exploration and a
> notebook is the right tool. Day 20 *is* leaving the notebook — handing out a notebook to
> do that in would contradict the lesson — and from Day 20 on participants edit `.py` files
> with the guide open in VS Code's preview pane beside their code. Every day has material
> the participant opens; only the format changes, and the change is the point.

> **The same editor all 24 days.** VS Code opens both `.ipynb` and `.py`. Day 20 therefore
> introduces two new things — a `.py` file and a terminal — not three.

> **Armenian prose, English code.** Every explanation, comment and exercise is in Armenian.
> Every keyword, variable name and function name is English. Every example string value is
> Armenian, so participants see from Day 2 that Python handles Armenian text correctly.
> The agreed terms are in `CHEATSHEET.md`'s glossary and nowhere else.

> **The grading scale is 1–10 and the pass mark is 4** in every example, written once as
> `PASS_MARK = 4` from Day 9 onward. Participants change it to their own school's value on
> Day 9, and that edit is the exercise.

---

## The standard shape

Days 2–5, 7, 8, 10–19 and 22 use this agenda exactly:

| # | Activity | Min |
|---|---|---|
| 1 | Recap, and last time's retrospective question | 5 |
| 2 | **Teach:** the new idea — ends with something running | 12 |
| 3 | **Run together:** the notebook's example cells, cell by cell | 15 |
| 4 | **Do it yourself:** the exercises | 15 |
| 5 | Retrospective: where we got to, what breaks next | 3 |
| | **Total** | **50** |

Hands-on is 30 of 50 minutes. **Activity 2 never exceeds 12 minutes.** Days 1, 6, 9, 20,
21, 23 and 24 have bespoke agendas, written out in full below; each still sums to 50.

---

## Day 1 — Install everything and run your first line

**Concepts:** what a program is · what Python is · what a notebook is

**Tools & Skills:** installing Anaconda · installing VS Code and two extensions · making a
folder · opening a folder in VS Code · creating a notebook · running a cell with Shift+Enter

The whole day is installation, and that is not a compromise — it is the highest-risk hour
of the programme. The reward at the end is small and real: a line of Armenian text printed
by a machine, which every participant has made happen themselves.

| # | Activity | Min |
|---|---|---|
| 1 | Welcome. A live demo of the finished gradebook: it loads a class, prints who failed, and saves the file back. "In eight weeks this is yours, with your class in it" | 5 |
| 2 | **Hands-on:** install Anaconda — or check the one you installed at home. Offline installers on the USB stick for anyone whose download fails | 15 |
| 3 | **Hands-on:** install VS Code, then its two extensions: Python and Jupyter | 10 |
| 4 | **Hands-on:** make `Documents/python_course`, open it in VS Code, create `day01.ipynb`, **pick the kernel** | 10 |
| 5 | **Hands-on:** `print("Բարև, աշխարհ")`, then your own name. Then run `check_setup.py` — six green lines | 8 |
| 6 | Retrospective. What to do if it broke: nothing is wrong with you, and nothing is wrong with your laptop | 2 |
| | **Total** | **50** |

**📦 By the end of today you have:** `check_setup.py` printing six green lines, and a
notebook of your own that prints your name in Armenian.

---

## Day 2 — Printing properly

**Concepts:** `print` · text in quotes · comments · what an error message is

**Tools & Skills:** several values in one `print` · quotes inside quotes · blank lines ·
`#` comments · reading a `SyntaxError`

Everything printed today is a class register header. The deliberate error is a missing
closing quote, because that is the mistake every beginner makes in their first week and
the message Python gives for it is unhelpful until someone has read one with you.

Standard shape (5 / 12 / 15 / 15 / 3).

**📦 By the end of today you have:** a four-line class register header printed by your own
notebook, and one deliberate `SyntaxError` that you caused and then fixed.

---

## Day 3 — Four kinds of value

**Concepts:** `str` · `int` · `float` · `bool` · why the type matters

**Tools & Skills:** `type()` · arithmetic on numbers · what `+` does to two pieces of text ·
reading a `TypeError`

A name is text, a grade is a whole number, an average is a decimal, and "passed" is a
yes/no. Four kinds, and the whole course uses only these four. The deliberate error is
`"2" + 2`, which is the moment the word "type" stops being abstract.

Standard shape.

**📦 By the end of today you have:** a cell showing all four types with `type()`, and a
written one-sentence answer to why `"2" + 2` fails but `"2" + "2"` does not.

---

## Day 4 — Changing type, and asking a question

**Concepts:** conversion · `input()` always gives you text

**Tools & Skills:** `int()` · `float()` · `str()` · `input()` · reading a `ValueError`

The lesson is one sentence long: whatever the teacher types, `input()` hands you text, so
a grade arrives as `"9"` and not `9`. Everything else today is practice on that. The
deliberate error is `int("ինը")`.

Standard shape.

**📦 By the end of today you have:** a cell that asks for a grade and prints that grade
plus one — which only works because you converted it.

---

## Day 5 — Giving a value a name

**Concepts:** variables · assignment · reassignment · f-strings

**Tools & Skills:** naming rules · `=` is not "equals" · `f"{name}: {grade}"` · reading a
`NameError`

Twelve minutes on what a variable is, and then thirty-three on using them. The privacy
rule is stated **today**, before the first exercise that asks for real students: first
names or initials only, no surnames, no real grades, no ID numbers.

Standard shape.

**📦 By the end of today you have:** one student's full row — name, grade, pass or fail —
printed from named values with an f-string.

---

## Day 6 — One hundred variables  ⟵ *pain day*

**Concepts:** none. Today is practice.

**Tools & Skills:** typing · editing · noticing that something is wrong with the way you
are working

The notebook ships thirty variables already written. Participants add ten of their own,
and then the ministry adds one point to every grade in the school and they change all
forty by hand. Nobody is shown a better way today. The retrospective makes them write
down, in their own words, what was wrong with it — and names Day 10 as the day it gets
fixed.

| # | Activity | Min |
|---|---|---|
| 1 | Recap | 5 |
| 2 | **Teach:** nothing new today. Today is typing, and that is deliberate | 3 |
| 3 | **Run together:** thirty variables that are already written. Read them out loud | 7 |
| 4 | **Do it yourself:** add ten more, with your own students' first names | 12 |
| 5 | **Do it yourself:** every grade goes up by one. Change all forty | 15 |
| 6 | Retrospective: **write one sentence** saying what was wrong with that. Collect them out loud | 8 |
| | **Total** | **50** |

**📦 By the end of today you have:** forty variables written and edited by hand, and one
written sentence in your own notebook saying what was wrong with doing it that way.

---

## Day 7 — The first decision

**Concepts:** `if` / `else` · comparison · indentation is not decoration

**Tools & Skills:** `>` `<` `>=` `<=` `==` `!=` · the colon · four spaces · reading a
`SyntaxError` from a missing colon and an `IndentationError`

The first time the program does something different depending on the data. Indentation
gets its own deliberate error, because in every other program a teacher has used,
whitespace meant nothing.

Standard shape.

**📦 By the end of today you have:** a cell that prints "անցավ" or "չանցավ" for a grade,
using your own school's pass mark.

---

## Day 8 — More than two outcomes

**Concepts:** `elif` · `and` · `or` · `not`

**Tools & Skills:** ordering an `elif` chain correctly · combining two conditions

Grades band into four levels, and a real school rule needs two conditions at once — present
**and** passing. The trap worth ten minutes: an `elif` chain in the wrong order silently
gives the wrong answer and never errors.

Standard shape.

**📦 By the end of today you have:** a grade sorted into four named bands, and one rule of
your own that uses `and` or `or`.

---

## Day 9 — One hundred ifs  ⟵ *pain day, and half a fix*

**Concepts:** none new — but one idea they already have, used properly

**Tools & Skills:** finding every copy of a number · replacing it with one variable

Twenty-five `if` blocks, already written, each with `4` typed into it. The pass mark
changes to 5 and they edit twenty-five numbers by hand. Then the fix, which they can do
themselves because they learned it on Day 5: one `PASS_MARK` variable at the top. **The
residue is named out loud** — twenty-five nearly identical blocks are still twenty-five
blocks — and left standing until Day 14.

| # | Activity | Min |
|---|---|---|
| 1 | Recap | 5 |
| 2 | **Teach:** nothing new today either. Today is typing again | 3 |
| 3 | **Run together:** twenty-five `if` blocks that are already written. Find every `4` | 7 |
| 4 | **Do it yourself:** the pass mark is now 5. Change all twenty-five | 12 |
| 5 | **Teach:** one name instead of twenty-five numbers — and you have known how since Day 5 | 8 |
| 6 | **Do it yourself:** rewrite it so that changing the pass mark is **one** edit. Prove it: change it to 6 | 12 |
| 7 | Retrospective: what is *still* wrong. Write it down; Day 14 fixes it | 3 |
| | **Total** | **50** |

**📦 By the end of today you have:** the same file rewritten so that one edit changes the
pass mark everywhere, proved by changing it twice — and a written sentence about what is
still wrong with twenty-five near-identical blocks.

---

## Day 10 — One name for many values

**Concepts:** lists · position starts at zero · `len()`

**Tools & Skills:** `[ ]` · `class_grades[0]` · `len()` · reading an `IndexError`

The answer to Day 6, delivered as an answer. The notebook opens with Day 6's forty
variables on the screen and replaces them with one line. Counting from zero is the only
genuinely confusing thing today, so it gets the deliberate error: `class_grades[12]` on a
list of twelve.

Standard shape.

**📦 By the end of today you have:** Day 6's forty variables as one list, and the answer to
"how many students are in it?" computed rather than counted.

---

## Day 11 — Working with a list

**Concepts:** a list can change · slices

**Tools & Skills:** `.append()` · `.remove()` · `in` · `.sort()` · `[0:3]`

A class list is a thing that changes: a student arrives, a student leaves, you want the
names in order, you want the first three. The day ends by planting the next pain —
printing forty names still means writing forty `print` lines.

Standard shape.

**📦 By the end of today you have:** your own class as a list, sorted, with one student
added and one removed — and forty `print` lines you are not happy about.

---

## Day 12 — Doing it to everyone

**Concepts:** the `for` loop · the loop variable

**Tools & Skills:** `for student_name in student_names:` · indentation again · what the
loop variable holds on each pass

The biggest single relief of the course. Day 11's forty `print` lines become three, on
screen, side by side. Twelve minutes of explanation, then thirty-three minutes of looping
over everything in sight.

Standard shape.

**📦 By the end of today you have:** yesterday's forty print lines as a three-line loop,
and the same loop run over your own class.

---

## Day 13 — Counting and totalling

**Concepts:** an accumulator · `range()` · integer versus decimal

**Tools & Skills:** `total = total + grade` · `range(1, 11)` · dividing to get an average ·
rounding with `round()`

The class average, computed. This is where `float` stops being abstract: twelve grades
adding to 78 gives 6.5, and 6.5 is not a whole number. The day plants the next pain — a
list of names and a list of grades, side by side, and no safe way to say which belongs to
whom.

Standard shape.

**📦 By the end of today you have:** your own class average, computed by a loop, rounded
to one decimal place.

---

## Day 14 — Loops that decide

**Concepts:** a loop with an `if` inside it · building a new list while looping

**Tools & Skills:** counting matches · collecting into a new list · finding the highest

Day 9's twenty-five blocks collapse to four lines, shown side by side with the original.
This is the promise made on Day 9, kept.

Standard shape.

**📦 By the end of today you have:** for your own class — who failed, how many passed, and
the highest grade, each computed by a loop rather than by looking.

---

## Day 15 — Repeating until you say stop

**Concepts:** `while` · a loop that does not know how many times it will run

**Tools & Skills:** `while True:` with `break` · checking what the user typed · stopping a
runaway loop with the stop button

The only day whose output is a program that *waits for you*. It is also the most cuttable
day in the course (see `INSTRUCTOR_NOTES.md`), which is why nothing later depends on it
except the project menu, which ships written.

Standard shape.

**📦 By the end of today you have:** a menu that keeps asking until you type `դուրս`, and
refuses a grade that is not a number between 1 and 10.

---

## Day 16 — Which grade belongs to whom

**Concepts:** dictionaries · key and value

**Tools & Skills:** `{ }` · `class_grades["Անի"]` · adding and updating a key · reading a
`KeyError`

The answer to Day 13's pain. A name goes in, a grade comes out, and nothing depends on
two lists staying in the same order. The deliberate error is looking up a student who left.

Standard shape.

**📦 By the end of today you have:** your own class as a dictionary of `name → grade`, with
one grade corrected after the fact.

---

## Day 17 — Reports from a dictionary

**Concepts:** looping over a dictionary · a value that is itself a list

**Tools & Skills:** `.items()` · two loop variables at once · a dictionary of lists · one
student with several grades

A report card per student, printed. The day ends by planting the last pain before
functions: the same six-line calculation now appears in four places in the notebook, and
a mistake in it has to be fixed four times.

Standard shape.

**📦 By the end of today you have:** a printed report card for every student in your class,
each with several grades and their own average.

---

## Day 18 — Writing it once

**Concepts:** functions · `def` · parameters · calling

**Tools & Skills:** `def average_of(grades):` · defining versus calling · why the same
name inside and outside is a different thing

The answer to Day 17. The six lines are written once and called four times, and then the
bug in them is fixed **once**. That demonstration is the lesson; everything else today is
practice.

Standard shape.

**📦 By the end of today you have:** yesterday's calculation as a function, called four
times, with one bug fixed in one place.

---

## Day 19 — Sending an answer back

**Concepts:** `return` · a function that gives you a value instead of printing one · a
default parameter

**Tools & Skills:** `return` · using the returned value · `def has_passed(grade,
pass_mark=PASS_MARK):`

The difference between a function that prints and a function that answers, which is the
difference that makes the project's four files possible. The day ends by naming both
remaining pains: nothing is saved, and none of this is something you can give a colleague.

Standard shape.

**📦 By the end of today you have:** four working grade functions in one notebook —
`average_of`, `has_passed`, `highest_of`, `failing_students` — each returning a value.

---

## Day 20 — Leaving the notebook  ⟵ *transition*

**Concepts:** a `.py` file · the terminal · `if __name__ == "__main__":`

**Tools & Skills:** creating a `.py` file in VS Code · `Ctrl+`` ` `` to open the terminal ·
`cd` · `python grades.py`

Nothing new is learned about Python. Four functions move out of a notebook into a file,
and that file is run from a terminal — which is the moment it becomes something you can
give to someone. **Exactly two terminal commands are taught, today and for the rest of the
course:** `cd` and `python file.py`.

| # | Activity | Min |
|---|---|---|
| 1 | Recap: your four functions from Day 19, on screen | 5 |
| 2 | **Teach:** why leave the notebook. A notebook is a workbench; you hand someone the thing, not the bench | 8 |
| 3 | **Hands-on:** create `grades.py`, paste the four functions in, save | 12 |
| 4 | **Hands-on:** open the terminal inside VS Code. `cd`, then `python grades.py`. It prints nothing — and that is correct | 12 |
| 5 | **Teach + hands-on:** `if __name__ == "__main__":` — the part that runs when you run the file. Now it prints | 10 |
| 6 | Retrospective | 3 |
| | **Total** | **50** |

**📦 By the end of today you have:** `python grades.py` running in a terminal and printing
your class average — no notebook involved.

---

## Day 21 — Four files that each do one thing  ⟵ *transition*

**Concepts:** modules · `import` · one job per file · which file is allowed to know about
which

**Tools & Skills:** `import settings` · `from grades import average_of` · running a program
made of several files

The pivot of the whole course. `settings.py` is Day 9's lesson made structural: every
number that might change, in one place.

| # | Activity | Min |
|---|---|---|
| 1 | Recap: `python grades.py` still runs for everyone. Confirm it before changing anything | 5 |
| 2 | **Teach:** four files, one job each, drawn on the board with the arrows between them | 10 |
| 3 | **Hands-on:** `settings.py` — every number in one place. Run it: it does nothing, and that is correct. Then `storage.py` | 12 |
| 4 | **Hands-on:** `grades.py` — yesterday's file, now importing `settings` | 8 |
| 5 | **Hands-on:** `main.py` — ask, calculate, print. **Run `python main.py` for the first time** | 12 |
| 6 | Retrospective. **The instructor confirms `python main.py` individually for every participant before they leave** | 3 |
| | **Total** | **50** |

**📦 By the end of today you have:** **a working `python main.py`** — a real program, made
of four files, run from a terminal. Confirmed individually for every participant.

---

## Day 22 — Your own class, saved

**Concepts:** files persist and variables do not · reading a file · writing a file

**Tools & Skills:** `open()` with `encoding="utf-8"` · reading lines · splitting on a comma ·
writing the file back · checking a file exists before opening it

The answer to "I closed it and everything was gone". Armenian text makes `encoding="utf-8"`
a thing they can see the need for rather than a magic argument.

Standard shape.

**📦 By the end of today you have:** your own class — first names or initials only, no real
grades — in `data/my_class.csv`, loaded by your program and saved back after a change.

---

## Day 23 — Make it yours

**Concepts:** choosing a feature · where a new piece of code belongs

**Tools & Skills:** editing across two files · deciding which file a change goes in

Four suggested features, each achievable in thirty minutes with only what the course has
taught. Participants pick one. Sixteen identical gradebooks would be a failed course.

| # | Activity | Min |
|---|---|---|
| 1 | Recap: everyone's `python main.py` runs | 5 |
| 2 | **Teach:** four features you could add, and the one question that decides where the code goes — does it calculate, or does it talk to the human? | 10 |
| 3 | **Hands-on:** build the one you chose. The instructor circulates; nobody is given code | 30 |
| 4 | Retrospective: what you chose and why | 5 |
| | **Total** | **50** |

**📦 By the end of today you have:** one feature of your own design, working, in the right
file.

---

## Day 24 — Finish and show

**Concepts:** what makes a program finished · explaining your own technical work

**Tools & Skills:** writing a README a colleague can follow · testing on someone else's
laptop · demoing in 90 seconds

Sixteen demos at 90 seconds is 24 minutes, which is why the group is capped at 16.

| # | Activity | Min |
|---|---|---|
| 1 | Recap | 3 |
| 2 | **Hands-on:** write your `README.md`, then swap laptops with your neighbour and run theirs from their README alone | 12 |
| 3 | **Showcase:** 90 seconds each — what your program does, one thing that broke on the way, one thing you would add next | 24 |
| 4 | Where to go next: the three things to learn after this course, and the two not to bother with yet | 8 |
| 5 | Close | 3 |
| | **Total** | **50** |

**📦 By the end of today you have:** a finished, documented program that a colleague
successfully ran from your README alone, and a 90-second demo of it given out loud.

---

## Time check

```
Days  1- 6   300      Days 13-18   300
Days  7-12   300      Days 19-24   300
                    ---------------------
                      1,200 minutes  =  20 hours  ✓
```

Notebook phase: Days 1–19 (950 min / 15 h 50).
Transition: Days 20–21 (100 min / 1 h 40).
Project: Days 22–24 (150 min / 2 h 30).

## Week map

| Week | Days | Arc |
|---|---|---|
| 1 | 1–3 | It runs on my laptop, and I know what a value is |
| 2 | 4–6 | I can name things — and naming a hundred things is awful |
| 3 | 7–9 | The computer can decide — and deciding a hundred times is awful |
| 4 | 10–12 | Lists and loops. **The two worst days of the course get fixed this week** |
| 5 | 13–15 | I can compute things about my whole class |
| 6 | 16–18 | Dictionaries, and my first function |
| 7 | 19–21 | It is a program now, not a notebook |
| 8 | 22–24 | It has my class in it, and I showed it to someone |

Week 4 is the emotional centre of the course. If the schedule slips, protect it.
