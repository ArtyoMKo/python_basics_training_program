
#%% md
# Թեմա 8 — Դասարան՝ աշակերտներով լի

### Python 11-րդ դասարանի համար · Թեմա 8-ը 24-ից

Աշակերտը օբյեկտ է։ Բայց դասարանը դեռ **սովորական ցուցակ** է, և ամեն անգամ, երբ
տնօրենը դասարանի մասին բան է հարցնում, մենք գրում ենք նոր ֆունկցիա։

Այսօր դասարանն էլ է դառնում օբյեկտ։

## ԱՅՍՕՐ:

- **Ա մաս:** դասարանը՝ օբյեկտների ցուցակով
- **Բ մաս:** մեթոդներ, որոնք անցնում են ներսի օբյեկտների վրայով
- **Գ մաս:** դպրոցը՝ դասարաններով

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>class Student</code> · մեթոդներ · <code>self.average()</code> ·
<code>__str__</code><br/><br/>
<b>Այսօր օբյեկտը կպարունակի ուրիշ օբյեկտներ։</b>
</p>
</div>

#%% md
## Ա մաս: Ցուցակը, որ ամեն անգամ նույնն է

Ահա աշակերտի դասը, ամբողջական։

#%% code
SUBJECT_NAMES = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]
PASS_MARK = 4


class Student:
    def __init__(self, name, class_name, grades, attendance, note=""):
        self.name = name
        self.class_name = class_name
        self.grades = grades
        self.attendance = attendance
        self.note = note

    def average(self):
        return sum(self.grades) / len(self.grades)

    def has_passed(self):
        return min(self.grades) >= PASS_MARK

    def __str__(self):
        return f"{self.name} ({self.class_name}), average {self.average():.1f}"


group = [
    Student("Ani Hakobyan", "11A", [7, 6, 8, 9, 8], 94),
    Student("Davit Grigoryan", "11A", [5, 3, 6, 5, 7], 78),
    Student("Nare Petrosyan", "11A", [10, 9, 10, 9, 10], 99),
    Student("Aram Harutyunyan", "11A", [3, 2, 4, 3, 5], 65),
]

for student in group:
    print(student)

#%% md
Իսկ հիմա՝ դասարանի մասին հարցերը։ Ամեն մեկի համար՝ առանձին ֆունկցիա։

#%% code
def class_average(students):
    return sum(s.average() for s in students) / len(students)


def class_failing(students):
    return [s for s in students if not s.has_passed()]


def class_best(students):
    return sorted(students, key=lambda s: s.average(), reverse=True)[0]


print(f"average: {class_average(group):.2f}")
print("failing:", [s.name for s in class_failing(group)])
print("best:   ", class_best(group).name)

#%% md
Երեք ֆունկցիա, և երեքն էլ առաջին արգումենտով ստանում են **նույն ցուցակը**։

Դա նույն նշանն է, որ տեսանք 7-րդ թեմայում՝ երբ `average_of(student)`-ը տեղափոխեցինք
աշակերտի ներս։

#%% md
## Բ մաս: Դասարանը՝ օբյեկտ

#%% code
class SchoolClass:
    def __init__(self, name, students=None):
        self.name = name
        if students is None:
            students = []
        self.students = students

    def add(self, student):
        self.students.append(student)

    def size(self):
        return len(self.students)

    def average(self):
        return sum(s.average() for s in self.students) / len(self.students)

    def failing(self):
        return [s for s in self.students if not s.has_passed()]

    def best(self):
        return sorted(self.students, key=lambda s: s.average(), reverse=True)[0]

    def __str__(self):
        return f"{self.name}: {self.size()} students, average {self.average():.2f}"


eleven_a = SchoolClass("11A", group)

print(eleven_a)
print("failing:", [s.name for s in eleven_a.failing()])
print("best:   ", eleven_a.best().name)

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b><code>self.students</code>-ը ցուցակ է, որի ներսում <code>Student</code>
օբյեկտներ են։</b><br/><br/>
<code>eleven_a.best().name</code> — կարդա՛ ձախից աջ.<br/>
«վերցրու դասարանը → հարցրու լավագույնին → վերցրու նրա անունը»։
</p>
</div>

#%% md
### `students=None`, ոչ թե `students=[]`

Նկատի՛ր `__init__`-ի առաջին տողերը։ Սա հենց այն թակարդն է, որ տեսանք 2-րդ թեմայի
Մարտահրավերում։

**Գործարկի՛ր ներքևի բջիջը և նայի՛ր, թե ինչ է լինում, երբ կանխադրվածը ցուցակ է։**

#%% code
class Broken:
    def __init__(self, name, students=[]):
        self.name = name
        self.students = students


first = Broken("11A")
second = Broken("11B")

first.students.append("Ani")

print("first: ", first.students)
print("second:", second.students)
print("the same list?", first.students is second.students)

#%% md
<div style="border-left: 6px solid #d33; background: #fff5f5; padding: 12px 16px; margin: 12px 0;">
<p style="color:#d33; margin:0;">
🔍 <b>Երկու դասարան, մեկ ցուցակ։</b> Սխալի հաղորդագրություն չկա — պարզապես
11B-ում հայտնվեց աշակերտ, որին այնտեղ չենք դրել։<br/><br/>
<b>Կանոն:</b> կանխադրված արժեքը երբեք չպետք է լինի ցուցակ կամ բառարան։ Գրի՛ր
<code>None</code>, և ցուցակը սարքի՛ր ներսում։
</p>
</div>

#%% md
## Գ մաս: Դպրոցը՝ դասարաններով

Նույն ձևը ևս մեկ շերտ վեր։

#%% code
class School:
    def __init__(self, name):
        self.name = name
        self.classes = []

    def add(self, school_class):
        self.classes.append(school_class)

    def students(self):
        everyone = []
        for school_class in self.classes:
            everyone = everyone + school_class.students
        return everyone

    def size(self):
        return len(self.students())

    def average(self):
        people = self.students()
        return sum(s.average() for s in people) / len(people)

    def __str__(self):
        return (f"{self.name}: {len(self.classes)} classes, "
                f"{self.size()} students, average {self.average():.2f}")


school = School("School N 5")
school.add(eleven_a)
school.add(SchoolClass("11B", [
    Student("Mariam Sargsyan", "11B", [8, 7, 9, 8, 10], 97),
    Student("Tigran Mkrtchyan", "11B", [6, 5, 7, 6, 7], 88),
]))

print(school)
for school_class in school.classes:
    print(" ", school_class)

#%% md
**Երեք շերտ՝ դպրոց → դասարան → աշակերտ։** Ամեն շերտը գիտի միայն իր ներքևինը։

`school.average()` չի իմանում, թե ինչպես է հաշվվում աշակերտի միջինը — այն
պարզապես հարցնում է։

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Հաճախումների միջինը

Ավելացրո՛ւ `SchoolClass`-ին `attendance()` մեթոդ, որը վերադարձնում է դասարանի
միջին հաճախումը։

#%% code
# Add the method to SchoolClass, then:
# print(eleven_a.attendance())

#%% md
### 2. Ամենացածրը

Ավելացրո՛ւ `worst()` մեթոդ՝ `best()`-ի նմանությամբ։

#%% code
# ...

#%% md
### 3. Որոնել ըստ անվան

Ավելացրո՛ւ `find(name)` մեթոդ, որը վերադարձնում է այդ անունով աշակերտին, կամ
`None`, եթե չկա։

#%% code
# found = eleven_a.find("Nare Petrosyan")
# print(found)
# print(eleven_a.find("Someone Else"))

#%% md
### 4. Դասարանի հաշվետվությունը

Ավելացրո՛ւ `report()` մեթոդ, որը տպում է դասարանի վերնագիրը և ամեն աշակերտի
տողը՝ դասավորված ըստ միջինի։

#%% code
# eleven_a.report()

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Առարկայի միջինը դասարանում

Ավելացրո՛ւ `subject_average(index)` մեթոդ, որը վերադարձնում է տվյալ առարկայի
միջինը ամբողջ դասարանում։

#%% code
# for i in range(len(SUBJECT_NAMES)):
#     print(f"{SUBJECT_NAMES[i]:<14} {eleven_a.subject_average(i):.2f}")

#%% md
### 6. Տեղափոխել աշակերտին

Ավելացրո՛ւ `School`-ին `move(student_name, from_class, to_class)` մեթոդ։
Ուշադի՛ր եղիր՝ աշակերտի `class_name`-ն էլ պետք է փոխվի։

#%% code
# ...

#%% md
### 7. Ամենալավ դասարանը

Ավելացրո՛ւ `School`-ին `best_class()` մեթոդ։

#%% code
# print(school.best_class().name)

#%% md
### 8. Ամբողջ դպրոցը ֆայլից

Կարդա՛ `school.csv`-ը և կառուցի՛ր `School` օբյեկտ՝ երեք `SchoolClass`-ով և
36 `Student`-ով։ Ապա տպի՛ր դպրոցը և երեք դասարանը։

**Ստուգի՛ր:** դպրոցի միջինը պետք է լինի **7.0**։

#%% code
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

# Build name -> (class, [grades]) first, then the objects.
# ...

#%% md
## Մարտահրավեր

#%% md
### 9. Երկու ուղղությամբ կապ

Հիմա աշակերտը գիտի իր դասարանի **անունը**, բայց ոչ իր **դասարանը**։ Ավելացրո՛ւ
`SchoolClass.add()`-ին տող, որը աշակերտի մեջ պահում է նաև դասարանի օբյեկտը՝
`student.school_class = self`։

Ապա ստուգի՛ր՝ `ani.school_class.average()` պետք է աշխատի։

Markdown-ում գրի՛ր, թե ինչ վտանգ կա այս ձևում։

#%% code
# ...

#%% md
### 10. Դպրոցը՝ առանց ցուցակների միացման

`School.students()`-ը ամեն կանչի ժամանակ նոր ցուցակ է սարքում՝ միացնելով բոլոր
դասարանների ցուցակները։ 36 աշակերտի համար դա նկատելի չէ, 3000-ի համար՝ արդեն այո։

Վերագրի՛ր `School.average()`-ը այնպես, որ այն **ոչ մի նոր ցուցակ չսարքի**։

#%% code
# ...

#%% md
<div style="border-left: 6px solid #747; background: #f8f6fb; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#747; margin-top:0;">🏠 Տնային</h3>
<p style="color:#747; margin-bottom:0;">
Այս նոթատետրի <b>Պարտադիր</b> առաջադրանքները — այս նիստում երկու նոթատետր ենք անցնում, և դրանք դասին չեն տեղավորվում։<br/><b>Լրացուցիչը տանը պետք չէ անել։</b><br/><br/>
<b>Նոր բան չկա</b> — ամեն առաջադրանք այս նոթատետրից է, նույն ձևի, ինչ դասին
արածները, և օգտագործում է միայն այն, ինչ այսօր սովորեցինք։<br/>
Հաջորդ նիստը սկսվում է դրանց ստուգումով։
</p>
</div>

#%% md
## Ինչի հասանք

- Օբյեկտը կարող է պարունակել **ուրիշ օբյեկտների ցուցակ**
- `self.students` — ցուցակ `Student`-երով, ոչ թե տողերով
- Մեթոդը կարող է անցնել ներսի օբյեկտների վրայով և **հարցնել** նրանց
- `eleven_a.best().name` — շղթա, կարդացվում է ձախից աջ
- **Կանխադրված արժեքը երբեք ցուցակ չէ** — գրի՛ր `None`
- Երեք շերտ՝ դպրոց → դասարան → աշակերտ։ Ամեն շերտը գիտի միայն ներքևինը

## Ի՞նչ է գալիս հետո

Դպրոցում ուսուցիչներ էլ կան։ Նրանք ունեն անուն, դասարան և հեռախոս՝ ինչպես
աշակերտը։ Եվ ունեն առարկա ու աշխատավարձ՝ ինչպես աշակերտը **չունի**։

Հաջորդ նիստում կպատճենենք ամբողջ `Student` դասը և կխմբագրենք։ Հետո՝ նույն նիստում — կստանանք
այն, ինչով դա արվում է **առանց պատճենելու**։
