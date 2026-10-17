# Roadmap — the grade-11 course

**This course is two parts: Part 1 is 2 months, Part 2 is 4 months.**

**Part 1 is built. Part 2 is a vision, and it only runs if Part 1 succeeds.**

| | What it is | Length | Status |
|---|---|---|---|
| **Part 1** | **Coding skills** — writing working code with classes, libraries and real data, with the algorithmic difficulty deliberately removed | **9 weeks** — 18 sessions × 75 min = 22 h 30 | **Built and verified.** Not yet taught |
| **Part 2** | **Algorithmic work and the theory Part 1 postponed** | **4 months** — five stages | **Vision only.** Outlined below; not written |

The split is the same argument the grade-10 course makes, one level up. Part 1 removes
every algorithmic difficulty so attention goes to the mechanics: a class, a dataframe, a
chart, a recursive walk. Part 2 is where that investment is spent.

Building Part 2 before Part 1 reports would be assuming the answer to the question Part 1
exists to ask (`RATIONALE.md` §5).

---

## Part 1 — what it leaves a teacher able to do

Teach **grade 11** as the ministry's document specifies it, and the half of grade 10's
second semester the first course did not reach. Concretely: write and explain a class,
read a library's output, and produce a report with statistics and a chart from their own
school's data.

**What it does not leave them able to do:** solve a problem whose solution they have not
been shown. That is deliberate, and it is what Part 2 is for.

---

## Part 2 — depth and algorithms (vision)

Four months. **Runs only if Part 1 meets its success criterion.** If Part 1 lands in the
middle band, Part 2 is deferred until Part 1 is adjusted and run again with a new cohort.

### Who enters

The same gate as the grade-10 programme: `python main.py` running on their own school's
data, and more than 85% of the final assessment's tasks done (the
assessment is being redesigned; the rule is agreed). Those at 70–85% are reviewed individually, and the team decides whether
they continue. Those under 70% leave the programme: **Part 1 is not repeated**.

### How Part 2 is judged — the final milestone

Agreed with partners on 15 October 2026.

**The milestone is a real teacher's level, not a number we chose.** Teachers who completed
an earlier run of this training and now teach Python in a school are the benchmark — two
or three teachers. **Before Part 1 begins**, they sit a set of **beginner Python
problems from LeetCode** (Easy level), under the same conditions Part 2 participants will
meet at the end: the same problems, the same time limit, no internet and no AI. Their
results — problems solved correctly, and time taken — **are the milestone our teachers
should reach by the end of the school year**. It shows from the start where we are going
and how far there is to go.

**The benchmark also sets the content, depth and thresholds of Part 2's two exams**, so
it is sat before Part 1 and the results are told to teachers before they enrol (partner
email, 16 October 2026). **Part 2 has a midpoint exam and a final exam on Part 1's
principle**: at the midpoint a teacher is on track or on probation for the rest of Part 2,
and nobody leaves; at the final a teacher passes, goes to individual review, or leaves.
The percentages are set from the benchmark. At the end of the four months, Part 2 participants sit the same
problem set and are judged against those ranges.

Three things keep the benchmark honest:

- **The problem set is fixed before the benchmark sitting** and is not changed afterwards.
- **The exact problems are not taught or set as practice in Part 2.** Similar problems
  are; these ones are not, or the milestone measures memory.
- **A handful of teachers is a small baseline.** Each result is recorded separately as
  well as together, and if they differ widely we say so in the report rather than average
  it away.

### Trial lessons in Part 2

**Two, on theoretical material**, following the one or two coding lessons each teacher
taught in Part 1. Recorded the same way
(`RATIONALE.md` §5a), and reported separately from the milestone.

### Stage 1 — recursion, properly

Part 1 taught recursion as a way to walk a nested structure, and said so: factorial and
Fibonacci were named as absent and the style checker fails a build that mentions them.

This stage is where they arrive, together with the call stack, Python's depth limit, when
recursion costs more than a loop, and memoisation.

> **This is the test of the programme's central claim.** If the theory lands easily now
> that the mechanics are automatic, the method worked. If it is as hard as it would have
> been in month one, the method bought fluency and nothing else — and we should say so.

### Stage 2 — algorithmic problems

**The thing Part 1 was clearing the ground for.** Searching, sorting, counting, the
shapes that recur. Not competitive programming: problems a teacher would recognise from a
school, solved without being shown the solution first.

Whether the discovery method survives here is **unproven**. "Do it the long way, then
take the tool" works for concrete mechanics. Whether it works for problems where there is
no long way to do first is the open question, and stage 2 may need a different shape
entirely. We should expect to find that out rather than assume it.

### Stage 3 — complexity, and why it matters at school scale

Big-O as something a teacher can feel rather than recite: a loop over 36 students, then
3,000, then 300,000. Where pandas stops helping and why. Built on measurements they take
themselves, as on topic 12's timing exercises.

### Stage 4 — bigger projects

Part 1's project is five files and about 330 lines. Part 2's should be several times
that, over several weeks, with a specification that changes partway through — because
that is the part no single-session exercise can teach.

### Stage 5 — reading other people's code

Part 1 never asks for it, and the pupils' curriculum assumes it. A real repository,
opened and understood well enough to change one thing in it.

### Not scheduled — git and version control

State topic 23, six pupil-hours. **Deliberately out of scope for now**, by decision: it
is taken up once the rest of the subject is secure, not before. The natural home is
alongside stage 4, where a project large enough to need it finally exists.

---

## What has to be decided before Part 2 is written

Part 2's hours should be settled before enrolment; the rest should wait until Part 1 reports.

| Question | Why it waits |
|---|---|
| **Does Part 2 run at all?** | It depends entirely on Part 1's result |
| ~~Same cohort, or filtered?~~ | **Decided:** filtered by the final assessment ("Who enters", above) |
| **Part 2's hours** | Partners asked for them **before teachers enrol in Part 1**, so that teachers consent to the whole programme. Four months is fixed; the weekly hours are not yet |
| **Does the method carry over?** | Unproven for algorithmic work. Stage 2 is where we find out |
| Assessment | Part 1's assessments are being redesigned, and measure mechanics. **How Part 2's two exams are set is agreed** (above); their scope and percentages follow the benchmark, which is sat **before Part 1 starts** |
| Toolchain | Thonny and Colab are under discussion for both courses. Part 2's answer should follow Part 1's, not lead it |

---

## How the two courses sit together

```
Grade-10 course    Part 1  2 months   built        topics 1-14
                   Part 2  4 months   vision

Grade-11 course    Part 1  2 months   BUILT        topics 15-22, 24
                   Part 2  4 months   vision
```

A teacher who completes both Part 1s can teach the whole of the state curriculum except
topic 23 (git). The two Part 2s are where the subject stops being a syllabus and starts
being programming.
