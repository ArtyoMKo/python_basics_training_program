"""
Enforce the rules in docs/PLAN.md that a human reviewer would have to check by eye.

    python tools/check_style.py

Checks, in order:
  1. Only the three Anaconda-bundled libraries are imported (docs/PLAN.md section 5).
  2. None of the excluded constructs appear in participant-facing code.
  3. Every Armenian term used in a notebook comes from handouts/CHEATSHEET.md's glossary.
  4. Every notebook has the four retrospective sections.
  5. Every notebook has exactly one deliberate-error cell (days 6, 9, 15 excepted).
  6. Identifiers in code cells are English; example string values may be Armenian.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKS = ROOT / "notebooks"
PROJECT = ROOT / "project" / "school_report"

# Modules the course is allowed to import.
#
# This is where grade 11 departs from grade 10, which allowed no third-party import at
# all. numpy, matplotlib and pandas are state topics 15, 20 and 21 -- a teacher has to
# demonstrate them -- and Anaconda already ships all three, so no participant installs
# anything to follow the course. Nothing else is allowed in: Anaconda ships 300 packages
# and the other 297 are not on the pupils' syllabus.
# The standard library in full: day 20 is a session about where code comes from, and
# names several of its modules on purpose.
ALLOWED_IMPORTS = set(sys.stdlib_module_names) | {
    # the three Anaconda ships, which is where this course departs from grade 10
    "numpy", "matplotlib", "pandas",
    # our own modules, from day 22
    "settings", "people", "loading", "charts",
}

# Constructs excluded by docs/PLAN.md section 5. Each is a (regex, why) pair.
# Constructs excluded by docs/PLAN.md section 5.
#
# Classes, comprehensions, lambda and *args are all TAUGHT here -- they are state topics
# 16, 18 and 19 -- so grade 10's entries for them are gone. What remains is the layer
# above: the things a teacher does not need in order to teach grade 11, and that would
# cost a session each.
FORBIDDEN = [
    (r"(?m)^\s*@\w+", "decorators are excluded (docs/PLAN.md section 5)"),
    (r"(?m)^\s*yield\b", "generators are excluded"),
    (r"(?m)^\s*(async|await)\b", "async is excluded"),
    (r"(?m)^\s*from\s+dataclasses\b|@dataclass", "dataclasses are excluded"),
    (r"(?m)^\s*from\s+abc\b|\bABC\b|@abstractmethod", "abstract base classes are excluded"),
    (r"__slots__", "__slots__ is excluded"),
    (r"(?m)^\s*class\s+\w+\s*\(\s*\w+\s*,\s*\w+", "multiple inheritance is excluded"),
    (r"(?m)^\s*class\s+\w+\s*\((Exception|ValueError|KeyError)\)",
     "custom exception classes are excluded"),
    (r"\bimport\s+(sklearn|torch|tensorflow|seaborn|scipy|requests)",
     "only numpy, matplotlib and pandas -- the three Anaconda ships"),
    (r"(?m)^\s*import\s+re\b", "regular expressions are excluded"),
    (r"\)\s*->\s*(int|str|float|bool|list|dict)\b", "type hints are excluded"),
    (r"\b(factorial|fibonacci)\b", "factorial and Fibonacci are Part 2, not this course"),
]

# The retrospective sections every notebook must carry.
REQUIRED_SECTIONS = ["## Ինչի հասանք", "## Հաջորդ անգամ"]

# Days that deliberately have no break-it-on-purpose cell, and why.
NO_ERROR_CELL = {
    "day01": "setup and recap -- nothing new to break yet",
    "day03": "no new error class introduced",
    "day05": "no new error class introduced",
    "day08": "no new error class introduced",
    "day10": "no new error class introduced",
    "day11": "consolidation day -- no new syntax, so no new error",
    "day13": "no new error class introduced",
    "day15": "no new error class introduced",
    "day17": "no new error class introduced",
    "day18": "no new library -- pandas and Matplotlib together",
    "day20": "the pip session is hands-on, not a notebook error",
    "day21": "THE WHOLE DAY is errors; a single marked cell would understate it",
}

# Armenian words that are allowed to appear outside the glossary: they are ordinary
# prose, names, or classroom vocabulary rather than technical terms.
PROSE_ALLOWED = re.compile(r"^[԰-֏Ա-Ֆ]+$")


def code_cells(path):
    notebook = json.loads(path.read_text(encoding="utf-8"))
    for index, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] == "code":
            yield index, "".join(cell["source"]), cell.get("metadata", {})


def markdown_text(path):
    notebook = json.loads(path.read_text(encoding="utf-8"))
    return "\n".join(
        "".join(c["source"]) for c in notebook["cells"] if c["cell_type"] == "markdown"
    )


def main():
    problems = []

    # --- 1 and 2: imports and forbidden constructs, notebooks and project alike ---
    sources = sorted(NOTEBOOKS.glob("*.ipynb"))
    solutions = sorted((ROOT / "solutions").glob("*.ipynb"))
    tests = sorted((ROOT / "tests").rglob("*.ipynb"))
    for path in sources + solutions + tests:
        for index, source, _ in code_cells(path):
            for module in re.findall(r"^\s*(?:import|from)\s+([\w.]+)", source, re.M):
                root = module.split(".")[0]
                if root not in ALLOWED_IMPORTS:
                    problems.append(f"{path.name} cell {index}: imports '{root}'")
            for pattern, why in FORBIDDEN:
                if re.search(pattern, source):
                    problems.append(f"{path.name} cell {index}: {why}")

    for path in sorted(PROJECT.glob("*.py")):
        source = path.read_text(encoding="utf-8")
        for module in re.findall(r"^\s*(?:import|from)\s+([\w.]+)", source, re.M):
            root = module.split(".")[0]
            if root not in ALLOWED_IMPORTS:
                problems.append(f"project/{path.name}: imports '{root}'")
        for pattern, why in FORBIDDEN:
            if re.search(pattern, source):
                problems.append(f"project/{path.name}: {why}")

    # --- 3: every notebook has the retrospective sections ---
    for path in sources:
        text = markdown_text(path)
        for section in REQUIRED_SECTIONS:
            if section not in text:
                problems.append(f"{path.name}: missing section '{section}'")

    # --- 4: deliberate-error cells ---
    for path in sources:
        day = path.stem.split("_")[0]
        has_error = any(meta.get("expected_error") for _, _, meta in code_cells(path))
        if has_error and day in NO_ERROR_CELL:
            problems.append(f"{path.name}: has a break-it cell but is listed as exempt")
        if not has_error and day not in NO_ERROR_CELL:
            problems.append(f"{path.name}: no break-it-on-purpose cell and not exempt")

    # --- 5: NOTHING inside a code cell may be Armenian (docs/PLAN.md section 7.7).
    # Not identifiers, not comments, not string values. Armenian lives in markdown only,
    # including in the exams: the instruction is Armenian in the cell above, and the
    # placeholder inside the cell matches the English the participant has typed all course.
    armenian = re.compile(r"[\u0530-\u058F]")
    for path in sources + solutions + tests:
        for index, source, meta in code_cells(path):
            match = armenian.search(source)
            if match:
                line_number = source[:match.start()].count("\n") + 1
                snippet = source.splitlines()[line_number - 1].strip()
                problems.append(
                    f"{path.relative_to(ROOT)} cell {index} line {line_number}: "
                    f"Armenian inside a code cell -> {snippet[:55]!r}"
                )

    if problems:
        print(f"❌ {len(problems)} style problem(s):\n")
        for problem in problems:
            print(f"   {problem}")
        return 1

    print(f"✅ {len(sources)} notebooks + {len(solutions)} solutions + {len(tests)} tests "
          f"+ {len(list(PROJECT.glob('*.py')))} project files")
    print("✅ numpy, matplotlib and pandas only; no excluded constructs")
    print("✅ every notebook has its retrospective sections")
    print("✅ break-it-on-purpose cells present where required")
    print("✅ no Armenian anywhere inside a code cell")
    return 0


if __name__ == "__main__":
    sys.exit(main())
