"""
Build notebooks/*.ipynb from the plain-text sources in src/.

WHY THIS EXISTS. Nineteen notebooks are 19 large JSON files. Editing Armenian prose
inside JSON string arrays is unreviewable and error-prone, and the participant-facing
simplicity rule (PLAN.md section 0) says nothing about how we author the material. So the
source of truth is a readable text file per day, and the .ipynb is generated.

    python tools/nbbuild.py            # build everything
    python tools/nbbuild.py day03      # build one

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

MARKER = re.compile(r"^#%%\s+(md|code)(?:\s+(expected-error|interactive):\s*(.*))?\s*$")


def parse(text):
    """Turn one source file into a list of (kind, tag, tag_value, source) cells."""
    cells = []
    kind = tag = value = None
    body = []

    for line in text.splitlines():
        match = MARKER.match(line)
        if match:
            if kind is not None:
                cells.append((kind, tag, value, "\n".join(body).strip("\n")))
            kind, tag, value = match.group(1), match.group(2), match.group(3)
            body = []
        elif kind is not None:
            body.append(line)

    if kind is not None:
        cells.append((kind, tag, value, "\n".join(body).strip("\n")))

    return [cell for cell in cells if cell[3].strip()]


def build(cells):
    out = []
    for index, (kind, tag, value, source) in enumerate(cells):
        metadata = {}
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


def main(argv):
    wanted = argv[1] if len(argv) > 1 else None
    sources = sorted(SRC.glob("*.py"))
    if wanted:
        sources = [s for s in sources if s.stem.startswith(wanted)]
    if not sources:
        print(f"❌ No sources found in {SRC}" + (f" matching '{wanted}'" if wanted else ""))
        return 1

    OUT.mkdir(exist_ok=True)
    for source in sources:
        cells = parse(source.read_text(encoding="utf-8"))
        target = OUT / f"{source.stem}.ipynb"
        target.write_text(
            json.dumps(build(cells), ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
        )
        code = sum(1 for c in cells if c[0] == "code")
        print(f"✅ {target.name:<34} {len(cells):>3} cells ({code} code, {len(cells) - code} md)")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
