#%% md
# Օր 12 — Լուծումներ

#%% code
# Exercises 3, 4 and 5 - everything with a loop

PASS_MARK = 4

student_names = ["Ani", "Davit", "Nare", "Aram", "Mariam"]
class_grades = [9, 6, 10, 3, 8]

for student_name in student_names:
    print(student_name)

print()

for grade in class_grades:
    if grade >= PASS_MARK:
        print(grade, "- passed")
    else:
        print(grade, "- failed")

#%% code
# Exercise 6 - the whole register in four lines

for position in range(len(student_names)):
    if class_grades[position] >= PASS_MARK:
        print(f"{student_names[position]}: passed")
    else:
        print(f"{student_names[position]}: failed")

#%% code
# Extra 11 - after the loop, the variable keeps the LAST value it had

for student_name in student_names:
    pass

print("after the loop:", student_name)

#%% code
# Challenge 12 - a numbered register. position starts at 0, so add 1.

for position in range(len(student_names)):
    print(f"{position + 1}. {student_names[position]}: {class_grades[position]}")
