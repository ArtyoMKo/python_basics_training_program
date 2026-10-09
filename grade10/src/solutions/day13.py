#%% md
# Թեմա 16 — Լուծումներ

#%% code
# Exercises 1, 2, 3 and 4 - all together

PASS_MARK = 4

student_names = ["Ani", "Davit", "Nare", "Aram", "Mariam", "Tigran",
                 "Lilit", "Gor", "Anahit", "Hayk", "Sona", "Vahe"]
class_grades = [9, 6, 10, 3, 8, 5, 8, 4, 9, 2, 8, 6]

how_many_passed = 0
failing_students = []

for position in range(len(class_grades)):
    if class_grades[position] >= PASS_MARK:
        how_many_passed = how_many_passed + 1
    else:
        failing_students.append(student_names[position])

print(f"passed: {how_many_passed}")
print(f"failed: {failing_students}")

best_position = 0
for position in range(len(class_grades)):
    if class_grades[position] > class_grades[best_position]:
        best_position = position

print(f"highest: {student_names[best_position]} ({class_grades[best_position]})")

#%% code
# Extra 5 - the lowest. Same shape, < instead of >.

worst_position = 0
for position in range(len(class_grades)):
    if class_grades[position] < class_grades[worst_position]:
        worst_position = position

print(f"lowest: {student_names[worst_position]} ({class_grades[worst_position]})")

#%% code
# Challenge 11 - the student closest to the average.
# abs() removes the minus sign, so a distance is never negative.

total = 0
for grade in class_grades:
    total = total + grade
average = total / len(class_grades)

closest_position = 0
for position in range(len(class_grades)):
    if abs(class_grades[position] - average) < abs(class_grades[closest_position] - average):
        closest_position = position

print(f"average {average:.1f}, closest: {student_names[closest_position]}")
