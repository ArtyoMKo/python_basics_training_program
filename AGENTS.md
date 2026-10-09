# AGENTS.md — repository root

This repository holds **two courses**, each self-contained:

| Folder | Course | Its contract |
|---|---|---|
| `grade10/` | prepares teachers for **grade 10** — state topics 1–14 | `grade10/AGENTS.md` |
| `grade11/` | prepares teachers for **grade 11** — state topics 15–22, 24 | `grade11/AGENTS.md` |
| `shared/` | the state curriculum both answer to | `shared/GOVERNMENT_ASSIGNMENT.md` |

> ### ⛔ Read the `AGENTS.md` of the course you are changing. It is the authority there.
>
> The two share a method and nothing else. A rule from one is **not** a rule in the other —
> `grade10/` forbids classes and third-party imports; `grade11/` teaches both.

Never change a file in one course because of something you read in the other. If a change
belongs in both, make it twice and say so.

## What is the same in both

These hold everywhere, and a change to any of them belongs in both courses:

1. **Armenian explains, English codes.** Markdown, guides and handouts in Armenian; every
   identifier, comment, docstring, string and printed line in English.
2. **A laborious task and its replacement happen in the SAME session.** Never split one.
3. **The tedium is never named.** A participant is never told they are suffering to make a
   point. The notebook promises the shortcut in writing before the long stretch begins.
4. **Every agenda sums to exactly 75 minutes.** Teaching never exceeds 12 minutes in one
   block. If content does not fit, cut a topic — never compress one.
5. **Three exercise tiers in every notebook** — Պարտադիր 3–4, Լրացուցիչ 3–4, Մարտահրավեր 1–2.
6. **Every example is a classroom.** No `foo`, no `x = 5`, no fizzbuzz.
7. **`notebooks/`, `solutions/` and `tests/` are generated from `src/`.** Never edit a
   `.ipynb`.

## The build loop, in either course

```bash
cd grade10                      # or grade11
python tools/nbbuild.py         # rebuild notebooks, solutions and tests from src/
python tools/verify.py          # nothing is done until this passes
```

Each course has its own copy of `tools/`. They are deliberately duplicated rather than
shared: the checkers encode course-specific rules — `grade10/` fails a build that contains
the word `class`, `grade11/` requires it — and a shared tool with a configuration file
would be more moving parts, not fewer (`grade10/docs/PLAN.md` §0).
