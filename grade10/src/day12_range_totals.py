#%% md
# Թեմա 12 — Հաշվել և գումարել

### Python զրոյից · Թեմա 12-ը 24-ից

Նախորդ թեմայում սովորեցինք **անել** մի բան բոլորի հետ։ Այսօր սովորում ենք **հաշվել**։

Այսօրվա վերջում կունենաս քո դասարանի իրական միջինը՝ հաշված ծրագրով։

## ԱՅՍՕՐ:

- **Ա մաս:** կուտակիչ — գումարել ցիկլով
- **Բ մաս:** միջինը
- **Գ մաս:** `range` — թվերի շարք

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>for grade in class_grades:</code> — կրկնում է ներսի կոդը ամեն տարրի համար։<br/>
Եվ 5-րդ թեմայից՝ <code>student_grade = student_grade + 1</code>։ Այսօր դա կենտրոնական է։
</p>
</div>

#%% md
## Ա մաս: Կուտակիչ

Խնդիրը՝ գումարել բոլոր միավորները։

#%% code
class_grades = [9, 6, 10, 3, 8]

print(9 + 6 + 10 + 3 + 8)

#%% md
Աշխատում է հինգի համար։ Քսանի համար՝ ոչ, և դասարանը կփոխվի։

Գաղափարը՝ պահել «մինչ այժմ հավաքած գումարը» մի փոփոխականում և ամեն պտույտում
ավելացնել նրան։

#%% code
class_grades = [9, 6, 10, 3, 8]

total = 0

for grade in class_grades:
    total = total + grade

print(total)

#%% md
Երեք մասից բաղկացած ձև, որը կհանդիպի ամբողջ դասընթացում.

1. **Մինչ ցիկլը՝** `total = 0` — սկսում ենք զրոյից
2. **Ցիկլի ներսում՝** `total = total + grade` — ավելացնում ենք
3. **Ցիկլից հետո՝** `print(total)` — նայում ենք արդյունքին

Ուշադրություն՝ `print`-ը **ցիկլից դուրս** է։ Եթե ներսում լիներ, կտպեր ամեն պտույտում։

#%% code
class_grades = [9, 6, 10, 3, 8]

total = 0

for grade in class_grades:
    total = total + grade
    print("added", grade, "- total is now", total)

print("final total:", total)

#%% md
Նույն ձևով կարելի է **հաշվել**, ոչ միայն գումարել։ Ավելացնում ենք 1՝ միավորի փոխարեն։

#%% code
class_grades = [9, 6, 10, 3, 8]

how_many = 0

for grade in class_grades:
    how_many = how_many + 1

print(how_many)

#%% md
Այստեղ `len()`-ը ավելի կարճ կլիներ։ Բայց հաշվիչի ձևը պետք կգա **ընդմիջումից հետո**, երբ ուզենք
հաշվել ոչ թե բոլորին, այլ միայն նրանց, ովքեր չեն անցել։

#%% md
## Բ մաս: Միջինը

Միջինը գումարն է՝ բաժանած քանակի։ Երկուսն էլ արդեն ունենք։

#%% code
class_grades = [9, 6, 10, 3, 8, 5, 8, 4, 9, 2, 8, 6]

total = 0

for grade in class_grades:
    total = total + grade

class_average = total / len(class_grades)

print("total:", total)
print("students:", len(class_grades))
print("average:", class_average)

#%% md
`6.5` — և ահա, 3-րդ թեմայի `float`-ը վերջապես իմաստ ունի։

Տասներկու միավորի գումարը 78 է, բաժանած 12-ի՝ 6.5։ **Միջինը գրեթե երբեք ամբողջ
թիվ չէ**, և դա հենց այն դեպքն է, որի համար տասնորդական թվեր կան։

#%% md
Երբեմն միջինը երկար է ստացվում։

#%% code
class_grades = [9, 6, 10, 3, 8, 5, 8]

total = 0
for grade in class_grades:
    total = total + grade

print(total / len(class_grades))

#%% md
Մատյանում այդպիսի թիվ չես գրի։ Կլորացնում ենք՝ 4-րդ թեմայի `round`-ով։

#%% code
class_average = total / len(class_grades)

print(round(class_average, 1))
print(f"Class average: {class_average:.1f}")

#%% md
Երկու ձևն էլ ճիշտ է։ `round()` — երբ թիվը պետք է հետագայում օգտագործես։
`:.1f` — երբ միայն տպում ես։

#%% md
## Գ մաս: `range` — թվերի շարք

Նախորդ թեմայում օգտագործեցինք `range(len(...))` առանց բացատրության։ Հիմա նայենք դրան առանձին։

#%% code
for number in range(1, 11):
    print(number)

#%% md
`range(1, 11)` — 1-ից **մինչև** 11, առանց 11-ի։ Վերջին թիվը ներառված չէ։

Սա սկզբում տարօրինակ է թվում, բայց նույն տրամաբանությունն է, ինչ 7-րդ թեմայի `[0:3]`-ը։

Եթե միայն մեկ թիվ գրես, սկսում է զրոյից։

#%% code
for number in range(5):
    print(number)

#%% md
Եվ ահա թե ինչու էր `range(len(...))`-ը աշխատում. `len(...)` = 5 նշանակում է
`range(5)` = 0, 1, 2, 3, 4 — ուղիղ այն ինդեքսները, որ ցուցակն ունի։

#%% code
student_names = ["Ani", "Davit", "Nare"]

for position in range(len(student_names)):
    print(position, student_names[position])

#%% md
<div style="border-left: 6px solid #181; background: #f2fff5; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#181; margin-top:0;">🏫 Քո դասարանում</h3>
<p style="color:#181; margin-bottom:0;">
Դասարանի միջինը հաշվելը այն բանն է, որ եռամսյակը մեկ անում ես ձեռքով, հաշվիչով,
և ամեն անգամ վախենում ես, որ սխալվել ես։ Ծրագիրը այն հաշվում է վայրկյանում և
<b>երբեք չի սխալվում</b>։ Այն կարող է սխալ տվյալ ստանալ, բայց գումարելիս չի սխալվի։
</p>
</div>

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Պարտադիր առաջադրանքներ</h3>
<p style="color:#900; margin-bottom:0;">
<b>1.</b> Հաշվի՛ր քո դասարանի միավորների գումարը ցիկլով։<br/><br/>
<b>2.</b> Հաշվի՛ր և տպի՛ր <b>քո դասարանի իրական միջինը</b>՝ մեկ նիշով կլորացրած։<br/><br/>
<b>3.</b> Տպի՛ր 1-ից 10 թվերը <code>range</code>-ով։<br/><br/>
<b>4.</b> Հաշվի՛ր, թե քո դասարանում քանի աշակերտ ունի 10 միավոր։
</p>
</div>

#%% code
# Exercise 1 and 2 - total and average

class_grades = [9, 6, 10, 3, 8]

total = 0
for grade in class_grades:
    total = total + grade

print(f"Total: {total}")
print(f"Average: {total / len(class_grades):.1f}")

#%% code
# Exercise 4 - how many students have 10

how_many = 0

for grade in class_grades:
    if grade == 10:
        how_many = how_many + 1

print(how_many)

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">🚀 Լրացուցիչ առաջադրանքներ</h3>
<p style="color:#f71; margin-bottom:0;">
<b>5.</b> Տպի՛ր միավորների բաշխումը՝ 1-ից 10, ամեն մեկի դիմաց՝ քանի աշակերտ։
(Հուշում՝ ցիկլ ցիկլի ներսում։)<br/><br/>
<b>6.</b> Հաշվի՛ր, թե աշակերտների քանի՞ տոկոսն է անցել։<br/><br/>
<b>7.</b> Հաշվի՛ր միջինը <b>միայն անցածների</b> համար։<br/><br/>
<b>8.</b> Տպի՛ր 10-ից 1 հակառակ կարգով։ (Հուշում՝ <code>range(10, 0, -1)</code>։)<br/><br/>
<b>9.</b> Հաշվի՛ր, թե քանի՞ միավոր է պակասում դասարանի միջինը 7-ի հասցնելու համար։
</p>
</div>

#%% code
# Extra 5-9 - your space

for mark in range(1, 11):
    how_many = 0
    for grade in class_grades:
        if grade == mark:
            how_many = how_many + 1
    print(f"{mark} points: {how_many} students")

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🧗 Մարտահրավեր</h3>
<p style="color:#06c; margin-bottom:0;">
<b>10.</b> Կառուցի՛ր տեքստային գծապատկեր՝ ամեն միավորի դիմաց այնքան աստղանիշ, քանի
աշակերտ ունի այդ միավորը.<br/><br/>
<code>10: **</code><br/>
<code> 9: ***</code><br/><br/>
Հուշում՝ <code>"*" * how_many</code> (3-րդ թեմայի լրացուցիչ առաջադրանքից)։
</p>
</div>

#%% code
# Challenge 10 - a text chart

for mark in range(10, 0, -1):
    how_many = 0
    for grade in class_grades:
        if grade == mark:
            how_many = how_many + 1
    print(f"{mark:>2}: {'*' * how_many}")

#%% md
<div style="border-left: 6px solid #747; background: #f8f6fb; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#747; margin-top:0;">🏠 Տնային</h3>
<p style="color:#747; margin-bottom:0;">
Այս նոթատետրի <b>Պարտադիր</b> առաջադրանքները, որ չհասցրիր դասին։<br/><br/>
<b>Նոր բան չկա</b> — ամեն առաջադրանք այս նոթատետրից է, և օգտագործում է միայն այն,
ինչ այսօր սովորեցինք։<br/>
Հաջորդ նիստը սկսվում է դրանց ստուգումով։
</p>
</div>

#%% md
## Ինչի հասանք

- **Կուտակիչի ձևը՝** `total = 0` մինչ ցիկլը, `total = total + ...` ներսում, `print` հետո։
- Միջինը՝ `total / len(...)`։ Գրեթե միշտ տասնորդական թիվ է։
- `round(x, 1)` կամ `f"{x:.1f}"` — կլորացնում են։
- `range(1, 11)` — 1-ից 10։ **Վերջին թիվը ներառված չէ։**

## Ի՞նչ է գալիս հետո

Ընդմիջումից հետո ցիկլն ու պայմանը միասին լուծելու են իսկական հարցեր՝ ո՞վ չի անցել,
քանի՞սն են անցել, ո՞րն է ամենաբարձր միավորը։

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Հաշվի՛ր քո դասարանի միջինը և համեմատի՛ր այն մատյանում գրվածի հետ։ Համընկնո՞ւմ է։
