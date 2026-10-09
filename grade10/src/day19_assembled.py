#%% md
# Թեմա 19 — Մատյանը՝ հավաքված

### Python զրոյից · Թեմա 19-ը 24-ից

**Այսօր նոր բան չենք սովորում։** Ոչ մի նոր բառ, ոչ մի նոր շարահյուսություն։

Այսօր հավաքում ենք տասնութ դասի ամեն ինչ մեկ տեղում և ստանում ամբողջական մատյանի
ծրագիր։ Այն, ինչ վաղը տեղափոխվելու է իսկական ֆայլ։

Սա նաև **հասնելու օրն** է։ Եթե ինչ-որ բան բաց ես թողել, այսօր ժամանակ կա։

## ԱՅՍՕՐ:

- **Ա մաս:** տվյալները և կարգավորումները
- **Բ մաս:** գործիքակազմը
- **Գ մաս:** մատյանը՝ ամբողջությամբ

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Տասնութ դասը՝ մեկ ցանկով</h3>
<p style="color:#06c; margin-bottom:0;">
<code>print</code> · տիպեր · <code>input</code> · փոփոխականներ · f-տողեր · ցուցակներ ·
<code>if</code>/<code>elif</code> · <code>for</code> · <code>range</code> ·
կուտակիչ · <code>while</code> · բառարաններ · <code>.items()</code> · ֆունկցիաներ ·
<code>return</code><br/><br/>
<b>Սա ամբողջ լեզուն է, որ պետք է այս ծրագրի համար։</b> Նոր շարահյուսություն այլևս
չի լինելու։
</p>
</div>

#%% md
## Ա մաս: Տվյալները և կարգավորումները

Ամեն ծրագիր սկսվում է երկու բանից՝ **կարգավորումներ** (թվեր, որ կարող են փոխվել) և
**տվյալներ**։

#%% code
# Settings - everything you might want to change lives here.
PASS_MARK = 4
DECIMAL_PLACES = 1
NAME_WIDTH = 12

#%% md
> Ուշադրություն՝ սրանք վերևում են, միասին, մեծատառերով։ **21-րդ թեման այս երեք տողը
> կդառնա առանձին ֆայլ՝ `settings.py`։**

#%% code
# The class. On day 22 this will come from a file instead.
class_grades = {
    "Ani": [9, 10, 8],
    "Davit": [6, 5, 7],
    "Nare": [10, 10, 9],
    "Aram": [3, 4, 2],
    "Mariam": [8, 8, 9],
    "Tigran": [5, 6, 5],
}

print(len(class_grades), "students")

#%% md
## Բ մաս: Գործիքակազմը

Երեկվա չորս ֆունկցիան, և ևս երկուսը։ **Ամեն մեկը մեկ բան է անում և վերադարձնում է
արժեք։**

#%% code
def average_of(grades):
    """Return the average of a list of grades."""
    if not grades:
        return 0
    total = 0
    for grade in grades:
        total = total + grade
    return round(total / len(grades), DECIMAL_PLACES)


def has_passed(grades, pass_mark=PASS_MARK):
    """Return True if this student's average is a pass."""
    return average_of(grades) >= pass_mark


def highest_of(class_grades):
    """Return the name of the student with the highest average."""
    best_name = ""
    best_average = -1
    for student_name, grades in class_grades.items():
        if average_of(grades) > best_average:
            best_average = average_of(grades)
            best_name = student_name
    return best_name


def failing_students(class_grades):
    """Return a list of the names of students who did not pass."""
    failing = []
    for student_name, grades in class_grades.items():
        if not has_passed(grades):
            failing.append(student_name)
    return failing


def class_average(class_grades):
    """Return the average of every student's average."""
    all_averages = []
    for student_name, grades in class_grades.items():
        all_averages.append(average_of(grades))
    return average_of(all_averages)

#%% md
Ուշադրություն երկու բանի.

- **`if not grades: return 0`** — պաշտպանություն դատարկ ցուցակից։ Առանց դրա
  `average_of([])`-ը կկանգնեցներ ծրագիրը՝ զրոյի վրա բաժանելով։
- **`has_passed`-ը կանչում է `average_of`-ը։** Ֆունկցիան կարող է կանչել ուրիշ ֆունկցիա։
  Այդպես տրամաբանությունը մեկ տեղում է մնում։

Ստուգենք բոլորը։

#%% code
print("average of Ani:", average_of(class_grades["Ani"]))
print("did Aram pass?", has_passed(class_grades["Aram"]))
print("highest:", highest_of(class_grades))
print("failing:", failing_students(class_grades))
print("class average:", class_average(class_grades))

#%% md
## Գ մաս: Մատյանը՝ ամբողջությամբ

Հիմա տպող մասը։ **Այս ֆունկցիաները տպում են և ոչինչ չեն հաշվում** — հաշվելը
գործիքակազմի գործն է։

#%% code
def print_register(class_grades):
    """Print the whole register, one line per student."""
    print()
    print("=== REGISTER ===")

    for student_name, grades in class_grades.items():
        if has_passed(grades):
            result = "passed"
        else:
            result = "failed"
        print(f"{student_name:<{NAME_WIDTH}} {str(grades):<14} "
              f"{average_of(grades):>5}   {result}")

    print()
    print(f"students:      {len(class_grades)}")
    print(f"class average: {class_average(class_grades)}")
    print(f"did not pass:  {len(failing_students(class_grades))}")


def print_failing(class_grades):
    """Print only the students who did not pass."""
    failing = failing_students(class_grades)

    print()
    if not failing:
        print("Everyone passed.")
        return

    print(f"Did not pass ({len(failing)}):")
    for student_name in failing:
        print(f" - {student_name}: {average_of(class_grades[student_name])}")

#%% code
print_register(class_grades)

#%% code
print_failing(class_grades)

#%% md
### Ավելացնել միավոր

Եվ վերջին կտորը՝ նոր միավոր ավելացնելը, 16-րդ թեմայի ստուգումներով։

#%% code
def add_grade(class_grades, student_name, answer):
    """Add one grade to a student. Returns True if it was added."""
    if not answer.isdigit():
        print("That is not a number.")
        return False

    grade = int(answer)

    if grade < 1 or grade > 10:
        print("The grade must be between 1 and 10.")
        return False

    if student_name not in class_grades:
        class_grades[student_name] = []
        print(f"{student_name} is new - added to the register.")

    class_grades[student_name].append(grade)
    print(f"{student_name}: added {grade}")
    return True

#%% code
add_grade(class_grades, "Ani", "10")
add_grade(class_grades, "Ani", "nine")
add_grade(class_grades, "Ani", "15")
add_grade(class_grades, "Gor", "7")

print_register(class_grades)

#%% md
**Սա քո ծրագիրն է։** Այն բացում է դասարանը, հաշվում է, որոշում է կայացնում,
ավելացնում է միավոր, և տպում է մատյան։

Երկու բան դեռ պակասում է, և երկուսն էլ լուծվում են հաջորդ շաբաթ.

- **Ոչինչ չի պահպանվում։** Փակի՛ր տետրը և ամեն ինչ կվերանա։ → **22-րդ թեմա**
- **Սա տետր է, ոչ թե ծրագիր։** Չես կարող այն տալ գործընկերոջդ և ասել «գործարկի՛ր»։
  → **20-րդ և 21-րդ թեմաներ**

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Պարտադիր առաջադրանքներ</h3>
<p style="color:#900; margin-bottom:0;">
<b>Այսօրվա արդյունքը վաղը տեղափոխվում է ֆայլ։ Գրի՛ր այն ուշադիր։</b><br/><br/>
<b>1.</b> Գրի՛ր կարգավորումների բլոկը՝ քո դպրոցի արժեքներով։<br/><br/>
<b>2.</b> Գրի՛ր <b>քո դասարանը</b> բառարանով՝ ամեն աշակերտ երեք միավորով։<br/><br/>
<b>3.</b> Գրի՛ր հինգ ֆունկցիաները։ Ստուգի՛ր ամեն մեկը առանձին։<br/><br/>
<b>4.</b> Գրի՛ր <code>print_register</code>-ը և կանչի՛ր այն։<br/><br/>
<b>5.</b> Ավելացրո՛ւ երկու նոր միավոր <code>add_grade</code>-ով և տպի՛ր մատյանը նորից։
</p>
</div>

#%% code
# Exercise 1 and 2 - settings and your class

PASS_MARK = 4
DECIMAL_PLACES = 1
NAME_WIDTH = 12

my_class = {
    "Ani": [9, 10, 8],
    "Davit": [6, 5, 7],
}

print(len(my_class), "students")

#%% code
# Exercise 3 and 4 - the toolkit and the register

print_register(my_class)

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">🚀 Լրացուցիչ առաջադրանքներ</h3>
<p style="color:#f71; margin-bottom:0;">
<b>6.</b> Ավելացրո՛ւ <code>print_summary(class_grades)</code>՝ միայն ամփոփիչ թվերը,
առանց աշակերտների։<br/><br/>
<b>7.</b> Ավելացրո՛ւ <code>best_student(class_grades)</code> և տպի՛ր նրան մատյանի
վերջում։<br/><br/>
<b>8.</b> Ավելացրո՛ւ <code>remove_student(class_grades, student_name)</code>՝
<code>in</code>-ի ստուգումով։<br/><br/>
<b>9.</b> Ավելացրո՛ւ <code>grade_band</code>-ը 18-րդ թեմայինից և ցույց տո՛ւր այն
մատյանի ամեն տողում։<br/><br/>
<b>10.</b> Կազմի՛ր մենյու 16-րդ թեմայի մարտահրավերի ձևով, որը կանչում է այս
ֆունկցիաները։ <b>Այն 21-րդ թեման գրեթե անփոփոխ կտեղափոխվի քո ծրագիր։</b>
</p>
</div>

#%% code
# Extra 6-10 - your space

def print_summary(class_grades):
    """Print only the summary numbers."""
    print(f"students:      {len(class_grades)}")
    print(f"class average: {class_average(class_grades)}")
    print(f"did not pass:  {len(failing_students(class_grades))}")


print_summary(class_grades)

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🧗 Մարտահրավեր</h3>
<p style="color:#06c; margin-bottom:0;">
<b>11.</b> Ամբողջական մենյու՝ <code>while True</code> ցիկլով, հինգ հրամանով.
մատյան, չանցածներ, ավելացնել միավոր, ամփոփում, դուրս գալ։<br/><br/>
Գրի՛ր այն այնպես, որ ամեն հրաման կանչի <b>մեկ ֆունկցիա</b>, և մենյուն ինքը ոչինչ
չհաշվի։<br/><br/>
<b>Եթե այսօր դա գրես, 21-րդ թեման ամենահեշտ օրը կլինի դասընթացում։</b>
</p>
</div>

#%% code interactive: 1; 2; 5
# Challenge 11 - the full menu

while True:
    print()
    print("1 - register    2 - failing    3 - summary    5 - quit")
    choice = input("Choose: ").strip()

    if choice == "1":
        print_register(class_grades)
    elif choice == "2":
        print_failing(class_grades)
    elif choice == "3":
        print_summary(class_grades)
    elif choice == "5":
        print("Goodbye.")
        break
    else:
        print("No such command.")

#%% md
<div style="border-left: 6px solid #747; background: #f8f6fb; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#747; margin-top:0;">🏠 Տնային</h3>
<p style="color:#747; margin-bottom:0;">
Այս նոթատետրի <b>Լրացուցիչ</b> առաջադրանքները, և ցանկացած <b>Պարտադիր</b>, որ չհասցրիր։<br/><br/>
<b>Նոր բան չկա</b> — ամեն առաջադրանք այս նոթատետրից է, և օգտագործում է միայն այն,
ինչ այսօր սովորեցինք։<br/>
Հաջորդ նիստը սկսվում է դրանց ստուգումով։
</p>
</div>

#%% md
## Ինչի հասանք

- **Ամբողջական մատյանի ծրագիր**, հավաքված տասնութ դասից։
- Կարգավորումները վերևում, միասին։ Գործիքակազմը՝ հաշվում է։ Տպող ֆունկցիաները՝ տպում են։
- Ֆունկցիան կարող է կանչել ուրիշ ֆունկցիա։
- **Նոր շարահյուսություն այլևս չի լինելու։** Մնացած հինգ օրը այս կոդը դարձնում ենք
  իսկական ծրագիր։

## Ի՞նչ է գալիս հետո

Հաջորդ դասին **փակում ենք տետրը** և բացում իսկական ֆայլ։

**Բեր այսօրվա տետրը** — ուղիղ այս կոդն է տեղափոխվելու այնտեղ։

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Համոզվի՛ր, որ այսօրվա տետրը պահպանված է և աշխատում է վերևից ներքև։
Վաղը այն պետք կգա ամբողջությամբ։
