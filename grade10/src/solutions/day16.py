#%% md
# Թեմա 15 — Լուծումներ

`input()`-ի փոխարեն ցուցակ է օգտագործված, որպեսզի կարողանաս գործարկել։
Քո տետրում `input()`-ը պետք է մնա։

#%% code
# Exercises 1-4 - the full loop with every check

answers = ["9", "nine", "15", "6", "quit"]      # what the teacher would type
class_grades = []

for answer in answers:
    if answer == "quit":
        break

    if not answer.isdigit():
        print(f"'{answer}' is not a number.")
        continue

    grade = int(answer)

    if grade < 1 or grade > 10:
        print(f"{grade} must be between 1 and 10.")
        continue

    class_grades.append(grade)

print(f"collected {len(class_grades)}: {class_grades}")

total = 0
for grade in class_grades:
    total = total + grade
print(f"average: {total / len(class_grades):.1f}")
