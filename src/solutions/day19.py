#%% md
# Օր 19 — Լուծումներ

**Պահի՛ր այս տետրը։** 20-րդ օրը այս չորս ֆունկցիան տեղափոխվում են `grades.py` ֆայլ։

#%% code
# Առաջադրանք 1-4 — չորս ֆունկցիա, որոնք վերադարձնում են արժեք

PASS_MARK = 4


def average_of(grades):
    """Վերադարձնում է գնահատականների միջինը։"""
    total = 0
    for grade in grades:
        total = total + grade
    return round(total / len(grades), 1)


def has_passed(grade, pass_mark=PASS_MARK):
    """Վերադարձնում է True, եթե գնահատականը անցողիկ է։"""
    return grade >= pass_mark


def highest_of(class_grades):
    """Վերադարձնում է ամենաբարձր գնահատական ունեցող աշակերտի անունը։"""
    best_name = ""
    best_grade = -1
    for student_name, grade in class_grades.items():
        if grade > best_grade:
            best_grade = grade
            best_name = student_name
    return best_name


def failing_students(class_grades, pass_mark=PASS_MARK):
    """Վերադարձնում է չանցած աշակերտների անունների ցուցակը։"""
    failing = []
    for student_name, grade in class_grades.items():
        if grade < pass_mark:
            failing.append(student_name)
    return failing


my_class = {"Անի": 9, "Դավիթ": 6, "Նարե": 10, "Արամ": 3,
            "Մարիամ": 8, "Տիգրան": 5, "Լիլիթ": 8, "Գոռ": 4,
            "Անահիտ": 9, "Հայկ": 2, "Սոնա": 8, "Վահե": 6}

print("Միջինը՝", average_of(list(my_class.values())))
print("Ամենաբարձրը՝", highest_of(my_class))
print("Չեն անցել՝", failing_students(my_class))

#%% code
# Առաջադրանք 5 — lowest_of. նույն ձևը, հակառակ համեմատությամբ

def lowest_of(class_grades):
    """Վերադարձնում է ամենացածր գնահատական ունեցող աշակերտի անունը։"""
    worst_name = ""
    worst_grade = 11
    for student_name, grade in class_grades.items():
        if grade < worst_grade:
            worst_grade = grade
            worst_name = student_name
    return worst_name


print("Ամենացածրը՝", lowest_of(my_class))
