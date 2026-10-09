# Enrolment questionnaire

**Sent to every teacher before a group is formed.** The course is delivered **remotely**,
so these answers are not background information — several of them decide whether a person
can take part at all, and all of them shape the group.

The questions as sent are in Armenian; the right-hand column is for us.

---

## The questionnaire

> **Python-ի դասընթաց — նախնական հարցաթերթ**
>
> Խնդրում ենք պատասխանել այս վեց հարցին։ Դրանք օգնում են մեզ կազմել խմբերը և
> նախապես լուծել տեխնիկական խնդիրները։ **Ճիշտ կամ սխալ պատասխան չկա** — եթե ինչ-որ
> բան չունես, ասա՛, և կփորձենք լուծել միասին։

| # | Question (as sent) | What the answer decides |
|---|---|---|
| 1 | Քանի՞ օր ես պատրաստ հատկացնել Python-ի դասերին՝ **2**։ | **Which group they join.** The two answers cannot be mixed in one group — they produce different schedules |
| 2 | Ինտերնետ կապդ բավարա՞ր է տեսազանգի համար։ | **Gating.** A video call with screen sharing for 75 minutes, twice a week, is the floor. If the answer is no, this has to be solved before they start, not during week 1 |
| 3 | Ունե՞ս վեբ-տեսախցիկ։ | Not gating, but it changes how we teach them. See below |
| 4 | Կարո՞ղ ես օգտվել Zoom-ից կամ Google Meet-ից։ | **Gating in practice.** "No" usually means "I have never tried", which is a 20-minute fix before session 1 — but only if we know |
| 5 | Ունե՞ս որևէ տեխնիկական խնդիր, որի մասին արժե իմանալ։ | The open question. **The most useful one on the form**, because it catches what we did not think to ask |
| 6 | Քո նոութբուքի մոդելը և հնարավորությունները՝ օպերատիվ հիշողություն (RAM) և ազատ տեղ սկավառակի վրա։ | **Gating.** Anaconda needs about 5 GB free and 8 GB RAM is comfortable. This is the answer that most often requires action |

---

## How to read the answers


### Question 2 — internet

The honest test is not "do you have internet" but **"can you hold a video call with
screen sharing for 75 minutes"**. Ask it that way in the follow-up if the answer is vague.

A teacher on an unstable connection is the hardest case in a remote course: they miss the
explanation, not just the room. If it cannot be fixed, consider whether they can attend
from their school rather than home.

### Question 3 — webcam

**Not a requirement.** Nobody is excluded for lacking one. But it matters more than it
looks: without a camera, an instructor cannot see the thing that is most informative in a
beginner class — someone stuck, not typing, and not saying so.

Where a teacher has no camera, compensate by asking them to **share their screen more
often**, and check in on them by name rather than waiting for a question.

### Question 4 — Zoom or Google Meet

Almost always answered "no" by people who simply have not used it. Treat a "no" as a
booking for a **ten-minute call before session 1** to install it and practise screen sharing
once. That call also doubles as the connection test for question 2.

### Question 5 — any technical problem

Open-ended on purpose. Read every answer individually. The ones that have turned up in
planning so far: a shared family laptop, no administrator password, a school laptop
locked down by its IT department, and "my son uses it in the evenings".

**A shared laptop is a scheduling problem, not a technical one**, and it is better solved
before enrolment than in week 3.

### Question 6 — laptop model and resources

| Finding | What to do |
|---|---|
| Less than ~5 GB free disk | Fixable: ask them to clear space before session 1, with help if needed |
| Less than 8 GB RAM | Workable but slower. Expect Anaconda to take longer to start; warn them so they do not think it has frozen |
| No administrator rights | **The serious one.** Both installers offer a per-user install, which usually works; test it with them before session 1 rather than discovering it live |
| A tablet or Chromebook, not a laptop | Anaconda will not install. This is the case where the browser-based fallback is the only option, and it costs them the final sessions (see `INSTRUCTOR_NOTES.md`) |

---

## What must be said at enrolment, not later

Two things change what a teacher is agreeing to, and both belong in the enrolment
conversation rather than being discovered during the course:

| | |
|---|---|
| **The last assessment decides who continues** | The first two are diagnostic and are not graded. **The third gates entry to Part 2.** People behave differently when they know this, so telling them afterwards would be both unfair and would spoil the result |
| **There is a trial class with real pupils in March** | After Part 1. It is the point of the whole programme, and some teachers will find it the most daunting part. Saying so early gives them months to get used to the idea rather than three weeks |

Both are in `docs/ANNOUNCEMENT.md` in Armenian, so a teacher reads them before applying.

---

## What this questionnaire is for

Remote delivery removes the single best mitigation an in-person course has: **an
instructor who can walk over and look at the screen.** Everything that would have been
fixed in thirty seconds in a room becomes a call.

So the questionnaire is doing the job that a USB stick full of installers used to do. It
is worth being thorough with it, and worth acting on the answers **before** a group is
formed rather than after.

**Keep the answers.** When the programme reports its result (`RATIONALE.md` §5), the
question "did the people who struggled have worse equipment?" is one we should be able
to answer rather than guess at.


## Homework — say this before they agree

**Homework is required on this schedule.** Two 75-minute sessions a week cannot hold 24
topics and their practice, so on the sessions that cover two topics the Required tier of
both notebooks goes home — 45–60 minutes. Everywhere else it is the Extra tier, 15–30
minutes. **Nothing new is introduced at home**, and the next session opens by checking it.

A participant who does no homework will not finish. That is a fair thing to say at
enrolment and an unfair thing to discover in week three.
