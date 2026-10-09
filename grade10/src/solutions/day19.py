#%% md
# Թեմա 19 — Լուծումներ

**Սա ամբողջական ծրագիրն է։** 20-րդ և 21-րդ թեմաներին այն բաժանվում է չորս ֆայլի։

#%% code
# The whole assembled register program

PASS_MARK = 4
DECIMAL_PLACES = 1
NAME_WIDTH = 12

class_grades = {
    "Ani": [9, 10, 8],
    "Davit": [6, 5, 7],
    "Nare": [10, 10, 9],
    "Aram": [3, 4, 2],
    "Mariam": [8, 8, 9],
    "Tigran": [5, 6, 5],
}


def average_of(grades):
    """Return the average of a list of grades."""
    if not grades:
        return 0
    total = 0
    for grade in grades:
        total = total + grade
    return round(total / len(grades), DECIMAL_PLACES)


def has_passed(grades, pass_mark=PASS_MARK):
    """Return True if this student's average is a pass."""
    return average_of(grades) >= pass_mark


def failing_students(class_grades):
    """Return the names of the students who did not pass."""
    failing = []
    for student_name, grades in class_grades.items():
        if not has_passed(grades):
            failing.append(student_name)
    return failing


def class_average(class_grades):
    """Return the average of every student's average."""
    all_averages = []
    for student_name, grades in class_grades.items():
        all_averages.append(average_of(grades))
    return average_of(all_averages)


def print_register(class_grades):
    """Print the whole register, one line per student."""
    print()
    print("=== REGISTER ===")
    for student_name, grades in class_grades.items():
        if has_passed(grades):
            result = "passed"
        else:
            result = "failed"
        print(f"{student_name:<{NAME_WIDTH}} {str(grades):<14} "
              f"{average_of(grades):>5}   {result}")
    print()
    print(f"students:      {len(class_grades)}")
    print(f"class average: {class_average(class_grades)}")
    print(f"did not pass:  {len(failing_students(class_grades))}")


print_register(class_grades)

#%% code
# Extra 8 - removing a student, guarded with in

def remove_student(class_grades, student_name):
    """Remove one student. Says so if there is no such student."""
    if student_name not in class_grades:
        print(f"{student_name} is not in this class - nothing removed")
        return
    del class_grades[student_name]
    print(f"{student_name} removed")


remove_student(class_grades, "Tigran")
remove_student(class_grades, "Vahe")
