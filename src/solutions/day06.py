#%% md
# Օր 6 — Լուծումներ

#%% code
# Exercises 3 and 4 - the whole class in two lists

student_names = ["Ani", "Davit", "Nare", "Aram", "Mariam",
                 "Tigran", "Lilit", "Gor", "Anahit", "Hayk"]
class_grades = [9, 6, 10, 3, 8, 5, 8, 4, 9, 2]

print("students:", len(student_names))
print("first:   ", student_names[0])
print("last:    ", student_names[-1])

#%% code
# Extra 6 and 7 - one row, and the sum of the first three

print(f"{student_names[2]}: {class_grades[2]}")
print(class_grades[0] + class_grades[1] + class_grades[2])

#%% code
# Challenge 10 - the whole register, one index at a time.
# Ten students, ten lines. Day 10 turns this into four.

print(f"{student_names[0]}: {class_grades[0]}")
print(f"{student_names[1]}: {class_grades[1]}")
print(f"{student_names[2]}: {class_grades[2]}")
