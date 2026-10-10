# Curriculum — the grade-10 course

**18 sessions × 75 minutes = 22 hours 30 minutes.** Two a week over nine weeks. **Fully remote** — every
session, without exception — in groups of 4–8. Arithmetic verified by `tools/check_times.py`.

> **The course teaches 24 topics across 18 sessions.** A topic is one notebook and one
> idea. A session is 75 minutes in a room. Seven sessions hold one topic with its practice
> in the room; five hold one discovery arc; six hold two topics, and those are the ones
> whose practice moves to homework.

## The session map

| # | Session | Topics | Shape | Min |
|---|---|---|---|---|
| 1 | It runs on my laptop, and it prints | 1–2 | Setup | 75 |
| 2 | Four kinds of value | 3 | Single | 75 |
| 3 | Changing type, and asking a question | 4 | Single | 75 |
| 4 | Giving a value a name | 5 | Single | 75 |
| 5 | **A register for the whole class** | 6 | **Discovery** | 75 |
| 6 | Working with the register, and two near-relatives | 7 | Single | 75 |
| 7 | **Finding one student** | 8 | **Discovery** | 75 |
| 8 | The computer decides | 9–10 | Paired | 75 |
| 9 | **Marking the whole class** | 11 | **Discovery** | 75 |
| 10 | Counting, totalling, and loops that decide | 12–13 | Paired | 75 |
| 11 | Reports from the register | 14 | Single | 75 |
| 12 | Several grades per student | 15 | Single | 75 |
| 13 | Entering grades one by one | 16 | Single | 75 |
| 14 | **An average on every card** | 17 | **Discovery** | 75 |
| 15 | Sending an answer back, and the register assembled | 18–19 | Paired | 75 |
| 16 | Leaving the notebook, and four files | 20–21 | Transition | 75 |
| 17 | **Keeping it after you close it** | 22 | **Discovery** | 75 |
| 18 | Make it yours, and show it | 23–24 | Project | 75 |

Five discovery sessions — **5, 7, 9, 14, 17**. Each holds one topic and resolves its own
difficulty inside its own session. **Never split one.**

## The three agenda shapes

All three sum to 75.

### Single session — one topic, practice in the room

| # | Block | Min |
|---|---|---|
| 1 | Recap, and last session's homework | 5 |
| 2 | **Teach:** the new idea — ends with something running | 12 |
| 3 | **Run together:** the notebook's example cells, cell by cell | 20 |
| 4 | **Do it yourself:** the exercises — Required, then Extra | 33 |
| 5 | Retrospective: where we got to, what comes next | 5 |
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
> rather than hidden.** Hands-on is **41 of 75** against 53 on a single session: the
> participant follows two notebooks in the room and does most of the typing afterwards.
> **Three** sessions use this agenda — 8, 10 and 15 — and three more hold two topics under a
> bespoke agenda that is more hands-on. None of the six is a discovery
> session — the arcs always keep their full 75 minutes.

Teaching never exceeds **12 minutes** in one block; a paired session is two blocks of 12,
not one of 24. Hands-on is **53 of 75** on a single session, **49** on a discovery
session, **41** on a paired one.

> **Never split a discovery session.** If it runs long, cut the Extra tasks — never the
> second half.

---

## Session agendas that differ from the shapes

### Session 1 — It runs on my laptop, and it prints · *topics 1–2*

The highest-risk session of the programme. The reward at the end is small and real.

| # | Activity | Min |
|---|---|---|
| 1 | Welcome. A live demo of the finished program: it opens a class, prints who failed, saves the file. "In nine weeks this is yours, with your class in it" | 6 |
| 2 | **Hands-on:** confirm the install done at home. Screen-share with anyone whose `check_setup.py` is not green | 20 |
| 3 | **Hands-on:** install VS Code, then its two extensions: Python and Jupyter | 12 |
| 4 | **Hands-on:** make `Documents/python_course`, open it, create a notebook, **select the kernel**, then `print("Hello")` and your own name | 12 |
| 5 | **Teach:** printing properly — several values, quotes inside quotes, comments | 10 |
| 6 | **Run together:** topic 2's cells, including the deliberate `SyntaxError` | 10 |
| 7 | Retrospective. What to do if it broke: nothing is wrong with you, and nothing is wrong with your laptop | 5 |
| | **Total** | **75** |

### Session 16 — Leaving the notebook, and four files · *topics 20–21 · transition*

**Neither half may be cut.** This session is the split between a notebook and a program.

| # | Activity | Min |
|---|---|---|
| 1 | Recap: the assembled notebook, on screen | 4 |
| 2 | **Teach:** why leave the notebook. A notebook is a workbench; you hand someone the thing, not the bench | 10 |
| 3 | **Hands-on:** create `grades.py`, move the functions in, save | 14 |
| 4 | **Hands-on:** the terminal inside VS Code, `python grades.py`, then `if __name__ == "__main__":` | 12 |
| 5 | **Teach:** four files, one job each, drawn on screen with the arrows between them | 10 |
| 6 | **Hands-on:** `settings.py`, `storage.py`, `grades.py` importing `settings`, then `main.py`. **Run `python main.py` for the first time** | 20 |
| 7 | Retrospective. **The instructor confirms `python main.py` individually for every participant, on a shared screen, before they leave** | 5 |
| | **Total** | **75** |

### Session 18 — Make it yours, and show it · *topics 23–24 · project*

| # | Activity | Min |
|---|---|---|
| 1 | Recap: everyone's `python main.py` runs on their own class | 3 |
| 2 | **Teach:** four features you could add, and the one question that decides where the code goes — does it calculate, or does it talk to the human? | 10 |
| 3 | **Hands-on:** build the one you chose. The instructor moves between shared screens; nobody is given code | 25 |
| 4 | **Hands-on:** write your `README.md` | 10 |
| 5 | **Hands-on:** send your folder to a colleague, who runs it **from your README alone** | 17 |
| 6 | **Showcase**, then where to go next, and what happens in March | 10 |
| | **Total** | **75** |

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
`read_text()` / `write_text()` with `encoding="utf-8"` · `split(",")` · writing the file back

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

Eight demos at 90 seconds is 12 minutes, which is why the group is capped at 8.

**📦 By the end of this topic you have:** a finished, documented program that a colleague
successfully ran from your README alone, and a 90-second demo given out loud.

> **The final practical is sat on this day**, as a separate 90–120 minute sitting. Its
> last question is the transfer question described in `RATIONALE.md` §5.

---

---

---

## Time check

```
Sessions  1- 6   450      Sessions 13-18   450
Sessions  7-12   450
                        ---------------------
                          1,350 minutes  =  22 h 30  ✓
```

Notebook phase: sessions 1–15, topics 1–19 (1,125 min / 18 h 45).
Transition: session 16, topics 20–21 (75 min).
Project: sessions 17–18, topics 22–24 (150 min / 2 h 30).

> **This schedule has the least contact time of any the programme has used** — 22½ hours
> against 30 for three sessions a week and 32 for two of two hours. Nothing was cut from <!--history-->
> the course: all 24 topics survive, and the practice that no longer fits in the room is
> set as homework. **That makes homework load-bearing here in a way it was not before**,
> and the risk is stated plainly in `RATIONALE.md`.

## Homework

**Homework is the practice that no longer fits, not new work.** Every notebook carries
8–13 tasks in three tiers. What changes with this schedule is how much of that tier a
participant reaches in the room.

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
- **No Challenge task is ever homework.** Those are for the fastest one or two in the
  room, and only in the room.
- **Nothing new is introduced at home.** Homework uses only what that session taught.
- **The next session opens by checking it**, and every agenda has that block.

> **A participant who does no homework will not finish this version of the course.** On
> the three-a-week schedule that was true only of the Extra tier; here the Required tier
> of six sessions is set at home. **Say so at enrolment**, not in week three.

## Assessment

**Three sittings**, designed with our partner colleague. They are **separate sittings,
not session time** — the 18 teaching sessions remain 22½ hours exactly, and the
assessments add roughly 3½ hours on top.

| | Test | When | Length | Points | Covers |
|---|---|---|---|---|---|
| 1 | Initial diagnostic | **Before session 1** | 45–60 min | 44 | Nothing — it measures the baseline |
| 2 | Midpoint | **After session 10** | 60–75 min | 50 | Topics 6–13: lists, tuples, sets, dictionaries, conditions, loops, totals, filtering |
| 3 | Final practical | **Session 18** | 90–120 min | 70 **+ 10 reported separately** | Topics 14–24: reports, functions, files, the project |

- **Each question has variants A, B and C**, equivalent in difficulty and points.
- **Two versions of every test are generated**: `tests/<name>.ipynb` for the grader, with
  the rubric, and `tests/participant/<name>.ipynb` with questions only. Hand out the
  participant copy.
- **Record a help level with every score** — `3` independent, `2` after one hint, `1`
  with step-by-step help, `0` did not finish.
- **Scores diagnose the programme, not the teachers**, and participants are told so.
- Each test ships a marking guide at `tests/markN_guide.md`.

**Question 8 of the final test is the transfer question** — one small task using only
taught syntax that the course never demonstrates. It is marked separately, never reported
as a pass rate, and a correct plan with incomplete code counts as a success.

## Week map

| Week | Sessions | Topics | Arc | Assessment |
|---|---|---|---|---|
| 1 | 1–2 | 1–3 | It runs on my laptop, and I know what a value is | *(diagnostic sat before session 1)* |
| 2 | 3–4 | 4–5 | I can name things | |
| 3 | 5–6 | 6–7 | A whole class in one list | |
| 4 | 7–8 | 8–10 | I can find one student, and the computer decides | |
| 5 | 9–10 | 11–13 | One loop marks thirty students | **Midpoint**, sat after session 10 |
| 6 | 11–12 | 14–15 | I can report on the whole class | |
| 7 | 13–14 | 16–17 | I write the calculation once and use it everywhere | |
| 8 | 15–16 | 18–21 | It is a program now, not a notebook | |
| 9 | 17–18 | 22–24 | It has my class in it, it saves, and I showed it to someone | **Final practical**, sat in session 18 |
