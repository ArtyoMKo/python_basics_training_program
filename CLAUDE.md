# CLAUDE.md

**Read `AGENTS.md` at the repository root before changing anything.** It is the complete
contract for agents working here, and it is the single source of truth — this file
deliberately contains no rules of its own, so the two cannot drift apart.

The one thing worth repeating here, because it silently destroys work:

> **`notebooks/`, `solutions/` and `tests/` are generated from `src/`.**
> Never edit a `.ipynb`.

The whole workflow is two commands:

```bash
python tools/nbbuild.py     # rebuild notebooks, solutions and tests from src/
python tools/verify.py      # four checks; nothing is done until this passes
```
