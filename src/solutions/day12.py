#%% md
# Օր 12 — Լուծումներ

#%% code
# Առաջադրանք 1, 2, 3 — ամեն ինչ ցիկլով

PASS_MARK = 4

student_names = ["Անի", "Դավիթ", "Նարե", "Արամ", "Մարիամ"]
class_grades = [9, 6, 10, 3, 8]

for student_name in student_names:
    print(student_name)

print()

for grade in class_grades:
    if grade >= PASS_MARK:
        print(grade, "— անցավ")
    else:
        print(grade, "— չանցավ")

#%% code
# Առաջադրանք 5 — երկու ցուցակը միասին

for position in range(len(student_names)):
    print(f"{student_names[position]}: {class_grades[position]}")
