
#%% md
# Օր 2 — Ֆունկցիաներ, որոնք ճկվում են

### Python 11-րդ դասարանի համար · Օր 2-ը 24-ից

Անցած դասընթացում գրեցիր ֆունկցիա՝ `def`, պարամետրեր, `return`։ Այսօր նույն
ֆունկցիան սովորում է **ճկվել** — նույն գործը, մի փոքր այլ կերպ, առանց երկրորդ
ֆունկցիա գրելու։

## ԱՅՍՕՐ:

- **Ա մաս:** պարամետր, որն ունի կանխադրված արժեք
- **Բ մաս:** անունով փոխանցել արգումենտը
- **Գ մաս:** ֆունկցիա, որը ընդունում է ցանկացած թվով արժեք

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>def report_line(name, grade):</code> — սահմանում ենք մեկ անգամ, կանչում՝ շատ։<br/>
<code>return</code> — պատասխանը հետ է ուղարկում։<br/><br/>
<b>Այսօր պարամետրերը դառնում են ավելի ճկուն։</b>
</p>
</div>

#%% md
## Ա մաս: Երբ արժեքը սովորաբար նույնն է

Ահա ֆունկցիա, որը գրել ես անցած դասընթացում։

**Գործարկի՛ր։**

#%% code
def report_line(name, grade):
    return f"{name}: {grade}"


print(report_line("Ani", 9))
print(report_line("Davit", 6))

#%% md
Հիմա տնօրենը խնդրում է, որ հաշվետվության մեջ երևա նաև **անցողիկ նիշը** — այն թիվը,
որից ցածրը չանցած է։ Գրեթե միշտ դա **4**-ն է, բայց քննությունների ժամանակ՝ **5**։

Առաջին միտքը՝ ավելացնել պարամետր.

#%% code
def report_line(name, grade, pass_mark):
    if grade >= pass_mark:
        status = "passed"
    else:
        status = "failed"
    return f"{name}: {grade} ({status})"


print(report_line("Ani", 9, 4))
print(report_line("Davit", 6, 4))
print(report_line("Aram", 3, 4))

#%% md
Աշխատում է։ Բայց նկատի՛ր՝ **ամեն կանչում գրում ենք `4`**։ Միշտ նույնը։

Իսկ եթե մոռանանք այն գրել — սխալ ենք ստանում։ **Գործարկի՛ր ներքևի բջիջը և
կարդա՛ սխալը։**

#%% code expected-error: TypeError
print(report_line("Mariam", 8))

#%% md
<div style="border-left: 6px solid #d33; background: #fff5f5; padding: 12px 16px; margin: 12px 0;">
<p style="color:#d33; margin:0;">
🔍 <b><code>TypeError: report_line() missing 1 required positional argument: 'pass_mark'</code></b><br/><br/>
Python-ը ուղիղ ասում է՝ <b>ո՞ր ֆունկցիան</b>, <b>քանի՞ արգումենտ է պակաս</b>, և
<b>ո՞ր պարամետրի</b>։ Երեք բան՝ մեկ տողում։
</p>
</div>

#%% md
## Բ մաս: Կանխադրված արժեք

Եթե պարամետրը գրեթե միշտ նույնն է, Python-ին կարելի է ասել՝ **«եթե չեն տվել, վերցրու սա»**։

Գրվում է հավասարման նշանով՝ ուղիղ պարամետրի անունից հետո։

#%% code
def report_line(name, grade, pass_mark=4):
    if grade >= pass_mark:
        status = "passed"
    else:
        status = "failed"
    return f"{name}: {grade} ({status})"


# No third argument -- pass_mark is 4
print(report_line("Mariam", 8))
print(report_line("Aram", 3))

# A third argument -- it replaces the default
print(report_line("Aram", 3, 3))

#%% md
Մեկ ֆունկցիա, երկու օգտագործում։ Ոչ մի կրկնություն։

<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b>Կանոն:</b> կանխադրված արժեք ունեցող պարամետրերը գրվում են <b>վերջում</b>։<br/>
<code>def f(a, b, c=4)</code> — ճիշտ է։ <code>def f(a=4, b, c)</code> — Python-ը չի ընդունի։
</p>
</div>

#%% md
Մի քանի կանխադրված արժեք միանգամից՝

#%% code
def report_line(name, grade, pass_mark=4, show_status=True):
    if not show_status:
        return f"{name}: {grade}"
    if grade >= pass_mark:
        status = "passed"
    else:
        status = "failed"
    return f"{name}: {grade} ({status})"


print(report_line("Nare", 10))
print(report_line("Nare", 10, 4, False))

#%% md
## Գ մաս: Անունով փոխանցել

Վերջին կանչում գրեցինք `report_line("Nare", 10, 4, False)`։

Մի հարց՝ **ի՞նչ է նշանակում այդ `False`-ը**։ Առանց ֆունկցիայի սահմանումը նայելու՝
հնարավոր չէ ասել։

Լուծումը՝ գրել **պարամետրի անունը**։

#%% code
print(report_line("Nare", 10, show_status=False))
print(report_line("Aram", 3, pass_mark=3))
print(report_line(name="Lilit", grade=7))

#%% md
Երեք առավելություն՝

| | |
|---|---|
| **Կարդացվում է** | `show_status=False` ինքն իրեն բացատրում է |
| **Կարգը կարևոր չէ** | `report_line(grade=7, name="Lilit")` — նույնն է |
| **Կարելի է բաց թողնել միջինը** | `report_line("Nare", 10, show_status=False)` — `pass_mark`-ը մնում է 4 |

#%% md
## Դ մաս: Ցանկացած թվով արժեք

Վերջին բանը այսօրվա համար։ Երբեմն չգիտենք՝ քանի արժեք կտան։

#%% code
def average(*grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)


print(average(9, 6, 10))
print(average(9, 6, 10, 3, 8))
print(average(7))

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Աստղանիշը նշանակում է՝ «հավաքիր բոլորը մեկ տեղում»։</b> Ֆունկցիայի ներսում
<code>grades</code>-ը դառնում է սովորական ցուցակ։<br/><br/>
Սա <b>պետք է ճանաչես</b>, որովհետև կա աշակերտների ծրագրում։ Այսօր ավելի խորը չենք
գնում — մեկ օրինակ բավական է։
</p>
</div>

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Կանխադրված կլորացում

Գրի՛ր ֆունկցիա, որը հաշվում է միջինը և կլորացնում։ Կլորացումը սովորաբար **1**
նիշ է, բայց պետք է լինի փոփոխելի։

#%% code
def class_average(grades, digits=1):
    # Return the average of the list, rounded to `digits` places.
    # ...
    return 0


print(class_average([9, 6, 10, 3, 8]))
print(class_average([9, 6, 10, 3, 8], 2))

#%% md
### 2. Հաշվետվության վերնագիր

Գրի՛ր ֆունկցիա, որը տպում է հաշվետվության վերնագիր։ Դպրոցի անունը գրեթե միշտ
նույնն է։

#%% code
def report_header(class_name, school="School N 5"):
    # Print two lines: the school, then the class.
    # ...
    pass


report_header("11A")
report_header("11B", "School N 12")

#%% md
### 3. Անունով կանչել

Ահա ֆունկցիա չորս պարամետրով։ Կանչի՛ր այն **երեք անգամ**, ամեն անգամ փոխելով
միայն **մեկ** կանխադրված արժեք — և օգտագործելով պարամետրի անունը։

#%% code
def attendance_line(name, present=True, late=False, note=""):
    status = "present" if present else "absent"
    if late:
        status = status + ", late"
    if note != "":
        status = status + f" ({note})"
    return f"{name}: {status}"


print(attendance_line("Ani"))
# Three more calls, each changing exactly one thing, by name.
# ...

#%% md
### 4. Երկու կանխադրված արժեք

Գրի՛ր ֆունկցիա, որը վերադարձնում է չանցածների ցուցակը։ Անցողիկ նիշը կանխադրված
**4** է, իսկ արդյունքը կանխադրված **չի** դասավորվում։

#%% code
def failing_students(grades, pass_mark=4, sort_them=False):
    # grades is a dictionary: name -> grade
    # Return a list of the names below pass_mark.
    # If sort_them is True, sort the list before returning it.
    # ...
    return []


register = {"Ani": 9, "Davit": 6, "Aram": 3, "Hayk": 2, "Nare": 10}
print(failing_students(register))
print(failing_students(register, sort_them=True))
print(failing_students(register, pass_mark=7, sort_them=True))

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Գնահատականի բառը

Գրի՛ր ֆունկցիա, որը թիվը դարձնում է բառ՝ 9–10 `"excellent"`, 7–8 `"good"`,
4–6 `"satisfactory"`, 1–3 `"failed"`։ Ավելացրո՛ւ կանխադրված պարամետր `short=False`,
որը `True` լինելու դեպքում վերադարձնում է միայն առաջին տառը։

#%% code
def grade_word(grade, short=False):
    # ...
    return ""


print(grade_word(9), grade_word(7), grade_word(5), grade_word(2))
print(grade_word(9, short=True))

#%% md
### 6. Տարանջատիչ

Գրի՛ր ֆունկցիա, որը ցուցակը դարձնում է մեկ տող։ Տարանջատիչը կանխադրված
`", "` է։

#%% code
def join_names(names, separator=", "):
    # Build one string out of the list.
    # ...
    return ""


print(join_names(["Ani", "Davit", "Nare"]))
print(join_names(["Ani", "Davit", "Nare"], " | "))

#%% md
### 7. Ամենաբարձրը՝ ցանկացած թվով

Գրի՛ր `highest(*grades)` ֆունկցիա, որը վերադարձնում է ամենամեծ թիվը՝ առանց
`max()`-ի։

#%% code
def highest(*grades):
    # ...
    return 0


print(highest(9, 6, 10, 3))
print(highest(4, 4, 4))

#%% md
### 8. Երկու ֆունկցիան՝ մեկում

Վերևում ունեինք `report_line` և `attendance_line`։ Գրի՛ր **մեկ** ֆունկցիա
`student_line`, որը կանխադրված պարամետրով որոշում է, թե որ տեսակի տող տպի։

#%% code
def student_line(name, grade=None, present=None):
    # If grade is given, print a grade line.
    # If present is given, print an attendance line.
    # ...
    return ""


print(student_line("Ani", grade=9))
print(student_line("Ani", present=False))

#%% md
## Մարտահրավեր

#%% md
### 9. Հաշվետվություն՝ ամբողջ դպրոցի համար

Կարդա՛ `school.csv`-ը և գրի՛ր ֆունկցիա

```python
def school_report(lines, class_name=None, subject=None, pass_mark=4):
```

որը տպում է միջինը։ Եթե `class_name` տրված է՝ միայն այդ դասարանի։ Եթե `subject`
տրված է՝ միայն այդ առարկայի։ Եթե երկուսն էլ՝ երկուսի հատումը։

#%% code
from pathlib import Path

lines = Path("school.csv").read_text(encoding="utf-8").strip().splitlines()

# def school_report(lines, class_name=None, subject=None, pass_mark=4):
#     ...

#%% md
### 10. Փոփոխվող կանխադրված արժեքը

**Գործարկի՛ր ներքևի բջիջը երկու անգամ** և բացատրի՛ր, թե ինչու է արդյունքը
երկրորդ անգամ այլ։

Սա Python-ի ամենահայտնի թակարդն է։ Պատասխանը գրի՛ր markdown բջիջում։

#%% code
def add_student(name, register=[]):
    register.append(name)
    return register


print(add_student("Ani"))
print(add_student("Davit"))

#%% md
## Ինչի հասանք

- `def f(a, b=4)` — **կանխադրված արժեք**։ Եթե չեն տվել, վերցվում է այն
- Կանխադրված պարամետրերը գրվում են **վերջում**
- `f(name="Ani")` — **անունով** փոխանցել։ Կարդացվում է, և կարգը կարևոր չէ
- `def f(*grades)` — **ցանկացած թվով** արժեք, ֆունկցիայի ներսում՝ ցուցակ
- `TypeError: missing 1 required positional argument` — պակասող արգումենտ

## Հաջորդ անգամ

Ֆունկցիան կսովորի վերադարձնել **մեկից ավելի պատասխան** — միջինը **և** ամենաբարձրը
**և** չանցածների թիվը, մեկ `return`-ով։
