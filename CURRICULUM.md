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
| 6 | **A register for the whole class** | **Discovery** | `notebooks/day06_class_register.ipynb` | 50 |
| 7 | Working with the register | Notebook | `notebooks/day07_list_methods.ipynb` | 50 |
| 8 | The first decision | Notebook | `notebooks/day08_if_else.ipynb` | 50 |
| 9 | More than two outcomes | Notebook | `notebooks/day09_elif_and_or.ipynb` | 50 |
| 10 | **Marking the whole class** | **Discovery** | `notebooks/day10_for_loops.ipynb` | 50 |
| 11 | Counting and totalling | Notebook | `notebooks/day11_range_totals.ipynb` | 50 |
| 12 | Loops that decide | Notebook | `notebooks/day12_loops_and_ifs.ipynb` | 50 |
| 13 | Entering grades one by one | Notebook | `notebooks/day13_while.ipynb` | 50 |
| 14 | **Finding one student** | **Discovery** | `notebooks/day14_dictionaries.ipynb` | 50 |
| 15 | Reports from the register | Notebook | `notebooks/day15_dict_reports.ipynb` | 50 |
| 16 | Several grades per student | Notebook | `notebooks/day16_dict_of_lists.ipynb` | 50 |
| 17 | **An average on every card** | **Discovery** | `notebooks/day17_functions.ipynb` | 50 |
| 18 | Sending an answer back | Notebook | `notebooks/day18_return.ipynb` | 50 |
| 19 | The register, assembled | Notebook | `notebooks/day19_assembled.ipynb` | 50 |
| 20 | Leaving the notebook | **Transition** | `guides/day20_leaving_the_notebook.md` | 50 |
| 21 | Four files that each do one thing | **Transition** | `guides/day21_four_files.md` | 50 |
| 22 | **Keeping it after you close it** | **Discovery** | `guides/day22_your_own_class.md` | 50 |
| 23 | Make it yours | Project | `guides/day23_make_it_yours.md` | 50 |
| 24 | Finish and show | Project | `guides/day24_finish_and_show.md` | 50 |
| | | | **Total** | **1,200 min = 20 h** |

> **Nineteen notebooks, then five markdown guides.** Days 1–19 are exploration and a
> notebook is the right tool. Day 20 *is* leaving the notebook, so handing out a notebook
> to do that in would contradict the lesson; from Day 20 on participants edit `.py` files
> with the guide open in VS Code's preview pane. Every day has material the participant
> opens; only the format changes, and the change is the point.

> **Armenian describes; English codes.** Every markdown cell, callout and exercise
> instruction is Armenian. **Everything inside a code cell is English** — keywords,
> variable names, comments, docstrings and string values alike. Example names are
> transliterated Armenian (`Ani`, `Davit`, `Nare`) so the data stays familiar while the
> code stays copyable. See `PLAN.md` §7.7.

> **The grading scale is 1–10 and the pass mark is 4**, written once as `PASS_MARK = 4`
> from Day 8. Participants change it to their own school's value, and that edit is an
> exercise.

---

## The two agenda shapes

**Standard day** — Days 2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16, 18, 19:

| # | Activity | Min |
|---|---|---|
| 1 | Recap, and last time's retrospective question | 5 |
| 2 | **Teach:** the new idea — ends with something running | 12 |
| 3 | **Run together:** the notebook's example cells, cell by cell | 15 |
| 4 | **Do it yourself:** the exercises | 15 |
| 5 | Retrospective: where we got to, what comes next | 3 |
| | **Total** | **50** |

**Discovery day** — Days 6, 10, 14, 17, 22, where a tool arrives to shorten work done in
the same session:

| # | Activity | Min |
|---|---|---|
| 1 | Recap | 5 |
| 2 | **Teach:** today's task, and the only way we can do it so far | 7 |
| 3 | **Do it the long way:** the real task, with most of it shipped | 13 |
| 4 | **Teach:** the tool that shortens it | 9 |
| 5 | **Do the same task again**, with the tool. Compare the two | 13 |
| 6 | Retrospective | 3 |
| | **Total** | **50** |

Teaching never exceeds 12 minutes in one block. Hands-on is 30 of 50 on a standard day,
26 of 50 on a discovery day.

> **Never split a discovery day.** If it runs long, cut the Extra tasks — never the
> second half. Ending a session after the long way and before the short way is the worst
> outcome this design can produce.

Days 1, 20, 21, 23 and 24 have bespoke agendas, written out in full below.

---

## Day 1 — Install everything and run your first line

**Concepts:** what a program is · what a notebook is

**Tools & Skills:** installing Anaconda and VS Code · two extensions · making a folder ·
selecting a kernel · running a cell with Shift+Enter

The whole day is installation, and that is not a compromise — it is the highest-risk hour
of the programme. The reward at the end is small and real: a line printed by a machine,
which every participant made happen themselves.

| # | Activity | Min |
|---|---|---|
| 1 | Welcome. A live demo of the finished program: it opens a class, prints who failed, saves the file. "In eight weeks this is yours, with your class in it" | 5 |
| 2 | **Hands-on:** install Anaconda — or check the one installed at home. Offline installers on the USB stick for anyone whose download fails | 15 |
| 3 | **Hands-on:** install VS Code, then its two extensions: Python and Jupyter | 10 |
| 4 | **Hands-on:** make `Documents/python_course`, open it in VS Code, create a notebook, **select the kernel** | 10 |
| 5 | **Hands-on:** `print("Hello")`, then their own name. Then run `check_setup.py` — six green lines | 8 |
| 6 | Retrospective. What to do if it broke: nothing is wrong with you, and nothing is wrong with your laptop | 2 |
| | **Total** | **50** |

**📦 By the end of today you have:** `check_setup.py` printing six green lines, and a
notebook of your own that prints your name.

---

## Day 2 — Printing properly

**Concepts:** `print` · text in quotes · comments · what an error message is

**Tools & Skills:** several values in one `print` · blank lines · `#` comments · reading a
`SyntaxError`

Everything printed today is a register header. The deliberate error is a missing closing
quote, because that is the mistake every beginner makes in their first week.

Standard shape.

**📦 By the end of today you have:** a four-line class register header printed by your own
notebook, and one `SyntaxError` you caused and then fixed.

---

## Day 3 — Four kinds of value

**Concepts:** `str` · `int` · `float` · `bool` · why the type matters

**Tools & Skills:** `type()` · arithmetic · what `+` does to two pieces of text · reading a
`TypeError`

A name is text, a grade is a whole number, an average is a decimal, "passed" is a yes/no.
Four kinds, and the whole course uses only these four.

Standard shape.

**📦 By the end of today you have:** a cell showing all four types with `type()`, and a
written one-sentence answer to why `"2" + 2` fails.

---

## Day 4 — Changing type, and asking a question

**Concepts:** conversion · `input()` always gives you text

**Tools & Skills:** `int()` · `float()` · `str()` · `round()` · `input()` · reading a
`ValueError`

The lesson is one sentence: whatever the teacher types, `input()` hands you text, so a
grade arrives as `"9"` and not `9`.

Standard shape.

**📦 By the end of today you have:** a cell that asks for a grade and prints that grade
plus one — which only works because you converted it.

---

## Day 5 — Giving a value a name

**Concepts:** variables · assignment · reassignment · f-strings

**Tools & Skills:** naming rules · `=` is not "equals" · `f"{name}: {grade}"` · reading a
`NameError`

Twelve minutes on what a variable is, then thirty-three on using them. The privacy rule is
stated **today**, before the first exercise that asks for real students.

Standard shape.

**📦 By the end of today you have:** one student's full row — name, grade, result —
printed from named values with an f-string.

---

## Day 6 — A register for the whole class  ⟵ *discovery*

**Concepts:** lists · position starts at zero · `len()`

**Tools & Skills:** one variable per student, and why that stops scaling · `[ ]` ·
`class_grades[0]` · `len()` · reading an `IndexError`

**The real task:** a teacher needs somewhere to keep the whole class — every name, every
score — so the program can work with all of them.

They build it the only way they can: one variable per student. The notebook ships twenty
already written; they add a few of their own and then update the scores. It works, and it
is long. **In the same session** the list arrives and the whole thing becomes two lines.

Before the long half begins, the notebook says plainly that a shorter way is coming after
the break. Nobody is told they are doing it to suffer — they are told they are building a
register, which is true.

| # | Activity | Min |
|---|---|---|
| 1 | Recap: variables and f-strings | 5 |
| 2 | **Teach:** today we build a register for the whole class. With what we know, that means one variable per student. *And: after the break we will learn something that makes this much shorter* | 7 |
| 3 | **Do it:** twenty students are shipped; add five of your own, then apply the new scores | 13 |
| 4 | **Teach:** one name for many values — the list. `[ ]`, `len()`, counting from zero | 9 |
| 5 | **Do the same again:** the whole register as one list. Put the two versions side by side and count the lines | 13 |
| 6 | Retrospective | 3 |
| | **Total** | **50** |

**📦 By the end of today you have:** your class as a single list, the count computed
rather than counted, and the same register written both ways in one notebook.

> **Test 1 is handed out at the end of this session** (Days 1–6).

---

## Day 7 — Working with the register

**Concepts:** a list can change · slices

**Tools & Skills:** `.append()` · `.remove()` · `in` · `.sort()` · `[0:3]`

A class list is a thing that changes: a student arrives, a student leaves, you want the
names in order. Printing them one index at a time is still awkward, and the notebook says
so plainly and names Day 10.

Standard shape.

**📦 By the end of today you have:** your own class as a list, sorted, with one student
added and one removed.

---

## Day 8 — The first decision

**Concepts:** `if` / `else` · comparison · indentation is not decoration

**Tools & Skills:** `>` `<` `>=` `<=` `==` `!=` · the colon · four spaces · reading a
`SyntaxError` from a missing colon and an `IndentationError`

The first time the program does something different depending on the data. `PASS_MARK`
is introduced here as a named value, so the number that matters lives in one place from
the beginning.

Standard shape.

**📦 By the end of today you have:** a cell that prints passed or failed for a grade,
using your own school's pass mark.

---

## Day 9 — More than two outcomes

**Concepts:** `elif` · `and` · `or` · `not`

**Tools & Skills:** ordering an `elif` chain correctly · combining two conditions

Grades band into four levels, and a real school rule needs two conditions at once. The
trap worth ten minutes: an `elif` chain in the wrong order silently gives the wrong answer
and never errors.

Standard shape.

**📦 By the end of today you have:** a grade sorted into four named bands, and one rule of
your own that uses `and` or `or`.

---

## Day 10 — Marking the whole class  ⟵ *discovery*

**Concepts:** the `for` loop · the loop variable

**Tools & Skills:** one `if` block per student, and why that stops scaling ·
`for grade in class_grades:` · indentation again

**The real task:** mark the whole register — print passed or failed for every student.

With what they know, that means one `if`/`else` block per student. The notebook ships
fifteen; they extend and adjust them. **In the same session** the `for` loop arrives and
the whole thing becomes four lines that work for any class size.

| # | Activity | Min |
|---|---|---|
| 1 | Recap: `if`/`else` and the register list | 5 |
| 2 | **Teach:** today we mark the whole class. So far that means one block per student. *After the break, something that does it in four lines* | 7 |
| 3 | **Do it:** fifteen blocks are shipped; extend them, then change the pass mark everywhere | 13 |
| 4 | **Teach:** `for` — do the same thing to every item | 9 |
| 5 | **Do the same again:** the whole register marked with one loop. Add five students and change nothing | 13 |
| 6 | Retrospective | 3 |
| | **Total** | **50** |

**📦 By the end of today you have:** the whole register marked in four lines, proved by
adding students without touching the loop.

---

## Day 11 — Counting and totalling

**Concepts:** an accumulator · `range()` · integer versus decimal

**Tools & Skills:** `total = total + grade` · `range(1, 11)` · dividing to get an average ·
`round()`

The class average, computed. This is where `float` stops being abstract: twelve grades
adding to 78 gives 6.5.

Standard shape.

**📦 By the end of today you have:** your own class average, computed by a loop, rounded
to one decimal place.

> **Test 2 is handed out at the end of Day 12** (Days 7–12).

---

## Day 12 — Loops that decide

**Concepts:** a loop with an `if` inside it · building a new list while looping

**Tools & Skills:** counting matches · collecting into a new list · finding the highest

Who failed, how many passed, who scored highest — each computed rather than looked up.

Standard shape.

**📦 By the end of today you have:** for your own class — who failed, how many passed, and
the highest grade, each computed by a loop.

---

## Day 13 — Entering grades one by one

**Concepts:** `while` · a loop that does not know how many times it will run

**Tools & Skills:** `while True:` with `break` · `.isdigit()` · `continue` · stopping a
runaway loop

The only day whose output waits for you. Also the most cuttable day in the course, which
is why nothing later depends on it except the project menu, which ships written.

Standard shape.

**📦 By the end of today you have:** a loop that collects grades until you type `quit`,
and refuses anything that is not a number between 1 and 10.

---

## Day 14 — Finding one student  ⟵ *discovery*

**Concepts:** dictionaries · key and value

**Tools & Skills:** two parallel lists and their failure mode · `{ }` ·
`class_grades["Ani"]` · adding and updating · reading a `KeyError`

**The real task:** a parent asks what Aram's score is. Find one student by name.

With two lists, that means finding the position in one and reading the same position in
the other. It works — until a student leaves one list and not the other, and every answer
after that is silently wrong. **In the same session** the dictionary arrives and the
position disappears.

| # | Activity | Min |
|---|---|---|
| 1 | Recap: the register, as two lists | 5 |
| 2 | **Teach:** looking up one student means matching positions across two lists. *After the break, a way to store them so that position never matters* | 7 |
| 3 | **Do it:** look up three students by position. Then remove one student from the names list only, and watch every later answer go wrong with no error | 13 |
| 4 | **Teach:** the dictionary — `name → grade` | 9 |
| 5 | **Do the same again:** the register as one dictionary. Remove a student and confirm nothing else shifts | 13 |
| 6 | Retrospective | 3 |
| | **Total** | **50** |

**📦 By the end of today you have:** your class as a dictionary of `name → grade`, and a
written note of what went wrong with two lists.

---

## Day 15 — Reports from the register

**Concepts:** looping over a dictionary

**Tools & Skills:** `.items()` · two loop variables at once · aligning columns

Everything from Days 10–12 rewritten against the dictionary, and shorter each time.

Standard shape.

**📦 By the end of today you have:** a printed register line per student, straight from
the dictionary, with columns that line up.

---

## Day 16 — Several grades per student

**Concepts:** a value that is itself a list

**Tools & Skills:** a dictionary of lists · `class_grades["Ani"].append(8)` · two nested
loops, once

A real register holds more than one grade per student.

Standard shape.

**📦 By the end of today you have:** a report card for every student, each with several
grades.

> **Test 3 is handed out at the end of Day 18** (Days 13–18).

---

## Day 17 — An average on every card  ⟵ *discovery*

**Concepts:** functions · `def` · parameters · calling

**Tools & Skills:** the same six lines repeated, and why that stops scaling ·
`def average_of(grades):` · defining versus calling

**The real task:** put an average on every report card, in four places in the program —
the card, the summary line, the pass check and the class total.

With what they know, that means writing the same six-line calculation four times. Then the
rounding rule changes, and it has to be fixed in four places. **In the same session** the
function arrives and the fix becomes one edit.

| # | Activity | Min |
|---|---|---|
| 1 | Recap: the report card from Day 16 | 5 |
| 2 | **Teach:** the average is needed in four places on this card. So far that means writing it four times. *After the break, a way to write it once* | 7 |
| 3 | **Do it:** four copies, working. Then the head teacher asks for two decimal places — change all four | 13 |
| 4 | **Teach:** `def` — giving a piece of code a name. Defining is not calling | 9 |
| 5 | **Do the same again:** one function, four calls. Change the rounding in one place and watch all four move | 13 |
| 6 | Retrospective | 3 |
| | **Total** | **50** |

**📦 By the end of today you have:** the average calculation as a function, called four
times, with a formatting change proved in one edit.

---

## Day 18 — Sending an answer back

**Concepts:** `return` · a function that answers instead of printing · a default parameter

**Tools & Skills:** `return` · using the returned value · `def has_passed(grade,
pass_mark=PASS_MARK):`

The difference between a function that prints and one that answers — the difference that
makes the project's four files possible.

Standard shape.

**📦 By the end of today you have:** four working grade functions — `average_of`,
`has_passed`, `highest_of`, `failing_students` — each returning a value.

---

## Day 19 — The register, assembled

**Concepts:** none new. Today is consolidation.

**Tools & Skills:** combining eighteen sessions into one working notebook

No new syntax. Participants assemble the complete register program in one notebook: load a
class, mark it, count it, average it, report it. This is the last notebook, and it is the
thing that moves into files next session.

It is also the catch-up day. Anyone who fell behind gets a session where nothing new
arrives.

Standard shape.

**📦 By the end of today you have:** the complete register program working in one
notebook — the exact code that becomes `grades.py` tomorrow.

---

## Day 20 — Leaving the notebook  ⟵ *transition*

**Concepts:** a `.py` file · the terminal · `if __name__ == "__main__":`

**Tools & Skills:** creating a `.py` file · `Ctrl+`` ` `` · `cd` · `python grades.py`

Nothing new is learned about Python. Functions move out of a notebook into a file, and that
file is run from a terminal. **Exactly two terminal commands are taught, today and for the
rest of the course:** `cd` and `python file.py`.

| # | Activity | Min |
|---|---|---|
| 1 | Recap: yesterday's assembled notebook, on screen | 5 |
| 2 | **Teach:** why leave the notebook. A notebook is a workbench; you hand someone the thing, not the bench | 8 |
| 3 | **Hands-on:** create `grades.py`, move the functions in, save | 12 |
| 4 | **Hands-on:** open the terminal inside VS Code. `cd`, then `python grades.py`. It prints nothing — and that is correct | 12 |
| 5 | **Teach + hands-on:** `if __name__ == "__main__":`. Now it prints | 10 |
| 6 | Retrospective | 3 |
| | **Total** | **50** |

**📦 By the end of today you have:** `python grades.py` running in a terminal and printing
your class average — no notebook involved.

---

## Day 21 — Four files that each do one thing  ⟵ *transition*

**Concepts:** modules · `import` · one job per file

**Tools & Skills:** `import settings` · running a program made of several files

The pivot of the course. `settings.py` is Day 8's `PASS_MARK` made structural: every
number that might change, in one place.

| # | Activity | Min |
|---|---|---|
| 1 | Recap: `python grades.py` still runs for everyone. Confirm before changing anything | 5 |
| 2 | **Teach:** four files, one job each, drawn on the board with the arrows between them | 10 |
| 3 | **Hands-on:** `settings.py` — every number in one place. Run it: it does nothing, and that is correct. Then `storage.py` | 12 |
| 4 | **Hands-on:** `grades.py` — yesterday's file, now importing `settings` | 8 |
| 5 | **Hands-on:** `main.py` — ask, calculate, print. **Run `python main.py` for the first time** | 12 |
| 6 | Retrospective. **The instructor confirms `python main.py` individually for every participant before they leave** | 3 |
| | **Total** | **50** |

**📦 By the end of today you have:** **a working `python main.py`** — a real program of
four files, run from a terminal. Confirmed individually for every participant.

---

## Day 22 — Keeping it after you close it  ⟵ *discovery*

**Concepts:** files persist and variables do not · reading and writing a file

**Tools & Skills:** typing the class into the code every time, and why that stops scaling ·
`open()` with `encoding="utf-8"` · `split(",")` · writing the file back

**The real task:** the register has to survive closing the program.

They start by editing the class straight into the code — which is what they have been doing
for sixteen sessions — and add three students that way. Then they close the program and
lose the lot. **In the same session** the file arrives, and the class outlives the program.

This is where `encoding="utf-8"` earns its place: the sample data is Latin, but their own
class file will have Armenian names in it.

| # | Activity | Min |
|---|---|---|
| 1 | Recap: `python main.py` runs for everyone | 5 |
| 2 | **Teach:** the class lives inside the code, so every change means editing the program. *After the break, a way to keep it outside* | 7 |
| 3 | **Do it:** add three students by editing the code. Then close, reopen, and add them again | 13 |
| 4 | **Teach:** reading and writing a file — `read_text`, `write_text`, `split(",")`, and why `encoding="utf-8"` matters for your own class | 9 |
| 5 | **Do the same again:** `data/my_class.csv` with **your own class**. Add a student through the menu, save, reopen, confirm it is still there | 13 |
| 6 | Retrospective | 3 |
| | **Total** | **50** |

**📦 By the end of today you have:** your own class — first names or initials only — in
`data/my_class.csv`, loaded by your program and saved back after a change.

---

## Day 23 — Make it yours

**Concepts:** choosing a feature · where a new piece of code belongs

**Tools & Skills:** editing across two files · deciding which file a change goes in

Four suggested features, each achievable in thirty minutes with only what the course has
taught. Sixteen identical gradebooks would be a failed course.

| # | Activity | Min |
|---|---|---|
| 1 | Recap: everyone's `python main.py` runs on their own class | 5 |
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
| 4 | Where to go next: three things to learn after this course, and two not to bother with yet | 8 |
| 5 | Close | 3 |
| | **Total** | **50** |

**📦 By the end of today you have:** a finished, documented program that a colleague
successfully ran from your README alone, and a 90-second demo given out loud.

> **Test 4 is handed out at the end of this session** (Days 19–24), and carries the
> transfer question described in `RATIONALE.md` §5.

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

## Assessment

Four take-home tests, one per fortnight. Handed out at the end of a session, collected at
the start of the next. **They do not consume session time**, so every agenda above still
sums to 50.

| Test | After day | Covers | Notebook |
|---|---|---|---|
| 1 | 6 | `print`, types, `input`, variables, f-strings, lists | `tests/test1_first_steps.ipynb` |
| 2 | 12 | `if`/`elif`, `and`/`or`, `for`, `range`, totals, filtering | `tests/test2_decisions_and_loops.ipynb` |
| 3 | 18 | `while`, dictionaries, reports, functions | `tests/test3_data_and_functions.ipynb` |
| 4 | 24 | `return`, `.py` files, modules, files, the project | `tests/test4_the_program.ipynb` |

Each ships a marking guide at `tests/markN_guide.md` giving the expected answer **and what
a wrong answer tells the instructor**. The tests exist to show whether the method is
working, not to grade teachers.

## Week map

| Week | Days | Arc | Ends with |
|---|---|---|---|
| 1 | 1–3 | It runs on my laptop, and I know what a value is | |
| 2 | 4–6 | I can name things, and keep a whole class in one list | **Test 1** |
| 3 | 7–9 | The computer can decide | |
| 4 | 10–12 | One loop marks thirty students | **Test 2** |
| 5 | 13–15 | I can find any student by name | |
| 6 | 16–18 | I write the calculation once and use it everywhere | **Test 3** |
| 7 | 19–21 | It is a program now, not a notebook | |
| 8 | 22–24 | It has my class in it, it saves, and I showed it to someone | **Test 4** |
