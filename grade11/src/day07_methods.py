
#%% md
# Թեմա 7 — Հաշվարկը տեղափոխվում է ներս

### Python 11-րդ դասարանի համար · Թեմա 7-ը 24-ից

Երեկ աշակերտը դարձավ օբյեկտ։ Բայց `average_of(student)`-ը մնաց **դրսում**՝
առանձին ֆունկցիա։

Այսօր այն տեղափոխվում է ներս, և կանչվում է այսպես՝ `student.average()`։

## ԱՅՍՕՐ:

- **Ա մաս:** ֆունկցիան դասի ներսում
- **Բ մաս:** մեթոդներ, որոնք օգտագործում են միմյանց
- **Գ մաս:** `__str__` — երբ օբյեկտը ինքն իրեն տպում է

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>class Student:</code> · <code>__init__</code> · <code>self</code> ·
<code>student.name</code><br/><br/>
<b>Այսօր դասի ներսում կգրենք ոչ միայն տվյալ, այլև գործողություն։</b>
</p>
</div>

#%% md
## Ա մաս: Ֆունկցիան, որ դրսում է

Ահա երեկվա վիճակը։

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


def average_of(student):
    return sum(student.grades) / len(student.grades)


def has_passed(student):
    return min(student.grades) >= PASS_MARK


ani = Student("Ani Hakobyan", "11A", [7, 6, 8, 9, 8], 94)
aram = Student("Aram Harutyunyan", "11B", [3, 2, 4, 3, 5], 65, "needs support")

print(average_of(ani), has_passed(ani))
print(average_of(aram), has_passed(aram))

#%% md
Աշխատում է։ Բայց նկատի՛ր մի բան.

`Student`-ը և `average_of`-ը **առանձին են**, բայց մեկը առանց մյուսի անիմաստ է։
Եթե վաղը `grades`-ը դառնա բառարան, `average_of`-ը կկոտրվի — և ոչինչ չի հիշեցնի,
որ պետք է այն էլ ուղղել։

#%% md
## Բ մաս: Ֆունկցիան՝ ներսում

Տեղափոխում ենք ֆունկցիան դասի ներս։ Փոխվում է **երկու բան**.

1. Գրվում է `class`-ի ներսում, ներս ընկած
2. Առաջին պարամետրը դառնում է `self`

#%% code
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


ani = Student("Ani Hakobyan", "11A", [7, 6, 8, 9, 8], 94)
aram = Student("Aram Harutyunyan", "11B", [3, 2, 4, 3, 5], 65, "needs support")

print(ani.average(), ani.has_passed())
print(aram.average(), aram.has_passed())

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b>Դասի ներսում գրված ֆունկցիային ասում են <b>մեթոդ</b>։</b><br/><br/>
<code>self</code>-ը գրվում է սահմանելիս, բայց <b>չի գրվում կանչելիս</b>։<br/>
<code>def average(self):</code> &nbsp;→&nbsp; <code>ani.average()</code><br/><br/>
Python-ը ինքն է <code>ani</code>-ն դնում <code>self</code>-ի տեղը։
</p>
</div>

#%% md
**Փակագծերը պարտադիր են։** Առանց դրանց արդյունքը սխալ չէ, բայց այն չէ, ինչ սպասում ես։

#%% code
print(ani.average)
print(ani.average())

#%% md
Առաջին տողը **ֆունկցիան ինքն է**, երկրորդը՝ **նրա պատասխանը**։ Սա այն սխալն է, որ
ամենահաճախն է լինում՝ և սխալի հաղորդագրություն չի տալիս։

Իսկ ահա այն սխալը, որը **տալիս է**։ **Գործարկի՛ր և կարդա՛։**

#%% code expected-error: AttributeError
print(ani.avarage())

#%% md
<div style="border-left: 6px solid #d33; background: #fff5f5; padding: 12px 16px; margin: 12px 0;">
<p style="color:#d33; margin:0;">
🔍 <b><code>AttributeError: 'Student' object has no attribute 'avarage'</code></b><br/><br/>
Python-ը ասում է երեք բան՝ <b>ո՞ր դասի</b> օբյեկտ, <b>ի՞նչ անուն</b> էր փնտրում,
և որ այն <b>չկա</b>։<br/><br/>
Երեկ բառարանի տառասխալը տալիս էր <code>KeyError</code> և ոչ մի ակնարկ։
</p>
</div>

#%% md
## Գ մաս: Մեթոդները օգտագործում են միմյանց

Մեթոդի ներսից մյուս մեթոդը կանչվում է նույն կետով՝ `self.`-ով։

#%% code
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

    def failed_subjects(self):
        return [SUBJECT_NAMES[i] for i in range(len(self.grades))
                if self.grades[i] < PASS_MARK]

    def report_line(self):
        status = "passed" if self.has_passed() else "failed"
        return f"{self.name:<20} {self.class_name}  {self.average():.1f}  {status}"


ani = Student("Ani Hakobyan", "11A", [7, 6, 8, 9, 8], 94)
aram = Student("Aram Harutyunyan", "11B", [3, 2, 4, 3, 5], 65, "needs support")

print(ani.report_line())
print(aram.report_line())
print(aram.failed_subjects())

#%% md
`report_line`-ը կանչում է `has_passed`-ը և `average`-ը։ Ոչ մի արգումենտ չի
փոխանցվում — **նրանք արդեն գիտեն, թե որ աշակերտի մասին է խոսքը**։

#%% md
## Դ մաս: Երբ օբյեկտը ինքն իրեն տպում է

Երեկ նկատեցիր՝ `print(ani)` տալիս էր անհասկանալի բան։

#%% code
print(ani)

#%% md
Python-ին կարելի է ասել, թե ինչպես տպի այս դասի օբյեկտները։ Դրա համար կա
հատուկ անունով մեթոդ՝ `__str__`։

#%% code
class Student:
    def __init__(self, name, class_name, grades, attendance, note=""):
        self.name = name
        self.class_name = class_name
        self.grades = grades
        self.attendance = attendance
        self.note = note

    def average(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name} ({self.class_name}), average {self.average():.1f}"


ani = Student("Ani Hakobyan", "11A", [7, 6, 8, 9, 8], 94)
print(ani)

group = [ani, Student("Nare Petrosyan", "11B", [10, 9, 10, 9, 10], 99)]
for student in group:
    print(student)

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Երկու ընդգծում՝ առջևում և հետևում, նշանակում է՝ «Python-ն է սա կանչում, ոչ թե դու»։</b><br/>
<code>__init__</code> — կանչվում է <code>Student(...)</code> գրելիս։<br/>
<code>__str__</code> — կանչվում է <code>print(student)</code> գրելիս։<br/><br/>
Այս դասընթացում այս երկուսը բավական են։
</p>
</div>

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Հաճախումների մեթոդ

Ավելացրո՛ւ `Student`-ին `attends_enough()` մեթոդ, որը վերադարձնում է `True`,
եթե հաճախումը 85%-ից բարձր է։

#%% code
class Student:
    def __init__(self, name, class_name, grades, attendance, note=""):
        self.name = name
        self.class_name = class_name
        self.grades = grades
        self.attendance = attendance
        self.note = note

    def average(self):
        return sum(self.grades) / len(self.grades)

    # def attends_enough(self):
    #     ...


ani = Student("Ani Hakobyan", "11A", [7, 6, 8, 9, 8], 94)
davit = Student("Davit Grigoryan", "11A", [5, 3, 6, 5, 7], 78)
# print(ani.attends_enough(), davit.attends_enough())

#%% md
### 2. Ամենաբարձրն ու ամենացածրը

Ավելացրո՛ւ `best_subject()` և `worst_subject()` մեթոդներ, որոնք վերադարձնում են
առարկայի **անունը**։

#%% code
SUBJECT_NAMES = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]

# Add the two methods to Student above, then:
# print(ani.best_subject(), ani.worst_subject())

#%% md
### 3. Մեթոդ, որը փոխում է օբյեկտը

Ավելացրո՛ւ `add_grade(subject_index, grade)` մեթոդ, որը **փոխում է** աշակերտի
գնահատականը տվյալ առարկայից, և ոչինչ չի վերադարձնում։

#%% code
# Add the method, then:
# print(ani.average())
# ani.add_grade(1, 10)
# print(ani.average())

#%% md
### 4. `__str__` քո ձևով

Գրի՛ր `__str__`, որը տպում է այսպես՝

```
Ani Hakobyan · 11A · 7.6 · 94%
```

#%% code
# ...

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Ուսուցիչը՝ մեթոդներով

Գրի՛ր `Teacher` դաս՝ անուն, առարկա, տարիներ, և `is_experienced()` մեթոդ, որը
`True` է 10 տարուց ավելիի դեպքում։ Ավելացրո՛ւ նաև `__str__`։

#%% code
# ...

#%% md
### 6. Համեմատել երկու աշակերտի

Գրի՛ր `better_than(other)` մեթոդ, որը ընդունում է **ուրիշ աշակերտ** և
վերադարձնում `True`, եթե այս մեկի միջինը ավելի բարձր է։

#%% code
# print(ani.better_than(davit))

#%% md
### 7. Հաշվետվություն ամբողջ խմբի համար

Գրի՛ր ֆունկցիա, որը ստանում է `Student` օբյեկտների ցուցակ և տպում է բոլորի
տողերը՝ դասավորված ըստ միջինի։

#%% code
def print_group(students):
    # sorted() with a lambda on student.average()
    # ...
    pass

#%% md
### 8. Դպրոցի ֆայլից՝ մեթոդներով

Կառուցի՛ր 36 `Student` օբյեկտ `school.csv`-ից և տպի՛ր նրանց, ում միջինը 5-ից
ցածր է։

#%% code
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

school = []
# ...
print(len(school))

#%% md
## Մարտահրավեր

#%% md
### 9. Մեթոդ, որը վերադարձնում է օբյեկտ

Ավելացրո՛ւ `copy()` մեթոդ, որը վերադարձնում է **նոր** `Student` օբյեկտ՝ նույն
տվյալներով։ Ապա ստուգի՛ր, որ երեկվա 10-րդ Մարտահրավերի խնդիրը այլևս չկա։

#%% code
# second = ani.copy()
# second.class_name = "11C"
# print(ani.class_name, second.class_name)

#%% md
### 10. Քանի՞ աշակերտ ենք սարքել

Գտի՛ր ձև, որով դասը հաշվում է, թե **ընդհանուր քանի** օբյեկտ է ստեղծվել։

**Հուշում:** փոփոխականը պետք է պատկանի **դասին**, ոչ թե առանձին աշակերտին։
Փորձի՛ր գրել այն `__init__`-ից դուրս, բայց `class`-ի ներսում, և `__init__`-ում
ավելացնել մեկով՝ `Student.count = Student.count + 1`։

#%% code
# ...

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

- **Մեթոդ** — դասի ներսում գրված ֆունկցիա
- `self` գրվում է **սահմանելիս**, չի գրվում **կանչելիս**
- `self.average()` — մեթոդը կանչում է մյուսին, առանց արգումենտի
- `ani.average` առանց փակագծերի — **ֆունկցիան ինքը**, ոչ թե պատասխանը
- `AttributeError` — սխալ անունով մեթոդ, և Python-ը ասում է՝ որ դասում
- `__str__` — ինչպես տպվի օբյեկտը

## Ի՞նչ է գալիս հետո

Աշակերտները առայժմ սովորական ցուցակում են։ Վաղը ցուցակը դառնում է **դասարան** —
օբյեկտ, որի ներսում ուրիշ օբյեկտներ են։
