#%% md
# Օր 17 — Լուծումներ

#%% code
# Exercises 2, 4 and 5 - the function, used everywhere

PASS_MARK = 4

class_grades = {
    "Ani": [9, 10, 8],
    "Davit": [6, 5, 7],
    "Nare": [10, 10, 9],
    "Aram": [3, 4, 2],
}


def average_of(grades):
    total = 0
    for grade in grades:
        total = total + grade
    return round(total / len(grades), 1)


for student_name, grades in class_grades.items():
    print(f"{student_name:<10} {average_of(grades)}")

#%% code
# Extra 6, 7 and 8 - three more small functions

def highest_of(grades):
    highest = grades[0]
    for grade in grades:
        if grade > highest:
            highest = grade
    return highest


def lowest_of(grades):
    lowest = grades[0]
    for grade in grades:
        if grade < lowest:
            lowest = grade
    return lowest


def print_report_card(student_name, grades):
    print(f"{student_name:<10} {average_of(grades):>5}  "
          f"best {highest_of(grades)}  worst {lowest_of(grades)}")


for student_name, grades in class_grades.items():
    print_report_card(student_name, grades)

#%% code
# Extra 10 - an empty list divides by zero. Guard it inside the function.

def average_of(grades):
    if not grades:
        return 0
    total = 0
    for grade in grades:
        total = total + grade
    return round(total / len(grades), 1)


print(average_of([]))

#%% code
# Challenge 11 - the whole register as one function

def class_report(class_grades):
    print("=== REGISTER ===")
    for student_name, grades in class_grades.items():
        print(f"{student_name:<10} {average_of(grades)}")
    print(f"{len(class_grades)} students")


class_report(class_grades)
