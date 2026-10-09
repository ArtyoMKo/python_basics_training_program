#%% md
# Օր 1 — Դպրոցը, և այն, ինչ կառուցելու ենք

### Python 11-րդ դասարանի համար · Օր 1-ը 24-ից

Բարի՛ վերադարձ։ Անցած դասընթացում դու գրեցիր մի ծրագիր, որն աշխատում է **քո
դասարանի** հետ՝ կարդում է անունները, հաշվում միջինը, ասում՝ ով չի անցել։

Այսօր սկսում ենք այնտեղից, որտեղ ավարտեցինք — և նայում ենք, թե ինչ է **իրականում**
խնդրում դպրոցը։

## ԱՅՍՕՐ:

- **Ա մաս:** ստուգում ենք, որ ամեն ինչ տեղում է
- **Բ մաս:** հիշում ենք, ինչ ունենք արդեն
- **Գ մաս:** դպրոցի իրական ֆայլը — երեք դասարան, հինգ առարկա

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🎒 Ինչ ես բերում քեզ հետ</h3>
<p style="color:#06c; margin-bottom:0;">
<code>for</code> ցիկլ · բառարան · <code>def</code> և <code>return</code> · ֆայլ կարդալ և գրել ·
չորս ֆայլից բաղկացած ծրագիր<br/><br/>
<b>Սա բավական է։</b> Այն ամենը, ինչ այսօրվանից նոր է, սովորելու ենք զրոյից՝
ճիշտ այնպես, ինչպես անցած դասընթացում սովորեցինք փոփոխականը։
</p>
</div>

#%% md
## Ա մաս: Ամեն ինչ տեղո՞ւմ է

Անցած դասընթացում տեղադրեցինք Anaconda-ն և VS Code-ը։ Նույնն են՝ նորից տեղադրելու
կարիք չկա։

Բայց այս դասընթացում օգտագործելու ենք **երեք գործիք**, որոնք Anaconda-ն արդեն բերել է
քո համակարգչին։ Ստուգենք, որ դրանք տեղում են։

**Գործարկի՛ր ներքևի բջիջը։** Եթե սխալ չկա — ամեն ինչ կարգին է։

#%% code
import numpy
import matplotlib
import pandas

print("numpy     ", numpy.__version__)
print("matplotlib", matplotlib.__version__)
print("pandas    ", pandas.__version__)
print()
print("All three are here. Nothing to install.")

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b>Երեք տող՝ երեք համար։</b> Այս երեք գործիքը դեռ չենք օգտագործելու։ Առաջինին
կհասնենք <b>12-րդ օրը</b> — և այն ժամանակ արդեն կիմանաս, թե ինչու է պետք։<br/><br/>
Մինչ այդ՝ ոչինչ տեղադրելու կարիք չկա, և ինտերնետ էլ պետք չէ։
</p>
</div>

#%% md
## Բ մաս: Այն, ինչ արդեն ունենք

Ահա անցած դասընթացի մատյանը՝ մեկ դասարան, բառարանի տեսքով։ Ծանո՞թ է։

**Գործարկի՛ր։**

#%% code
grades = {
    "Ani": 9,
    "Davit": 6,
    "Nare": 10,
    "Aram": 3,
    "Mariam": 8,
}

PASS_MARK = 4

total = 0
for name in grades:
    total = total + grades[name]

print("students:", len(grades))
print("average: ", total / len(grades))

for name in grades:
    if grades[name] < PASS_MARK:
        print(name, "did not pass")

#%% md
Ամեն տող այստեղ քեզ ծանոթ է։ Սա քո գրածն է։

**Եվ այս ձևը լավ է աշխատում** — մեկ դասարանի, մեկ գնահատականի համար։

#%% md
## Գ մաս: Այն, ինչ խնդրում է դպրոցը

Հիմա նայի՛ր իրական խնդրանքին։ Տնօրենը ուղարկել է դպրոցի ֆայլը՝ `school.csv`։

Այնտեղ կա՝

| | |
|---|---|
| **3** դասարան | 11Ա, 11Բ, 11Գ |
| **36** աշակերտ | ամեն դասարանում՝ 12 |
| **5** առարկա | ամեն աշակերտի համար |
| **180** գնահատական | 36 × 5 |

Բացե՛նք այն այն գործիքներով, որ արդեն ունենք։

#%% code
from pathlib import Path

text = Path("school.csv").read_text(encoding="utf-8")
lines = text.strip().splitlines()

print("lines in the file:", len(lines))
print()
for line in lines[:6]:
    print(line)

#%% md
Առաջին տողը **վերնագիրն** է՝ ասում է, թե ամեն սյունակն ինչ է։ Մնացածը տվյալներն են։

Հիմա վերցնենք մեկ տող և բաժանենք ստորակետերով — ճիշտ այնպես, ինչպես անցած
դասընթացում։

#%% code
header = lines[0].split(",")
first = lines[1].split(",")

print("columns:", header)
print()
for column_name, value in zip(header, first):
    print(f"{column_name:<10} {value}")

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Ուշադրությո՛ւն։</b> Այս ֆայլում <b>180 տող</b> տվյալ կա, ոչ թե 5։ Եվ ամեն
աշակերտ ունի ոչ թե մեկ գնահատական, այլ հինգ՝ տարբեր առարկաներից։<br/><br/>
Բառարանը, որ գրեցինք Բ մասում, <b>մեկ անունին տալիս է մեկ թիվ</b>։ Այսօր ոչինչ
չենք փոխում — պարզապես նայում ենք, թե ինչ է պետք։
</p>
</div>

#%% md
Վերջին բան՝ հաշվենք դպրոցի միջինը այն ձևով, որ գիտենք։

#%% code
total = 0
count = 0

for line in lines[1:]:
    if line == "":
        continue
    parts = line.split(",")
    total = total + int(parts[3])
    count = count + 1

print("grades counted:", count)
print("school average:", total / count)

#%% md
**180 գնահատական, միջինը՝ ճիշտ 7.0։** Սա այն թիվն է, որին վերադառնալու ենք ամբողջ
դասընթացի ընթացքում։

Ամեն ինչ կարգին է։ **Եվ հենց դա է ամենահետաքրքիրը։**

Ֆայլի տողերից մեկում ծանոթագրության մեջ կա ստորակետ՝ `"absent, retake scheduled"`։
`split(",")`-ը չգիտի դա։ Այդ տողը նա բաժանում է **վեց** մասի, ոչ թե հինգի։

Գնահատականը ճիշտ ստացվեց միայն այն պատճառով, որ այն **ստորակետից առաջ է**։ Եթե
ծանոթագրությունը լիներ գնահատականից ձախ, այս բջիջի բոլոր թվերը սխալ կլինեին — և
սխալի հաղորդագրություն չէինք տեսնի։

**16-րդ օրը կստանանք մի գործիք, որը այս ամբողջ բջիջը դարձնում է մեկ տող** և
ստորակետը ինքն է ճիշտ կարդում։

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Քանի՞ տարբեր առարկա

Ֆայլի **երրորդ** սյունակը առարկան է։ Հավաքի՛ր բոլոր առարկաների անունները մեկ
ցուցակում, առանց կրկնության, և տպի՛ր։

#%% code
subjects = []

for line in lines[1:]:
    if line == "":
        continue
    parts = line.split(",")
    subject = parts[2]
    # Add it only if it is not already in the list.
    # ...

print(subjects)

#%% md
### 2. Մեկ դասարանի աշակերտները

Տպի՛ր **11Բ** դասարանի բոլոր աշակերտների անունները, առանց կրկնության։
Դասարանը առաջին սյունակն է, անունը՝ երկրորդը։

#%% code
names = []

for line in lines[1:]:
    if line == "":
        continue
    parts = line.split(",")
    # Keep the name only when parts[0] is the class we want.
    # ...

print(len(names), "students")
print(names)

#%% md
### 3. Քանի՞ չանցած գնահատական

Հաշվի՛ր, թե քանի գնահատական է **4-ից ցածր** ամբողջ դպրոցում։

#%% code
PASS_MARK = 4
failing = 0

for line in lines[1:]:
    if line == "":
        continue
    # Compare int(parts[3]) with PASS_MARK.
    # ...

print("failing grades:", failing)

#%% md
### 4. Մեկ առարկայի միջինը

Հաշվի՛ր **Mathematics** առարկայի միջին գնահատականը ամբողջ դպրոցում։

#%% code
subject_total = 0
subject_count = 0

for line in lines[1:]:
    if line == "":
        continue
    parts = line.split(",")
    # When parts[2] is "Mathematics", add int(parts[3]) to subject_total
    # and add 1 to subject_count.
    # ...

print("total:", subject_total)
print("count:", subject_count)
# The last line is yours: print the average.

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Ամենաբարձր գնահատականը

Գտի՛ր ամենաբարձր գնահատականը ֆայլում և տպի՛ր, թե ո՞վ է ստացել և ո՞ր առարկայից։

#%% code
best_grade = 0
best_name = ""
best_subject = ""

for line in lines[1:]:
    if line == "":
        continue
    # ...

print(best_name, best_subject, best_grade)

#%% md
### 6. Ամեն դասարանի աշակերտների թիվը

Օգտագործի՛ր բառարան՝ `{"11Ա": 12, ...}`։ Դասարանի անունը բանալին է, աշակերտների
թիվը՝ արժեքը։ Ուշադի՛ր եղիր՝ ամեն աշակերտ ֆայլում հանդիպում է հինգ անգամ։

#%% code
students_by_class = {}

for line in lines[1:]:
    if line == "":
        continue
    # ...

print(students_by_class)

#%% md
### 7. Չանցած աշակերտները

Հավաքի՛ր այն աշակերտների անունները, ովքեր ունեն **գոնե մեկ** 4-ից ցածր
գնահատական։ Քանի՞սն են։

#%% code
at_risk = []

for line in lines[1:]:
    if line == "":
        continue
    # ...

print(len(at_risk), "students at risk")

#%% md
### 8. Առարկան՝ ամենացածր միջինով

Հաշվի՛ր բոլոր հինգ առարկաների միջինը և տպի՛ր, թե որն է ամենացածրը։

#%% code
totals = {}
counts = {}

for line in lines[1:]:
    if line == "":
        continue
    # ...

for subject in totals:
    print(f"{subject:<14} {totals[subject] / counts[subject]:.2f}")

#%% md
## Մարտահրավեր

#%% md
### 9. Ամեն դասարանի միջինը, դասավորված

Հաշվի՛ր երեք դասարանի միջինը և տպի՛ր դրանք **ամենաբարձրից ամենացածր**։

Արդյունքը պետք է լինի այսպիսին.

```
11Գ   7.68
11Ա   6.98
11Բ   6.33
```

#%% code
# Two dictionaries: one for the totals, one for the counts.
# Then sorted() with a key -- or by hand, with a loop.

#%% md
### 10. Գտի՛ր վտանգավոր տողը

Վերևում ասացինք, որ մեկ տող `split(",")`-ից հետո դառնում է վեց մաս, ոչ թե հինգ։
Գտի՛ր այն՝ տպելով տողի համարը։

**Հուշում:** `len(parts)`-ը ստուգի՛ր ամեն տողի համար և տպի՛ր այն, որը 5 չէ։

#%% code
for number, line in enumerate(lines[1:], start=2):
    parts = line.split(",")
    # Print the line number when len(parts) is not 5.

#%% md
## Ինչի հասանք

Այսօր նոր շարահյուսություն չսովորեցինք — և դա դիտավորյալ է։

- Երեք գործիք **արդեն տեղում են**՝ numpy, matplotlib, pandas
- Դպրոցի ֆայլը **բացվում է** այն գիտելիքով, որ արդեն ունես
- 36 աշակերտ · 5 առարկա · 180 գնահատական · միջինը՝ **7.0**
- Բառարանը, որ ունենք, **մեկ անունին տալիս է մեկ թիվ** — իսկ այստեղ ամեն աշակերտ
  ունի հինգ գնահատական, դասարան, և ծանոթագրություն
- Մեկ ստորակետ ծանոթագրության մեջ բավական է, որ `split(",")`-ը սխալվի **առանց
  սխալի հաղորդագրության**

## Հաջորդ անգամ

Գրելու ենք ֆունկցիա, որը տպում է հաշվետվության տող։ Հետո տնօրենը կխնդրի **նույնը,
բայց մի փոքր այլ կերպ** — վեց անգամ։

Եվ նույն դասին կստանանք այն, ինչով դա գրվում է **մեկ անգամ**։
