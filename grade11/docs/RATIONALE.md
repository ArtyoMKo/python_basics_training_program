# Why this course is built this way

*For colleagues. The argument, the risk, and the rule we will be judged by.*

---

## 1. The problem this course solves

A teacher who finished our grade-10 course can write a loop, a dictionary and a function.
In September they will be asked to teach **classes, inheritance, three libraries,
recursion and debugging** to seventeen-year-olds.

Those are not an extension of what they know. They are a different kind of thing, and
nothing in the first course prepares them for it.

**The gap is not knowledge. It is that nobody has ever shown them why any of it exists.**

A teacher who has been told "a class groups data and behaviour together" can repeat that
sentence to a pupil. A teacher who has watched a misspelled dictionary key fail silently
thirty lines later, and then watched the same typo raise `TypeError` on the spot, can
answer the question a pupil actually asks: *why would I bother?*

---

## 2. The method, and the one rule that makes it work

Seven of the 18 sessions are **discovery days**. Each gives a real task, lets the
participant solve it the long way, and then hands them the tool that collapses it.

**All of that happens inside one session.** Never across two.

> Ending a session after the long way and before the short way is the worst outcome this
> design can produce. A participant goes home having spent an hour on something tedious,
> with no payoff, and the next session starts from resentment.

Two rules protect it:

1. **The shortcut is promised in writing before the long stretch begins**, and the
   notebook names when it arrives. "After the break we will learn something that makes
   this whole cell four lines."
2. **The tedium is never named.** A participant is never told they are doing something in
   order to suffer, or that the long way was there to make a point. They are given a task
   a teacher actually has. The comparison afterwards is a table of line counts and
   nothing else.

---

## 3. What is deliberately left out, and why

| Left out | Why |
|---|---|
| decorators, generators, `@property`, `dataclasses` | Not in the pupils' curriculum. Each costs a session and buys a teacher nothing |
| multiple inheritance, abstract base classes | Not in the pupils' curriculum, and actively harmful at this level |
| `sklearn`, `PyTorch`, `TensorFlow` | **Named once in session 18, never used.** Topic 21 lists them; a grade-11 teacher does not need them, and topic 24 says so in words they can repeat to a pupil |
| **factorial, Fibonacci, the call stack, complexity** | Recursion's *algorithmic* side. Part 2's material. The style checker fails a build that mentions either name |
| **git** | State topic 23. Deferred by decision until the rest of the subject is secure |

**The question any addition has to answer:** which line of the final school report tool
needs it?

---

## 4. What makes this course different from the grade-10 one

Two rules invert, and both inversions are the point.

**Classes are the centre, not forbidden.** The grade-10 course fails a build containing
the word `class`. Here, topics 6 to 11 are about nothing else. Topics 18 and 19 are 22
pupil-hours.

**Three libraries are allowed.** The grade-10 course allows no third-party import at all,
because `pandas` would make its topic 11 a one-liner and teach nothing about loops. Here,
NumPy, Matplotlib and pandas are state topics 15, 20 and 21, and a teacher has to
demonstrate them.

**But the order is preserved.** Topic 12 writes the standard deviation formula out by hand
before `numpy.std()` appears. Topic 16 spends twenty-two lines parsing a CSV before
`pd.read_csv()` appears. The library arrives as relief from work already done, not as a
way to avoid understanding.

---

## 5. The experiment, and how we will judge it

### 5a. The decision rule

Agreed **before the cohort starts**, and it does not move because the result is
disappointing.

| Result | What it means | What we do |
|---|---|---|
| **More than 80%** meet the pass criterion | The approach works | Run it again, and write Part 2 |
| **Between 70% and 80%** | It partly works | Adjust Part 1 and run it with a new cohort. **Do not start Part 2** |
| **Under 70%** | It does not work | Stop and redesign. A third repeat of an approach that has not worked is not persistence |

The thresholds were agreed with partners on 15 October 2026, and are the same as the
grade-10 course's.

**The pass criterion**, both halves required:

1. `python main.py` runs on their **own school's data** — confirmed individually in
   session 18 (topic 23), on a shared screen, not self-reported
2. **More than 85%** of the final assessment's tasks done

**The individual result has three bands, at two exams** — the same as the grade-10
course's:

| Tasks passed correctly | Midpoint (after session 8) | Final assessment (session 18) |
|---|---|---|
| **More than 85%** | **On track** — continues unconditionally | **Pass** — continues to Part 2 |
| **70% to 85%** | **Probation** — continues; told where the problem is; the method is adjusted for them | **Individual review** — the team decides whether they continue or leave |
| **Less than 70%** | **Probation**, with the highest priority | **Leaves the programme** |

The assessments themselves are being redesigned (removed 16 Oct 2026); this rule applies to
them as agreed. **Part 1 is not repeated.** **Nobody
leaves at the midpoint**: under 85% there means probation until the final assessment. In
the cohort figure above, only a pass in the sense above counts; a reviewed teacher who continues is reported separately.

### 5b. The second criterion — the trial classes

A teacher who can write code is not the same as a teacher who can teach it. **The real
measurement is teaching real pupils**, as for the grade-10 course: one or two coding
trial lessons in Part 1, the first in the middle of the second month (around week 7), and
two lessons on theoretical material in Part 2.

What to record is agreed in advance, and kept light: did the lesson happen, did the
pupils run something themselves, what did the teacher do when a pupil's code broke.

---

## 6. What could go wrong

Practical points to watch, each with a plan.

**The entry assumption may be wrong.** This course assumes a teacher arrives able to
write a loop and a function. If the grade-10 course did not produce that, everything from
topic 2 is built on sand. **Session 1 shows it early**, and the instructor notes say what
to do — including the option of repeating the grade-10 course instead of starting this one.

**Objects may not land in four sessions.** Topics 6 to 11 are sessions 5–8, 5 hours for
what the pupils' curriculum gives 22. If classes have not landed by session 8, the
libraries block cannot start, and we lose a session to revision. Nothing in the 18 × 75
shape is spare, so the time comes out of the cut list (`INSTRUCTOR_NOTES.md`); it is
still cheaper than pressing on.

**Three libraries in five sessions may be too fast.** NumPy gets one session (10),
Matplotlib and pandas two each (11–12, 13–14). That is enough to use them and not enough to be comfortable. We are betting
that a teacher who has *used* each one on their own school's data can teach the pupils'
version, which is shallower than ours.

**The method may not transfer.** Discovery works when there is a long way to do first.
By topic 20 — packages and environments — there is no laborious version to replace; it is
ordinary explanation. Topics 20 and 21 are the weakest in the course by this measure, and
we should watch them.

**Nobody has taught this.** Not one session has been delivered to a cohort. Every claim
in this document is a design claim, not a result.

---

## 7. What happens after two months

Either the numbers meet the rule in §5a and we write Part 2, or they do not and we fix
Part 1 first.

**Both outcomes are worth two months**, provided we agree the rule now and hold to it
then. The failure mode is not a disappointing number. It is a disappointing number
followed by an argument about whether it counts.
