#%% md
# Օր 14 — Լուծումներ

#%% code
# Առաջադրանք 1, 2, 3, 4 — բոլորը միասին

PASS_MARK = 4

student_names = ["Անի", "Դավիթ", "Նարե", "Արամ", "Մարիամ", "Տիգրան",
                 "Լիլիթ", "Գոռ", "Անահիտ", "Հայկ", "Սոնա", "Վահե"]
class_grades = [9, 6, 10, 3, 8, 5, 8, 4, 9, 2, 8, 6]

how_many_passed = 0
failing_students = []

for position in range(len(class_grades)):
    if class_grades[position] >= PASS_MARK:
        how_many_passed = how_many_passed + 1
    else:
        failing_students.append(student_names[position])

print(f"Անցել է՝ {how_many_passed}")
print(f"Չեն անցել՝ {failing_students}")

best_position = 0
for position in range(len(class_grades)):
    if class_grades[position] > class_grades[best_position]:
        best_position = position

print(f"Ամենաբարձրը՝ {student_names[best_position]} ({class_grades[best_position]})")

#%% code
# Առաջադրանք 5 — ամենացածրը. նույն ձևը, > -ի փոխարեն <

worst_position = 0
for position in range(len(class_grades)):
    if class_grades[position] < class_grades[worst_position]:
        worst_position = position

print(f"Ամենացածրը՝ {student_names[worst_position]} ({class_grades[worst_position]})")
