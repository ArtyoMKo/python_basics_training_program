# Pretest — grade 10, before session 1

**Instructor-facing.** Participants get `pretest.ipynb` (on Google Colab). Never hand out
`pretest_answers.ipynb` — it holds the reference answers.

Both notebooks are generated from `src/pretest.py` by `python tools/nbbuild.py`. Never edit
them directly.

| | |
|---|---|
| **When** | Before session 1, as a separate sitting, outside session time |
| **Length** | 45 minutes |
| **Where** | Google Colab — nothing to install, so it does not depend on session 1's setup |
| **Tasks** | 18, in three parts (below) |
| **Score** | **Share of tasks done**, overall and per part. No points, no partial credit |
| **Help** | None during the sitting — no internet, no AI, no other person |

## What it is for

1. **Fix each participant's baseline** before anything is taught. It filters nobody.
2. **Measure progress at the midpoint.** Every Python task sits inside topics 1–13 —
   what sessions 1–10 teach — so the midpoint (after session 10) re-sits **the same 18
   tasks** and each participant's change is read task by task. Never hand back marked
   copies or answers, or the re-sit measures memory instead.

## Why three parts

The participants are teachers with no programming background. A test of writing code
alone would put almost all of them at the same floor and the baseline would say nothing
per person. So the tasks run from what anyone can do to what the course will teach:

| Part | Tasks | Needs | What it separates at the baseline |
|---|---|---|---|
| A — notebook and table | 1–3 | nothing | who can operate a notebook and read data unaided |
| B — read code, predict output | 4–9 | reasoning only | who already has an intuition for code. **The main per-person signal before the course** |
| C — write code | 10–18 | Python | expected near zero for non-programmers; flags anyone who has coded before |

At the midpoint, expect A to stay full, B to rise first and C to show the most change.
Record the three part shares, not only the total: two participants at 22% overall (4 of 18) can be
3/3 + 1/6 + 0/9 or 0/3 + 4/6 + 0/9, and they need different help in session 1.

## A task is done when

Open the participant's shared copy, choose **Runtime → Run all**, and compare.

| # | Topic | Done when | Also check |
|---|---|---|---|
| 1 | running a cell | prints `Hello, <their name>` | the name was changed |
| 2 | reading a table | `Nare 1` | |
| 3 | applying a rule | `failed passed passed` | |
| 4 | `print` with commas (topic 2) | `Ani: 9` | spacing may differ |
| 5 | reassigning a variable (topic 5) | `9` | |
| 6 | text is not a number (topic 3) | `91` | |
| 7 | list index from 0 (topic 6) | `Davit` | |
| 8 | `if`/`else` (topic 9) | `failed` | |
| 9 | a total in a loop (topic 12) | `10` | |
| 10 | `print` (topic 2) | `7-B class - biology` | exact text |
| 11 | variables (topic 5) | `Ani 9` | two variables, one `print` of the variables |
| 12 | arithmetic with variables (topic 5) | `8.0` (or `8`) | computed, not typed in |
| 13 | text → number (topics 3–4) | `9` | uses `int()`, not a typed `9` |
| 14 | lists (topics 6–7) | `5` then `Ani` | `.append` used; count from `len()` |
| 15 | dictionaries (topic 8) | `10` then `5` | the value was changed in the dictionary |
| 16 | `if` alone (topic 9) | `excellent` | change `grade` to 5 → prints nothing |
| 17 | `if`/`else` (topic 9) | `failed` | change `grade` to 7 → `passed` |
| 18 | loop with a decision (topics 11–13) | the four `grade passed/failed` lines | one loop, not four `print`s |

Part B answers are text in quotes; accept `9` or `"9"` and ignore extra spaces.
A different working solution in Part C counts as done.

The last cell (`experience`, `language`) is not a task and is not scored. Record it next
to the score: it explains a high Part C result.

## What to record

Per participant: done / not done for each of the 18 tasks, the share done for A, B, C and
overall, and the experience answer. Keep it — the midpoint fills the same columns.
