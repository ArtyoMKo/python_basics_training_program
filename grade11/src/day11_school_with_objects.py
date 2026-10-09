#%% md
# Թեմա 11 — Մատյանը, վերագրված

### Python 11-րդ դասարանի համար · Թեմա 11-ը 24-ից

Այսօր **նոր շարահյուսություն չկա**։

Վերցնում ենք անցած դասընթացի մատյանը՝ այն, որ գրել ես բառարաններով, և վերագրում
ենք ամբողջությամբ՝ օբյեկտներով։ Կողք կողքի։

## ԱՅՍՕՐ:

- **Ա մաս:** հին մատյանը, ամբողջությամբ
- **Բ մաս:** նույնը՝ օբյեկտներով
- **Գ մաս:** ի՞նչ փոխվեց, և ի՞նչը՝ ոչ

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Այս բլոկում սովորեցինք</h3>
<p style="color:#06c; margin-bottom:0;">
<code>class</code> · <code>__init__</code> · <code>self</code> · մեթոդներ ·
<code>__str__</code> · օբյեկտ օբյեկտի մեջ · <code>class X(Y)</code> ·
<code>super()</code> · վերասահմանում<br/><br/>
<b>Այսօր այս ամենը մեկ ծրագրում է։</b>
</p>
</div>

#%% md
## Ա մաս: Հին մատյանը

Ահա այն, ինչ գրել ես անցած դասընթացում՝ բառարաններով և առանձին ֆունկցիաներով։

**Գործարկի՛ր և հիշի՛ր։**

#%% code
PASS_MARK = 4
SUBJECT_NAMES = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]

register = {
    "Ani Hakobyan": {"class": "11A", "grades": [7, 6, 8, 9, 8], "attendance": 94},
    "Davit Grigoryan": {"class": "11A", "grades": [5, 3, 6, 5, 7], "attendance": 78},
    "Nare Petrosyan": {"class": "11B", "grades": [10, 9, 10, 9, 10], "attendance": 99},
    "Aram Harutyunyan": {"class": "11B", "grades": [3, 2, 4, 3, 5], "attendance": 65},
}


def average_of(entry):
    return sum(entry["grades"]) / len(entry["grades"])


def has_passed(entry):
    return min(entry["grades"]) >= PASS_MARK


def report_line(name, entry):
    if has_passed(entry):
        status = "passed"
    else:
        status = "failed"
    return f"{name:<20} {entry['class']}  {average_of(entry):.1f}  {status}"


def class_report(register, class_name):
    print(f"--- {class_name} ---")
    total = 0
    count = 0
    for name in register:
        entry = register[name]
        if entry["class"] == class_name:
            print(report_line(name, entry))
            total = total + average_of(entry)
            count = count + 1
    print(f"class average: {total / count:.2f}")


class_report(register, "11A")
class_report(register, "11B")

#%% md
Աշխատում է։ Եվ նկատի՛ր երեք բան.

| | |
|---|---|
| Ամեն ֆունկցիա ստանում է `entry` | և պետք է **հիշի**, թե ինչ բանալիներ ունի այն |
| `name`-ը առանձին է `entry`-ից | այդ պատճառով `report_line`-ը ունի **երկու** արգումենտ |
| `class_report`-ը զտում, տպում և հաշվում է | երեք գործ՝ մեկ ֆունկցիայում |

#%% md
## Բ մաս: Նույնը՝ օբյեկտներով

#%% code
class Person:
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name

    def label(self):
        return f"{self.name:<20} {self.class_name}"


class Student(Person):
    def __init__(self, name, class_name, grades, attendance):
        super().__init__(name, class_name)
        self.grades = grades
        self.attendance = attendance

    def average(self):
        return sum(self.grades) / len(self.grades)

    def has_passed(self):
        return min(self.grades) >= PASS_MARK

    def failed_subjects(self):
        return [SUBJECT_NAMES[i] for i in range(len(self.grades))
                if self.grades[i] < PASS_MARK]

    def label(self):
        status = "passed" if self.has_passed() else "failed"
        return super().label() + f"  {self.average():.1f}  {status}"

    def __str__(self):
        return self.label()


class SchoolClass:
    def __init__(self, name, students=None):
        self.name = name
        if students is None:
            students = []
        self.students = students

    def add(self, student):
        self.students.append(student)

    def average(self):
        return sum(s.average() for s in self.students) / len(self.students)

    def failing(self):
        return [s for s in self.students if not s.has_passed()]

    def report(self):
        print(f"--- {self.name} ---")
        for student in sorted(self.students, key=lambda s: s.average(), reverse=True):
            print(student)
        print(f"class average: {self.average():.2f}")


eleven_a = SchoolClass("11A", [
    Student("Ani Hakobyan", "11A", [7, 6, 8, 9, 8], 94),
    Student("Davit Grigoryan", "11A", [5, 3, 6, 5, 7], 78),
])
eleven_b = SchoolClass("11B", [
    Student("Nare Petrosyan", "11B", [10, 9, 10, 9, 10], 99),
    Student("Aram Harutyunyan", "11B", [3, 2, 4, 3, 5], 65),
])

eleven_a.report()
eleven_b.report()

#%% md
## Գ մաս: Ի՞նչ փոխվեց

### Ի՞նչ դարձավ ավելի լավ

| | Բառարաններով | Օբյեկտներով |
|---|---|---|
| Աշակերտը նկարագրված է | ոչ մի տեղ | `class Student` |
| Անունը և տվյալները | **առանձին** | **միասին** |
| `report_line` արգումենտներ | 2 | 0 |
| Դասարանը զտվում է ամեն անգամ | այո | ոչ — այն **ունի** իր աշակերտներին |
| Տառասխալը երևում է | օգտագործելիս | ստեղծելիս |
| Նոր տեսակ (ուսուցիչ) ավելացնելը | նոր ֆունկցիաներ ամենուր | `class Teacher(Person)` |

### Ի՞նչը չփոխվեց

**Ցիկլերը նույնն են։ `if`-երը նույնն են։ Հաշվարկները նույնն են։**

`sum(self.grades) / len(self.grades)` — ուղիղ նույն տողն է, որ գրել ես անցած
դասընթացում։ Օբյեկտը չփոխեց **ինչպես ենք հաշվում**։ Փոխեց **որտեղ է գրված
հաշվարկը**։

<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Օբյեկտը նոր մաթեմատիկա չէ։ Նոր կարգ է։</b><br/><br/>
Եթե ծրագիրը փոքր է — բառարանը լրիվ բավական է, և ավելորդ դաս գրելը <b>վատ է</b>։<br/>
Օբյեկտը սկսում է արժենալ այն ժամանակ, երբ տվյալը ունի <b>շատ դաշտ</b>, <b>շատ
տեսակ</b>, և <b>գործողություններ, որոնք միայն իրեն են վերաբերում</b>։
</p>
</div>

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Ուսուցիչը՝ մատյանում

Ավելացրո՛ւ `Teacher(Person)` դաս՝ առարկայով։ Վերասահմանի՛ր `label()`-ը։
Ավելացրո՛ւ մեկ ուսուցիչ ամեն դասարանին և տպի՛ր հաշվետվությունները։

**Ուշադի՛ր:** `SchoolClass.average()`-ը չպետք է ուսուցչին հաշվի։

#%% code
# ...

#%% md
### 2. Դպրոցը՝ ամբողջությամբ

Գրի՛ր `School` դաս, որը պարունակում է `SchoolClass`-եր, և ունի `report()`
մեթոդ, որը տպում է բոլոր դասարանների հաշվետվությունները և դպրոցի միջինը։

#%% code
# ...

#%% md
### 3. Չանցածների ցուցակը

Ավելացրո՛ւ `School`-ին `at_risk()` մեթոդ, որը վերադարձնում է բոլոր չանցած
աշակերտների ցուցակը՝ ամբողջ դպրոցից։

#%% code
# ...

#%% md
### 4. Ֆայլից՝ ամբողջ դպրոցը

Կառուցի՛ր `school.csv`-ից ամբողջական `School` օբյեկտ՝ 3 դասարան, 36 աշակերտ։

**Ստուգի՛ր այս երեք թիվը.**

| | |
|---|---|
| աշակերտներ | 36 |
| դպրոցի միջինը | 7.0 |
| ռիսկի տակ | 12 |

#%% code
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

# Collect name -> (class, [grades]) first, then build the objects.
# ...

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Առարկայի հաշվետվությունը

Ավելացրո՛ւ `School`-ին `subject_report()` մեթոդ, որը տպում է ամեն առարկայի
միջինը ամբողջ դպրոցում՝ դասավորված ըստ միջինի։

**Ստուգի՛ր:** Informatics-ը պետք է լինի ամենաբարձրը (7.56), Physics-ը՝
ամենացածրը (6.28)։

#%% code
# ...

#%% md
### 6. Հաճախումների զեկույցը

Ավելացրո՛ւ `attendance` դաշտը ֆայլից կառուցված աշակերտներին (սարքի՛ր այն՝
`85 + (index % 15)` բանաձևով) և տպի՛ր 90%-ից ցածր հաճախող աշակերտներին։

#%% code
# ...

#%% md
### 7. Լավագույնը ամեն դասարանից

Տպի՛ր ամեն դասարանի լավագույն աշակերտին՝ մեկ տողով դասարանի համար։

#%% code
# ...

#%% md
### 8. Բառարանից դեպի օբյեկտ

Գրի՛ր ֆունկցիա, որը հին `register` բառարանը վերածում է `Student` օբյեկտների
ցուցակի։ Սա այն գործողությունն է, որ պետք կգա, երբ հին ծրագիրը նորի վրա տեղափոխես։

#%% code
def register_to_students(register):
    # ...
    return []


# print([str(s) for s in register_to_students(register)])

#%% md
## Մարտահրավեր

#%% md
### 9. Երկու տարբերակը՝ նույն պատասխանով

Գրի՛ր ստուգում, որը **ապացուցում է**, որ երկու տարբերակը տալիս են նույն
արդյունքը՝ համեմատելով 11A դասարանի միջինը հին և նոր ձևով։

Ստուգումը պետք է տպի `True`։

#%% code
# ...

#%% md
### 10. Ե՞րբ օբյեկտը ավելորդ է

Ահա դաս, որը **չպետք է գրվեր**.

```python
class Grade:
    def __init__(self, value):
        self.value = value
```

Markdown-ում գրի՛ր, թե ինչու, և ինչ պետք է լիներ դրա փոխարեն։

Ապա գտի՛ր քո գրած կոդում մի տեղ, որտեղ դաս գրելը **արժեր**, և մի տեղ, որտեղ
բառարանը լրիվ բավական էր։

#%% code
# No code needed -- the answer goes in a markdown cell.

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

- Նույն մատյանը՝ երկու ձևով, կողք կողքի
- Օբյեկտը **միացնում է** տվյալը և գործողությունը
- Ցիկլերը, `if`-երը և հաշվարկները **չփոխվեցին**
- Փոխվեց այն, թե **որտեղ են դրանք գրված**
- **Օբյեկտը նոր մաթեմատիկա չէ, նոր կարգ է** — և փոքր ծրագրում ավելորդ է

## Ի՞նչ է գալիս հետո

**Միջանկյալ թեստը հանձնվում է այս դասից հետո** — առանձին նիստով, 60–75 րոպե։
Այն ընդգրկում է 2-րդից 11-րդ թեմաները։

Հետո սկսվում է դասընթացի երկրորդ կեսը։ Նախարարությունը խնդրում է կիսամյակի
թվերը՝ միջին, ամենաբարձր, ամենացածր, և թե **որքան ցրված** են գնահատականները։

Դա 600 թիվ է։ Մեկ ցիկլով կսկսենք, և նույն դասին կստանանք մի գործիք, որը
այդ ամենը անում է **չորս տողով**։
