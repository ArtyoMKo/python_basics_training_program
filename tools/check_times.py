"""
Verify the time arithmetic in CURRICULUM.md.

Every agenda table must sum to exactly 50 minutes, the standard shape must sum to 50,
and 24 days must total 1,200 minutes. Run this after every edit to the curriculum.

    python tools/check_times.py
"""

import re
import sys
from pathlib import Path

LESSON_MINUTES = 50
TOTAL_DAYS = 24

CURRICULUM = Path(__file__).resolve().parent.parent / "CURRICULUM.md"

# A row of an agenda table: exactly three columns -- | 3 | activity text | 12 |
# The five-column day index at the top of the file deliberately does not match.
AGENDA_ROW = re.compile(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*$", re.M)

# The heading above each bespoke agenda, so a failure names the day
DAY_HEADING = re.compile(r"^## Day (\d+) — (.+?)(?:\s+⟵.*)?$", re.M)


def agenda_blocks(text):
    """Yield (label, block_text) for every agenda table in the document."""
    headings = [(m.start(), m.group(1), m.group(2)) for m in DAY_HEADING.finditer(text)]

    # The standard shape lives above the first day heading.
    first = headings[0][0] if headings else len(text)
    yield "the standard shape", text[:first]

    for index, (start, number, title) in enumerate(headings):
        end = headings[index + 1][0] if index + 1 < len(headings) else len(text)
        yield f"Day {number} ({title})", text[start:end]


def main():
    text = CURRICULUM.read_text(encoding="utf-8")
    problems = []
    checked = 0

    for label, block in agenda_blocks(text):
        rows = AGENDA_ROW.findall(block)
        if not rows:
            continue  # a day on the standard shape has no table of its own
        total = sum(int(minutes) for _, _, minutes in rows)
        checked += 1
        if total != LESSON_MINUTES:
            listed = ", ".join(f"{n}={m}" for n, _, m in rows)
            problems.append(f"{label}: activities sum to {total}, not {LESSON_MINUTES}  [{listed}]")

    # The day index table at the top must list 24 days, each of 50 minutes.
    index_rows = re.findall(r"^\|\s*(\d+)\s*\|\s*[^|]+\|[^|]+\|[^|]+\|\s*(\d+)\s*\|\s*$", text, re.M)
    day_numbers = [int(n) for n, _ in index_rows]
    day_minutes = [int(m) for _, m in index_rows]

    if day_numbers != list(range(1, TOTAL_DAYS + 1)):
        problems.append(f"the day index lists {day_numbers}, not 1..{TOTAL_DAYS}")
    if any(m != LESSON_MINUTES for m in day_minutes):
        problems.append(f"the day index has a day that is not {LESSON_MINUTES} minutes")
    if sum(day_minutes) != TOTAL_DAYS * LESSON_MINUTES:
        problems.append(f"the day index totals {sum(day_minutes)}, not {TOTAL_DAYS * LESSON_MINUTES}")

    if problems:
        print("❌ CURRICULUM.md time check failed:\n")
        for problem in problems:
            print(f"   {problem}")
        return 1

    print(f"✅ {checked} agenda tables, each summing to {LESSON_MINUTES}")
    print(f"✅ {len(day_numbers)} days listed, {sum(day_minutes)} minutes "
          f"= {sum(day_minutes) // 60} hours")
    return 0


if __name__ == "__main__":
    sys.exit(main())
