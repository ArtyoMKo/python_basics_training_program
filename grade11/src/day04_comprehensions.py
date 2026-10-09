
#%% md
# Թեմա 4 — Վեց հաշվետվություն, վեց ցիկլ

### Python 11-րդ դասարանի համար · Թեմա 4-ը 24-ից

Տնօրենը պատրաստվում է մանկավարժական խորհրդին։ Նրան պետք է **վեց ցուցակ** նույն
մատյանից։

## ԱՅՍՕՐ:

- **Ա մաս:** վեց ցուցակը՝ այն ձևով, որ գիտենք
- **Բ մաս:** նույնը՝ մեկ տողով
- **Գ մաս:** երկու տարբերակը կողք կողքի

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>return a, b</code> և unpacking։ Կանխադրված արժեքներ։<br/><br/>
<b>Այսօր առաջին անգամ ցուցակ ենք կառուցելու առանց <code>append</code>-ի։</b>
</p>
</div>

#%% md
## Ա մաս: Վեց ցուցակ, վեց ցիկլ

Ահա դպրոցի մատյանը՝ մեկ դասարան, տուփից հանված։

#%% code
register = {
    "Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3, "Mariam": 8, "Tigran": 7,
    "Lilit": 5, "Gor": 4, "Anahit": 9, "Hayk": 2, "Sona": 8, "Vahe": 6,
}

PASS_MARK = 4
print(len(register), "students")

#%% md
Տնօրենին պետք է վեց ցուցակ.

| | |
|---|---|
| 1 | բոլոր անունները |
| 2 | անցածների անունները |
| 3 | չանցածների անունները |
| 4 | բոլոր գնահատականները |
| 5 | անունները՝ մեծատառով |
| 6 | 8-ից բարձր ստացածները |

<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Այս ձևն աշխատում է, բայց երկար է։</b> Դասի երկրորդ կեսին կսովորենք մի ձև,
որը այս վեց ցիկլի ամեն մեկը դարձնում է <b>մեկ տող</b>։
</p>
</div>

**Առաջին երեքը պատրաստ են։ Գործարկի՛ր և կարդա՛։**

#%% code
# 1. every name
all_names = []
for name in register:
    all_names.append(name)

# 2. the ones who passed
passed = []
for name in register:
    if register[name] >= PASS_MARK:
        passed.append(name)

# 3. the ones who did not
failed = []
for name in register:
    if register[name] < PASS_MARK:
        failed.append(name)

print("all:   ", all_names)
print("passed:", passed)
print("failed:", failed)

#%% md
**Հիմա դու։** Գրի՛ր մնացած երեքը՝ ճիշտ նույն ձևով։

#%% code
# 4. every grade
all_grades = []
# ...

# 5. every name in capitals
shouted = []
# ...

# 6. the ones above 8
top = []
# ...

print("grades: ", all_grades)
print("shouted:", shouted)
print("top:    ", top)

#%% md
Հիմա տնօրենը զանգում է. **անցողիկ նիշը դարձել է 5**, ոչ թե 4։

Քանի՞ տեղ պետք է փոխել։

#%% code
# Change PASS_MARK and run the six loops again.
# How many lines did you have to touch?
PASS_MARK = 5

#%% md
## Բ մաս: Նույն ցուցակը՝ մեկ տողով

Նայի՛ր երկրորդ ցիկլին։ Նա ասում է երեք բան.

```python
passed = []
for name in register:              # 1. ամեն անունի համար
    if register[name] >= PASS_MARK:   # 2. եթե պայմանը ճիշտ է
        passed.append(name)           # 3. վերցրու անունը
```

Python-ը թույլ է տալիս գրել այս երեքը **մեկ տողում**, նույն կարգով՝
*վերցրու — ամեն մեկի համար — եթե*։

#%% code
passed = [name for name in register if register[name] >= PASS_MARK]

print(passed)

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#0a7; margin-top:0;">✅ Ինչպե՞ս կարդալ</h3>
<p style="color:#0a7; margin-bottom:0;">
<code>[ <b>name</b> &nbsp; for name in register &nbsp; if ... ]</code><br/><br/>
<b>Կարդա՛ միջից՝ աջ ու ձախ։</b><br/>
Մեջտեղը՝ <code>for name in register</code> — նույն ցիկլն է։<br/>
Աջը՝ <code>if ...</code> — նույն պայմանը։<br/>
Ձախը՝ <code>name</code> — <b>այն, ինչ դնում ենք ցուցակում</b>։<br/><br/>
Քառակուսի փակագծերը նշանակում են՝ արդյունքը <b>ցուցակ</b> է։
</p>
</div>

#%% md
Առանց պայմանի՝ պարզապես բաց թողնում ենք `if`-ը։

#%% code
all_names = [name for name in register]
all_grades = [register[name] for name in register]

print(all_names)
print(all_grades)

#%% md
Ձախ կողմում կարելի է ոչ միայն անունը դնել, այլ **ինչ ուզես դրանից սարքել**։

#%% code
shouted = [name.upper() for name in register]
doubled = [grade * 2 for grade in register.values()]

print(shouted)
print(doubled)

#%% md
Մի բան, որ արժե իմանալ հիմա՝ **ցիկլի փոփոխականը ապրում է միայն փակագծերի ներսում։**

**Գործարկի՛ր ներքևի բջիջը և կարդա՛ սխալը։**

#%% code expected-error: NameError
squares = [grade * grade for grade in register.values()]

print(squares)
print(grade)

#%% md
<div style="border-left: 6px solid #d33; background: #fff5f5; padding: 12px 16px; margin: 12px 0;">
<p style="color:#d33; margin:0;">
🔍 <b><code>NameError: name 'grade' is not defined</code></b><br/><br/>
Սովորական <code>for</code> ցիկլից հետո <code>grade</code>-ը մնում է։ Այստեղ՝ ոչ։
Փակագիծը փակվեց — անունը վերացավ։<br/><br/>
<b>Սա լավ բան է։</b> Պատահական անուն չի մնում ծրագրում։
</p>
</div>

#%% md
## Գ մաս: Վեցն էլ, նորից

Հիմա գրի՛ր բոլոր վեցը՝ ամեն մեկը մեկ տողով։

#%% code
PASS_MARK = 4

all_names = [name for name in register]
passed = [name for name in register if register[name] >= PASS_MARK]
failed = [name for name in register if register[name] < PASS_MARK]
all_grades = [register[name] for name in register]
shouted = [name.upper() for name in register]
top = [name for name in register if register[name] > 8]

print("all:    ", len(all_names))
print("passed: ", passed)
print("failed: ", failed)
print("top:    ", top)

#%% md
### Երկու տարբերակը կողք կողքի

| | Ցիկլով | Մեկ տողով |
|---|---|---|
| Ցուցակ 1 | 3 տող | 1 տող |
| Ցուցակ 2 | 4 տող | 1 տող |
| Ցուցակ 3 | 4 տող | 1 տող |
| Ցուցակ 4 | 3 տող | 1 տող |
| Ցուցակ 5 | 3 տող | 1 տող |
| Ցուցակ 6 | 4 տող | 1 տող |
| **Ընդամենը** | **21 տող** | **6 տող** |

Եվ երբ անցողիկ նիշը նորից փոխվի՝ փոխվում է **երկու տող**, ոչ թե ութ։

<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<p style="color:#06c; margin:0;">
<b>Ե՞րբ օգտագործել։</b> Երբ ցիկլը կառուցում է ցուցակ և <b>ուրիշ ոչինչ չի անում</b>։<br/>
Եթե ցիկլի ներսում կա <code>print</code>, երկու <code>if</code>, կամ հաշվիչ —
<b>թո՛ղ սովորական ցիկլ</b>։ Մեկ տողը նպատակ չէ։
</p>
</div>

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Երեքը՝ մեկ տողով

Գրի՛ր երեք ցուցակ մեկական տողով՝ 7-ից բարձր ստացածների անունները, բոլոր
գնահատականները՝ մեկով ավելացրած, և այն անունները, որոնք սկսվում են `"A"`-ով։

#%% code
above_seven = []
plus_one = []
starts_with_a = []

print(above_seven)
print(plus_one)
print(starts_with_a)

#%% md
### 2. Ցիկլից՝ մեկ տող

Ահա ցիկլ։ Վերածի՛ր այն մեկ տողի։

#%% code
short_names = []
for name in register:
    if len(name) <= 4:
        short_names.append(name)

print(short_names)

# The same thing, on one line:
short_names_again = []
print(short_names_again)

#%% md
### 3. Մեկ տողից՝ ցիկլ

Հիմա հակառակը։ Ահա մեկ տող — գրի՛ր այն սովորական ցիկլով։

#%% code
result = [name + ": " + str(register[name]) for name in register if register[name] >= 8]
print(result)

# The same thing, as a loop:
result_again = []
# ...
print(result_again)

#%% md
### 4. Դպրոցի ֆայլից

Կարդա՛ `school.csv`-ը և հավաքի՛ր **մեկ տողով** բոլոր Mathematics-ի
գնահատականները։

#%% code
from pathlib import Path

lines = Path("school.csv").read_text(encoding="utf-8").strip().splitlines()
rows = [line.split(",") for line in lines[1:] if line != ""]

print(len(rows), "rows")

# One line: every grade whose subject is "Mathematics", as an int.
maths = []
print(len(maths), "maths grades")

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Երկու պայման

Հավաքի՛ր այն աշակերտներին, ովքեր անցել են **և** ունեն 4 տառից երկար անուն։

#%% code
both = []
print(both)

#%% md
### 6. Տեքստից՝ թվեր

Ահա ցուցակ, որտեղ գնահատականները տեքստ են։ Մեկ տողով դարձրո՛ւ դրանք թվեր։

#%% code
text_grades = ["9", "6", "10", "3", "8"]

numbers = []
print(numbers, sum(numbers))

#%% md
### 7. Ցուցակից՝ հաշվետվության տողեր

Մեկ տողով սարքի՛ր հաշվետվության տողերի ցուցակ՝ `"Ani: 9 (passed)"` տեսքով։
Կարող ես օգտագործել 2-րդ թեմայի `report_line` ֆունկցիան։

#%% code
def report_line(name, grade, pass_mark=4):
    if grade >= pass_mark:
        status = "passed"
    else:
        status = "failed"
    return f"{name}: {grade} ({status})"


report = []
for line in report:
    print(line)

#%% md
### 8. Ամեն դասարանի անունները

`school.csv`-ից մեկ տողով հավաքի՛ր **11B** դասարանի աշակերտների անունները։
Ուշադի՛ր եղիր կրկնություններին — ամեն աշակերտ ֆայլում հինգ անգամ է։

#%% code
names_11b = []
print(len(names_11b))

# Now without repeats. Hint: set() takes a list and removes duplicates.
unique = []
print(len(unique))

#%% md
## Մարտահրավեր

#%% md
### 9. Ամեն առարկայի միջինը՝ մեկ տողով

Ունենք առարկաների ցուցակը։ Կառուցի՛ր բառարան՝ առարկա → միջին, որտեղ միջինը
հաշվվում է մեկ տողով գրված ցուցակից։

#%% code
subjects = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]

averages = {}
for subject in subjects:
    grades = []
    # one line that collects this subject's grades from rows
    # averages[subject] = sum(grades) / len(grades)

for subject in averages:
    print(f"{subject:<14} {averages[subject]:.2f}")

#%% md
### 10. Ցուցակ՝ ցուցակների մեջ

Կառուցի՛ր **երեք** ցուցակից բաղկացած ցուցակ՝ ամեն դասարանի համար մեկը, որտեղ
ամեն ներքին ցուցակում այդ դասարանի գնահատականներն են։

Ապա տպի՛ր ամեն դասարանի միջինը։

#%% code
classes = ["11A", "11B", "11C"]

by_class = []
# ...

for position in range(len(by_class)):
    print(classes[position], len(by_class[position]))

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

- `[name for name in register]` — ցուցակ **առանց** `append`-ի
- `[... for ... in ... if ...]` — պայմանը գնում է **վերջում**
- Ձախ կողմում կարող է լինել ցանկացած արտահայտություն՝ `name.upper()`, `grade * 2`
- Ցիկլի փոփոխականը **չի ապրում** փակագծերից դուրս — `NameError`
- **21 տող → 6 տող**, և փոփոխությունը՝ մեկ տեղում
- Եթե ցիկլը միայն ցուցակ չի կառուցում — **թո՛ղ սովորական ցիկլ**

## Ի՞նչ է գալիս հետո

Նույն մեկ տողը կսովորի **ընտրել կառուցելու ընթացքում** — «եթե անցել է՝ գրիր
անունը, այլապես՝ աստղանիշ», մեկ տողում։
