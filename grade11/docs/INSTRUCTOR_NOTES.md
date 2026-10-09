# Instructor notes — the grade-11 course

**Read this before session 1.**

---

## 1. Before the first session

| | |
|---|---|
| **The diagnostic is sat before session 1** | Mark it the same day. It changes how session 1 runs — see `tests/mark1_guide.md` |
| **Every participant has run `check_setup.py`** and replied | Six green lines. **Do not start without the reply**; a silent participant is a broken install |
| **You have run session 1 yourself**, on a machine that is not yours | Especially the three imports |
| **The Google Meet link is sent**, with screen sharing tested | Ten-minute call with anyone who has not shared a screen before |
| **`school.csv` is sent** and participants have opened it | It sits beside the notebook, under that exact name |

> **The riskiest moment in this course is not session 1.** It is topic 12, when the first
> library import happens. If Anaconda is incomplete on somebody's machine you want to know
> in week one, not week five — which is why `check_setup.py` imports all three.

---

## 2. Timing

Every day's agenda is in `CURRICULUM.md` and sums to exactly **120 minutes**, verified by
script. Two shapes:

| | Standard day | Discovery day |
|---|---|---|
| Recap | 5 | 5 |
| Teach | **12** | 7, then 9 |
| Hands-on | 20 + 33 | 22 + 27 |
| Retrospective | 5 | 5 |

**Hands-on is at least 49 of 75.** That is a floor.

> **The rule to hold yourself to: if you have been talking for more than 12 minutes, you
> are behind and the lesson is already worse.**

### What to cut when a day runs long

1. **Extra tasks** — always first, every time
2. **The last Required exercise** — it is placed last for this reason
3. Never: the second half of a discovery day

---

## 3. The seven discovery days

Days **4, 6, 9, 12, 14, 16, 19**. These are the ones that need the most care.

| What goes wrong | What to do |
|---|---|
| The long half runs over and the tool does not arrive | **Cut the long half short mid-task.** Say "stop there, we have enough" and move to the tool. An unfinished long half is fine; a missing short half is not |
| Somebody finishes the long half in five minutes | Give them the Extra tasks from the previous day. **Do not** let them start the second half early — the comparison is the lesson |
| Somebody says "why are we doing it this way, there must be a better way" | **Agree with them, out loud, and say the better way is coming after the break.** This is the best thing that can happen in the session |

**Never say "notice how slow that was".** The notebook makes the comparison with a table
of line counts. Saying it aloud turns a discovery into a lecture.

---

## 4. The days most likely to go wrong

| Day | Risk | What to do |
|---|---|---|
| **6** | Classes. The single hardest idea in the course | The long half **must fail visibly** before the class arrives. If nobody's dictionary breaks, slow down and make it break |
| **9** | `super().__init__()` is forgotten by almost everyone | The `AttributeError` cell is there for this. Run it together, slowly |
| **12** | The first import of something we did not write | If an import fails here, the setup check was not done. Have a backup: Colab, from topic 20's material, brought forward |
| **16** | pandas does in one line what topic 16 spent 22 lines on | Some participants find this deflating rather than freeing. Say explicitly that the 22 lines were how you learn what the one line does |
| **20** | **The only session needing internet**, and the only one with no laborious half | If the network fails, swap it with session 14 and run it later. Nothing depends on it until topic 24 |
| **21** | Debugging is hard to teach remotely | Do it on **your** screen, with a bug you introduce live. Do not ask them to watch their own |
| **22** | Five files at once | Confirm `python main.py` **individually, for every participant, on a shared screen, before anybody leaves** |

---

## 5. Assessment

| | Test | When | Length | Points |
|---|---|---|---|---|
| 1 | Initial diagnostic | **Before session 1** | 45–60 min | 40 |
| 2 | Midpoint | **After topic 11** | 60–75 min | 50 |
| 3 | Final practical | **Session 16** | 90–120 min | 70 + 10 separate |

**Record a help level with every score** — `3` independent, `2` after one hint, `1`
step-by-step, `0` did not finish. On the diagnostic this matters more than the score.

**Hand out the participant build**, `tests/participant/*.ipynb`. The other one has the
rubric in it.

### The two questions that change what you do next

| | Question | If it is weak |
|---|---|---|
| Diagnostic | **Q1 — did they write a loop?** | Extend session 1 and run a loop clinic before topic 2. Do not carry on as planned |
| Midpoint | **Q4 — did they write a working `__init__`?** | **Do not start topic 12.** Add a revision session on topics 6–8 |

Each guide — `tests/mark1_guide.md` and so on — says what every wrong answer means.

---

## 6. Telling participants what the scores are for

Say this out loud, before the first sitting, in these words or close to them:

> «Այս թեստը գնահատում է **ծրագիրը**, ոչ թե ձեզ։»

Participants who believe they are being judged behave differently, and the measurement is
worthless if they do. The one exception is the **third** sitting, which does gate entry to
Part 2 — and they are told that in advance, at enrolment, not afterwards.

---

## 7. Running it remotely

| | |
|---|---|
| **Screen sharing is the whole lesson** | Yours for the teach blocks, theirs for the hands-on |
| **Ask people to share, do not wait for volunteers** | Rotate through everyone across the eight weeks |
| **Watch for silence** | In a group of 4–8, a participant who has not spoken in two sessions is stuck, not quiet |
| **The chat is for code** | Paste every command you type. Some will have missed it on screen |
| **Record nothing without asking** | And if anyone objects, do not record |

---

## 8. What this course costs to run

| | |
|---|---|
| Software | **Zero.** Anaconda and VS Code, already installed |
| Installation | **None** — all three libraries ship with Anaconda |
| Network | **One session of 24** |
| Instructor time | 32 contact hours, plus ~3½ hours of assessment |
