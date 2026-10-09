"""Read the school's file and turn it into objects.

This is the only file that knows the CSV exists. Everything else works with
Student, SchoolClass and School -- so when the ministry changes the file format,
this is the one file that changes.
"""

import pandas as pd

import settings
from people import School, SchoolClass, Student

REQUIRED_COLUMNS = ["class", "student", "subject", "grade"]


def read_table(path=None):
    """The raw file, checked. Raises if it is not the file we expect."""
    if path is None:
        path = settings.DATA_FILE

    data = pd.read_csv(path)

    missing = [name for name in REQUIRED_COLUMNS if name not in data.columns]
    if missing:
        raise ValueError(f"{path} is missing column(s): {', '.join(missing)}")

    # A boolean column counted with sum(), exactly as on day 13.
    outside = (data["grade"] < settings.LOWEST_GRADE) | \
              (data["grade"] > settings.HIGHEST_GRADE)
    if outside.sum() > 0:
        raise ValueError(f"{outside.sum()} grade(s) outside "
                         f"{settings.LOWEST_GRADE}-{settings.HIGHEST_GRADE}")

    return data


def build_school(path=None):
    """The file, as a School full of SchoolClasses full of Students."""
    data = read_table(path)
    school = School(settings.SCHOOL_NAME)

    for class_name in sorted(data["class"].unique()):
        rows = data[data["class"] == class_name]
        school_class = SchoolClass(class_name)

        for student_name in sorted(rows["student"].unique()):
            marks = rows[rows["student"] == student_name]
            subjects = marks["subject"].tolist()
            values = marks["grade"].tolist()
            grades = {}
            for position in range(len(subjects)):
                grades[subjects[position]] = int(values[position])
            school_class.add(Student(student_name, class_name, grades))

        school.add(school_class)

    return school
