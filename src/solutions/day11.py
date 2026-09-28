#%% md
# Օր 11 — Լուծումներ

#%% code
# Առաջադրանք 1, 2, 3

student_names = ["Անի", "Դավիթ", "Նարե", "Արամ"]

student_names.append("Տիգրան")

if "Արամ" in student_names:
    student_names.remove("Արամ")

student_names.sort()

print(student_names)

#%% code
# Առաջադրանք 5 — առաջին երեքը

print(student_names[0:3])
