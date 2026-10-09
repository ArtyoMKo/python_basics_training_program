#%% md
# Թեմա 10 — Լուծումներ

#%% code
# Exercises 1, 2 and 3

PASS_MARK = 4

student_name = "Ani"
grade = 9

if grade == 10:
    print(f"{student_name}: excellent")
elif grade >= PASS_MARK:
    print(f"{student_name}: passed")
else:
    print(f"{student_name}: failed")

#%% code
# Extra 7 - compare two grades

first_grade = 9
second_grade = 6

if first_grade > second_grade:
    print("the first one is higher")
else:
    print("the second one is higher or equal")

#%% code
# Challenge 11 - a condition inside a condition

student_names = ["Ani", "Davit"]
student_name = "Ani"
grade = 10

if student_name in student_names:
    if grade == 10:
        print(f"{student_name} is in the class and has a perfect grade")
