# Instructor notes

Read this before Day 1.

> **Vocabulary, because the word collides.** In this course the **participants are
> teachers**. So: *participant* = the person taking the course; *student* = a child in
> the participant's own class, i.e. the data in every example; *instructor* = you.
> The materials hold this distinction throughout. Keep it when you speak.

---

## 1. Day 1 is the highest-risk hour of the programme

Everything else can be recovered from. A lost Day 1 costs confidence, and this audience
arrives with very little of it.

| Scenario | Day 1 | Consequence |
|---|---|---|
| Most participants installed at home (expected, if `SETUP.md` went out 3 days early) | ~25 min | Day 1 runs as written, with time to spare |
| Nobody installed anything | 50+ min | Day 1 is lost. 16 × 1 GB over school wifi will not finish |

**Send `SETUP.md` at least three days before Day 1**, with the sentence: *trying it at
home is welcome, and failing at it is expected — that is what Day 1 is for.*

### Mandatory kit

- **A USB stick with the offline Anaconda installer for Windows and macOS**, plus the
  VS Code installers. This is not optional. It is the difference between losing Day 1 and
  not.
- Both installers' file names written on the board.
- `check_setup.py`, `sample_class.csv` and `day01_first_program.ipynb` on that same stick.

### Not yet verified — you must do this

⏳ **The fresh-laptop test has not been run.** Before Day 1, follow `SETUP.md` literally
on a machine that has never had Python on it — **once on Windows, once on macOS** — and
time it. Put the real number in this file.

Three things to confirm specifically, because they are the ones that bite:

1. VS Code offers **exactly one** kernel, and its name matches what `SETUP.md` says.
2. `Ctrl+`` ` `` opens a terminal where `python --version` works, with no conda activation
   typed by hand — **on Windows**. If it does not, set the default terminal to Command
   Prompt and correct `SETUP.md`.
3. `check_setup.py` runs green from inside VS Code, not just from a terminal.

---

## 2. The kernel picker is the single most common problem

VS Code asks which Python to use for every notebook. Pick wrong, and packages "aren't
installed" even though they are.

**Before answering any other question, ask: which kernel is selected?** Ten times out of
ten in the first fortnight, that is the answer. `SETUP.md` step 6 and the Day 1 and Day 2
red callouts cover it, and `check_setup.py` prints which Python is actually running.

Other frequent problems, in order of how often they occur:

| What they see | What it is | Fix |
|---|---|---|
| `NameError` | A cell above was not run | Run → Run All Above |
| `IndentationError` | Tab/space mix, or a missing four spaces | Retype the line; do not copy it |
| Nothing prints in a `.py` file (Day 20+) | They expect notebook behaviour | Everything you want to see needs `print()` |
| `FileNotFoundError` (Day 21+) | Wrong folder, or `data/` misplaced | `python_course` must be the opened folder |

---

## 3. The two pain days are the course. Do not rescue them.

**Day 6** (forty variables by hand) and **Day 9** (twenty-five `if` blocks) are designed
to be tedious. Participants will ask, halfway through, whether there is a better way.

**Say yes, and say which day.** Do not show them. Day 6's answer is Day 10; Day 9's
residue is answered on Day 14. The materials name the day in writing, so you are not
being evasive — you are keeping a promise they can check.

The retrospective on both days asks them to **write one sentence** about what was wrong.
Read three or four out loud. That two minutes is what makes Day 10 and Day 14 land; skipping
it turns the relief into just another feature.

**Week 4 (Days 10–12) is the emotional centre of the course.** If the schedule slips,
protect it.

---

## 4. Timing

Every day's agenda is in `CURRICULUM.md` and sums to exactly 50 minutes, verified by
script. The standard shape is 5 recap / **12 teach** / 15 run together / 15 exercises /
3 retrospective.

> **The rule to hold yourself to: if you have been talking for more than 15 minutes, you
> are behind and the lesson is already worse.**

Hands-on is 30 of 50 minutes. That is a floor. These are adults who will not ask you to
stop, so nobody will tell you when you are over.

**If you run out of time, cut — never compress.** In this order:

1. **Day 15 (`while` loops).** The only genuinely removable day. The project's menu ships
   written; explain it in two minutes on Day 21.
2. **Day 17's dict-of-lists** (several grades per student). The project works with one.
3. **Day 23's own-feature work.** It can become optional homework.

**Never cut:** Day 6 and Day 9 (the pain is the course), Day 12 (the first real relief),
Days 20–21 (the transition), Day 24 (finishing something is the point).

---

## 5. Mixed pace, and the two-day gap

These are working adults meeting three times a week. Some will miss sessions.

- **Hand out `solutions/dayNN.ipynb` after each session, not with the notebook.** A
  participant who misses a day needs to catch up alone, and this is the artefact that
  lets them. Every notebook re-declares what it needs, so no day depends on the last one's
  variables still existing.
- **Exercises are marked Required or Extra.** Required ones fit the 15 minutes. Nobody
  should ever leave with Required work unfinished.
- **Pair fast finishers with slower ones from Day 3.** Explaining is the best available
  use of a fast participant, and it costs you nothing.
- **The practice task at the end of each notebook is optional and the next day never
  assumes it was done.** Say that out loud in week 1, or half the room will arrive
  anxious.

---

## 6. Privacy — say it on Day 5, before they choose their data

From Day 5 the exercises ask for the participant's real class. The Day 5 notebook carries
a red callout, and Day 22 repeats it where they create a real file.

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
| API / account cost | **Zero.** Nothing in this course touches a network after Day 1 |
| Group size | **≤ 16**, one instructor. Day 24's showcase is 16 × 90 s = 24 min, which fits |
| Machines | Participants' own or the school's. Mixed Windows and macOS |
| Disk space needed | ~5 GB per machine. Ask on the enrolment form |

**If a school laptop blocks installation outright**, the fallback is Google Colab for
Days 1–19 and pairing with a colleague for Days 20–24. That participant will not get the
full transition experience, which is the most valuable part of the course — so treat it
as a last resort and push the school's IT first.

This fallback is deliberately **not** in the participant materials. A fork in the road
printed in `SETUP.md` is a fork every participant has to think about.

---

## 8. Armenian terminology — an open item

⏳ **The glossary in `CHEATSHEET.md` §1 has not been reviewed by a native speaker.**

Every Armenian technical term in all 19 notebooks comes from that table and nowhere else,
and `tools/check_style.py` enforces it. That is what makes a correction a find-and-replace
instead of a re-read of nineteen files.

Terms marked **⚠** in the glossary are the ones I am least confident about. If your
school uses a different word, change the glossary and re-run the checker.

---

## 9. What "done" looks like for each participant

| Day | They leave with |
|---|---|
| 1 | `check_setup.py` green, and their name printed in Armenian |
| 6 | Forty variables edited by hand, and one written sentence about why that was bad |
| 9 | One edit that changes the pass mark everywhere, proved by changing it twice |
| 12 | Yesterday's forty print lines as a three-line loop |
| 19 | Four working grade functions |
| **21** | **A working `python main.py` — confirm this individually, for every person, before they leave** |
| 22 | Their own class in `data/my_class.csv`, loaded and saved back |
| 24 | A README a colleague successfully ran from, and a 90-second demo |

**Day 21 is the one to be strict about.** Do not let anyone leave that session without
`python main.py` running. Everything after it assumes that it does.
