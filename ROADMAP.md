# Roadmap — the six-month arc

**Part 1 is built. Part 2 is a vision, and it only runs if Part 1 succeeds.**

| | | Length | Status |
|---|---|---|---|
| **Part 1** | Coding fluency — the mechanics, taught to automaticity | 2 months | **Built and verified.** Materials complete, not yet taught |
| **Part 2** | Depth, algorithms and design — what the fluency was for | 4 months | **Vision only.** Outlined below; not written |

The split is the whole argument of the programme. Part 1 deliberately removes every
algorithmic difficulty so that attention goes to the mechanics. Part 2 is where that
investment is spent. Building Part 2 before Part 1 reports would be assuming the answer
to the question Part 1 exists to ask (`RATIONALE.md` §5).

---

## Part 1 — coding fluency (built)

Two months, 24 sessions. Teachers who have never programmed finish with a four-file
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

### Stage 1 — the theory we postponed

The first thing Part 2 does is **go back**. Part 1 taught constructs as tools that solved
a problem the participant had just met; it did not explain how they work underneath. Now
there is practice for the theory to attach to.

- **Functions properly** — parameters in depth: positional against keyword, default values
  and when they bite, returning several values, what scope means and why a name inside a
  function is not the one outside
- **Loops and conditions in depth** — nesting, loops over loops, `break` and `continue`
  in combination, when a `while` is the right answer and when it is a mistake
- **Data structures in depth** — lists of dictionaries, dictionaries of lists, choosing
  between them deliberately rather than by habit
- **Reading other people's code**, which Part 1 never asks for

> **This stage is the test of the programme's central claim.** If the theory now lands
> easily on top of eight weeks of practice, the sequencing was right. If it is as hard as
> it was two years ago, it was not — and that is worth knowing in month three rather than
> month six.

### Stage 2 — algorithmic tasks and problem-solving

**The thing Part 1 was clearing the ground for.** With the mechanics automatic, the whole
of a participant's attention is available for the problem.

- Problems with no given method: searching, sorting by hand before using the built-in,
  counting and grouping, finding and comparing
- The habit of **writing the approach in words before writing code** — rehearsed once
  already, in the transfer question at the end of Part 1
- Breaking a problem into steps that each fit in a function
- More than one correct solution, and comparing them

### Stage 3 — bigger projects

Part 1's project is four files and about 150 lines. Part 2's should be several times that,
built over weeks rather than three sessions.

- A project the participant chooses, grounded in their own school work
- Working on something across sessions without losing the thread
- When a program is big enough that structure starts to matter
- Testing your own work; keeping it working while you change it

### Stage 4 — objects and classes

Deliberately late. Classes solve a problem a participant only *feels* once their programs
are big enough to have the problem — which is why they come after stage 3, not before it.

- What a class is, arriving the same way everything in Part 1 arrived: as the fix for
  something that has become awkward
- Attributes and methods; a `Student` object instead of parallel dictionaries
- When a class is the right answer and when a function is

### Stage 5 — recursion and harder techniques

- Recursion, and why it is natural for some problems and perverse for others
- Techniques that need the fluency of stages 1–4 to be readable at all

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
