"""
The calculations: average, highest, passed or not.

This file knows nothing about files and nothing about printing. It only
calculates.

That is deliberate: it means you can test the calculations without having a
data file at all. Run this file on its own and you will see.
"""

import settings


def average_of(grades):
    """
    Return the average of a list of grades, rounded.

    Expects a list, like [9, 6, 10]. An empty list returns 0, because dividing
    by zero would stop the program.
    """
    if not grades:
        return 0

    total = 0
    for grade in grades:
        total = total + grade

    return round(total / len(grades), settings.DECIMAL_PLACES)


def has_passed(grade, pass_mark=settings.PASS_MARK):
    """Return True if this grade is a pass."""
    return grade >= pass_mark


def highest_of(class_grades):
    """
    Return the name of the student with the highest grade.

    Expects a dictionary, like {"Ani": 9}. An empty class returns "".
    If several students share the highest grade, the first one is returned.
    """
    best_name = ""
    best_grade = -1

    for student_name, grade in class_grades.items():
        if grade > best_grade:
            best_grade = grade
            best_name = student_name

    return best_name


def failing_students(class_grades, pass_mark=settings.PASS_MARK):
    """Return a list of the names of the students who did not pass."""
    failing = []

    for student_name, grade in class_grades.items():
        if grade < pass_mark:
            failing.append(student_name)

    return failing


def class_average(class_grades):
    """Return the average grade of the whole class."""
    return average_of(list(class_grades.values()))


if __name__ == "__main__":
    # This part only runs when you run this file directly:
    #     python grades.py
    # When main.py imports this file, these lines do not run.
    test_class = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3}

    print("Checking grades.py")
    print("class average:", class_average(test_class))
    print("highest:      ", highest_of(test_class))
    print("failing:      ", failing_students(test_class))
