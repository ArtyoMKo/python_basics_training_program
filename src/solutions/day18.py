#%% md
# Օր 18 — Լուծումներ

#%% code
# Առաջադրանք 1-4

def greet_student(student_name):
    print(f"Բարև, {student_name}")


def print_student_row(student_name, grade):
    print(f"{student_name:<10} {grade}")


def print_average(grades):
    total = 0
    for grade in grades:
        total = total + grade
    print(f"Միջինը՝ {total / len(grades):.1f}")


greet_student("Անի")

simple_grades = {"Անի": 9, "Դավիթ": 6, "Նարե": 10}

for student_name, grade in simple_grades.items():
    print_student_row(student_name, grade)

print_average([9, 10, 8])

#%% code
# Առաջադրանք 5

PASS_MARK = 4


def print_result(student_name, grade):
    if grade >= PASS_MARK:
        print(f"{student_name}: անցավ")
    else:
        print(f"{student_name}: չանցավ")


print_result("Անի", 9)
print_result("Հայկ", 2)
