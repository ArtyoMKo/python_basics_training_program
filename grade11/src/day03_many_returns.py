
#%% md
# Օր 3 — Հետ ուղարկել մեկից ավելի պատասխան

### Python 11-րդ դասարանի համար · Օր 3-ը 24-ից

Տնօրենը խնդրում է դասարանի **միջինը**։ Հետո՝ **ամենաբարձրը**։ Հետո՝ **չանցածների
թիվը**։

Երեք ֆունկցիա գրե՞լ։ Պետք չէ։

## ԱՅՍՕՐ:

- **Ա մաս:** `return`, որը տալիս է երկու բան
- **Բ մաս:** բացել պատասխանը մյուս կողմում
- **Գ մաս:** երբ պատասխանները շատ են

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>def f(a, b=4)</code> — կանխադրված արժեք։<br/>
<code>f(name="Ani")</code> — անունով փոխանցել։<br/><br/>
<b>Այսօր <code>return</code>-ը սովորում է տալ մեկից ավելի արժեք։</b>
</p>
</div>

#%% md
## Ա մաս: Երեք ֆունկցիա, որ նույն բանն են անում

Ահա այն, ինչ գիտենք անելու։

**Գործարկի՛ր։**

#%% code
register = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3, "Mariam": 8, "Hayk": 2}
PASS_MARK = 4


def class_average(grades):
    return sum(grades.values()) / len(grades)


def class_highest(grades):
    return max(grades.values())


def class_failing(grades):
    count = 0
    for name in grades:
        if grades[name] < PASS_MARK:
            count = count + 1
    return count


print("average:", class_average(register))
print("highest:", class_highest(register))
print("failing:", class_failing(register))

#%% md
Երեք ֆունկցիա, և **երեքն էլ անցնում են նույն մատյանի վրայով**։

Քանի՞ անգամ է Python-ը կարդում `register`-ը այստեղ։ Երեք։ Իսկ եթե դպրոցում 180
գնահատական է՝ երեք անգամ 180։

#%% md
## Բ մաս: Մեկ `return`, երկու արժեք

`return`-ից հետո կարելի է գրել մի քանի բան՝ ստորակետերով։

#%% code
def class_summary(grades):
    average = sum(grades.values()) / len(grades)
    highest = max(grades.values())
    return average, highest


result = class_summary(register)
print(result)
print(type(result))

#%% md
Արդյունքը **մեկ արժեք** է, որը ներսում պահում է երկուսը։ Python-ում դրան ասում են
**tuple**։

<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b>Tuple-ը ցուցակ է, որը չի փոխվում։</b> Կլոր փակագծեր՝ <code>( )</code>,
ոչ թե քառակուսի։<br/><br/>
Անցած դասընթացում արդեն օգտագործել ես այն՝ <code>for name, grade in
register.items():</code>։ Այնտեղ <code>.items()</code>-ը հենց tuple-ներ էր տալիս։
Պարզապես բառը չէինք ասում։
</p>
</div>

#%% md
## Գ մաս: Բացել պատասխանը

Tuple-ից արժեքները հանելու երկու ձև կա։

#%% code
# By position -- works, but what is [0]?
print(result[0])
print(result[1])

# By unpacking -- each value gets a name
average, highest = class_summary(register)
print("average:", average)
print("highest:", highest)

#%% md
Երկրորդ ձևը կոչվում է **unpacking**՝ «բացել»։ Ձախ կողմում այնքան անուն, որքան
արժեք կա աջում։

Եվ հիմա՝ երեք արժեք, մեկ անցումով։

#%% code
def class_summary(grades, pass_mark=4):
    total = 0
    highest = 0
    failing = 0
    for name in grades:
        grade = grades[name]
        total = total + grade
        if grade > highest:
            highest = grade
        if grade < pass_mark:
            failing = failing + 1
    return total / len(grades), highest, failing


average, highest, failing = class_summary(register)
print(f"average {average:.2f} · highest {highest} · failing {failing}")

#%% md
**Մեկ անցում մատյանի վրայով։ Երեք պատասխան։**

#%% md
## Դ մաս: Երբ պատասխանները շատանում են

Երեք արժեք՝ լավ է։ Ութ արժեք՝ արդեն վտանգավոր։

#%% code
# Easy to get wrong: which one was "failing" again?
a, b, c = class_summary(register)
print(c, b, a)

#%% md
Երբ արժեքները շատ են, վերադարձրո՛ւ **բառարան**։ Այնտեղ ամեն արժեք ունի անուն։

#%% code
def class_summary(grades, pass_mark=4):
    total = 0
    highest = 0
    failing = 0
    for name in grades:
        grade = grades[name]
        total = total + grade
        if grade > highest:
            highest = grade
        if grade < pass_mark:
            failing = failing + 1
    return {
        "average": total / len(grades),
        "highest": highest,
        "failing": failing,
        "students": len(grades),
    }


summary = class_summary(register)
print(summary["average"])
print(summary["failing"])
print(summary)

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Ո՞ր մեկը ընտրել։</b><br/>
<b>Երկու-երեք արժեք</b> → tuple։ Կարճ է, և unpacking-ը կարդացվում է։<br/>
<b>Չորսից ավելի</b> → բառարան։ Անունները պաշտպանում են կարգը շփոթելուց։
</p>
</div>

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Ամենաբարձրը և ամենացածրը

Գրի՛ր ֆունկցիա, որը մեկ անցումով վերադարձնում է ամենաբարձր **և** ամենացածր
գնահատականը։

#%% code
def highest_and_lowest(grades):
    # grades is a dictionary: name -> grade
    # Return two values.
    # ...
    return 0, 0


highest, lowest = highest_and_lowest(register)
print("highest:", highest, "lowest:", lowest)

#%% md
### 2. Անունն էլ հետը

Հիմա վերադարձրո՛ւ ոչ թե թիվը, այլ **անունը և թիվը**՝ ամենաբարձրի համար։

#%% code
def best_student(grades):
    # Return the name and the grade of the best student.
    # ...
    return "", 0


name, grade = best_student(register)
print(f"best: {name} with {grade}")

#%% md
### 3. Անցած և չանցած

Գրի՛ր ֆունկցիա, որը վերադարձնում է **երկու ցուցակ**՝ անցածների անունները և
չանցածների անունները։

#%% code
def split_by_result(grades, pass_mark=4):
    passed = []
    failed = []
    # One loop. Put each name in the right list.
    # ...
    return passed, failed


passed, failed = split_by_result(register)
print("passed:", passed)
print("failed:", failed)

#%% md
### 4. Բառարանով հաշվետվություն

Գրի՛ր ֆունկցիա, որը վերադարձնում է բառարան չորս բանալիով՝ `"students"`,
`"average"`, `"passed"`, `"failed"`։

#%% code
def register_report(grades, pass_mark=4):
    # Return a dictionary with four keys.
    # ...
    return {}


report = register_report(register)
for key in report:
    print(f"{key:<10} {report[key]}")

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Երեք թիվ՝ մեկ տողում

Գրի՛ր ֆունկցիա, որը վերադարձնում է գումարը, միջինը և քանակը, և տպի՛ր դրանք
**մեկ** `print`-ով՝ unpacking-ով։

#%% code
def totals(grades):
    # ...
    return 0, 0.0, 0


# print with unpacking, on one line
# ...

#%% md
### 6. Փոխանակել երկու արժեք

Tuple-ը թույլ է տալիս փոխանակել երկու փոփոխական **մեկ տողով**՝ առանց երրորդի։
Փորձի՛ր գտնել այդ տողը։

#%% code
first = "Ani"
second = "Davit"

# One line that swaps them.
# ...

print(first, second)

#%% md
### 7. Առարկայի ամփոփում

Կարդա՛ `school.csv`-ը և գրի՛ր ֆունկցիա, որը մեկ առարկայի համար վերադարձնում է
միջինը, ամենաբարձրը և չանցածների թիվը։

#%% code
from pathlib import Path

lines = Path("school.csv").read_text(encoding="utf-8").strip().splitlines()


def subject_summary(lines, subject, pass_mark=4):
    # ...
    return 0.0, 0, 0


# print(subject_summary(lines, "Mathematics"))

#%% md
### 8. Չափից շատ անուն

Ի՞նչ է լինում, եթե ձախ կողմում երեք անուն գրես, իսկ ֆունկցիան երկու արժեք
վերադարձնի։ Փորձի՛ր և կարդա՛ սխալը։

#%% code
# a, b, c = highest_and_lowest(register)
# Uncomment the line above, run it, then read the error.

#%% md
## Մարտահրավեր

#%% md
### 9. Մեկ անցում՝ ամեն ինչի համար

Գրի՛ր **մեկ** ֆունկցիա, որը `school.csv`-ի տողերի վրայով անցնում է **մեկ անգամ**
և վերադարձնում բառարան՝ դպրոցի միջինը, ամեն դասարանի միջինը և ամեն առարկայի
միջինը։

#%% code
def whole_school(lines, pass_mark=4):
    # One pass. Three dictionaries built as you go.
    # ...
    return {}

#%% md
### 10. Tuple-ը բանալի

Բառարանի բանալին չի կարող լինել ցուցակ, բայց **կարող է լինել tuple**։ Փորձի՛ր
կառուցել բառարան, որի բանալին `(class_name, subject)` զույգն է, իսկ արժեքը՝ այդ
դասարանի այդ առարկայի միջինը։

Ինչո՞ւ է ցուցակը չի կարող, իսկ tuple-ը՝ կարող։ Պատասխանը գրի՛ր markdown-ում։

#%% code
averages = {}

# averages[("11A", "Mathematics")] = 7.1
# ...

#%% md
## Ինչի հասանք

- `return a, b` — մեկ `return`, մի քանի արժեք
- Արդյունքը **tuple** է՝ ցուցակ, որը չի փոխվում
- `average, highest = f(...)` — **unpacking**, ամեն արժեքին անուն
- Չորսից ավելի արժեք → **բառարան**, ոչ թե tuple
- Մեկ անցում տվյալների վրայով, ոչ թե երեք

## Հաջորդ անգամ

Տնօրենը կխնդրի **վեց ցուցակ**՝ անցածները, չանցածները, լավագույն հինգը, ամեն
առարկայից առանձին։

Վեց ցիկլ կգրենք։ Հետո նույն դասին կստանանք այն, ինչով ամեն մեկը գրվում է
**մեկ տողով**։
