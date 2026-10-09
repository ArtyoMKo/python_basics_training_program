#%% md
# Թեմա 18 — Լուծումներ

**Պահի՛ր այս տետրը։** 20-րդ թեման այս ֆունկցիաները տեղափոխվում են `grades.py` ֆայլ։

#%% code
# Exercises 1-4 - the four-function toolkit

PASS_MARK = 4


def average_of(grades):
    """Return the average of a list of grades."""
    if not grades:
        return 0
    total = 0
    for grade in grades:
        total = total + grade
    return round(total / len(grades), 1)


def has_passed(grade, pass_mark=PASS_MARK):
    """Return True if this grade is a pass."""
    return grade >= pass_mark


def highest_of(class_grades):
    """Return the name of the student with the highest grade."""
    best_name = ""
    best_grade = -1
    for student_name, grade in class_grades.items():
        if grade > best_grade:
            best_grade = grade
            best_name = student_name
    return best_name


def failing_students(class_grades, pass_mark=PASS_MARK):
    """Return a list of the names of the students who did not pass."""
    failing = []
    for student_name, grade in class_grades.items():
        if grade < pass_mark:
            failing.append(student_name)
    return failing


my_class = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3,
            "Mariam": 8, "Tigran": 5, "Lilit": 8, "Gor": 4,
            "Anahit": 9, "Hayk": 2, "Sona": 8, "Vahe": 6}

print("average:", average_of(list(my_class.values())))
print("highest:", highest_of(my_class))
print("failing:", failing_students(my_class))

#%% code
# Extra 5, 6 and 8

def lowest_of(class_grades):
    """Return the name of the student with the lowest grade."""
    worst_name = ""
    worst_grade = 11
    for student_name, grade in class_grades.items():
        if grade < worst_grade:
            worst_grade = grade
            worst_name = student_name
    return worst_name


def how_many_passed(class_grades, pass_mark=PASS_MARK):
    """Return how many students passed."""
    how_many = 0
    for student_name, grade in class_grades.items():
        if grade >= pass_mark:
            how_many = how_many + 1
    return how_many


def grade_band(grade):
    """Return the name of the band this grade falls into."""
    if grade >= 9:
        return "excellent"
    elif grade >= 7:
        return "good"
    elif grade >= 4:
        return "satisfactory"
    return "unsatisfactory"


print(lowest_of(my_class))
print(how_many_passed(my_class))
print(grade_band(9))

#%% code
# Extra 9 - a function with no return gives back None

def print_average(grades):
    print(sum(grades) / len(grades))


print(print_average([9]))

#%% code
# Challenge 11 - a function can return a dictionary

def class_summary(class_grades):
    """Return the headline numbers as a dictionary."""
    return {
        "average": average_of(list(class_grades.values())),
        "passed": how_many_passed(class_grades),
        "failed": len(failing_students(class_grades)),
    }


print(class_summary(my_class))
