#%% md
# Օր 15 — Լուծումներ

#%% code
# Exercises 1-4 - the full register from a dictionary

PASS_MARK = 4

class_grades = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3,
                "Mariam": 8, "Tigran": 5, "Lilit": 8, "Gor": 4}

total = 0
failing = 0

print("=== REGISTER ===")

for student_name, grade in class_grades.items():
    if grade >= PASS_MARK:
        result = "passed"
    else:
        result = "failed"
        failing = failing + 1
    total = total + grade
    print(f"{student_name:<10} {grade:>3}   {result}")

print()
print(f"students: {len(class_grades)}")
print(f"average:  {total / len(class_grades):.1f}")
print(f"failing:  {failing}")

#%% code
# Extra 8 - a numbered register needs a counter before the loop

number = 1

for student_name, grade in class_grades.items():
    print(f"{number}. {student_name:<10} {grade:>3}")
    number = number + 1

#%% code
# Extra 10 - names starting with A. student_name[0] is the first letter.

for student_name, grade in class_grades.items():
    if student_name[0] == "A":
        print(student_name)

#%% code
# Challenge 11 - sorted by grade, high to low

for mark in range(10, 0, -1):
    for student_name, grade in class_grades.items():
        if grade == mark:
            print(f"{student_name:<10} {grade:>3}")
