# Why we are teaching it this way

**A two-month experiment in teaching Python to school teachers.**

For colleagues. Read `OUTLINE.md` for what the course *is*; this document is why we are
building it this way, what we are betting on, and what we are risking.

> **This is a raw first version.** It is written to be argued with, and we expect to
> change it. If you think the bet is wrong, the useful time to say so is now.

---

## The programme in two parts

| | | |
|---|---|---|
| **Part 1** | Coding fluency — the mechanics, with no algorithmic difficulty at all | **2 months** |
| **Part 2** | Depth, algorithms, classes and libraries — what the fluency was for | **4 months** |

**Part 2 runs only if Part 1 meets the criterion in §5a.** The split is the whole argument
of this document: §2 says why the mechanics come first, and `ROADMAP.md` says what Part 2
would contain.

## The short version

We have been trying to teach these teachers for **two years, without the results we
wanted**. This course changes the method, not the effort.

The change in one sentence:

> **Teach coding first and algorithms later — not the other way round.**

We give them almost no theory and no algorithmic problems for two months. Instead they
write a lot of very simple code, feel concrete problems, and receive each concept as the
fix for a problem they just had. At the end we look at what actually happened and decide
whether to continue this way or go back.

**This is out of the ordinary**, so it comes with a clear measurement and a decision
point (§5a), and the one risk that matters is named in §4.

---

## 1. The problem, as we see it

Two years of teaching has not produced teachers who can write a program. The question is
why, and our answer determines everything else.

**Our diagnosis: the fundamental problem is that they cannot code.**

Not "they do not understand recursion". Not "they have not practised enough algorithms".
They cannot comfortably produce working code at all — the typing, the syntax, the loop
that runs, the error that gets read and fixed.

When we then teach through **algorithmic tasks**, two things have to happen at once:

1. Work out *what* the program should do — the logic, the approach
2. Work out *how* to write it — the syntax, the structure, the mechanics

**They are overloaded, they mix the two up, and they fail at both.** A teacher stuck on
an algorithm cannot tell whether they are stuck on the idea or on the semicolon. The
theory never connects to the practice, because they have no practice for it to connect to.

Adding more theory does not help, because theory is not the bottleneck. And adding harder
problems makes it worse.

---

## 2. The bet

**Separate the two loads. Teach the mechanics to fluency first, with no algorithmic
difficulty at all. Then add the algorithms, to someone who can already code.**

Concretely, for two months:

- **Almost no theory.** ~12 minutes of explanation per session, then 30 minutes of typing.
- **No algorithmic difficulty whatsoever.** Nothing in the course requires working anything
  out. Not a single clever solution, not one problem that needs an insight.
- **A great deal of very simple code**, all of it about their own classroom — students,
  grades, attendance, averages, report lines.
- **Concepts arrive as relief, never as definitions.** This is the mechanism, and it is
  worth explaining properly (§3).

The intended sequence is:

```
write code mechanically, like a robot, with no hard thinking
              ↓
concepts (lists, loops, functions) become obvious, because each one
removes a specific pain you personally just felt
              ↓
you can now code without thinking about coding
              ↓
NOW algorithmic problems become learnable -- your whole attention is free for them
```

The last step is **not in this course**. That is the next one, if this works.

---

## 3. How concepts get taught without teaching them

This is the part that is easiest to misunderstand, so here is the actual mechanism.

**Topic 6.** Participants are told: *a teacher needs somewhere to keep the whole class —
every name, every score — so the program can work with all of them.* That is a real task
and it is given as one. With what they know on Topic 6, it means one variable per student.
The notebook ships twenty already written; they add a few of their own and update the
scores. It works, and it takes a while.

**Thirty minutes later, in the same session**, the list arrives and the whole register
becomes two lines. The notebook puts the two versions side by side and counts the lines:
40 against 2.

We do not have to explain why lists are useful. They spent twenty minutes finding out —
and then got the answer before they went home.

The same thing happens five times:

| Day | The real task | The long way | The tool, same session |
|---|---|---|---|
| 6 | A register for the whole class | one variable per student | **lists** |
| 10 | Mark the whole class pass/fail | one `if` block per student | **`for` loops** |
| 14 | Find one student's grade by name | two parallel lists and a position | **dictionaries** |
| 17 | An average on every report card | the same six lines, four times | **functions** |
| 22 | Keep the register after closing it | retyping it every time | **files** |

### Two rules that make it work, and are easy to get wrong

**The relief comes in the same session. Always.** An earlier draft of this course planted
a problem on Topic 6 and solved it on Topic 10. That is good structure on paper and bad
teaching in practice: adults who spend an evening on tedious work and go home with no
resolution do not come back. The long way and its replacement are now always in the **same session**, never four sessions apart.

**The tedium is never named.** A participant is never told they are doing something in
order to suffer, or that the long way was there to make a point. They are building a class
register because a teacher needs a class register — which is true. The materials say, before
the long half begins, that a shorter way is coming later in the same session. They never say
afterwards "now you see how bad that was".

That distinction matters more than it sounds. Work you chose to do, and were then shown a
better way to do, is a lesson. The identical work, revealed afterwards to have been a
deliberate ordeal, is a trick — and this audience has been let down enough already.

**A teacher who has written out a whole register by hand understands why a list exists
better than one who was given a good definition of it.** That is the bet, in one sentence.

## 4. What could get in the way

**One risk really matters: that after Part 1 teachers still do not feel comfortable
writing code.** That is the goal, so it is also the risk. The course is built to see it
early: the midpoint shows it a month before the end, while the method can still be
adjusted for each teacher, and the hard gate and the final assessment confirm it (§5a).

The rest are practical matters, each with a plan:

- **Problem-solving comes later.** Part 1 builds fluency; algorithmic problems are Part 2's
  work, and the Part 2 benchmark measures it (`ROADMAP.md`).
- **Some participants may expect more explanation.** The first half of a discovery
  session is deliberately hands-on. Every one resolves within the same session, and the
  shortcut is promised in writing before the long half starts.
- **The time is compact** — 22½ hours, 75 minutes at a time, for working teachers. The
  scope is deliberately focused.
- **Attendance.** Two sessions a week on top of a teaching job. Every session is
  self-contained, solutions go out afterwards, and every session starts with a recap.
- **Setup.** Laptops that cannot install software, or a large download. Handled before
  session 1 (`INSTRUCTOR_NOTES.md` §1).

### The fair comparison

The conventional approach has **two years behind it without the result we wanted**. This
approach has an argument behind it, a defined measurement and a decision point. We believe
it gives teachers a real chance to become comfortable coding, and the measurement will
show it.

---

## 5. How we will know

An experiment we cannot evaluate is just a change of plan. **These checkpoints should be
agreed before session 1**, not argued about afterwards.

The course already produces objectively checkable artefacts, so most of this needs no
extra work:

| When | The check | Why it is the right one |
|---|---|---|
| **Midpoint** (after session 10) | Do they write a loop, or still repeat themselves? | The first real evidence for or against the method |
| **Final** (session 18) | Do they return a value, or print it? | If `return` never landed, the three-file project was not reachable |
| **session 16** | **Does `python main.py` run?** Confirmed individually, per person | Binary, unarguable, and the course's hard gate |
| **Session 18** | Does a colleague run their program **from their README alone**? | Tests that the thing is real, not just that it works on one desk |
| **Session 18** | Attendance across all 18 sessions | Below a certain point, nothing else is interpretable |

**The assessments are being redesigned.** The previous diagnostic, midpoint and final
practical were removed on 16 October 2026. Their replacements — a midpoint after session 10
and a final assessment in session 18 — keep two rules: the result is the **share of tasks
done**, and **no help is given during a sitting**. The decision rule in §5a applies to them
as agreed.

**Problem-solving is measured in Part 2.** The removed final practical carried a transfer
question — an untaught problem answered first as a plan in plain words. Whether the new
final assessment keeps one is part of the redesign; the Part 2 benchmark (`ROADMAP.md`)
measures problem-solving in any case.

Set the target numbers together before session 1. A target chosen afterwards is not a target.

---

## 5a. The decision rule — agreed with colleagues

**Part 1 succeeds or fails on one question: can they code?**

### What "can code" means, operationally

"Can code" has to be measurable or the criterion is unusable. A participant **can code**
if, unaided, they can **write a working program using the constructs the course taught** —
variables, conditions, lists, loops, dictionaries and functions.

That is judged from two artefacts the course already produces, both of which are
pass/fail and neither of which requires a new instrument:

| Evidence | Where it comes from |
|---|---|
| They left **session 16** with a working `python main.py`, confirmed individually | The hard gate already built into the course |
| Their share of tasks done on the final assessment is in the **pass** band below | Its tasks require writing code unaided, from a blank cell |

### The individual result — three bands, at two exams

Agreed with partners on 15 October 2026. The percentage is the share of the exam's tasks
done.

| Tasks passed correctly | Midpoint (after session 10) | Final assessment (session 18) |
|---|---|---|
| **More than 85%** | **On track** — continues unconditionally | **Pass** — can code. Continues to Part 2 |
| **70% to 85%** | **Probation.** Continues; the teacher is told exactly where their problem is, and the method is adjusted for them in the sessions that remain | **Individual review.** The team looks at the teacher's work as a whole and decides whether they continue to Part 2 or leave |
| **Less than 70%** | **Probation**, with the highest priority | **Leaves the programme** |

**Part 1 is not
repeated**: a teacher who does not continue after the final assessment leaves the programme.

**Nobody leaves at the midpoint.** A teacher under 85% continues on probation through the
second month: they know their own problem while there is still time to fix it, and the
final assessment decides, on the same bands as everyone else. The midpoint also adjusts
the course. Its bar
is that a teacher can write code with every topic taught so far, with no algorithmic
difficulty.

A participant whose score is in the pass band **and** who left session 16 with a working
`python main.py` **can code**. Meeting one but not the other is not a pass, and goes to the
individual review — it is not rounded up.

### The thresholds — the cohort result

Agreed with partners on 15 October 2026. The percentage is of teachers who **pass**, in the
sense above:

| Result | Meaning | What happens next |
|---|---|---|
| **More than 80% pass** | **Success** | Continue to Part 2 (`ROADMAP.md`) |
| **70% to 80%** | **Inconclusive** | The method is not refuted and not proved. Adjust Part 1 and run it with a new cohort before committing to Part 2 |
| **Less than 70% pass** | **Failure** | Return to the conventional approach, informed by where it broke (§6) |

Here a teacher **passes** if they meet both halves of "can code" above — over 85% on the
final assessment and a working `python main.py` at session 16. A teacher in the
70–85% band whom the review lets continue goes on to Part 2, but is reported separately
rather than counted as a pass, so that the figure measures the method and not the review.

The middle band is not a hedge. It is the most likely outcome of a first run of anything,
and deciding in advance what we do with it prevents the result being argued into whichever
camp someone already preferred.

### The trial classes — a second criterion, measuring something else

**Each teacher teaches real pupils: one or two coding trial lessons in Part 1, the first in
the middle of the second month (around week 7), and two lessons on theoretical material
in Part 2.**

This matters more than it first appears, because **it does not measure the same thing as
§5a**. "Can they code" and "can they teach it to a child" are different abilities, and a
teacher can have either without the other:

| | Can code | Cannot code |
|---|---|---|
| **Can teach it** | The outcome the programme exists for | Not possible for this material |
| **Cannot teach it** | **The failure mode we would otherwise miss entirely** | Clear failure |

The bottom-left cell is why the trial classes are worth running. Nothing in the
assessments would detect a teacher who writes correct code and cannot explain it to a
fifteen-year-old — and that teacher cannot deliver the state curriculum, which is the
whole point of the programme.

**It does not replace the coding criterion and must not be averaged with it.** Report the
two separately:

| | What it answers |
|---|---|
| §5a, from the assessments | Can they code? |
| The trial classes | Can they teach what they can code? |

**What to record from each trial class.** Agree this before week 7, and keep it light — a
first trial lesson by a nervous adult is not a performance review:

- Did the lesson happen at all, and did it finish?
- Did the pupils end up running code themselves, or did the teacher demonstrate throughout?
- When a pupil hit an error, could the teacher read it and act on it **live**?
- One sentence from the teacher: what surprised them?

The third of these is the most diagnostic, and it is the one our own course drills from
topic 2 onward. If it holds up in front of a class, the method transferred.

### ⚠ The thresholds and the group size are in tension

Groups are **4 to 8 teachers** (`OUTLINE.md`). At that size a percentage is a very coarse
instrument:

| Group size | To reach "more than 80%" | "Less than 70%" means |
|---|---|---|
| 4 | **4 of 4** | 2 of 4 or fewer |
| 5 | **5 of 5** | 3 of 5 or fewer |
| 6 | **5 of 6** | 4 of 6 or fewer — **there is no middle band at six** |
| 8 | **7 of 8** | 5 of 8 or fewer |

**In groups of four or five, "more than 80%" still means every single participant.**
At six, one teacher short is success and two short is failure, with nothing between. One
teacher whose laptop dies in week 6, or who leaves for reasons that have nothing to do
with the course, can decide a small group's result on their own.

Two things follow, and we should agree both before the first cohort:

1. **Judge the criterion across all cohorts pooled, not per group.** Four groups of six is
   24 people, where a percentage means something. A single group of six is not a sample.
2. **Record withdrawals separately from failures.** A teacher who left in week 2 because
   their school reassigned them has not failed to learn to code, and counting them as such
   would make the criterion measure staffing rather than teaching.

Neither of these weakens the bar. They stop it from being decided by one broken laptop.

## 6. What happens after two months

**If it works** — they can code, comfortably:

- Continue with the same method into **OOP** and more advanced material
- **Go back and add the theory** we deliberately skipped, now that there is practice to
  attach it to. The theory is not cancelled; it is **postponed until it can stick**
- Begin real algorithmic work, which is where we wanted to be two years ago

**If it does not work** — we return to the conventional approach, having learned something
specific rather than having failed again in the same way. And we will know *where* it
broke: at the mechanics, at the acceptance, or at the transfer. Those are three different
lessons and they point in three different directions.

Either result is worth two months. **A third repeat of the approach that has not worked is
not.**

---

## 7. Status, and what we want from you

**This is a raw first version.** The material is complete and verified — every notebook
runs, the project works end to end, the time arithmetic is checked by script — but it has
been taught to nobody. It will need adapting, and the first cohort is going to find things
we did not.

Two items are openly unverified and named as such in the materials:

- The Armenian terminology has not been reviewed by a native speaker
- The installation instructions have not been tested on a clean school laptop

**What is most useful from you, now:**

1. **Is the diagnosis right?** Is "they cannot code" really the bottleneck, or are we
   fixing the wrong thing?
2. **Is 22 h 30 enough** to produce the fluency the bet depends on?
3. ~~**What should the success numbers be?**~~ **Agreed with partners on 15 October
   2026** (§5a): a teacher passes above 85%; the cohort succeeds above 80% passing.
4. **Will topics 6 and 8 be accepted or resented?** Anyone who knows this audience better
   than we do should say so before we run it, not after.
