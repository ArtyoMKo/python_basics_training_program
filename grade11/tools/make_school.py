"""
Generate data/school.csv -- the sample school every example in this course uses.

The numbers are ENGINEERED, not random, because prose throughout the course quotes
them (docs/PLAN.md section 11.6). The search below looks for a school that hits every
target exactly; the seed that found it is recorded so the file is reproducible.

    python tools/make_school.py            # regenerate and report
    python tools/make_school.py --check    # fail if the file does not match the targets

If you change a target, you must grep the whole course for the number that was true
before -- see AGENTS.md, "Numbers that are load-bearing".
"""

import csv
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "school.csv"

CLASSES = ["11Ա", "11Բ", "11Գ"]
SUBJECTS = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]
PASS_MARK = 4

FIRST = [
    "Ani", "Davit", "Nare", "Aram", "Mariam", "Tigran", "Lilit", "Gor", "Anahit", "Hayk",
    "Sona", "Vahe", "Armen", "Nune", "Karen", "Syuzan", "Levon", "Gayane", "Artur",
    "Mane", "Narek", "Lusine", "Vardan", "Satenik", "Grigor", "Astghik", "Suren",
    "Zaruhi", "Hovhannes", "Ruzan", "Samvel", "Hasmik", "Arsen", "Knarik", "Edgar",
    "Siranush",
]
LAST = [
    "Hakobyan", "Grigoryan", "Sargsyan", "Petrosyan", "Harutyunyan", "Khachatryan",
    "Mkrtchyan", "Vardanyan", "Avetisyan", "Martirosyan", "Gevorgyan", "Hovhannisyan",
]
NAMES = [f"{FIRST[i]} {LAST[i % len(LAST)]}" for i in range(36)]

# Every target the course's prose depends on.
TARGETS = {
    "students": 36,
    "grades": 180,
    "total": 1260,          # => school average exactly 7.0
    "failing_grades": 18,   # => exactly 10% of all grades
    "students_at_risk": 12, # => exactly one third of the school
    "top_subject": "Informatics",
    "bottom_subject": "Physics",
}


def build(seed):
    """One candidate school, constructed then repaired. None if it cannot be made."""
    rng = random.Random(seed)
    # Subject difficulty, so the bar chart on day 14 has something to show.
    bias = {"Mathematics": 0, "Physics": -1, "Armenian": 0, "History": 0, "Informatics": 1}

    # 1. Twelve students carry every failing grade: six with two, six with one.
    #    Spread across all three classes so no class looks artificially clean.
    at_risk = [i for i in range(36) if i % 3 == 0][:12]
    failing_slots = set()
    for position, student in enumerate(at_risk):
        for subject in rng.sample(SUBJECTS, 2 if position < 6 else 1):
            failing_slots.add((student, subject))

    # 2. Everyone else is at or above the pass mark.
    rows = []
    for index, name in enumerate(NAMES):
        ability = rng.choice([5, 6, 6, 7, 7, 8, 8, 9, 9, 10])
        for subject in SUBJECTS:
            if (index, subject) in failing_slots:
                grade = rng.choice([1, 2, 3])
            else:
                grade = max(4, min(10, ability + bias[subject] + rng.choice([-1, 0, 0, 1])))
            rows.append([CLASSES[index // 12], name, subject, grade, ""])

    # 3. Repair the total to exactly 1260 by nudging passing grades one step at a time.
    #    A grade never crosses the pass mark here, so steps 1 and 2 stay true.
    movable = [i for i, r in enumerate(rows) if r[3] >= PASS_MARK]
    for _ in range(20000):
        difference = TARGETS["total"] - sum(r[3] for r in rows)
        if difference == 0:
            break
        step = 1 if difference > 0 else -1
        index = rng.choice(movable)
        if PASS_MARK <= rows[index][3] + step <= 10:
            rows[index][3] += step
    else:
        return None
    if sum(r[3] for r in rows) != TARGETS["total"]:
        return None

    grades = [r[3] for r in rows]
    if sum(1 for g in grades if g < PASS_MARK) != TARGETS["failing_grades"]:
        return None
    if len({r[1] for r in rows if r[3] < PASS_MARK}) != TARGETS["students_at_risk"]:
        return None

    averages = {s: sum(r[3] for r in rows if r[2] == s) / 36 for s in SUBJECTS}
    if max(averages, key=averages.get) != TARGETS["top_subject"]:
        return None
    if min(averages, key=averages.get) != TARGETS["bottom_subject"]:
        return None
    # Distinct subject averages, so a bar chart has five visibly different bars.
    if len({round(v, 2) for v in averages.values()}) != len(SUBJECTS):
        return None
    return rows, averages


def report(rows, averages):
    grades = [r[3] for r in rows]
    print(f"   students            {len({r[1] for r in rows})}")
    print(f"   grades              {len(grades)}")
    print(f"   total               {sum(grades)}")
    print(f"   school average      {sum(grades) / len(grades):.1f}")
    print(f"   failing grades      {sum(1 for g in grades if g < PASS_MARK)}"
          f"  ({sum(1 for g in grades if g < PASS_MARK) * 100 // len(grades)}%)")
    print(f"   students at risk    {len({r[1] for r in rows if r[3] < PASS_MARK})}")
    for subject in SUBJECTS:
        print(f"   {subject:<20}{averages[subject]:.2f}")
    for name in CLASSES:
        marks = [r[3] for r in rows if r[0] == name]
        print(f"   class {name:<14}{sum(marks) / len(marks):.2f}")


def check():
    """Fail if data/school.csv no longer matches the targets the course prose quotes."""
    if not OUT.exists():
        print("❌ data/school.csv is missing -- run python tools/make_school.py")
        return 1
    rows = list(csv.reader(OUT.open(encoding="utf-8")))[1:]
    rows = [r for r in rows if r]
    grades = [int(r[3]) for r in rows]
    problems = []
    if len({r[1] for r in rows}) != TARGETS["students"]:
        problems.append(f"{len({r[1] for r in rows})} students, not {TARGETS['students']}")
    if len(grades) != TARGETS["grades"]:
        problems.append(f"{len(grades)} grades, not {TARGETS['grades']}")
    if sum(grades) != TARGETS["total"]:
        problems.append(f"total {sum(grades)}, not {TARGETS['total']} (average is not 7.0)")
    if sum(1 for g in grades if g < PASS_MARK) != TARGETS["failing_grades"]:
        problems.append(f"{sum(1 for g in grades if g < PASS_MARK)} failing grades, "
                        f"not {TARGETS['failing_grades']}")
    at_risk = len({r[1] for r in rows if int(r[3]) < PASS_MARK})
    if at_risk != TARGETS["students_at_risk"]:
        problems.append(f"{at_risk} students at risk, not {TARGETS['students_at_risk']}")
    averages = {s: sum(int(r[3]) for r in rows if r[2] == s) / TARGETS["students"]
                for s in SUBJECTS}
    if max(averages, key=averages.get) != TARGETS["top_subject"]:
        problems.append(f"top subject is {max(averages, key=averages.get)}, "
                        f"not {TARGETS['top_subject']}")
    if min(averages, key=averages.get) != TARGETS["bottom_subject"]:
        problems.append(f"bottom subject is {min(averages, key=averages.get)}, "
                        f"not {TARGETS['bottom_subject']}")
    if problems:
        print("❌ data/school.csv no longer matches the course prose:\n")
        for problem in problems:
            print(f"   {problem}")
        print("\n   Either regenerate it, or grep the course for the number that changed.")
        return 1
    print(f"✅ sample school: 36 students, 180 grades, average 7.0, 18 failing, 12 at risk")
    return 0


def main():
    if "--check" in sys.argv:
        return check()
    for seed in range(400000):
        found = build(seed)
        if found:
            rows, averages = found
            break
    else:
        print("❌ no school hit every target; widen the search or move a target")
        return 1

    # Day 16 needs three things a hand-written split(",") gets wrong: a header, a blank
    # line, and a field containing a comma. Each is here exactly once, on purpose.
    rows[41][4] = "absent, retake scheduled"

    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["class", "student", "subject", "grade", "note"])
        for index, row in enumerate(rows):
            writer.writerow(row)
            if index == 89:
                handle.write("\n")       # the blank line, halfway down

    # Participants receive a flat folder, so the notebooks refer to "school.csv" with no
    # path (AGENTS.md, "Where things live"). Keep the copy beside them in step.
    beside = ROOT / "notebooks" / "school.csv"
    if beside.parent.exists():
        beside.write_bytes(OUT.read_bytes())

    print(f"✅ data/school.csv  (seed {seed})")
    report(rows, averages)
    return 0


if __name__ == "__main__":
    sys.exit(main())
