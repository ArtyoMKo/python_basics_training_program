#%% day02 md
# Օր 2 — Լուծումներ

Այս լուծումները **մեկ հնարավոր տարբերակն** են։ Եթե քոնը այլ է, բայց աշխատում է —
քոնը նույնպես ճիշտ է։

#%% day02 code
# Առաջադրանք 1 — դասարանի վերնագիրը

print("7-րդ Բ դասարան — կենսաբանություն")

#%% day02 code
# Առաջադրանք 2 — չորս աշակերտ

print("Անի:", 9)
print("Դավիթ:", 6)
print("Նարե:", 10)
print("Արամ:", 3)

#%% day02 code
# Առաջադրանք 5 — ամբողջ մատյանը, դատարկ տողով բաժանված

print("7-րդ Բ դասարան")
print()
print("Անի:", 9)
print("Դավիթ:", 6)

#%% day03 md
# Օր 3 — Լուծումներ

#%% day03 code
# Առաջադրանք 1 և 2 — չորս տեսակ և դրանց ստուգումը

student_name = "Անի"
student_grade = 9
class_average = 6.5
has_passed = True

print(type(student_name))
print(type(student_grade))
print(type(class_average))
print(type(has_passed))

#%% day03 code
# Առաջադրանք 3 — երկու գնահատականի գումարը և միջինը

print(9 + 6)
print((9 + 6) / 2)

#%% day03 code
# Առաջադրանք 4 — ուղղված տարբերակը. երկուսն էլ տեքստ

print("Անի" + " " + "9")

#%% day03 code
# Առաջադրանք 5 — "Անի" * 3 կրկնում է տեքստը երեք անգամ

print("Անի" * 3)

#%% day04 md
# Օր 4 — Լուծումներ

Այս տետրում input()-ի փոխարեն արժեքները ուղիղ գրված են, որպեսզի կարողանաս գործարկել
առանց պատասխանելու։ Քո տետրում input()-ը պետք է մնա։

#%% day04 code
# Առաջադրանք 2 — գնահատականը գումարած մեկ

answer = "9"                  # այն, ինչ input()-ը կտար
grade = int(answer)

print(grade + 1)

#%% day04 code
# Առաջադրանք 3 — երկու գնահատականի միջինը

first_grade = int("9")
second_grade = int("6")

print(round((first_grade + second_grade) / 2, 1))

#%% day04 code
# Առաջադրանք 5 — int("9.5") չի աշխատում, որովհետև "9.5"-ը ամբողջ թիվ չէ։
# Ճիշտ ձևն է float()-ը։

print(float("9.5"))

#%% day05 md
# Օր 5 — Լուծումներ

#%% day05 code
# Առաջադրանք 1, 2, 3

student_name = "Անի"
student_grade = 9
subject = "կենսաբանություն"

print(f"{student_name} — {subject} — {student_grade} միավոր")

student_grade = student_grade + 1

print(f"{student_name} — {subject} — {student_grade} միավոր")

#%% day05 code
# Առաջադրանք 5 — երկու գնահատականի միջինը, մեկ նիշով

first_grade = 9
second_grade = 6
average = (first_grade + second_grade) / 2

print(f"Միջինը՝ {average:.1f}")

#%% day06 md
# Օր 6 — Լուծումներ

Այս օրվա առաջադրանքը լուծում չունի. այն կատարվում է ձեռքով, և դա հենց դասն էր։

Առաջադրանք 3-ի համար ահա մի քանի պատասխան, որ մասնակիցները սովորաբար գրում են.

- «Վատն այն էր, որ նույն բանը քառասուն անգամ գրեցի»։
- «Վատն այն էր, որ մեկ փոփոխության համար քառասուն տեղ պետք էր ուղղել»։
- «Վատն այն էր, որ չգիտեի՝ ինչ-որ մեկը բաց թողեցի, թե ոչ»։

Երեքն էլ ճիշտ են։ **10-րդ օրը այս երեքն էլ լուծվում են։**

#%% day07 md
# Օր 7 — Լուծումներ

#%% day07 code
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

#%% day07 code
# Առաջադրանք 5 — if grade = 9 տալիս է SyntaxError։
# Պայմանում պետք է == (հարցնել), ոչ թե = (վերագրել)։

grade = 9

if grade == 9:
    print("ինը է")

#%% day08 md
# Օր 8 — Լուծումներ

#%% day08 code
# Առաջադրանք 1 և 2 — չորս մակարդակ, ստուգված չորս գնահատականով

for grade in [10, 8, 5, 2]:
    if grade >= 9:
        print(grade, "— գերազանց")
    elif grade >= 7:
        print(grade, "— լավ")
    elif grade >= 4:
        print(grade, "— բավարար")
    else:
        print(grade, "— անբավարար")

#%% day08 code
# Առաջադրանք 3 — կանոն and-ով

grade = 8
attendance = 90

if grade >= 4 and attendance >= 80:
    print("վկայականը տրվում է")
else:
    print("վկայականը չի տրվում")

#%% day08 code
# Առաջադրանք 5 — not (grade >= 4) և grade < 4 նույն բանն են

grade = 3

print(not (grade >= 4))
print(grade < 4)

#%% day09 md
# Օր 9 — Լուծումներ

#%% day09 code
# Առաջադրանք 2 — մեկ փոփոխական քսանհինգ թվի փոխարեն

PASS_MARK = 4

class_grades = {"Անի": 9, "Դավիթ": 6, "Նարե": 10, "Արամ": 3}

for student_name, grade in class_grades.items():
    if grade >= PASS_MARK:
        print(f"{student_name}: անցավ")
    else:
        print(f"{student_name}: չանցավ")

#%% day09 md
> Այս լուծումը ցիկլ է օգտագործում, որը դեռ չենք սովորել 9-րդ օրը։ Այն այստեղ է,
> որպեսզի տեսնես, թե ուր ենք գնում։ **14-րդ օրը դա գրելու ես ինքդ։**

#%% day10 md
# Օր 10 — Լուծումներ

#%% day10 code
# Առաջադրանք 1, 2, 3

student_names = ["Անի", "Դավիթ", "Նարե", "Արամ", "Մարիամ",
                 "Տիգրան", "Լիլիթ", "Գոռ", "Անահիտ", "Հայկ"]
class_grades = [9, 6, 10, 3, 8, 5, 8, 4, 9, 2]

print("Աշակերտների թիվը՝", len(student_names))
print("Առաջինը՝", student_names[0])
print("Վերջինը՝", student_names[-1])

#%% day11 md
# Օր 11 — Լուծումներ

#%% day11 code
# Առաջադրանք 1, 2, 3

student_names = ["Անի", "Դավիթ", "Նարե", "Արամ"]

student_names.append("Տիգրան")

if "Արամ" in student_names:
    student_names.remove("Արամ")

student_names.sort()

print(student_names)

#%% day11 code
# Առաջադրանք 5 — առաջին երեքը

print(student_names[0:3])

#%% day12 md
# Օր 12 — Լուծումներ

#%% day12 code
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

#%% day12 code
# Առաջադրանք 5 — երկու ցուցակը միասին

for position in range(len(student_names)):
    print(f"{student_names[position]}: {class_grades[position]}")

#%% day13 md
# Օր 13 — Լուծումներ

#%% day13 code
# Առաջադրանք 1, 2 — գումարը և միջինը

class_grades = [9, 6, 10, 3, 8, 5, 8, 4, 9, 2, 8, 6]

total = 0
for grade in class_grades:
    total = total + grade

print(f"Գումարը՝ {total}")
print(f"Միջինը՝ {total / len(class_grades):.1f}")

#%% day13 code
# Առաջադրանք 4 — քանի՞սն ունեն 10

how_many = 0

for grade in class_grades:
    if grade == 10:
        how_many = how_many + 1

print(how_many)

#%% day13 code
# Առաջադրանք 5 — բաշխումը

for mark in range(1, 11):
    how_many = 0
    for grade in class_grades:
        if grade == mark:
            how_many = how_many + 1
    print(f"{mark} միավոր՝ {how_many} աշակերտ")

#%% day14 md
# Օր 14 — Լուծումներ

#%% day14 code
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

#%% day14 code
# Առաջադրանք 5 — ամենացածրը. նույն ձևը, > -ի փոխարեն <

worst_position = 0
for position in range(len(class_grades)):
    if class_grades[position] < class_grades[worst_position]:
        worst_position = position

print(f"Ամենացածրը՝ {student_names[worst_position]} ({class_grades[worst_position]})")

#%% day15 md
# Օր 15 — Լուծումներ

Այս տետրում input()-ի փոխարեն ցուցակ է օգտագործված, որպեսզի կարողանաս գործարկել։
Քո տետրում input()-ը պետք է մնա։

#%% day15 code
# Առաջադրանք 1-4 — ամբողջական ցիկլ բոլոր ստուգումներով

answers = ["9", "ինը", "15", "6", "դուրս"]      # այն, ինչ օգտվողը կգրեր
class_grades = []

for answer in answers:
    if answer == "դուրս":
        break

    if not answer.isdigit():
        print(f"«{answer}» — դա թիվ չէ։")
        continue

    grade = int(answer)

    if grade < 1 or grade > 10:
        print(f"{grade} — պետք է լինի 1-ից 10։")
        continue

    class_grades.append(grade)

print(f"Հավաքվեց {len(class_grades)} գնահատական՝ {class_grades}")
print(f"Միջինը՝ {sum(class_grades) / len(class_grades):.1f}")

#%% day16 md
# Օր 16 — Լուծումներ

#%% day16 code
# Առաջադրանք 1, 2, 3

class_grades = {"Անի": 9, "Դավիթ": 6, "Նարե": 10, "Արամ": 3, "Մարիամ": 8}

print(class_grades["Անի"])
print(class_grades["Նարե"])

class_grades["Տիգրան"] = 5          # ավելացնել
class_grades["Արամ"] = 4            # ուղղել
del class_grades["Դավիթ"]           # հեռացնել

print(class_grades)

#%% day16 code
# Առաջադրանք 4 և 5 — անվտանգ որոնում

def look_up(class_grades, student_name):
    if student_name in class_grades:
        print(f"{student_name}: {class_grades[student_name]}")
    else:
        print(f"{student_name} — այդպիսի աշակերտ չկա")

look_up(class_grades, "Անի")
look_up(class_grades, "Դավիթ")

#%% day17 md
# Օր 17 — Լուծումներ

#%% day17 code
# Առաջադրանք 1-4 — ամբողջական մատյան

PASS_MARK = 4

class_grades = {
    "Անի": [9, 10, 8],
    "Դավիթ": [6, 5, 7],
    "Նարե": [10, 10, 9],
    "Արամ": [3, 4, 2],
}

print("=== ՄԱՏՅԱՆ ===")

for student_name, grades in class_grades.items():
    total = 0
    for grade in grades:
        total = total + grade
    student_average = total / len(grades)

    if student_average >= PASS_MARK:
        result = "անցավ"
    else:
        result = "չանցավ"

    print(f"{student_name:<10} {grades}  միջինը՝ {student_average:.1f}  — {result}")

#%% day18 md
# Օր 18 — Լուծումներ

#%% day18 code
# Առաջադրանք 1-4

def greet_student(student_name):
    print(f"Բարև, {student_name}")


def print_student_row(student_name, grade):
    print(f"{student_name:<10} {grade}")


def print_average(grades):
    total = 0
    for grade in grades:
        total = total + grade
    print(f"Միջինը՝ {total / len(grades):.1f}")


greet_student("Անի")

simple_grades = {"Անի": 9, "Դավիթ": 6, "Նարե": 10}

for student_name, grade in simple_grades.items():
    print_student_row(student_name, grade)

print_average([9, 10, 8])

#%% day18 code
# Առաջադրանք 5

PASS_MARK = 4


def print_result(student_name, grade):
    if grade >= PASS_MARK:
        print(f"{student_name}: անցավ")
    else:
        print(f"{student_name}: չանցավ")


print_result("Անի", 9)
print_result("Հայկ", 2)

#%% day19 md
# Օր 19 — Լուծումներ

**Պահի՛ր այս տետրը։** 20-րդ օրը այս չորս ֆունկցիան տեղափոխվում են `grades.py` ֆայլ։

#%% day19 code
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

#%% day19 code
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
