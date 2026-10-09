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

Every session's agenda is in `CURRICULUM.md` and sums to exactly **75 minutes**,
verified by script. There are three shapes, plus bespoke agendas for sessions 1, 17 and 18:

| | Single | Discovery | Paired |
|---|---|---|---|
| Recap | 5 | 5 | 5 |
| Teach | **12** | 7, then 9 | **12**, then **12** |
| Hands-on | 20 + 33 | 22 + 27 | 16 + 16 + 9 |
| Retrospective | 5 | 5 | 5 |
| **Hands-on** | **53** | **49** | **41** |

**Hands-on is never below 41 of 75.** That is a floor.

> **A paired session is two teach blocks of 12, not one of 24.** The cap is per block.

> **The rule to hold yourself to: if you have been talking for more than 12 minutes, you
> are behind and the lesson is already worse.**

### What to cut when a session runs long

1. **Extra tasks** — always first, every time
2. **The last Required exercise** — it is placed last for this reason
3. Never: the second half of a discovery day

---

## 3. The seven discovery topics

**Topics 4, 6, 9, 12, 14, 16, 19** — sessions 3, 5, 7, 9, 11, 13, 15. These are the ones that need the most care.

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
| **20** | **The only topic needing internet**, and the only one with no laborious half | Topics 20 and 21 share session 16. **If the network fails, teach topic 21 first and topic 20 second**, and if it is still down, carry topic 20 into session 18's recap or set it as reading. Nothing depends on it until topic 24 |
| **21** | Debugging is hard to teach remotely | Do it on **your** screen, with a bug you introduce live. Do not ask them to watch their own |
| **22** | Five files at once | Confirm `python main.py` **individually, for every participant, on a shared screen, before anybody leaves** |

---

## Homework — required on this schedule, and you must say so

Two sessions a week of 75 minutes is **22½ contact hours**, against 30 on the original
three-a-week schedule. Nothing was cut from the course; the practice moved.

| Session shape | What goes home | Roughly |
|---|---|---|
| Single | the Extra tier | 15–20 min |
| Discovery | the Extra tier | 20–30 min |
| **Paired** | **the Required tier of both notebooks**, then Extra | **30–40 min** |
| Setup, transition, project | nothing, or the second notebook's Required | 0–30 min |

- **Nothing new is ever introduced at home.** Every task is already in the notebook and
  uses only what the session taught.
- **Every agenda opens with a recap block, and that is where homework is checked.** If you
  skip it, the paired sessions stop working within a fortnight.
- **Say in week 1 that homework is required**, and that a participant who does none will
  not finish. They were told at enrolment; hearing it again from you makes it real.
- A participant falling behind on homework is the **earliest** signal you get. Act on it
  in week 2, not week 6.

## 5. Assessment

| | Test | When | Length | Points |
|---|---|---|---|---|
| 1 | Initial diagnostic | **Before session 1** | 30–40 min | 40 |
| 2 | Midpoint | **After session 8** (topics 2–11) | 60–75 min | 50 |
| 3 | Final practical | **Session 18** | 90–120 min | 70 + 10 separate |

**Record a help level with every score** — `3` independent, `2` after one hint, `1`
step-by-step, `0` did not finish. On the diagnostic this matters more than the score.

**Hand out the participant build**, `tests/participant/*.ipynb`. The other one has the
rubric in it.

### The two questions that change what you do next

| | Question | If it is weak |
|---|---|---|
| Diagnostic | **Q1 — did they write a loop?** | Extend session 1 and run a loop clinic before topic 2. Do not carry on as planned |
| Midpoint | **Q4 — did they write a working `__init__`?** | **Do not start session 9.** Add a revision session on topics 6–8 |

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
| **Ask people to share, do not wait for volunteers** | Rotate through everyone across the nine weeks |
| **Watch for silence** | In a group of 4–8, a participant who has not spoken in two sessions is stuck, not quiet |
| **The chat is for code** | Paste every command you type. Some will have missed it on screen |
| **Record nothing without asking** | And if anyone objects, do not record |

---

## 8. What this course costs to run

| | |
|---|---|
| Software | **Zero.** Anaconda and VS Code, already installed |
| Installation | **None** — all three libraries ship with Anaconda |
| Network | **One session of 16** |
| Instructor time | 22½ contact hours, plus ~3½ hours of assessment |
