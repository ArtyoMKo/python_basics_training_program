#%% md
# Օր 14 — Գտնել մեկ աշակերտի

### Python զրոյից · Օր 14-ը 24-ից

Ծնողը զանգում է և հարցնում՝ **«Արամի միավորը քանի՞սն է»**։

Այսօր ծրագիրը սովորում է պատասխանել այդ հարցին — և մենք գտնում ենք, թե ինչու է
ներկայիս ձևը վտանգավոր։

## ԱՅՍՕՐ:

- **Ա մաս:** գտնել՝ այն ձևով, որ արդեն գիտենք
- **Բ մաս:** բառարան
- **Գ մաս:** ավելացնել, ուղղել, ստուգել

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
Մատյանը՝ երկու ցուցակ։<br/>
<code>student_names[position]</code> և <code>class_grades[position]</code> —
կապված են միայն հերթականությամբ։
</p>
</div>

#%% md
## Ա մաս: Գտնել՝ այն ձևով, որ արդեն գիտենք

Աշակերտի միավորը գտնելու համար պետք է իմանալ նրա **տեղը** ցուցակում, և հետո վերցնել
նույն տեղը մյուս ցուցակից։

<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Այս ձևն աշխատում է, բայց փխրուն է։</b> Դասի երկրորդ կեսին կսովորենք ձև, որտեղ
տեղը ընդհանրապես նշանակություն չունի։
</p>
</div>

#%% code
student_names = ["Ani", "Davit", "Nare", "Aram"]
class_grades = [9, 6, 10, 3]

print(f"{student_names[3]}'s grade is {class_grades[3]}")

#%% md
Դա նշանակում է, որ ամեն անգամ պետք է հաշվես, թե որերորդն է աշակերտը։ Կարող ենք
դա անել ցիկլով՝ 12-րդ օրվա ձևով։

#%% code
looking_for = "Aram"

for position in range(len(student_names)):
    if student_names[position] == looking_for:
        print(f"{looking_for}: {class_grades[position]}")

#%% md
Աշխատում է։ Հինգ տող՝ մեկ հարցի պատասխանելու համար։

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Առաջադրանք 1 — պարտադիր</h3>
<p style="color:#900; margin-bottom:0;">
Ներքևի բջիջում գտի՛ր <b>երեք աշակերտի</b> միավորը՝ անունով։ Առաջինը գրված է։
</p>
</div>

#%% code
# Exercise 1 - look up three students by name

student_names = ["Ani", "Davit", "Nare", "Aram"]
class_grades = [9, 6, 10, 3]

looking_for = "Nare"

for position in range(len(student_names)):
    if student_names[position] == looking_for:
        print(f"{looking_for}: {class_grades[position]}")

#%% md
### Իսկ հիմա մի բան, որ տեղի է ունենում իրական կյանքում

Դավիթը տեղափոխվեց ուրիշ դպրոց։ Հանում ես նրան ցուցակից։

Բայց շտապում ես և **մոռանում ես հանել նրա միավորը մյուս ցուցակից**։

#%% code
student_names = ["Ani", "Nare", "Aram"]
class_grades = [9, 6, 10, 3]

looking_for = "Aram"

for position in range(len(student_names)):
    if student_names[position] == looking_for:
        print(f"{looking_for}: {class_grades[position]}")

#%% md
**Արամը հանկարծ ստացավ 10։** Իր 3-ի փոխարեն։

Ոչ մի կարմիր տեքստ։ Ոչ մի սխալի հաղորդագրություն։ Ծրագիրը հանգիստ աշխատեց և տվեց
**սխալ պատասխան**։ Եթե դա իրական մատյան լիներ, ոչ ոք չէր նկատի։

Խնդիրը արմատային է. անունն ու միավորը կապված են միայն նրանով, որ **պատահաբար նույն
տեղում են**։

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Առաջադրանք 2 — պարտադիր</h3>
<p style="color:#900; margin-bottom:0;">
Ներքևի բջիջում հանի՛ր <b>առաջին</b> աշակերտին միայն <code>student_names</code>-ից և
գործարկի՛ր որոնումը։<br/><br/>
Քանի՞ աշակերտի պատասխանն է սխալ դառնում։
</p>
</div>

#%% code
# Exercise 2 - remove one name only, then look up

student_names = ["Ani", "Davit", "Nare", "Aram"]
class_grades = [9, 6, 10, 3]

student_names.remove("Ani")

for position in range(len(student_names)):
    print(f"{student_names[position]}: {class_grades[position]}")

#%% md
## Բ մաս: Բառարան

Python-ում կա ձև, որտեղ արժեքը պահվում է **անվան տակ**, ոչ թե տեղում։
Այն կոչվում է **բառարան**։

#%% code
class_grades = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3}

print(class_grades)

#%% md
Ձևավոր փակագծեր `{ }`, և ամեն զույգը՝ `բանալի: արժեք`։

- **Բանալին** (`"Ani"`) — այն, ինչով փնտրում ենք
- **Արժեքը** (`9`) — այն, ինչ գտնում ենք

Հասնում ենք արժեքին ուղիղ այնպես, ինչպես ցուցակում — բայց թվի փոխարեն գրում ենք
**անունը**։

#%% code
print(class_grades["Ani"])
print(class_grades["Aram"])

#%% md
**Մեկ տող։** Ցիկլ չկա, ինդեքս չկա, `range` չկա։

Եվ հիմա Դավիթին հանելը անվտանգ է։

#%% code
class_grades = {"Ani": 9, "Nare": 10, "Aram": 3}

print(f"Aram's grade is {class_grades['Aram']}")

#%% md
Արամը ստացավ իր 3-ը։ Հերթականությունը նշանակություն չունի, որովհետև
**միավորը կապված է անվան հետ, ոչ թե տեղի**։

> Ուշադրություն f-տողի ներսում չակերտներին. դրսում կրկնակի են (`f"..."`), ուստի
> ներսում գրում ենք միակի (`'Aram'`)։

#%% md
## Գ մաս: Ավելացնել, ուղղել, ստուգել

#%% code
class_grades = {"Ani": 9, "Nare": 10, "Aram": 3}

class_grades["Gor"] = 4

print(class_grades)

#%% md
Գնահատականը ուղղելը՝ **ուղիղ նույն տողը**։

#%% code
class_grades["Ani"] = 10

print(class_grades)

#%% md
Եթե բանալին չկա՝ ավելանում է։ Եթե կա՝ փոխարինվում է։ Մեկ ձև՝ երկու գործողության համար։

Հանելը՝ `del`։ Իսկ քանիսն են՝ `len()`, ուղիղ ինչպես ցուցակում։

#%% code
del class_grades["Aram"]

print(class_grades)
print(len(class_grades))

#%% md
### Հիմա կոտրենք

Ի՞նչ է լինում, երբ փնտրում ես աշակերտի, ով բառարանում չկա։

#%% code expected-error: KeyError
print(class_grades["Aram"])

#%% md
```
KeyError: 'Aram'
```

«Այդ բանալին բառարանում չկա»։ Python-ը ուղիղ ցույց է տալիս, թե որն է չգտել։

**Ուշադրություն՝ այս անգամ սխալ եղավ։** Երկու ցուցակի դեպքում սխալ պատասխան էինք
ստանում լռելյայն։ Հիմա ծրագիրը **բողոքում է**, և դա շատ ավելի լավ է։

Խուսափելու ձևը՝ `in`, ուղիղ ինչպես ցուցակում։

#%% code
if "Aram" in class_grades:
    print(class_grades["Aram"])
else:
    print("no such student in this class")

#%% md
### Երկու տարբերակը կողք կողքի

| | Երկու ցուցակ | Բառարան |
|---|---|---|
| Գտնել մեկին | 5 տող ցիկլով | **1 տող** |
| Աշակերտ հանել | երկու տեղից, զգույշ | մեկ տեղից |
| Եթե մոռանաս մի տեղից | **սխալ պատասխան, առանց սխալի** | անհնար է |
| Եթե աշակերտը չկա | ոչինչ չի տպվում | `KeyError` — բողոքում է |

#%% md
<div style="border-left: 6px solid #181; background: #f2fff5; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#181; margin-top:0;">🏫 Քո դասարանում</h3>
<p style="color:#181; margin-bottom:0;">
Ցուցակը Excel-ի <b>սյունակն</b> է։ Բառարանը՝ <b>երկու սյունակ, որոնք միշտ իրար հետ
են</b> — ուղիղ այն, ինչ անում է <code>ՈւՂՂԱՀԱՅԱՑ.ՓՆՏՐԵԼ</code>-ը։ Տարբերությունն այն
է, որ այստեղ դրանք չեն կարող իրարից անջատվել, որովհետև դրանք մեկ բան են։
</p>
</div>

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Պարտադիր առաջադրանքներ</h3>
<p style="color:#900; margin-bottom:0;">
<b>3.</b> Գրի՛ր <b>քո ամբողջ դասարանը մեկ բառարանով</b>՝ անուն → միավոր։
Երկու ցուցակն այլևս պետք չեն։<br/><br/>
<b>4.</b> Տպի՛ր երեք աշակերտի միավորը՝ անունով փնտրելով։<br/><br/>
<b>5.</b> Ավելացրո՛ւ նոր աշակերտ, ուղղի՛ր մեկի միավորը, հանի՛ր մեկին։ Տպի՛ր
բառարանը ամեն քայլից հետո։<br/><br/>
<b>6.</b> <b>Կոտրի՛ր դիտավորյալ։</b> Փնտրի՛ր աշակերտի, ով չկա։ Կարդա՛
<code>KeyError</code>-ը, հետո ուղղի՛ր <code>in</code>-ով։
</p>
</div>

#%% code
# Exercise 3 - your whole class in one dictionary

class_grades = {"Ani": 9, "Davit": 6}

print(class_grades)

#%% code
# Exercise 5 - add, correct, remove

class_grades["Nare"] = 10
class_grades["Ani"] = 10
del class_grades["Davit"]

print(class_grades)

#%% code
# Exercise 6 - break it on purpose, then fix it with in

if "Davit" in class_grades:
    print(class_grades["Davit"])
else:
    print("no such student")

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">🚀 Լրացուցիչ առաջադրանքներ</h3>
<p style="color:#f71; margin-bottom:0;">
<b>7.</b> Գրի՛ր ստուգում, որը հարցնում է անուն և տպում միավորը կամ ասում, որ
այդպիսի աշակերտ չկա։<br/><br/>
<b>8.</b> Երկու աշակերտի միավորները փոխի՛ր տեղերով։<br/><br/>
<b>9.</b> Գրի՛ր երկրորդ բառարան՝ անուն → հաճախում։ Տպի՛ր մեկ աշակերտի երկու
տվյալն էլ։<br/><br/>
<b>10.</b> Ի՞նչ է լինում, եթե նույն բանալին երկու անգամ գրես բառարանում՝
<code>{"Ani": 9, "Ani": 10}</code>։ Նախ գուշակի՛ր։<br/><br/>
<b>11.</b> Կարո՞ղ է բանալին թիվ լինել՝ <code>{1: "Ani"}</code>։ Փորձի՛ր։
</p>
</div>

#%% code
# Extra 7-11 - your space

looking_for = "Nare"

if looking_for in class_grades:
    print(f"{looking_for}: {class_grades[looking_for]}")
else:
    print("no such student")

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🧗 Մարտահրավեր</h3>
<p style="color:#06c; margin-bottom:0;">
<b>12.</b> Վերցրո՛ւ երկու ցուցակ և <b>ծրագրով</b> սարքի՛ր դրանցից բառարան։
Հուշում՝ ցիկլ <code>range(len(...))</code>-ով, և ներսում՝
<code>class_grades[student_names[position]] = ...</code><br/><br/>
Սա ուղիղ այն է, ինչ 22-րդ օրը ֆայլից կարդալիս անելու ենք։
</p>
</div>

#%% code
# Challenge 12 - build a dictionary from two lists

student_names = ["Ani", "Davit", "Nare"]
grade_values = [9, 6, 10]

class_grades = {}

for position in range(len(student_names)):
    class_grades[student_names[position]] = grade_values[position]

print(class_grades)

#%% md
## Ինչի հասանք

- `{"Ani": 9}` — **բանալի → արժեք**։ Անունը ներս, միավորը դուրս։
- `class_grades["Ani"] = 10` — ավելացնում է, եթե չկա, ուղղում է, եթե կա։
- `del` — հանում է։ `len()` — քանիսն են։ `in` — կա՞։
- `KeyError` — այդ բանալին չկա։ **Ծրագիրը բողոքում է, ոչ թե սխալ պատասխան տալիս։**
- **Հերթականությունը այլևս նշանակություն չունի։**

## Հաջորդ անգամ

Հիմա գիտենք, թե ինչպես գտնել **մեկ** աշակերտի միավորը։ Հաջորդ դասին ցիկլ ենք գրելու
բառարանի վրայով և տպելու ենք **ամբողջ մատյանը** — և կտեսնենք, որ 10-րդ և 12-րդ օրվա
բոլոր ցիկլերը դառնում են ավելի կարճ։

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Վերաշարադրի՛ր քո դասարանը բառարանով և գտի՛ր հինգ աշակերտի միավորը՝ անունով։
