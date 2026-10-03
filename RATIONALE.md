# Why we are teaching it this way

**A two-month experiment in teaching Python to school teachers.**

For colleagues. Read `OUTLINE.md` for what the course *is*; this document is why we are
building it this way, what we are betting on, and what we are risking.

> **This is a raw first version.** It is written to be argued with, and we expect to
> change it. If you think the bet is wrong, the useful time to say so is now.

---

## The short version

We have been trying to teach these teachers for **two years, without the results we
wanted**. This course changes the method, not the effort.

The change in one sentence:

> **Teach coding first and algorithms later — not the other way round.**

We give them almost no theory and no algorithmic problems for two months. Instead they
write a lot of very simple code, feel concrete problems, and receive each concept as the
fix for a problem they just had. At the end we look at what actually happened and decide
whether to continue this way or go back.

**This is out of the ordinary and it carries real risk.** That is stated plainly below,
because the point of an experiment is to be able to say it did not work.

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

**Day 6.** Participants are told: *a teacher needs somewhere to keep the whole class —
every name, every score — so the program can work with all of them.* That is a real task
and it is given as one. With what they know on Day 6, it means one variable per student.
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
a problem on Day 6 and solved it on Day 10. That is good structure on paper and bad
teaching in practice: adults who spend an evening on tedious work and go home with no
resolution do not come back. The long way and its replacement are now always fifty minutes
apart, never four sessions.

**The tedium is never named.** A participant is never told they are doing something in
order to suffer, or that the long way was there to make a point. They are building a class
register because a teacher needs a class register — which is true. The materials say, before
the long half begins, that a shorter way is coming after the break. They never say
afterwards "now you see how bad that was".

That distinction matters more than it sounds. Work you chose to do, and were then shown a
better way to do, is a lesson. The identical work, revealed afterwards to have been a
deliberate ordeal, is a trick — and this audience has been let down enough already.

**A teacher who has written out a whole register by hand understands why a list exists
better than one who was given a good definition of it.** That is the bet, in one sentence.

## 4. Why this is risky

Stated honestly, because we will have to judge it fairly in two months.

**The core assumption may simply be wrong.** We are betting that coding fluency transfers
— that someone who can code mechanically will find algorithmic problems learnable later.
That is plausible, and it is not proven. It is possible to produce teachers who can type
Python fluently and still cannot solve a problem with it. **If that happens, this failed**,
and no amount of the course being pleasant changes that.

**Participants may not accept it.** Adults often judge a course by how substantial it
feels. A course that explains little and asks them to type a lot can read as shallow, or
as not respecting their time. The discovery days are the sharpest version of this risk:
the first half of those sessions is deliberately laborious. We mitigate it by resolving
every one of them within the same fifty minutes, by promising the shortcut in writing
before the long half starts, and by never framing the work as an ordeal — but a
participant who leaves on Day 6 thinking "I typed for twenty minutes" rather than "I
learned what a list is for" is a real failure mode, and it will happen to somebody.

**Twenty hours is not much.** Eight weeks, 50 minutes at a time, for working teachers.
The scope is deliberately narrow, and narrow means things are missing.

**Attendance.** Three sessions a week for eight weeks, on top of a teaching job. Every
session is built to be self-contained and solutions go out afterwards, but people will
still drop out.

**Practical failure modes that have nothing to do with the method.** Laptops that cannot
install software; a 1 GB download on school wifi; a lost first session. These can sink the
experiment without telling us anything about whether the approach works — which is
precisely why they have to be managed hard (`INSTRUCTOR_NOTES.md` §1).

### The fair comparison

The comparison is **not** "risky new thing versus safe known thing".

The conventional approach has **two years of evidence of not producing the result we
wanted**. That is not a safe option; it is a known-unsuccessful one. This is a risky option
with an argument behind it.

**Here we have a chance to succeed.** That is the honest claim — not that it will work.

---

## 5. How we will know

An experiment we cannot evaluate is just a change of plan. **These checkpoints should be
agreed before Day 1**, not argued about afterwards.

The course already produces objectively checkable artefacts, so most of this needs no
extra work:

| When | The check | Why it is the right one |
|---|---|---|
| **Diagnostic** (before Day 1) | Q1: can they run a cell at all, and at what help level? | **The baseline.** Without it we can only report an endpoint, not change |
| **Midpoint** (after Day 12) | Q4: do they write a loop, or still index by hand? | The first real evidence for or against the method |
| **Final** (Day 24) | Q2/Q3: do they return a value, or print it? | If `return` never landed, the four-file project was not reachable |
| **Day 21** | **Does `python main.py` run?** Confirmed individually, per person | Binary, unarguable, and the course's hard gate |
| **Day 24** | Does a colleague run their program **from their README alone**? | Tests that the thing is real, not just that it works on one desk |
| **Day 24** | Attendance across all 24 sessions | Below a certain point, nothing else is interpretable |

**Three assessments**, designed with our partner colleague: a diagnostic before day 1, a
midpoint after day 12, and a final practical on day 24. They are supervised sittings
outside the 20 teaching hours, scored out of 44, 50 and 70, with a help level recorded
beside every score.

**Scoring them does not make them exams.** The scores diagnose the programme, not the
teachers, and the materials say so. What scoring buys is the thing the earlier
not-graded design could not give us: **a before-measurement**. We can now report change
rather than an endpoint, and the diagnostic's help levels tell us how much of any result
came from support rather than from the course.

**The one measurement we have to add.** None of the above tests the actual bet, because
none of them is an algorithmic problem. So:

> **Question 8 of the final practical** is that measurement, and it is already written:
> *given a class register, find the student whose grade is closest to the class average.*
> It uses no syntax the course did not teach, and the course never demonstrates it. It is
> the same for every participant — the only question with no A/B/C variants — and its 10
> points are reported separately from the other 70.
>
> The question asks them to **write their approach in plain words first**, then attempt the
> code, and to say where they stopped if they could not finish.

Four things get recorded, not one (`tests/mark3_guide.md`):

1. Did they write the plain-words plan at all?
2. Was the plan a **correct approach**, even if the code failed?
3. Did the code work?
4. **Where did they stop, in their own words?**

**A correct plan with incomplete code is a success.** It means they can now reason about a
problem and the remaining gap is practice — which is exactly what the next course would
provide. Do not report question 8 as a pass rate.

That is the experiment. Everything else measures whether the course ran well; **this
measures whether the theory was right.**

Set the target numbers together before Day 1. A target chosen afterwards is not a target.

---

## 6. What happens after two months

**If it works** — they can code, and the transfer test suggests problem-solving is now
reachable:

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
2. **Is 20 hours enough** to produce the fluency the bet depends on?
3. **What should the success numbers be?** (§5) — agreed in advance.
4. **Will Days 6 and 9 be accepted or resented?** Anyone who knows this audience better
   than we do should say so before we run it, not after.
