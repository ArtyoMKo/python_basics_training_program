"""
Verify the time arithmetic in CURRICULUM.md.

Every agenda table must sum to exactly 50 minutes, and 24 days must total 1,200.
Run this after every edit to the curriculum.

    python tools/check_times.py
"""

import re
import sys
from pathlib import Path

LESSON_MINUTES = 50
TOTAL_DAYS = 24

CURRICULUM = Path(__file__).resolve().parent.parent / "CURRICULUM.md"

# An agenda row has exactly three columns: | 3 | activity text | 12 |
# The five-column day index at the top of the file deliberately does not match.
AGENDA_ROW = re.compile(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*$")

# A day index row: | 7 | title | phase | file | 50 |
INDEX_ROW = re.compile(r"^\|\s*(\d+)\s*\|[^|]+\|[^|]+\|[^|]+\|\s*(\d+)\s*\|\s*$")


def tables(lines):
    """Yield (first_line_number, [lines]) for each run of consecutive table lines."""
    run, start = [], 0
    for number, line in enumerate(lines, start=1):
        if line.lstrip().startswith("|"):
            if not run:
                start = number
            run.append(line)
        elif run:
            yield start, run
            run = []
    if run:
        yield start, run


def label_for(lines, table_start):
    """The nearest heading above this table, so a failure names the day."""
    for number in range(table_start - 1, 0, -1):
        match = re.match(r"^##+ (.+?)(?:\s+⟵.*)?$", lines[number - 1])
        if match:
            return match.group(1).strip()
    return f"the table at line {table_start}"


def main():
    lines = CURRICULUM.read_text(encoding="utf-8").splitlines()
    problems = []
    agendas = 0

    for start, block in tables(lines):
        rows = [AGENDA_ROW.match(line) for line in block]
        rows = [m for m in rows if m]
        if len(rows) < 3:
            continue  # not an agenda -- a two-row reference table, or the day index

        total = sum(int(m.group(3)) for m in rows)
        agendas += 1
        if total != LESSON_MINUTES:
            listed = ", ".join(f"{m.group(1)}={m.group(3)}" for m in rows)
            problems.append(
                f"{label_for(lines, start)} (line {start}): "
                f"sums to {total}, not {LESSON_MINUTES}  [{listed}]"
            )

    # The day index: 24 rows, each 50 minutes.
    index = [INDEX_ROW.match(line) for line in lines]
    index = [m for m in index if m]
    numbers = [int(m.group(1)) for m in index]
    minutes = [int(m.group(2)) for m in index]

    if numbers != list(range(1, TOTAL_DAYS + 1)):
        problems.append(f"the day index lists {numbers}, not 1..{TOTAL_DAYS}")
    if any(m != LESSON_MINUTES for m in minutes):
        problems.append(f"the day index has a day that is not {LESSON_MINUTES} minutes")
    if sum(minutes) != TOTAL_DAYS * LESSON_MINUTES:
        problems.append(f"the day index totals {sum(minutes)}, not {TOTAL_DAYS * LESSON_MINUTES}")

    if problems:
        print("❌ CURRICULUM.md time check failed:\n")
        for problem in problems:
            print(f"   {problem}")
        return 1

    print(f"✅ {agendas} agenda tables, each summing to {LESSON_MINUTES}")
    print(f"✅ {len(numbers)} days listed, {sum(minutes)} minutes "
          f"= {sum(minutes) // 60} hours")
    return 0


if __name__ == "__main__":
    sys.exit(main())
