#%% md
# Թեմա 13 — Լուծումներ

#%% code
# Exercises 1 and 2 - total and average

class_grades = [9, 6, 10, 3, 8, 5, 8, 4, 9, 2, 8, 6]

total = 0
for grade in class_grades:
    total = total + grade

print(f"Total:   {total}")
print(f"Average: {total / len(class_grades):.1f}")

#%% code
# Exercise 4 - how many have 10

how_many = 0

for grade in class_grades:
    if grade == 10:
        how_many = how_many + 1

print(how_many)

#%% code
# Extra 6 and 7 - percentage passed, and the average of those who passed

PASS_MARK = 4

passed_total = 0
passed_count = 0

for grade in class_grades:
    if grade >= PASS_MARK:
        passed_total = passed_total + grade
        passed_count = passed_count + 1

print(f"passed: {passed_count / len(class_grades) * 100:.0f}%")
print(f"their average: {passed_total / passed_count:.1f}")

#%% code
# Challenge 10 - a text chart

for mark in range(10, 0, -1):
    how_many = 0
    for grade in class_grades:
        if grade == mark:
            how_many = how_many + 1
    print(f"{mark:>2}: {'*' * how_many}")
