#%% md
# Թեմա 11 — Գնահատել ամբողջ դասարանը

### Python զրոյից · Թեմա 11-ը 24-ից

Նախորդ թեմայում սովորեցինք որոշում ընդունել **մեկ** աշակերտի համար։ Այսօր անում ենք այն, ինչի
համար իսկապես պետք է՝ **ամբողջ դասարանի մատյանը** — ամեն աշակերտի դիմաց «անցավ»
կամ «չանցավ»։

## ԱՅՍՕՐ:

- **Ա մաս:** մատյանը՝ այն ձևով, որ արդեն գիտենք
- **Բ մաս:** ցիկլ — անել նույնը բոլորի համար
- **Գ մաս:** երկու տարբերակը կողք կողքի

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>if grade >= PASS_MARK:</code> ... <code>else:</code> — մեկ աշակերտի որոշումը։<br/>
Մատյանը՝ ցուցակներ և բառարան։<br/><br/>
<b>Այսօր առաջին անգամ ցիկլ ենք տեսնելու։</b>
</p>
</div>

#%% md
## Ա մաս: Մատյանը՝ այն ձևով, որ արդեն գիտենք

Մեզ պետք է տպել տասնհինգ աշակերտի արդյունքը։ Այն, ինչ գիտենք, մեկ բան է՝ ամեն
աշակերտի համար առանձին `if`/`else` բլոկ։

<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Այս ձևն աշխատում է, բայց երկար է։</b> Դասի երկրորդ կեսին կսովորենք մի ձև,
որը այս ամբողջ բջիջը դարձնում է <b>չորս տող</b> — և աշխատում է ցանկացած թվով
աշակերտի համար։
</p>
</div>

**Գործարկի՛ր և կարդա՛։**

#%% code
grade = 9
if grade >= 4:
    print("Ani: passed")
else:
    print("Ani: failed")

grade = 6
if grade >= 4:
    print("Davit: passed")
else:
    print("Davit: failed")

grade = 10
if grade >= 4:
    print("Nare: passed")
else:
    print("Nare: failed")

grade = 3
if grade >= 4:
    print("Aram: passed")
else:
    print("Aram: failed")

grade = 8
if grade >= 4:
    print("Mariam: passed")
else:
    print("Mariam: failed")

grade = 5
if grade >= 4:
    print("Tigran: passed")
else:
    print("Tigran: failed")

grade = 8
if grade >= 4:
    print("Lilit: passed")
else:
    print("Lilit: failed")

grade = 4
if grade >= 4:
    print("Gor: passed")
else:
    print("Gor: failed")

grade = 9
if grade >= 4:
    print("Anahit: passed")
else:
    print("Anahit: failed")

grade = 2
if grade >= 4:
    print("Hayk: passed")
else:
    print("Hayk: failed")

grade = 8
if grade >= 4:
    print("Sona: passed")
else:
    print("Sona: failed")

grade = 6
if grade >= 4:
    print("Vahe: passed")
else:
    print("Vahe: failed")

grade = 7
if grade >= 4:
    print("Mane: passed")
else:
    print("Mane: failed")

grade = 5
if grade >= 4:
    print("Samvel: passed")
else:
    print("Samvel: failed")

grade = 9
if grade >= 4:
    print("Elen: passed")
else:
    print("Elen: failed")

#%% md
Տասնհինգ աշակերտ, յոթանասունհինգ տող։ Աշխատում է։

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Առաջադրանք 1 — պարտադիր</h3>
<p style="color:#900; margin-bottom:0;">
Ավելացրո՛ւ <b>երեք աշակերտ քո դասարանից</b> ներքևի բջիջում՝ ուղիղ նույն ձևով։
Առաջինը գրված է։
</p>
</div>

#%% code
# Exercise 1 - add three students from your own class, the same way

grade = 7
if grade >= 4:
    print("Anna: passed")
else:
    print("Anna: failed")

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Առաջադրանք 2 — պարտադիր</h3>
<p style="color:#900; margin-bottom:0;">
Տնօրինությունը որոշեց, որ մատյանում «passed»-ի փոխարեն պետք է գրվի
<b>«satisfactory»</b>։<br/><br/>
Փոխի՛ր այն <b>վերևի մեծ բջիջում</b>՝ բոլոր տասնհինգ տեղում։<br/><br/>
Ուշադրություն դարձրու, թե ինչպես է դա ընթանում։
</p>
</div>

#%% md
## Բ մաս: Ցիկլ

Հիմա նայի՛ր այն մեծ բջիջին և մի բան նկատի՛ր.

Բոլոր տասնհինգ բլոկը **նույնն են**։ Ամեն մեկը նույն երեք տողն է։ Փոխվում է միայն
անունը և թիվը։

Python-ում կա ձև, որով նույն կոդը կատարվում է **ամեն տարրի համար**։ Այն կոչվում է
**ցիկլ**։

#%% code
student_names = ["Ani", "Davit", "Nare"]

for student_name in student_names:
    print(student_name)

#%% md
Կարդանք բառ առ բառ.

- `for` — «յուրաքանչյուրի համար»
- `student_name` — **անուն, որ մենք ենք ընտրում**։ Ամեն պտույտում այն ստանում է
  հաջորդ արժեքը
- `in student_names` — որ ցուցակից
- `:` և չորս բացատ — ուղիղ ինչպես `if`-ում

#%% code
student_names = ["Ani", "Davit", "Nare"]

for student_name in student_names:
    print("This time student_name is:", student_name)

#%% md
Երեք պտույտ, երեք տարբեր արժեք։ Ոչ մի կախարդանք — Python-ը կրկնում է ներսի տողերը՝
ամեն անգամ նոր արժեքով։

Ներսում կարող է լինել **որքան ուզես կոդ**, ոչ միայն մեկ տող։

#%% code
student_names = ["Ani", "Davit", "Nare"]

for student_name in student_names:
    print("Student:", student_name)
    print("Present")
    print()

#%% md
Իսկ ցիկլից **դուրս** գրվածը կատարվում է մեկ անգամ։ Բացատներն են որոշում։

#%% code
student_names = ["Ani", "Davit", "Nare"]

print("=== REGISTER ===")

for student_name in student_names:
    print(student_name)

print("=== END ===")

#%% md
### Ցիկլը և պայմանը միասին

Ցիկլի ներսում կարող է լինել `if`։ Այդ դեպքում **երկու անգամ** ենք ներս տեղաշարժում։

#%% code
PASS_MARK = 4
class_grades = [9, 6, 10, 3, 8]

for grade in class_grades:
    if grade >= PASS_MARK:
        print(grade, "- passed")
    else:
        print(grade, "- failed")

#%% md
### Անունը և միավորը միասին

Մեկ խնդիր մնաց. ցիկլը տալիս է **կա՛մ** անունը, **կա՛մ** միավորը։ Իսկ մատյանի համար
երկուսն էլ պետք են։

Առայժմ լուծենք ինդեքսով։

#%% code
student_names = ["Ani", "Davit", "Nare"]
class_grades = [9, 6, 10]

for position in range(len(student_names)):
    print(f"{student_names[position]}: {class_grades[position]}")

#%% md
`range(len(...))` — տալիս է 0, 1, 2 ... մինչև ցուցակի վերջը։ 12-րդ թեմայում `range`-ին
առանձին կնայենք։

**Աշխատում է, բայց պահանջում է, որ երկու ցուցակը միշտ նույն հերթականությամբ լինեն։**
Այդ խնդիրը 8-րդ թեմայում լուծվում է վերջնականապես։

#%% md
## Գ մաս: Երկու տարբերակը կողք կողքի

Ահա ամբողջ մատյանը՝ **չորս տողով**։

#%% code
PASS_MARK = 4

student_names = ["Ani", "Davit", "Nare", "Aram", "Mariam", "Tigran", "Lilit", "Gor",
                 "Anahit", "Hayk", "Sona", "Vahe", "Mane", "Samvel", "Elen"]
class_grades = [9, 6, 10, 3, 8, 5, 8, 4, 9, 2, 8, 6, 7, 5, 9]

for position in range(len(student_names)):
    if class_grades[position] >= PASS_MARK:
        print(f"{student_names[position]}: passed")
    else:
        print(f"{student_names[position]}: failed")

#%% md
Եվ հիմա փորձի՛ր այն, ինչ վերևի մեծ բջիջում դժվար էր.

- **«passed»-ը փոխի՛ր «satisfactory»-ի։** Մեկ խմբագրում, ոչ թե տասնհինգ։
- **Ավելացրո՛ւ հինգ աշակերտ** երկու ցուցակին։ Ցիկլում ոչինչ չես փոխում։
- **Փոխի՛ր `PASS_MARK`-ը։** Մեկ խմբագրում։

| | Առանձին բլոկներ | Ցիկլ |
|---|---|---|
| 15 աշակերտի համար | 75 տող | **4 տող** |
| «passed»-ը փոխել | 15 խմբագրում | 1 |
| Նոր աշակերտ ավելացնել | 5 նոր տող | 0 |
| 300 աշակերտի համար | ~1500 տող | **4 տող** |

#%% md
<div style="border-left: 6px solid #181; background: #f2fff5; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#181; margin-top:0;">🏫 Քո դասարանում</h3>
<p style="color:#181; margin-bottom:0;">
Այս չորս տողը այն է, ինչ անում է դպրոցի էլեկտրոնային մատյանը, երբ սեղմում ես
«չանցածների ցուցակ»։ Ոչ մի ավելի բարդ բան այնտեղ չկա՝ ցիկլ և պայման։<br/><br/>
Ցիկլն այն է, ինչի համար համակարգիչ ենք օգտագործում. մեկ անգամ գրում ես, թե ինչ անել
<b>մեկ</b> աշակերտի հետ, և համակարգիչը կրկնում է դա բոլորի համար։
</p>
</div>

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Պարտադիր առաջադրանքներ</h3>
<p style="color:#900; margin-bottom:0;">
<b>3.</b> Վերցրո՛ւ քո դասարանի ցուցակները և տպի՛ր բոլոր անունները ցիկլով։<br/><br/>
<b>4.</b> Տպի՛ր բոլոր միավորները ցիկլով՝ <code>Grade: 9</code> ձևով։<br/><br/>
<b>5.</b> Ցիկլի ներսում դի՛ր <code>if</code> և տպի՛ր <code>passed</code>/<code>failed</code>
ամեն միավորի համար։<br/><br/>
<b>6.</b> Տպի՛ր ամբողջ մատյանը՝ անուն և արդյունք, չորս տողով։ Հետո ավելացրո՛ւ հինգ
աշակերտ ցուցակներին և գործարկի՛ր նորից՝ <b>առանց ցիկլը դիպչելու</b>։
</p>
</div>

#%% code
# Exercise 3 and 4 - all names, all grades

student_names = ["Ani", "Davit", "Nare"]

for student_name in student_names:
    print(student_name)

#%% code
# Exercise 5 - a condition inside a loop

PASS_MARK = 4
class_grades = [9, 6, 10, 3, 8]

for grade in class_grades:
    if grade >= PASS_MARK:
        print(grade, "- passed")
    else:
        print(grade, "- failed")

#%% code
# Exercise 6 - the whole register in four lines

student_names = ["Ani", "Davit", "Nare"]
class_grades = [9, 6, 10]

for position in range(len(student_names)):
    if class_grades[position] >= PASS_MARK:
        print(f"{student_names[position]}: passed")
    else:
        print(f"{student_names[position]}: failed")

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">🚀 Լրացուցիչ առաջադրանքներ</h3>
<p style="color:#f71; margin-bottom:0;">
<b>7.</b> Տպի՛ր միայն անցած աշակերտներին (առանց <code>else</code>-ի)։<br/><br/>
<b>8.</b> Տպի՛ր մատյան՝ վերնագրով և ամփոփիչ տողով ցիկլից հետո։<br/><br/>
<b>9.</b> Ցիկլի ներսում դի՛ր 10-րդ թեմայի չորս մակարդակի շղթան՝ ամեն աշակերտի համար
<code>excellent</code> / <code>good</code> / <code>satisfactory</code> /
<code>unsatisfactory</code>։<br/><br/>
<b>10.</b> Գրի՛ր ցիկլ, որը տպում է ամեն աշակերտի անունը <b>մեծատառերով</b>՝
<code>student_name.upper()</code>։<br/><br/>
<b>11.</b> Ի՞նչ է լինում, եթե ցիկլից հետո տպես <code>student_name</code>-ը։
Ի՞նչ արժեք ունի այն։ Նախ գուշակի՛ր։
</p>
</div>

#%% code
# Extra 7-11 - your space

for grade in class_grades:
    if grade >= PASS_MARK:
        print(grade, "- passed")

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🧗 Մարտահրավեր</h3>
<p style="color:#06c; margin-bottom:0;">
<b>12.</b> Տպի՛ր մատյան, որտեղ ամեն տողի սկզբում կա համար՝
<code>1. Ani: passed</code>, <code>2. Davit: passed</code> ...<br/><br/>
Հուշում՝ <code>position</code>-ը սկսվում է 0-ից, բայց մատյանում համարակալումը
սկսվում է 1-ից։<br/><br/>
<b>13.</b> Երկու ցիկլ գրի՛ր՝ առաջինը տպում է անցածներին, երկրորդը՝ չանցածներին,
երկու առանձին ցուցակի տեսքով վերնագրերով։
</p>
</div>

#%% code
# Challenge 12-13 - a numbered register

for position in range(len(student_names)):
    print(f"{position + 1}. {student_names[position]}: {class_grades[position]}")

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

- `for value in list:` — կրկնում է ներսի կոդը ամեն տարրի համար։
- **Ցուցակի երկարությունը նշանակություն չունի։** Նույն կոդը՝ 5 և 500 աշակերտի համար։
- Ցիկլի ներսում կարող է լինել `if`։ Երկու անգամ ներս տեղաշարժ։
- **Ամբողջ դասարանի մատյանը՝ չորս տող։**

## Ի՞նչ է գալիս հետո

Հիմա կարող ենք **անել** մի բան բոլորի հետ։ Հաջորդ նիստում կսովորենք **հաշվել** —
քանիսն են, ինչքան է գումարը, որքան է դասարանի միջինը։

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Տպի՛ր քո ամբողջ դասարանի մատյանը ցիկլով և համեմատի՛ր 6-րդ թեմայի մարտահրավերի հետ։
