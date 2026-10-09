#%% md
# Թեմա 14 — Լուծումներ

#%% code
# Exercises 1-5 - report cards with several grades each

PASS_MARK = 4

class_grades = {
    "Ani": [9, 10, 8],
    "Davit": [6, 5, 7],
    "Nare": [10, 10, 9],
    "Aram": [3, 4, 2],
}

class_grades["Ani"].append(7)

print("=== REPORT CARDS ===")

for student_name, grades in class_grades.items():
    total = 0
    for grade in grades:
        total = total + grade
    student_average = total / len(grades)

    if student_average >= PASS_MARK:
        result = "passed"
    else:
        result = "failed"

    print(f"{student_name:<10} {str(grades):<16} {student_average:.1f}   {result}")

#%% code
# Extra 8 - each student's best grade

for student_name, grades in class_grades.items():
    highest = grades[0]
    for grade in grades:
        if grade > highest:
            highest = grade
    print(f"{student_name}: best {highest}")

#%% code
# Extra 11 - an empty list makes the average divide by zero.
# Guard it before dividing.

grades = []

if not grades:
    print("no grades yet")
else:
    print(sum(grades) / len(grades))

#%% code
# Challenge 12 - who improved the most. :+d shows the plus sign.

for student_name, grades in class_grades.items():
    improvement = grades[-1] - grades[0]
    print(f"{student_name}: {improvement:+d}")
