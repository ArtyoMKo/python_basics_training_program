# Roadmap — the six-month arc

**The programme is six months, in two parts: Part 1 is 2 months, Part 2 is 4 months.**

**Part 1 is built. Part 2 is a vision, and it only runs if Part 1 succeeds.**

| | | Length | Status |
|---|---|---|---|
| **Part 1** | **Coding skills** — writing working code to automaticity, with **no algorithmic difficulty at all** | **2 months** — 16 sessions × 120 min = 32 h | **Built and verified.** Materials complete, not yet taught |
| **Trial class** | Each teacher teaches real pupils, once | **March** | Planned |
| **Part 2** | **Algorithmic tasks and the theory Part 1 postponed**, then bigger projects, classes and libraries | **4 months** — six stages | **Vision only.** Outlined below; not written |

Part 2 is also where the programme finishes covering the school curriculum our teachers
must deliver. `../shared/GOVERNMENT_ASSIGNMENT.md` maps every one of its 24 topics to the part
that covers it.

The split is the whole argument of the programme. Part 1 deliberately removes every
algorithmic difficulty so that attention goes to the mechanics. Part 2 is where that
investment is spent. Building Part 2 before Part 1 reports would be assuming the answer
to the question Part 1 exists to ask (`RATIONALE.md` §5).

---

## Between the parts — the trial class, in March

After Part 1 and before Part 2, **each teacher takes a trial class with real pupils.**

It is the only point in the programme that tests the thing the programme actually exists
for. Everything else measures whether a teacher can code; this measures whether they can
**teach what they can code** — and a teacher can have either ability without the other.
`docs/RATIONALE.md` §5a sets out what to record and why it is reported separately from
the coding criterion rather than averaged with it.

It is also the natural place for the second decision. **Part 2 entry is gated** on the
final practical (below), but the trial class is what tells us whether the *programme*
should continue in this shape at all.

---

## Part 1 — coding fluency (built)

Two months, 16 sessions. Teachers who have never programmed finish with a four-file
gradebook program running over their own class data. Full detail in `CURRICULUM.md`;
the method is in `RATIONALE.md` §3.

**What it deliberately does not cover:** algorithmic problem-solving, classes, recursion,
and the theory behind the constructs it teaches. Those are Part 2. A participant finishing
Part 1 can write simple, working, useful code and read an error message — that is the
whole claim.

**It ends with a decision, not a graduation.** See `RATIONALE.md` §5.

---

## Part 2 — depth, algorithms and design (vision)

Four months. **Runs only if Part 1 meets its success criterion.** If Part 1 lands in the
middle band, Part 2 is deferred until Part 1 is adjusted and repeated.

The ordering below is not arbitrary. Each stage depends on the one before it, and the
first stage exists because Part 1 deliberately skipped it.

### Who enters Part 2

**The third assessment filters.** Teachers meeting the "can code" bar — a working
`python main.py` at session 14, and at least half of questions 1–7 of the final practical —
continue. Those who do not are offered Part 1 again rather than carried into material
that assumes fluency they do not have.

The transfer question does not gate; it measures problem-solving, which Part 1 does not
teach. See `docs/RATIONALE.md` §5a, which also notes that this makes the final assessment
consequential for the individual, so **it must be announced before the course starts**.

### Stage 1 — the theory we postponed

The first thing Part 2 does is **go back**. Part 1 taught constructs as tools that solved
a problem the participant had just met; it did not explain how they work underneath. Now
there is practice for the theory to attach to.

This stage maps onto the school curriculum's **topic 16, Խորացված ֆունկցիաներ** (15 pupil
hours), which Part 1 deliberately skipped:

- **Functions properly** — positional, keyword and default arguments; `*args` and
  `**kwargs`; returning several values with tuple unpacking; what scope means and why a
  name inside a function is not the one outside
- **Shorter forms** — list comprehensions and one-line `if-else`; **`lambda`**
- **Loops and conditions in depth** — nesting, `break` and `continue` in combination,
  when a `while` is right and when it is a mistake
- **Data structures in depth** — lists of dictionaries, dictionaries of lists, 2-D lists,
  mutability and references; choosing deliberately rather than by habit
- **Reading other people's code**, which Part 1 never asks for

> **This stage is the test of the programme's central claim.** If the theory now lands
> easily on top of eight weeks of practice, the sequencing was right. If it is as hard as
> it was two years ago, it was not — and that is worth knowing in month three rather than
> month six.

### Stage 2 — recursion

Curriculum **topic 17** (15 pupil hours), and placed here for the same reason the school
plan places it immediately after advanced functions: it is a fact about functions before
it is a technique.

- The idea of a function calling itself; base case and recursive case
- Factorial and Fibonacci; **the call stack** and Python's recursion limit
- Recursion against loops — readability and cost, and when each is the honest choice

**Recursion comes before classes**, following the school curriculum and the decision taken
with colleagues.

### Stage 3 — algorithmic tasks and problem-solving

**The thing Part 1 was clearing the ground for.** With the mechanics automatic, the whole
of a participant's attention is available for the problem.

- Problems with no given method: searching, sorting by hand before using the built-in,
  counting and grouping, finding and comparing
- The habit of **writing the approach in words before writing code** — rehearsed once
  already, in the transfer question at the end of Part 1
- Breaking a problem into steps that each fit in a function
- More than one correct solution, and comparing them

### Stage 4 — bigger projects

Part 1's project is four files and about 150 lines. Part 2's should be several times that,
built over weeks rather than three sessions.

- A project the participant chooses, grounded in their own school work
- Working on something across sessions without losing the thread
- When a program is big enough that structure starts to matter
- Testing your own work; keeping it working while you change it

### Stage 5 — objects and classes

Curriculum **topics 18–19** (22 pupil hours), and deliberately late. Classes solve a
problem a participant only *feels* once their programs are big enough to have it — which
is why they follow stage 4, not precede it.

- Class and object, `__init__`, attributes and methods, `self`
- A `Student` object instead of parallel dictionaries
- **Inheritance**, method overriding and polymorphism
- When a class is the right answer and when a function is

### Stage 6 — libraries and environments

Curriculum **topics 15 and 21** — together the largest block in the school plan (38 pupil
hours), and the bridge into the Artificial Intelligence subject that sits alongside Python
in the «ԱԲ սերունդ» programme.

- `pip`, `requirements.txt`, and what a virtual environment is for
- **NumPy** arrays and **Matplotlib** plotting; then **pandas**
- Working in **Google Colab** and Jupyter; Kaggle and Anaconda as environments
- What `sklearn`, `pytorch` and `tensorflow` are for, without teaching them

> **This stage breaks Part 1's standard-library-only rule, and should.** That rule exists
> to protect beginners from installation problems while they are learning to code. By
> Part 2 they can code, and the rule has done its job.

### Not scheduled — git and version control

Curriculum **topic 23** (6 pupil hours). **Out of scope for now.** It is revisited after
Part 1 reports: if the cohort arrives at Part 2 comfortably, git, environments and the
remaining tooling go in; if they do not, the time is better spent elsewhere.

---

## What has to be decided before Part 2 is written

These are open, and none should be settled before Part 1 reports.

| Question | Why it waits |
|---|---|
| **Does Part 2 run at all?** | It depends entirely on Part 1's result |
| Same cohort, or a filtered one? | If Part 1 produces a wide spread, Part 2 may need a floor to enter |
| Session length and frequency | Part 1 is still settling this for itself (see `OUTLINE.md`) |
| Does the method carry over? | "Do it the long way, then get the tool" works for concrete mechanics. **Whether it works for algorithmic thinking is unproven** — stage 2 may need a different shape entirely, and we should expect to find that out rather than assume it |
| Assessment | Part 1's three sittings are built for mechanics. Measuring problem-solving needs a different instrument |

**The last two are the real risks in Part 2**, and they are listed here rather than
discovered later.
