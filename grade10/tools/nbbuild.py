"""
Build notebooks/*.ipynb from the plain-text sources in src/.

WHY THIS EXISTS. Nineteen notebooks are 19 large JSON files. Editing Armenian prose
inside JSON string arrays is unreviewable and error-prone, and the participant-facing
simplicity rule (docs/PLAN.md section 0) says nothing about how we author the material. So the
source of truth is a readable text file per day, and the .ipynb is generated.

    python tools/nbbuild.py            # build everything: notebooks and solutions
    python tools/nbbuild.py day03      # build one notebook

SOURCE FORMAT. Cells are separated by marker lines:

    #%% md                       a markdown cell
    #%% code                     a code cell
    #%% code expected-error: TypeError    a cell that MUST raise TypeError
    #%% code interactive: 9      a cell using input(); the runner feeds "9"

The markers put tags in the cell's metadata, not in the participant's view -- nobody
taking this course should see "# interactive" in their notebook.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
OUT = ROOT / "notebooks"

# The 18 solutions live in ONE source file so they can be reviewed in one pass, and are
# split out per day at build time.
SOLUTIONS_SOURCE = SRC / "solutions_source.py"
SOLUTION_MARKER = re.compile(r"^#%% (day\d\d) (md|code)\s*$", re.M)

# #%% md | #%% code | #%% md teacher | #%% code expected-error: X | #%% code interactive: 9
# The optional `teacher` flag marks an instructor-only cell. The assessments that used it
# were removed on 16 Oct 2026; the flag is still parsed so an old source does not break.
MARKER = re.compile(
    r"^#%%\s+(md|code)"
    r"(?:\s+(teacher))?"
    r"(?:\s+(expected-error|interactive):\s*(.*))?"
    r"\s*$"
)


def parse(text):
    """Turn one source file into a list of (kind, tag, tag_value, source, teacher) cells."""
    cells = []
    kind = tag = value = None
    teacher = False
    body = []

    for line in text.splitlines():
        match = MARKER.match(line)
        if match:
            if kind is not None:
                cells.append((kind, tag, value, "\n".join(body).strip("\n"), teacher))
            kind = match.group(1)
            teacher = match.group(2) is not None
            tag, value = match.group(3), match.group(4)
            body = []
        elif kind is not None:
            body.append(line)

    if kind is not None:
        cells.append((kind, tag, value, "\n".join(body).strip("\n"), teacher))

    return [cell for cell in cells if cell[3].strip()]


def build(cells):
    out = []
    for index, (kind, tag, value, source, teacher) in enumerate(cells):
        metadata = {}
        if teacher:
            metadata["audience"] = "instructor"
        if tag == "expected-error":
            metadata["expected_error"] = value.strip()
        elif tag == "interactive":
            # Semicolon-separated answers fed to input() by the verification runner.
            metadata["interactive_input"] = [a.strip() for a in value.split(";") if a.strip()]

        cell = {
            "cell_type": "markdown" if kind == "md" else "code",
            "id": f"cell{index:03d}",
            "metadata": metadata,
            "source": source.splitlines(keepends=True),
        }
        if kind == "code":
            cell["execution_count"] = None
            cell["outputs"] = []
        out.append(cell)

    return {
        "cells": out,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.12"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def write_notebook(cells, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(build(cells), ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )
    code = sum(1 for c in cells if c[0] == "code")
    print(f"✅ {str(target.relative_to(ROOT)):<42} {len(cells):>3} cells "
          f"({code} code, {len(cells) - code} md)")


def build_solutions():
    """Split solutions_source.py into one source and one notebook per day."""
    if not SOLUTIONS_SOURCE.exists():
        return 0

    chunks = SOLUTION_MARKER.split(SOLUTIONS_SOURCE.read_text(encoding="utf-8"))
    days = {}
    for index in range(1, len(chunks), 3):
        day, kind, body = chunks[index], chunks[index + 1], chunks[index + 2]
        days.setdefault(day, []).append(f"#%% {kind}\n{body.strip()}\n")

    (SRC / "solutions").mkdir(exist_ok=True)
    for day, cell_sources in sorted(days.items()):
        text = "\n".join(cell_sources)
        (SRC / "solutions" / f"{day}.py").write_text(text, encoding="utf-8")
        write_notebook(parse(text), ROOT / "solutions" / f"{day}.ipynb")

    return len(days)


def prune(folder, expected):
    """
    Delete generated notebooks whose source no longer exists.

    Without this, renaming a source leaves the old notebook behind and the checkers
    happily verify a file nobody can reach from CURRICULUM.md. That is worse than a
    missing file, because it looks fine.
    """
    removed = []
    for path in sorted((ROOT / folder).glob("*.ipynb")):
        if path.stem not in expected:
            path.unlink()
            removed.append(path.stem)
    return removed


def main(argv):
    wanted = argv[1] if len(argv) > 1 else None

    # Only the dayNN sources become notebooks. solutions_source.py is split by
    # build_solutions() instead.
    sources = sorted(SRC.glob("day*.py"))
    if wanted:
        sources = [s for s in sources if s.stem.startswith(wanted)]
    if not sources:
        print(f"❌ No sources found in {SRC}" + (f" matching '{wanted}'" if wanted else ""))
        return 1

    OUT.mkdir(exist_ok=True)
    for source in sources:
        write_notebook(parse(source.read_text(encoding="utf-8")), OUT / f"{source.stem}.ipynb")

    # Building one notebook by name does not rebuild everything else.
    if wanted:
        return 0

    solutions = build_solutions()

    # Remove anything generated by an earlier run whose source has since been renamed
    # or deleted. Only runs on a full build, so `nbbuild.py day07` cannot prune.
    stale = (
        prune("notebooks", {p.stem for p in sources})
        + prune("solutions", {p.stem for p in (SRC / "solutions").glob("*.py")})
    )
    for name in stale:
        print(f"🗑  removed {name}.ipynb — no source any more")

    print()
    print(f"✅ {len(sources)} notebooks, {solutions} solutions")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
