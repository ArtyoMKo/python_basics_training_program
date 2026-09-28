#%% md
# Օր 16 — Լուծումներ

#%% code
# Առաջադրանք 1, 2, 3

class_grades = {"Անի": 9, "Դավիթ": 6, "Նարե": 10, "Արամ": 3, "Մարիամ": 8}

print(class_grades["Անի"])
print(class_grades["Նարե"])

class_grades["Տիգրան"] = 5          # ավելացնել
class_grades["Արամ"] = 4            # ուղղել
del class_grades["Դավիթ"]           # հեռացնել

print(class_grades)

#%% code
# Առաջադրանք 4 և 5 — անվտանգ որոնում

def look_up(class_grades, student_name):
    if student_name in class_grades:
        print(f"{student_name}: {class_grades[student_name]}")
    else:
        print(f"{student_name} — այդպիսի աշակերտ չկա")

look_up(class_grades, "Անի")
look_up(class_grades, "Դավիթ")
