"""Run the term report.

    python main.py

Reads data/school.csv, prints the summary, and writes two charts into output/.
"""

import sys

import settings
from charts import save_distribution_chart, save_subject_chart
from loading import build_school


def print_summary(school):
    at_risk = school.at_risk()

    print(f"{school.name} — {settings.TERM}")
    print("=" * 46)
    print(f"classes:        {len(school.classes):>5}")
    print(f"students:      {school.size():>6}")
    print(f"school average: {school.average():>5.1f}")
    print()

    print("Classes")
    print("-" * 46)
    for school_class in school.classes:
        print(f"  {school_class.name:<6} {school_class.size():>3} students"
              f"   average {school_class.average():>5.2f}")
    print()

    print("Subjects")
    print("-" * 46)
    averages = school.subject_averages()
    for subject in sorted(averages, key=averages.get, reverse=True):
        print(f"  {subject:<16} {averages[subject]:>5.2f}")
    print()

    print(f"At risk ({len(at_risk)} students)")
    print("-" * 46)
    for student in sorted(at_risk, key=lambda s: len(s.failed_subjects()),
                          reverse=True):
        failed = ", ".join(student.failed_subjects())
        print(f"  {student.name:<22} {student.class_name}  {failed}")


def main():
    try:
        school = build_school()
    except FileNotFoundError:
        print(f"Could not find {settings.DATA_FILE}")
        print("Put your class list there, or change DATA_FILE in settings.py.")
        return 1
    except ValueError as problem:
        print(f"The file is not in the expected shape: {problem}")
        return 1

    print_summary(school)

    settings.OUTPUT_DIR.mkdir(exist_ok=True)
    save_subject_chart(school, settings.OUTPUT_DIR / "subjects.png")
    save_distribution_chart(school, settings.OUTPUT_DIR / "distribution.png")

    print()
    print(f"Charts written to {settings.OUTPUT_DIR.name}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
