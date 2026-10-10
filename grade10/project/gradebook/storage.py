"""
Read the class from a file and write it back.

This file knows nothing about grades. To it they are just numbers.

The file format is:
    name,grade
    Ani,9
    Davit,6
"""

from pathlib import Path

import grades


def load_class(file_name=grades.CLASS_FILE):
    """
    Read the file and return a dictionary, like {"Ani": 9}.

    If the file is missing, say so and return an empty dictionary - the
    program keeps running instead of stopping with a traceback.
    """
    path = Path(file_name)

    if not path.exists():
        print(f"Could not find {file_name}")
        print("Check that it exists, and that the name in grades.py is right.")
        return {}

    # encoding="utf-8" is required: your own class file will have Armenian
    # names in it, and without this they come back broken.
    lines = path.read_text(encoding="utf-8").strip().splitlines()

    class_grades = {}

    # The first line is the header (name,grade), so start from the second.
    for line in lines[1:]:
        if not line.strip():
            continue

        parts = line.split(",")
        if len(parts) != 2:
            print(f"Skipped this line - it does not have exactly one comma: {line}")
            continue

        student_name = parts[0].strip()
        grade_text = parts[1].strip()

        if not grade_text.isdigit():
            print(f"Skipped {student_name} - '{grade_text}' is not a number.")
            continue

        class_grades[student_name] = int(grade_text)

    return class_grades


def save_class(class_grades, file_name=grades.CLASS_FILE):
    """Write the dictionary back to the file, in the same format."""
    path = Path(file_name)
    path.parent.mkdir(parents=True, exist_ok=True)

    lines = ["name,grade"]
    for student_name, grade in class_grades.items():
        lines.append(f"{student_name},{grade}")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Saved {file_name} ({len(class_grades)} students)")


if __name__ == "__main__":
    print("Checking storage.py")
    loaded = load_class()
    print(f"read {len(loaded)} students")
    print(loaded)
