# Curriculum — the grade-10 course

**16 sessions × 120 minutes = 32 hours.** Two a week over eight weeks. Remote, in groups
of 4–8. Arithmetic verified by `tools/check_times.py`.

> **The course teaches 24 topics across 16 sessions.** A topic is one notebook and one
> idea. A session is two hours in a room. Most sessions hold two topics; the discovery
> sessions hold one, because their arc may never be split.

## The session map

| # | Session | Topics | Shape | Min |
|---|---|---|---|---|
| 1 | It runs on my laptop, and it prints | 1–2 | Setup | 120 |
| 2 | Four kinds of value, and asking a question | 3–4 | Paired | 120 |
| 3 | Giving a value a name | 5 | Single | 120 |
| 4 | **A register for the whole class** | 6 | **Discovery** | 120 |
| 5 | Working with the register, and two near-relatives | 7 | Single | 120 |
| 6 | **Finding one student** | 8 | **Discovery** | 120 |
| 7 | The computer decides | 9–10 | Paired | 120 |
| 8 | **Marking the whole class** | 11 | **Discovery** | 120 |
| 9 | Counting, totalling, and loops that decide | 12–13 | Paired | 120 |
| 10 | Reports from the register | 14–15 | Paired | 120 |
| 11 | Entering grades one by one | 16 | Single | 120 |
| 12 | **An average on every card** | 17 | **Discovery** | 120 |
| 13 | Sending an answer back, and the register assembled | 18–19 | Paired | 120 |
| 14 | Leaving the notebook, and four files | 20–21 | Transition | 120 |
| 15 | **Keeping it after you close it** | 22 | **Discovery** | 120 |
| 16 | Make it yours, and show it | 23–24 | Project | 120 |

Five discovery sessions — **4, 6, 8, 12, 15**. Each resolves its own difficulty inside its
own session. **Never split one.**

## The four agenda shapes

Every session is one of these. All four sum to 120.

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
| 1 | Recap | 6 |
| 2 | **Teach:** today's task, and the only way we can do it so far | 10 |
| 3 | **Do it the long way:** the real task, with most of it shipped | 32 |
| 4 | **Teach:** the tool that shortens it | 12 |
| 5 | **Do the same task again**, with the tool. Compare the two | 50 |
| 6 | Retrospective | 10 |
| | **Total** | **120** |

### Project session — sessions 14 and 16

Their agendas are given in full below; they do not follow a shape.

Teaching never exceeds **12 minutes** in one block. Hands-on is **83 of 120** on a paired
session, **92** on a single, **82** on a discovery session — never below 68%.

> **Never split a discovery session.** If it runs long, cut the Extra tasks — never the
> second half. Ending a session after the long way and before the short way is the worst
> outcome this design can produce.

---

## Session agendas that differ from the shapes

### Session 1 — It runs on my laptop, and it prints · *topics 1–2*

The highest-risk two hours of the programme. The reward at the end is small and real.

| # | Activity | Min |
|---|---|---|
| 1 | Welcome. A live demo of the finished program: it opens a class, prints who failed, saves the file. "In eight weeks this is yours, with your class in it" | 8 |
| 2 | **Hands-on:** confirm the install done at home. Screen-share with anyone whose `check_setup.py` is not green | 22 |
| 3 | **Hands-on:** install VS Code, then its two extensions: Python and Jupyter | 14 |
| 4 | **Hands-on:** make `Documents/python_course`, open it, create a notebook, **select the kernel**, then `print("Hello")` and your own name | 16 |
| 5 | **Teach:** printing properly — several values, quotes inside quotes, comments | 12 |
| 6 | **Run together:** topic 2's cells, including the deliberate `SyntaxError` | 20 |
| 7 | **Do it yourself:** topic 2's Required tasks | 23 |
| 8 | Retrospective. What to do if it broke: nothing is wrong with you, and nothing is wrong with your laptop | 5 |
| | **Total** | **120** |

### Session 4 — A register for the whole class · *topic 6 · discovery*

| # | Activity | Min |
|---|---|---|
| 1 | Recap: variables and f-strings | 6 |
| 2 | **Teach:** today we build a register for the whole class. With what we know, that means one variable per student. *And: after the break we will learn something that makes this much shorter* | 10 |
| 3 | **Do it:** twenty students are shipped; add five of your own, then apply the new scores | 32 |
| 4 | **Teach:** one name for many values — the list. `[ ]`, `len()`, counting from zero | 12 |
| 5 | **Do the same again:** the whole register as one list. Put the two versions side by side and count the lines | 50 |
| 6 | Retrospective | 10 |
| | **Total** | **120** |

### Session 6 — Finding one student · *topic 8 · discovery*

| # | Activity | Min |
|---|---|---|
| 1 | Recap: the register, as two lists | 6 |
| 2 | **Teach:** looking up one student means matching positions across two lists. *After the break, a way to store them so that position never matters* | 10 |
| 3 | **Do it:** look up three students by position, by hand. Then remove one student from the names list only, and watch every later answer go wrong with no error | 32 |
| 4 | **Teach:** the dictionary — `name → grade` | 12 |
| 5 | **Do the same again:** the register as one dictionary. Remove a student and confirm nothing else shifts | 50 |
| 6 | Retrospective | 10 |
| | **Total** | **120** |

### Session 8 — Marking the whole class · *topic 11 · discovery*

| # | Activity | Min |
|---|---|---|
| 1 | Recap: `if`/`else` and the register list | 6 |
| 2 | **Teach:** today we mark the whole class. So far that means one block per student. *After the break, something that does it in four lines* | 10 |
| 3 | **Do it:** fifteen blocks are shipped; extend them, then change the pass mark everywhere | 32 |
| 4 | **Teach:** `for` — do the same thing to every item | 12 |
| 5 | **Do the same again:** the whole register marked with one loop. Add five students and change nothing | 50 |
| 6 | Retrospective | 10 |
| | **Total** | **120** |

### Session 12 — An average on every card · *topic 17 · discovery*

| # | Activity | Min |
|---|---|---|
| 1 | Recap: the report card from topic 16 | 6 |
| 2 | **Teach:** the average is needed in four places on this card. So far that means writing it four times. *After the break, a way to write it once* | 10 |
| 3 | **Do it:** four copies, working. Then the head teacher asks for two decimal places — change all four | 32 |
| 4 | **Teach:** `def` — giving a piece of code a name. Defining is not calling | 12 |
| 5 | **Do the same again:** one function, four calls. Change the rounding in one place and watch all four move | 50 |
| 6 | Retrospective | 10 |
| | **Total** | **120** |

### Session 14 — Leaving the notebook, and four files · *topics 20–21 · transition*

**Neither half may be cut.** This session is the split between a notebook and a program.

| # | Activity | Min |
|---|---|---|
| 1 | Recap: the assembled notebook, on screen | 5 |
| 2 | **Teach:** why leave the notebook. A notebook is a workbench; you hand someone the thing, not the bench | 12 |
| 3 | **Hands-on:** create `grades.py`, move the functions in, save | 18 |
| 4 | **Hands-on:** open the terminal inside VS Code. `cd`, then `python grades.py`. It prints nothing — and that is correct. Then `if __name__ == "__main__":` | 16 |
| 5 | **Teach:** four files, one job each, drawn on screen with the arrows between them | 12 |
| 6 | **Hands-on:** `settings.py` — every number in one place. Then `storage.py` | 18 |
| 7 | **Hands-on:** `grades.py` importing `settings`, then `main.py`. **Run `python main.py` for the first time** | 32 |
| 8 | Retrospective. **The instructor confirms `python main.py` individually for every participant, on a shared screen, before they leave** | 7 |
| | **Total** | **120** |

### Session 15 — Keeping it after you close it · *topic 22 · discovery*

| # | Activity | Min |
|---|---|---|
| 1 | Recap: `python main.py` runs for everyone | 6 |
| 2 | **Teach:** the class lives inside the code, so every change means editing the program. *After the break, a way to keep it outside* | 10 |
| 3 | **Do it:** add three students by editing the code. Then close, reopen, and add them again | 32 |
| 4 | **Teach:** reading and writing a file — `read_text`, `write_text`, `split(",")`, and why `encoding="utf-8"` matters for your own class | 12 |
| 5 | **Do the same again:** `data/my_class.csv` with **your own class**. Add a student through the menu, save, reopen, confirm it is still there | 50 |
| 6 | Retrospective | 10 |
| | **Total** | **120** |

### Session 16 — Make it yours, and show it · *topics 23–24 · project*

| # | Activity | Min |
|---|---|---|
| 1 | Recap: everyone's `python main.py` runs on their own class | 3 |
| 2 | **Teach:** four features you could add, and the one question that decides where the code goes — does it calculate, or does it talk to the human? | 12 |
| 3 | **Hands-on:** build the one you chose. The instructor moves between shared screens; nobody is given code | 40 |
| 4 | **Hands-on:** write your `README.md` | 15 |
| 5 | **Hands-on:** send your folder to a colleague, who runs it **from your README alone** and reports back on the call | 18 |
| 6 | **Showcase:** 90 seconds each — what your program does, one thing that broke on the way, one thing you would add next | 22 |
| 7 | Where to go next, close, and what happens in March | 10 |
| | **Total** | **120** |

---

# The 24 topics

## Topic 1 — Install everything and run your first line

**Concepts:** what a program is · what a notebook is

**Tools & Skills:** installing Anaconda and VS Code · two extensions · making a folder ·
selecting a kernel · running a cell with Shift+Enter

The whole day is installation, and that is not a compromise — it is the highest-risk hour
of the programme. The reward at the end is small and real: a line printed by a machine,
which every participant made happen themselves.

**📦 By the end of this topic you have:** `handouts/check_setup.py` printing six green lines, and a
notebook of your own that prints your name.

---

## Topic 2 — Printing properly

**Concepts:** `print` · text in quotes · comments · what an error message is

**Tools & Skills:** several values in one `print` · blank lines · `#` comments · reading a
`SyntaxError`

Everything printed today is a register header. The deliberate error is a missing closing
quote, because that is the mistake every beginner makes in their first week.

Standard shape.

**📦 By the end of this topic you have:** a four-line class register header printed by your own
notebook, and one `SyntaxError` you caused and then fixed.

---

## Topic 3 — Four kinds of value

**Concepts:** `str` · `int` · `float` · `bool` · why the type matters

**Tools & Skills:** `type()` · arithmetic · what `+` does to two pieces of text · reading a
`TypeError`

A name is text, a grade is a whole number, an average is a decimal, "passed" is a yes/no.
Four kinds, and the whole course uses only these four.

Standard shape.

**📦 By the end of this topic you have:** a cell showing all four types with `type()`, and a
written one-sentence answer to why `"2" + 2` fails.

---

## Topic 4 — Changing type, and asking a question

**Concepts:** conversion · `input()` always gives you text

**Tools & Skills:** `int()` · `float()` · `str()` · `round()` · `input()` · reading a
`ValueError`

The lesson is one sentence: whatever the teacher types, `input()` hands you text, so a
grade arrives as `"9"` and not `9`.

Standard shape.

**📦 By the end of this topic you have:** a cell that asks for a grade and prints that grade
plus one — which only works because you converted it.

---

## Topic 5 — Giving a value a name

**Concepts:** variables · assignment · reassignment · f-strings

**Tools & Skills:** naming rules · `=` is not "equals" · `f"{name}: {grade}"` · reading a
`NameError`

Twelve minutes on what a variable is, then thirty-three on using them. The privacy rule is
stated **today**, before the first exercise that asks for real students.

Standard shape.

**📦 By the end of this topic you have:** one student's full row — name, grade, result —
printed from named values with an f-string.

---

## Topic 6 — A register for the whole class  ⟵ *discovery*

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

**📦 By the end of this topic you have:** your class as a single list, the count computed
rather than counted, and the same register written both ways in one notebook.

---

## Topic 7 — Working with the register, and two near-relatives

**Concepts:** a list can change · slices · tuples and sets as near-relatives

**Tools & Skills:** `.append()` · `.remove()` · `in` · `.sort()` · `[0:3]` · `( )` and
`{ }` · when a thing should not be changeable

A class list is a thing that changes: a student arrives, a student leaves, you want the
names in order. The second half introduces **tuples and sets** briefly — a tuple as a list
that cannot change, a set as a list with no duplicates — because the school curriculum
teaches them and a teacher will meet them in their first semester. **They are shown and
compared, not drilled**; nothing later in the course depends on them.

Standard shape.

**📦 By the end of this topic you have:** your own class as a list, sorted, with one student
added and one removed — plus the same names as a tuple and as a set, and one sentence on
what each is for.

---

## Topic 8 — Finding one student  ⟵ *discovery*

**Concepts:** dictionaries · key and value

**Tools & Skills:** two parallel lists and their failure mode · `{ }` ·
`class_grades["Ani"]` · adding and updating · reading a `KeyError`

> **No loops are used in this session.** The long half looks students up **by position,
> by hand** — `student_names[3]` and `class_grades[3]` — which is exactly what makes the
> drift visible. Loops arrive on topic 11, and arrive more useful because there is now a
> dictionary to loop over.

**The real task:** a parent asks what Aram's score is. Find one student by name.

With two lists, that means finding the position in one and reading the same position in
the other. It works — until a student leaves one list and not the other, and every answer
after that is silently wrong. **In the same session** the dictionary arrives and the
position disappears.

**📦 By the end of this topic you have:** your class as a dictionary of `name → grade`, and a
written note of what went wrong with two lists.

---

## Topic 9 — The first decision

**Concepts:** `if` / `else` · comparison · indentation is not decoration

**Tools & Skills:** `>` `<` `>=` `<=` `==` `!=` · the colon · four spaces · reading a
`SyntaxError` from a missing colon and an `IndentationError`

The first time the program does something different depending on the data. `PASS_MARK` is introduced here as a named value, so the number that matters lives in one
place from the beginning.

Standard shape.

**📦 By the end of this topic you have:** a cell that prints passed or failed for a grade,
using your own school's pass mark.

---

## Topic 10 — More than two outcomes

**Concepts:** `elif` · `and` · `or` · `not`

**Tools & Skills:** ordering an `elif` chain correctly · combining two conditions

Grades band into four levels, and a real school rule needs two conditions at once. The
trap worth ten minutes: an `elif` chain in the wrong order silently gives the wrong answer
and never errors.

Standard shape.

**📦 By the end of this topic you have:** a grade sorted into four named bands, and one rule of
your own that uses `and` or `or`.

---

## Topic 11 — Marking the whole class  ⟵ *discovery*

**Concepts:** the `for` loop · the loop variable

**Tools & Skills:** one `if` block per student, and why that stops scaling ·
`for grade in class_grades:` · indentation again

**The real task:** mark the whole register — print passed or failed for every student.

With what they know, that means one `if`/`else` block per student. The notebook ships
fifteen; they extend and adjust them. **In the same session** the `for` loop arrives and
the whole thing becomes four lines that work for any class size.

**📦 By the end of this topic you have:** the whole register marked in four lines, proved by
adding students without touching the loop.

---

## Topic 12 — Counting and totalling

**Concepts:** an accumulator · `range()` · integer versus decimal

**Tools & Skills:** `total = total + grade` · `range(1, 11)` · dividing to get an average ·
`round()`

The class average, computed. This is where `float` stops being abstract: twelve grades
adding to 78 gives 6.5.

Standard shape.

**📦 By the end of this topic you have:** your own class average, computed by a loop, rounded
to one decimal place.

---

## Topic 13 — Loops that decide

**Concepts:** a loop with an `if` inside it · building a new list while looping

**Tools & Skills:** counting matches · collecting into a new list · finding the highest

Who failed, how many passed, who scored highest — each computed rather than looked up.

Standard shape.

**📦 By the end of this topic you have:** for your own class — who failed, how many passed, and
the highest grade, each computed by a loop.

> **The midpoint test is sat after this session**, as a separate 60–75 minute sitting
> covering topics 6–13.

---

## Topic 14 — Reports from the register

**Concepts:** looping over a dictionary

**Tools & Skills:** `.items()` · two loop variables at once · aligning columns

Everything from topics 11–13 rewritten against the dictionary, and shorter each time.

Standard shape.

**📦 By the end of this topic you have:** a printed register line per student, straight from
the dictionary, with columns that line up.

---

## Topic 15 — Several grades per student

**Concepts:** a value that is itself a list

**Tools & Skills:** a dictionary of lists · `class_grades["Ani"].append(8)` · two nested
loops, once

A real register holds more than one grade per student.

Standard shape.

**📦 By the end of this topic you have:** a report card for every student, each with several
grades.

---

## Topic 16 — Entering grades one by one

**Concepts:** `while` · a loop that does not know how many times it will run

**Tools & Skills:** `while True:` with `break` · `.isdigit()` · `continue` · stopping a
runaway loop

The only day whose output waits for you. Also the most cuttable day in the course, which
is why nothing later depends on it except the project menu, which ships written.

Standard shape.

**📦 By the end of this topic you have:** a loop that collects grades until you type `quit`,
and refuses anything that is not a number between 1 and 10.

---

## Topic 17 — An average on every card  ⟵ *discovery*

**Concepts:** functions · `def` · parameters · calling

**Tools & Skills:** the same six lines repeated, and why that stops scaling ·
`def average_of(grades):` · defining versus calling

**The real task:** put an average on every report card, in four places in the program —
the card, the summary line, the pass check and the class total.

With what they know, that means writing the same six-line calculation four times. Then the
rounding rule changes, and it has to be fixed in four places. **In the same session** the
function arrives and the fix becomes one edit.

**📦 By the end of this topic you have:** the average calculation as a function, called four
times, with a formatting change proved in one edit.

---

## Topic 18 — Sending an answer back

**Concepts:** `return` · a function that answers instead of printing · a default parameter

**Tools & Skills:** `return` · using the returned value · `def has_passed(grade,
pass_mark=PASS_MARK):`

The difference between a function that prints and one that answers — the difference that
makes the project's four files possible.

Standard shape.

**📦 By the end of this topic you have:** four working grade functions — `average_of`,
`has_passed`, `highest_of`, `failing_students` — each returning a value.

---

## Topic 19 — The register, assembled

**Concepts:** none new. Today is consolidation.

**Tools & Skills:** combining eighteen sessions into one working notebook

No new syntax. Participants assemble the complete register program in one notebook: load a
class, mark it, count it, average it, report it. This is the last notebook, and it is the
thing that moves into files next session.

It is also the catch-up day. Anyone who fell behind gets a session where nothing new
arrives.

Standard shape.

**📦 By the end of this topic you have:** the complete register program working in one
notebook — the exact code that becomes `grades.py` tomorrow.

---

## Topic 20 — Leaving the notebook  ⟵ *transition*

**Concepts:** a `.py` file · the terminal · `if __name__ == "__main__":`

**Tools & Skills:** creating a `.py` file · `Ctrl+`` ` `` · `cd` · `python grades.py`

Nothing new is learned about Python. Functions move out of a notebook into a file, and that
file is run from a terminal. **Exactly two terminal commands are taught, today and for the
rest of the course:** `cd` and `python file.py`.

**📦 By the end of this topic you have:** `python grades.py` running in a terminal and printing
your class average — no notebook involved.

---

## Topic 21 — Four files that each do one thing  ⟵ *transition*

**Concepts:** modules · `import` · one job per file

**Tools & Skills:** `import settings` · running a program made of several files

The pivot of the course. `settings.py` is topic 9's `PASS_MARK` made structural: every
number that might change, in one place.

**📦 By the end of this topic you have:** **a working `python main.py`** — a real program of
four files, run from a terminal. Confirmed individually for every participant.

---

## Topic 22 — Keeping it after you close it  ⟵ *discovery*

**Concepts:** files persist and variables do not · reading and writing a file

**Tools & Skills:** typing the class into the code every time, and why that stops scaling ·
`open()` with `encoding="utf-8"` · `split(",")` · writing the file back

**The real task:** the register has to survive closing the program.

They start by editing the class straight into the code — which is what they have been doing
for sixteen sessions — and add three students that way. Then they close the program and
lose the lot. **In the same session** the file arrives, and the class outlives the program.

This is where `encoding="utf-8"` earns its place: the sample data is Latin, but their own
class file will have Armenian names in it.

**📦 By the end of this topic you have:** your own class — first names or initials only — in
`data/my_class.csv`, loaded by your program and saved back after a change.

---

## Topic 23 — Make it yours

**Concepts:** choosing a feature · where a new piece of code belongs

**Tools & Skills:** editing across two files · deciding which file a change goes in

Four suggested features, each achievable in thirty minutes with only what the course has
taught. Sixteen identical gradebooks would be a failed course.

**📦 By the end of this topic you have:** one feature of your own design, working, in the right
file.

---

## Topic 24 — Finish and show

**Concepts:** what makes a program finished · explaining your own technical work

**Tools & Skills:** writing a README a colleague can follow · testing on someone else's
laptop · demoing in 90 seconds

Sixteen demos at 90 seconds is 24 minutes, which is why the group is capped at 16.

**📦 By the end of this topic you have:** a finished, documented program that a colleague
successfully ran from your README alone, and a 90-second demo given out loud.

> **The final practical is sat on this day**, as a separate 90–120 minute sitting. Its
> last question is the transfer question described in `RATIONALE.md` §5.

---

---

## Time check

```
Sessions  1- 4   480      Sessions  9-12   480
Sessions  5- 8   480      Sessions 13-16   480
                        ---------------------
                          1,920 minutes  =  32 hours  ✓
```

Notebook phase: sessions 1–13, topics 1–19 (1,560 min / 26 h).
Transition: session 14, topics 20–21 (120 min).
Project: sessions 15–16, topics 22–24 (240 min / 4 h).

> **The move from three 120-minute sessions a week to two of 120 added two hours of
> contact time**, not removed any. What it removed is the third touchpoint in a week —
> and that is what homework replaces.

## Homework

**Homework is the practice that did not fit, not new work.** Every notebook already
carries 8–13 tasks in three tiers; a paired session reaches the Required tier of both
notebooks and little more.

| Session shape | What is set | Roughly |
|---|---|---|
| **Paired** | finish the Required tasks you did not reach, then the Extra tier of both notebooks | 30–40 min |
| **Single** | nothing. The Extra tier is done **in the session** | — |
| **Discovery** | the Extra tier of that notebook | 20–30 min |
| **Transition, project** | nothing. Both are hands-on throughout | — |

Rules this follows:

- **No task was written for homework.** Every one is a task that already existed and that
  a three-a-week schedule had time for in the room.
- **Required tasks are never homework by design** — only by overflow, and the next
  session's first block is where they are checked.
- **Nothing new is introduced at home.** Homework uses only what the session taught.
- **A participant who does no homework still finishes the course.** They will be slower,
  and the instructor will see it in the recap block.

## Assessment

**Three sittings**, designed with our partner colleague. They are **separate sittings,
not session time** — the 16 teaching sessions remain 32 hours exactly, and the
assessments add roughly 3½ hours on top.

| | Test | When | Length | Points | Covers |
|---|---|---|---|---|---|
| 1 | Initial diagnostic | **Before session 1** | 45–60 min | 44 | Nothing — it measures the baseline |
| 2 | Midpoint | **After session 9** | 60–75 min | 50 | Topics 6–13: lists, tuples, sets, dictionaries, conditions, loops, totals, filtering |
| 3 | Final practical | **Session 16** | 90–120 min | 70 **+ 10 reported separately** | Topics 14–24: reports, functions, files, the project |

- **Each question has variants A, B and C**, equivalent in difficulty and points. The
  exam platform gives each participant **one**.
- **Two versions of every test are generated**: `tests/<name>.ipynb` for the grader, with
  the rubric, and `tests/participant/<name>.ipynb` with questions only. Hand out the
  participant copy.
- **Record a help level with every score** — `3` independent, `2` after one hint, `1`
  with step-by-step help, `0` did not finish. On the diagnostic this is more informative
  than the score itself.
- **Scores diagnose the programme, not the teachers**, and participants are told so.
- Each test ships a marking guide at `tests/markN_guide.md` giving what a wrong answer
  tells the instructor, and what to change in the next session because of it.

**Question 8 of the final test is the transfer question** — one small task using only
taught syntax that the course never demonstrates. It is marked separately, never reported
as a pass rate, and a correct plan with incomplete code counts as a success. See
`RATIONALE.md` §5.

**The diagnostic is what makes the experiment measurable.** Without a before-measurement
the programme can only report an endpoint; with one it can report change.

## Week map

| Week | Sessions | Topics | Arc | Assessment |
|---|---|---|---|---|
| 1 | 1–2 | 1–4 | It runs on my laptop, and I know what a value is | *(diagnostic sat before session 1)* |
| 2 | 3–4 | 5–6 | I can name things, and keep a whole class in one list | |
| 3 | 5–6 | 7–8 | Every data type I need, and I can find one student | |
| 4 | 7–8 | 9–11 | Conditions, then one loop marks thirty students | |
| 5 | 9–10 | 12–15 | I can compute and report on the whole class | **Midpoint**, sat after session 9 |
| 6 | 11–12 | 16–17 | I write the calculation once and use it everywhere | |
| 7 | 13–14 | 18–21 | It is a program now, not a notebook | |
| 8 | 15–16 | 22–24 | It has my class in it, it saves, and I showed it to someone | **Final practical**, sat in session 16 |
