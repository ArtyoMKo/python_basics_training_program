# Python for Armenian public-school teachers

Two courses, each nine weeks, that prepare serving teachers to deliver the state
curriculum **«ԱԲ սերունդ» — ՀԱՄԱԿԱՐԳՉԱՅԻՆ ԳԻՏՈՒԹՅՈՒՆ՝ PYTHON ԼԵԶՎՈՎ** (ministry order
1875 of 09.09.2026) to their own pupils.

| | Prepares a teacher for | State topics | Status |
|---|---|---|---|
| **[`grade10/`](grade10/README.md)** | **Grade 10** | 1–14 | **Built and verified.** Not yet taught |
| **[`grade11/`](grade11/README.md)** | **Grade 11** | 15–22, 24 | **Built and verified.** Not yet taught |
| [`shared/`](shared/GOVERNMENT_ASSIGNMENT.md) | the curriculum both answer to | all 24 | reference |
| [`partners/`](partners/) | the dossier and change log for external partners, covering **both** courses | — | generated |

Each course is **18 sessions × 75 minutes = 22 h 30**, two a week over nine weeks,
delivered **fully remotely — every session, without exception** — in groups of 4–8,
with required homework between sessions. Materials are in Armenian; code is in English.

## The two halves of each course

Every course is a **practical Part 1** and a **theoretical Part 2**, in that order and
never mixed:

| | What it is | Length |
|---|---|---|
| **Part 1** | **Writing working code**, with the algorithmic difficulty deliberately removed. Mechanics to automaticity | 9 weeks — the 18 sessions above |
| **Part 2** | **The theory Part 1 postponed, and algorithmic problems** | Outlined in each course's `docs/ROADMAP.md`; not written |

Part 2 of either course runs only if its Part 1 meets the success criterion
(`docs/RATIONALE.md` §5a). Building it earlier would assume the answer to the question
Part 1 exists to ask.

## Which teacher takes which

The grade-11 course **assumes the grade-10 course**, and assumes nothing beyond it. A
teacher arriving at `grade11/` can write a loop, a dictionary and a function, and can run
a three-file program. They have never seen a class, an object, a library or a comprehension,
and those are taught from zero, practically, the same way the grade-10 course teaches
variables and loops.

## Working in this repository

Each course folder is self-contained — its own `AGENTS.md`, `docs/`, `src/` and `tools/`.

```bash
cd grade10 && python tools/verify.py     # or grade11 — proves one course's material runs
python tools/check_docs.py               # from the root — proves the DOCUMENTS agree
python tools/check_topic_refs.py         # from the root — every "topic N" names the right topic
python tools/build_partner_docx.py       # from the root — rebuilds the partner dossier
```

> **Read the `AGENTS.md` inside the course folder you are changing.** The two courses share
> a method but not their rules: `grade10/` is standard-library-only and forbids classes;
> `grade11/` teaches both classes and libraries.
