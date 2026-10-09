# Instructor notes

Read this before session 1.

> **This is Part 1 of a two-part programme: Part 1 is 2 months, Part 2 is 4 months.** Part 2
> is outlined in `ROADMAP.md` and runs only if Part 1 meets the criterion in
> `RATIONALE.md` §5a.


> **Vocabulary, because the word collides.** In this course the **participants are
> teachers**. So: *participant* = the person taking the course; *student* = a child in
> the participant's own class, i.e. the data in every example; *instructor* = you.
> The materials hold this distinction throughout. Keep it when you speak.

---

## 1. Remote delivery — what it changes

**The course is taught remotely, over Google Meet, in groups of 4–8.** Nobody is in a
room. That changes three things, and they are the three things most likely to catch you
out.

### What gets better

The worst risk an in-person run would have had is **gone**: sixteen people downloading
1 GB over one school connection on session 1. Each teacher now installs at home, on their own
connection, in their own time — and the enrolment questionnaire (`ENROLMENT.md`) has
already found the ones who cannot.

**Send the setup instructions at least three days early and ask for a reply confirming
`handouts/check_setup.py` printed six green lines.** A teacher who has not replied has not tried.

### What gets worse

**You cannot walk over and look at their screen.** Everything that was a thirty-second
fix in a room is now a conversation, and a beginner often cannot describe what they are
seeing well enough for you to diagnose it.

The substitute is **screen sharing, used constantly and asked for by name**:

- Google Meet can now show **every participant's shared screen at once**, with switching
  between them. Use it. Ask the whole group to share at the start of hands-on work and
  leave it up — that is the remote equivalent of walking between desks.
- **Ask by name.** In a room you can see someone stuck and not typing. On a call you
  cannot, and this audience will not interrupt to say so. With 4–8 people you can afford
  to check in on each one in every hands-on block, and you should.
- A teacher with **no webcam** loses you the other signal — the face that has given up.
  Compensate by asking them to share screen more often than the others.

### What has to be redesigned

| In person | Remotely |
|---|---|
| Pair fast finishers with slower ones from topic 3 | **Breakout rooms**, two or three at a time, for the exercise block |
| Walk the room during exercises | All screens shared, switching between them |
| "Swap laptops with your neighbour" in session 16 | **Send your folder to a colleague**; they run it from your README alone and report back on the call |
| Confirm `python main.py` individually on session 14 | Same, but **each person shares their screen and runs it while you watch**. Do not accept "it works" |

### Group size: 4 to 8

**Fewer than 4** and there is no discussion — the session becomes a tutorial, and the
habit of explaining to each other never forms. **More than 8** and remote teaching stops
working: you cannot check in on everyone in a hands-on block, and the people who are
quietly stuck stay quietly stuck.

This also changes topic 24's showcase: 8 × 90 seconds is 12 minutes, not 24. Use the time
you get back for the colleague-runs-your-program test, which matters more.

### ⏳ Not yet verified — you must do this before the first cohort

**The installation instructions have never been followed on a clean machine.** Run
`handouts/SETUP.md` literally, once on a fresh Windows laptop and once on a fresh Mac, and time it.
Put the real numbers in this file.

Remotely, three things matter more than they would in a room, because you cannot reach
over and fix them:

1. VS Code offers **exactly one** kernel, and its name matches what `handouts/SETUP.md` says.
2. `Ctrl+`` ` `` opens a terminal where `python --version` works with no conda activation
   typed by hand — **on Windows**. If it does not, correct `handouts/SETUP.md` before session 1.
3. `handouts/check_setup.py` runs green **from inside VS Code**, not just from a terminal — that is
   how a participant will run it.

Do this on a machine resembling what the questionnaire says the cohort actually has, not
on a developer's laptop.

## 2. The kernel picker is the single most common problem

VS Code asks which Python to use for every notebook. Pick wrong, and packages "aren't
installed" even though they are.

**Before answering any other question, ask: which kernel is selected?** Ten times out of
ten in the first fortnight, that is the answer. `handouts/SETUP.md` step 6 and the session 1 and topic 2
red callouts cover it, and `handouts/check_setup.py` prints which Python is actually running.

Other frequent problems, in order of how often they occur:

| What they see | What it is | Fix |
|---|---|---|
| `NameError` | A cell above was not run | Run → Run All Above |
| `IndentationError` | Tab/space mix, or a missing four spaces | Retype the line; do not copy it |
| Nothing prints in a `.py` file (Topic 20+) | They expect notebook behaviour | Everything you want to see needs `print()` |
| `FileNotFoundError` (session 14+) | Wrong folder, or `data/` misplaced | `python_course` must be the opened folder |

---

## 3. The five discovery days are the course. Never split one.

**Topics 6, 8, 11, 17 and 22** each give participants a real task, let them solve it the
long way with what they know, and then — **in the same session** — hand them the tool
that collapses it.

**The single most important rule in this document: never let a discovery day end at the
halfway point.** If topic 11 is running long, cut its Extra tasks. Cut the Challenge. Cut the
recap. Do *not* stop after the fifteen `if` blocks and promise the loop on Thursday. A
session that ends after the long way and before the short way is the worst outcome this
design can produce, and with working adults it is the one that loses people.

**Do not rescue them early, either.** Someone will ask, twenty minutes in, whether there
is a faster way. The answer is yes, and it is after the break — the notebook says so in
writing before the long half starts, so you are keeping a promise, not being evasive.

**Never tell them the long way was a lesson.** They are building a class register because
a teacher needs a class register. That is true, and it is the only framing the materials
use. "Now you see how bad that was" undoes the whole effect: it turns work they chose to
do into a trick played on them. The notebooks compare the two versions with a table of line
counts and nothing else. Do the same out loud.

**Week 4 (topics 10–12) is the emotional centre of the course.** If the schedule slips,
protect it.

## 4. Timing

Every day's agenda is in `CURRICULUM.md` and sums to exactly 120 minutes, verified by
script. The standard shape is 5 recap / **12 teach** / 20 run together / 33 exercises /
5 retrospective.

> **The rule to hold yourself to: if you have been talking for more than 15 minutes, you
> are behind and the lesson is already worse.**

Hands-on is at least 82 of 120 minutes. That is a floor. These are adults who will not ask you to
stop, so nobody will tell you when you are over.

**If you run out of time, cut — never compress.** In this order:

1. **Topic 16 (`while` loops).** The only genuinely removable day. The project's menu ships
   written; explain it in two minutes on session 14.
2. **Topic 15's dict-of-lists** (several grades per student). The project works with one.
3. **Topic 19's consolidation**, if the room is already ahead — but see §5, it is also the
   catch-up day.
4. **Topic 23's own-feature work.** It can become optional homework.

**Never cut:** the five discovery days (6, 8, 11, 17, 22) — each is a concept *and* its
motivation in one session, so cutting one costs both. Nor topics 20–21 (the transition) or
session 16 (finishing something is the point).

---

## 5. Mixed pace, and the two-day gap

These are working adults meeting twice a week. Some will miss sessions.

- **Hand out `solutions/dayNN.ipynb` after each session, not with the notebook.** A
  participant who misses a day needs to catch up alone, and this is the artefact that
  lets them. Every notebook re-declares what it needs, so no day depends on the last one's
  variables still existing.
- **Exercises are marked Required or Extra.** Required ones fit the 15 minutes. Nobody
  should ever leave with Required work unfinished.
- **Pair fast finishers with slower ones from Topic 3.** Explaining is the best available
  use of a fast participant, and it costs you nothing.
- **The practice task at the end of each notebook is optional and the next day never
  assumes it was done.** Say that out loud in week 1, or half the room will arrive
  anxious.

---

## 5b. The three assessments

**Three sittings, not four take-home tests** — the design agreed with our partner
colleague. They are **separate sittings** and do not use session time.

| Test | When | Length | Points |
|---|---|---|---|
| Initial diagnostic | **Before session 1** | 45–60 min | 44 |
| Midpoint | **After session 9** | 60–75 min | 50 |
| Final practical | **Session 16** | 90–120 min | 70 + 10 separate |

### Before each sitting

> **Hand out `tests/participant/<name>.ipynb`, never `tests/<name>.ipynb`.**
>
> The second one is the grader's copy. It states what every question measures and what it
> is worth. Giving it out by accident is the one irreversible mistake available here, so
> the two are generated as separate files rather than by remembering to delete cells.

The platform assigns each participant **one** of variants A, B or C per question. They are
equivalent in difficulty and points.

### What to say when you hand out the first one

Say it plainly: **these are not exams and nobody is being ranked.** The scores tell you
where to slow down and tell the programme whether the method is working
(`RATIONALE.md` §5). An honest blank is more useful than a copied answer, and the tests
say so in writing.

### Record two numbers per question

Alongside the score, record the **help level** — `3` independent, `2` after one hint, `1`
step-by-step, `0` did not finish. On the diagnostic this matters more than the score: two
people can both reach 30/44, and the one who needed step-by-step help four times is a
different teaching problem from the one who worked alone and ran out of time.

### Three results that change what you do next

| Test | Watch | If it goes wrong |
|---|---|---|
| Diagnostic | Q1 — can they run a cell at all? | Several at help level 0–1 → add a helper to session 1, or run a setup clinic first. This is your advance warning on the riskiest session |
| Midpoint | **Q4 — did they write a loop?** | Still writing one block per student after nine sessions is the strongest early evidence against the approach. Record it; do not explain it away |
| Final | Q2 and Q3 — returning or printing? | Printing means `return` never landed, and the four-file project rests on it |

### The diagnostic is also a planning tool

It is sat before anyone has been taught anything, so it cannot be failed. Use the spread
to plan the pairing from topic 3, and keep the four self-assessment numbers — the
interesting comparison at the end is **confidence before against capability after**.

---

---

## 5c. The trial class, in March

After Part 1, **each teacher takes one trial class with real pupils.** It is the only
point in the programme that tests what the programme is for.

**Set expectations low and say so.** A first lesson taught by a nervous adult who learned
to code eight weeks ago is not a performance review, and treating it as one will produce
a worse lesson and a worse measurement. Tell them that in advance.

### What to record

Four things, agreed before March and kept light (`docs/RATIONALE.md` §5a):

1. Did the lesson happen, and did it finish?
2. Did the **pupils** end up running code themselves, or did the teacher demonstrate throughout?
3. When a pupil hit an error, could the teacher **read it and act on it live**?
4. One sentence from the teacher: what surprised them?

**Number 3 is the most diagnostic.** Reading an error message is drilled from topic 2 of our
course onward, with one deliberate error in every session. If it holds up in front of a
class — under pressure, on someone else's screen, with a child watching — the method
transferred. If the teacher freezes, that is worth more than any test score.

### What to avoid

- **Do not script the lesson for them.** A lesson they did not plan tells us nothing.
- **Do not send them in with the hardest topic.** session 1–5 material is enough; the point is
  the teaching, not the content.
- **Do not let it become an inspection.** One observer, known to them, no panel.

---

## 6. Privacy — say it on Topic 5, before they choose their data

From Topic 5 the exercises ask for the participant's real class. The Topic 5 notebook carries
a red callout, and Topic 22 repeats it where they create a real file.

Say it once, plainly, when you set that first exercise:

> **First names or initials only. No surnames. Change the grades. No birthdates, no
> addresses, no ID numbers.**

The data does not need to be *real* to teach the program. It needs to be *familiar*.
The shipped `sample_class.csv` is fictional, so nobody is blocked.

`.gitignore` excludes `**/my_class.csv` so that a participant who ever shares the folder
cannot leak a class list by accident.

---

## 7. Budget and logistics

| | |
|---|---|
| Software cost | **Zero.** Anaconda and VS Code are free |
| API / account cost | **Zero.** Nothing in this course touches a network after session 1 |
| Group size | **4–8**, one instructor. Topic 24's showcase is 8 × 90 s = 12 min, leaving time for the colleague-runs-your-program test |
| Machines | Participants' own or the school's. Mixed Windows and macOS |
| Disk space needed | ~5 GB per machine. Ask on the enrolment form |

**If a school laptop blocks installation outright**, the fallback is Google Colab for
topics 1–19 and pairing with a colleague for topics 20–24. That participant will not get the
full transition experience, which is the most valuable part of the course — so treat it
as a last resort and push the school's IT first.

This fallback is deliberately **not** in the participant materials. A fork in the road
printed in `handouts/SETUP.md` is a fork every participant has to think about.

---

## 8. Armenian terminology — an open item

⏳ **The glossary in `handouts/CHEATSHEET.md` §1 has not been reviewed by a native speaker.**

Every Armenian technical term in all 19 notebooks comes from that table and nowhere else,
and `tools/check_style.py` enforces it. That is what makes a correction a find-and-replace
instead of a re-read of nineteen files.

Terms marked **⚠** in the glossary are the ones I am least confident about. If your
school uses a different word, change the glossary and re-run the checker.

---

## 9. What "done" looks like for each participant

| Day | They leave with |
|---|---|
| 1 | `handouts/check_setup.py` green, and their name printed in Armenian |
| 6 | Their class as one list, written both ways, with the line counts compared |
| 11 | The whole register marked in four lines, proved by adding students |
| 8 | Their class as a dictionary, and a note of what went wrong with two lists |
| 17 | The average as a function, with a formatting change proved in one edit |
| 19 | The complete register program working in one notebook |
| **21** | **A working `python main.py` — confirm this individually, for every person, before they leave** |
| 22 | Their own class in `data/my_class.csv`, loaded and saved back |
| 24 | A README a colleague successfully ran from, and a 90-second demo |

**Session 14 is the one to be strict about.** Do not let anyone leave that session without
`python main.py` running. Everything after it assumes that it does.
