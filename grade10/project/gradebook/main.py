"""
Register - a program for teachers.

Run it like this:
    python main.py

This file does no calculating of its own and reads no files. It asks the
teacher what they want, and then asks the other files to do the work.
"""

import grades
import settings
import storage


def show_register(class_grades):
    """Print the whole register."""
    if not class_grades:
        print("The class is empty.")
        return

    print()
    print("=== REGISTER ===")

    for student_name, grade in class_grades.items():
        if grades.has_passed(grade):
            result = "passed"
        else:
            result = "failed"
        print(f"{student_name:<{settings.NAME_WIDTH}} {grade:>3}   {result}")

    print()
    print(f"students:      {len(class_grades)}")
    print(f"class average: {grades.class_average(class_grades)}")


def show_failing(class_grades):
    """Print only the students who did not pass."""
    failing = grades.failing_students(class_grades)

    print()
    if not failing:
        print("Everyone passed.")
        return

    print(f"Did not pass ({len(failing)} students):")
    for student_name in failing:
        print(f" - {student_name}: {class_grades[student_name]}")


def add_grade(class_grades):
    """Ask for a name and a grade, then add or correct it."""
    student_name = input("Student name: ").strip()
    if not student_name:
        print("The name is empty - nothing was added.")
        return

    answer = input("Grade (1-10): ").strip()
    if not answer.isdigit():
        print("That is not a number - nothing was added.")
        return

    grade = int(answer)
    if grade < 1 or grade > 10:
        print("The grade must be between 1 and 10 - nothing was added.")
        return

    if student_name in class_grades:
        print(f"{student_name}: changed from {class_grades[student_name]} to {grade}")
    else:
        print(f"{student_name} added.")

    class_grades[student_name] = grade


def show_menu():
    print()
    print("1 - show the register")
    print("2 - show who did not pass")
    print("3 - add or correct a grade")
    print("4 - save")
    print("5 - quit")


def main():
    class_grades = storage.load_class()
    print(f"Opened {settings.CLASS_FILE} - {len(class_grades)} students")

    while True:
        show_menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            show_register(class_grades)
        elif choice == "2":
            show_failing(class_grades)
        elif choice == "3":
            add_grade(class_grades)
        elif choice == "4":
            storage.save_class(class_grades)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("No such command. Type a number from 1 to 5.")


if __name__ == "__main__":
    # One try/except in the whole program, at the very outside.
    # If something unexpected happens, the teacher sees a sentence they can
    # act on instead of ten lines of red text.
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Interrupted. Goodbye.")
    except Exception as error:
        print()
        print(f"Unexpected error: {type(error).__name__}: {error}")
        print("Show this line to your instructor.")
