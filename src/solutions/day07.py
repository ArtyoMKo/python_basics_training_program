#%% md
# Օր 7 — Լուծումներ

#%% code
# Առաջադրանք 1, 2, 3 — երեք աշակերտ, պայմաններով

PASS_MARK = 4

student_name = "Անի"
grade = 9

if grade == 10:
    print(f"{student_name}: գերազանց")
elif grade >= PASS_MARK:
    print(f"{student_name}: անցավ")
else:
    print(f"{student_name}: չանցավ")

#%% code
# Առաջադրանք 5 — if grade = 9 տալիս է SyntaxError։
# Պայմանում պետք է == (հարցնել), ոչ թե = (վերագրել)։

grade = 9

if grade == 9:
    print("ինը է")
