#%% md
# Օր 17 — Լուծումներ

#%% code
# Առաջադրանք 1-4 — ամբողջական մատյան

PASS_MARK = 4

class_grades = {
    "Անի": [9, 10, 8],
    "Դավիթ": [6, 5, 7],
    "Նարե": [10, 10, 9],
    "Արամ": [3, 4, 2],
}

print("=== ՄԱՏՅԱՆ ===")

for student_name, grades in class_grades.items():
    total = 0
    for grade in grades:
        total = total + grade
    student_average = total / len(grades)

    if student_average >= PASS_MARK:
        result = "անցավ"
    else:
        result = "չանցավ"

    print(f"{student_name:<10} {grades}  միջինը՝ {student_average:.1f}  — {result}")
