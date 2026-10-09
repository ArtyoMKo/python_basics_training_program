
#%% md
# Թեմա 6 — Աշակերտը մեկ թիվ չէ

### Python 11-րդ դասարանի համար · Թեմա 6-ը 24-ից

Մինչ այժմ մեր մատյանում աշակերտը **մեկ անուն և մեկ թիվ** էր։

Իսկ իրական մատյանում նա ունի դասարան, հինգ առարկայի գնահատական, հաճախումներ և
ծանոթագրություն։ Այսօր կառուցում ենք հենց այդպիսի մատյան։

## ԱՅՍՕՐ:

- **Ա մաս:** աշակերտը՝ բառարանով
- **Բ մաս:** աշակերտը՝ նկարագրված մեկ անգամ
- **Գ մաս:** երկու տարբերակը կողք կողքի

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>register = {"Ani": 9}</code> — մեկ անուն, մեկ թիվ։<br/>
Ֆունկցիաներ կանխադրված արժեքներով, ցուցակներ մեկ տողով։<br/><br/>
<b>Այսօր առաջին անգամ դաս ենք գրելու։</b>
</p>
</div>

#%% md
## Ա մաս: Աշակերտը՝ բառարանով

Այն, ինչ գիտենք անել, մեկ բան է՝ **բառարան ամեն աշակերտի համար**։

<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Այս ձևն աշխատում է, բայց փխրուն է։</b> Դասի երկրորդ կեսին կսովորենք մի ձև,
որով աշակերտը նկարագրվում է <b>մեկ անգամ</b>, իսկ 36-ը ստեղծվում են մեկ տողով։
</p>
</div>

**Գործարկի՛ր և կարդա՛։**

#%% code
ani = {
    "name": "Ani Hakobyan",
    "class": "11A",
    "mathematics": 7,
    "physics": 6,
    "armenian": 8,
    "history": 9,
    "informatics": 8,
    "attendance": 94,
    "note": "",
}

davit = {
    "name": "Davit Grigoryan",
    "class": "11A",
    "mathematics": 5,
    "physics": 3,
    "armenian": 6,
    "history": 5,
    "informatics": 7,
    "attendance": 78,
    "note": "absent in March",
}

print(ani["name"], ani["class"])
print(davit["name"], davit["class"])

#%% md
Ինը տող՝ մեկ աշակերտի համար։ Դպրոցում 36 աշակերտ է։

Հիմա՝ ֆունկցիաները, որոնք աշխատում են այս բառարանների հետ։

#%% code
SUBJECTS = ["mathematics", "physics", "armenian", "history", "informatics"]
PASS_MARK = 4


def average_of(student):
    total = 0
    for subject in SUBJECTS:
        total = total + student[subject]
    return total / len(SUBJECTS)


def failed_subjects(student):
    return [s for s in SUBJECTS if student[s] < PASS_MARK]


def report_line(student):
    return f"{student['name']:<20} {student['class']}  {average_of(student):.1f}"


print(report_line(ani))
print(report_line(davit))
print("Davit failed:", failed_subjects(davit))

#%% md
**Հիմա դու։** Ավելացրո՛ւ երկու աշակերտ՝ Nare և Aram։ Պատճենի՛ր վերևի ձևը։

#%% code
nare = {
    # nine lines, like Ani's
    # ...
}

aram = {
    # nine lines again
    # ...
}

# print(report_line(nare))
# print(report_line(aram))

#%% md
### Եվ հիմա՝ մեկ տառ

Տնօրենը խնդրում է խմբավորել աշակերտներին ըստ դասարանի։ Ահա ևս մեկ աշակերտ, որը
գրել է գործընկերը։

**Նայի՛ր ուշադիր։ Սխալ տեսնո՞ւմ ես։**

#%% code
mariam = {
    "name": "Mariam Sargsyan",
    "clas": "11B",
    "mathematics": 8,
    "physics": 7,
    "armenian": 9,
    "history": 8,
    "informatics": 10,
    "attendance": 97,
    "note": "",
}

# Everything still works:
print(average_of(mariam))
print(failed_subjects(mariam))

#%% md
Երկու ֆունկցիան աշխատեց։ Սխալի հաղորդագրություն չկա։

Հիմա՝ խմբավորումը։ **Գործարկի՛ր և կարդա՛ սխալը։**

#%% code expected-error: KeyError
students = [ani, davit, mariam]

by_class = {}
for student in students:
    class_name = student["class"]
    if class_name not in by_class:
        by_class[class_name] = []
    by_class[class_name].append(student["name"])

print(by_class)

#%% md
<div style="border-left: 6px solid #d33; background: #fff5f5; padding: 12px 16px; margin: 12px 0;">
<p style="color:#d33; margin:0;">
🔍 <b><code>KeyError: 'class'</code></b><br/><br/>
Python-ը ասում է՝ այդ բանալին չկա։ Բայց <b>չի ասում, թե որ աշակերտի մոտ</b>, և
չի ասում, թե <b>որտեղ է սխալը թույլ տրվել</b>։<br/><br/>
Սխալը գրվել է 30 տող վերևում՝ բառարանը ստեղծելիս։ Երևաց հիմա։<br/>
Միջև ընկած ժամանակում <code>average_of</code>-ը և <code>failed_subjects</code>-ը
<b>հանգիստ աշխատեցին</b>։
</p>
</div>

#%% md
## Բ մաս: Նկարագրել աշակերտին մեկ անգամ

Խնդիրը սա է՝ **ոչ մի տեղ գրված չէ, թե ինչ է աշակերտը**։ Ամեն բառարան ինքնուրույն
է, և ոչինչ չի ստուգում, որ դրանք նույն ձևի են։

Python-ում կարելի է գրել **ձևանմուշ** — մեկ անգամ ասել, թե աշակերտն ինչ ունի։
Դրան ասում են **դաս** (class)։

#%% code
class Student:
    def __init__(self, name, class_name, grades, attendance, note=""):
        self.name = name
        self.class_name = class_name
        self.grades = grades
        self.attendance = attendance
        self.note = note


ani = Student("Ani Hakobyan", "11A", [7, 6, 8, 9, 8], 94)

print(ani)
print(ani.name)
print(ani.class_name)
print(ani.grades)

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#0a7; margin-top:0;">✅ Երեք բառ, որ պետք է հասկանալ</h3>
<p style="color:#0a7; margin-bottom:0;">
<b><code>class Student:</code></b> — ձևանմուշը։ Նկարագրություն, ոչ թե աշակերտ։<br/>
<b><code>__init__</code></b> — «սարքիր մեկը»։ Կանչվում է ավտոմատ, երբ գրում ես
<code>Student(...)</code>։<br/>
<b><code>self</code></b> — <b>այն մեկը, որը հենց հիմա սարքվում է</b>։
<code>self.name = name</code> նշանակում է՝ «այս աշակերտի անունը թող լինի այս»։<br/><br/>
<b>Սահմանելը ստեղծել չէ։</b> <code>class Student:</code> — ոչ մի աշակերտ չկա։
<code>Student("Ani", ...)</code> — հիմա կա մեկը։
</p>
</div>

#%% md
Ձևանմուշը գրված է **մեկ անգամ**։ Աշակերտները՝ մեկ տողով մեկը։

#%% code
davit = Student("Davit Grigoryan", "11A", [5, 3, 6, 5, 7], 78, "absent in March")
nare = Student("Nare Petrosyan", "11B", [10, 9, 10, 9, 10], 99)
aram = Student("Aram Harutyunyan", "11B", [3, 2, 4, 3, 5], 65, "needs support")

for student in [ani, davit, nare, aram]:
    print(f"{student.name:<20} {student.class_name}  {student.attendance}%")

#%% md
Ֆունկցիաները գրեթե չփոխվեցին։ Քառակուսի փակագծերի փոխարեն՝ **կետ**։

#%% code
def average_of(student):
    return sum(student.grades) / len(student.grades)


def report_line(student):
    return f"{student.name:<20} {student.class_name}  {average_of(student):.1f}"


for student in [ani, davit, nare, aram]:
    print(report_line(student))

#%% md
## Գ մաս: Նույն սխալը, նորից

Հիմա փորձի՛ր թույլ տալ **ճիշտ նույն սխալը**՝ սխալ գրիր դասարանի անունը։

**Գործարկի՛ր և համեմատի՛ր։**

#%% code
# A typo in a keyword argument, exactly like "clas" before
try:
    mariam = Student("Mariam Sargsyan", clas_name="11B", grades=[8, 7, 9, 8, 10],
                     attendance=97)
except TypeError as problem:
    print("TypeError:", problem)

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b>Սխալը երևաց հենց այնտեղ, որտեղ գրվել է։</b><br/><br/>
Ոչ թե 30 տող հետո, ոչ թե ուրիշ ֆունկցիայի ներսում։ <b>Նույն տողում։</b><br/>
Եվ Python-ը անունն էլ ասաց՝ <code>clas_name</code>։
</p>
</div>

### Երկու տարբերակը կողք կողքի

| | Բառարանով | Դասով |
|---|---|---|
| Աշակերտը նկարագրված է | **36 անգամ** | **մեկ անգամ** |
| Մեկ աշակերտ ստեղծելը | 9 տող | 1 տող |
| Տառասխալը երևում է | **օգտագործելիս**, հեռու | **ստեղծելիս**, տեղում |
| Նոր դաշտ ավելացնելը | 36 տեղ | 1 տեղ |
| Ի՞նչ է աշակերտը | ոչ մի տեղ գրված չէ | `class Student` |

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Ուսուցչի դասը

Գրի՛ր `Teacher` դաս՝ անունով, առարկայով և աշխատանքային տարիների թվով։
Ստեղծի՛ր երկուսը և տպի՛ր։

#%% code
class Teacher:
    def __init__(self, name, subject, years):
        # three lines
        # ...
        pass


# tigran = Teacher("Tigran Mkrtchyan", "Mathematics", 12)
# print(tigran.name, tigran.subject, tigran.years)

#%% md
### 2. Կանխադրված արժեք դասում

Ավելացրո՛ւ `Teacher`-ին `school` պարամետր՝ կանխադրված `"School N 5"` արժեքով։
Ստեղծի՛ր մեկը առանց այդ արգումենտի և մեկը՝ դրանով։

#%% code
# ...

#%% md
### 3. Չորս աշակերտ՝ ցուցակից

Ահա տվյալները ցուցակների ցուցակի տեսքով։ Կառուցի՛ր `Student` օբյեկտների ցուցակ
**մեկ ցիկլով**։

#%% code
raw = [
    ["Lilit Khachatryan", "11C", [9, 8, 9, 10, 9], 96],
    ["Gor Vardanyan", "11C", [4, 5, 4, 6, 5], 81],
    ["Anahit Avetisyan", "11A", [7, 5, 8, 7, 8], 90],
]

group = []
# ...

for student in group:
    print(student.name, student.class_name)

#%% md
### 4. Չանցած առարկաները

Գրի՛ր ֆունկցիա, որը `Student` օբյեկտից վերադարձնում է չանցած առարկաների
**անունների** ցուցակը։ Առարկաների անունները `SUBJECT_NAMES`-ում են։

#%% code
SUBJECT_NAMES = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]


def failed_subjects(student, pass_mark=4):
    # student.grades is a list of five numbers, in the same order as SUBJECT_NAMES
    # ...
    return []


# print(failed_subjects(aram))

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Հաճախումների նախազգուշացում

Գրի՛ր ֆունկցիա, որը վերադարձնում է այն աշակերտների ցուցակը, որոնց հաճախումը
85%-ից ցածր է։ Օգտագործի՛ր մեկ տողով ցուցակ։

#%% code
everyone = [ani, davit, nare, aram]

low_attendance = []
print([s.name for s in low_attendance])

#%% md
### 6. Դպրոցի դասը

Գրի՛ր `School` դաս՝ անունով և հասցեով։ Ավելացրո՛ւ նաև `students` պարամետր,
կանխադրված **դատարկ ցուցակ**։

Հետո գործարկի՛ր 2-րդ թեմայի 10-րդ Մարտահրավերը մտքումդ. ինչո՞ւ է կանխադրված
դատարկ ցուցակը վտանգավոր։

#%% code
# ...

#%% md
### 7. Ամենաբարձր միջինը

Դասավորի՛ր `everyone` ցուցակը ըստ միջինի՝ նվազման կարգով, և տպի՛ր առաջինի
անունը։ Օգտագործի՛ր `lambda`, ինչպես երեկ։

#%% code
# ...

#%% md
### 8. Դպրոցի ֆայլից՝ օբյեկտներ

Կարդա՛ `school.csv`-ը և կառուցի՛ր **36 `Student` օբյեկտ**։ Ամեն աշակերտի հինգ
տող ֆայլում պետք է դառնա մեկ օբյեկտ՝ հինգ գնահատականով։

#%% code
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

# First collect name -> list of grades, then build the objects.
school = []
print(len(school), "students")

#%% md
## Մարտահրավեր

#%% md
### 9. Ի՞նչ է կատարվում առանց `self`-ի

Ահա դաս, որտեղ `self`-ը մոռացվել է։ Գործարկի՛ր, կարդա՛ սխալը, և markdown բջիջում
բացատրի՛ր, թե ինչու է Python-ը դժգոհում։

#%% code
class Broken:
    def __init__(name, subject):
        self.name = name
        self.subject = subject


# broken = Broken("Ani", "Physics")
# Uncomment the line above, run it, and read the error.

#%% md
### 10. Երկու անուն, մեկ օբյեկտ

Գործարկի՛ր ներքևի բջիջը և բացատրի՛ր արդյունքը։

**Հուշում:** օբյեկտը, ինչպես ցուցակը, փոփոխվող է։ `second = first` նոր օբյեկտ
չի սարքում։

#%% code
first = Student("Sona Martirosyan", "11A", [8, 8, 8, 8, 8], 92)
second = first

second.class_name = "11C"

print(first.class_name)
print(second.class_name)
print(first is second)

#%% md
<div style="border-left: 6px solid #747; background: #f8f6fb; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#747; margin-top:0;">🏠 Տնային</h3>
<p style="color:#747; margin-bottom:0;">
Այս նոթատետրի <b>Լրացուցիչ</b> առաջադրանքները։<br/><br/>
<b>Նոր բան չկա</b> — ամեն առաջադրանք այս նոթատետրից է, և օգտագործում է միայն այն,
ինչ այսօր սովորեցինք։<br/>
Հաջորդ նիստը սկսվում է դրանց ստուգումով։
</p>
</div>

#%% md
## Ինչի հասանք

- `class Student:` — **ձևանմուշ**, գրվում է մեկ անգամ
- `__init__` — կանչվում է ավտոմատ, երբ ստեղծում ես օբյեկտ
- `self` — **այն մեկը, որը հենց հիմա սարքվում է**
- `student.name` — կետ, ոչ թե քառակուսի փակագիծ
- **Սահմանելը ստեղծել չէ**
- Բառարանում տառասխալը երևում է **օգտագործելիս**։ Դասում՝ **ստեղծելիս**
- `second = first` — նոր օբյեկտ չի սարքում

## Ի՞նչ է գալիս հետո

`average_of(student)`-ը դեռ առանձին ֆունկցիա է։ Վաղը այն **տեղափոխվում է
աշակերտի ներս** — և կանչվում է այսպես՝ `student.average()`։
