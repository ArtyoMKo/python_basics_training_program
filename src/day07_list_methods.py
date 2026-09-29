#%% md
# Օր 7 — Աշխատել մատյանի հետ

### Python զրոյից · Օր 7-ը 24-ից

Դասարանը փոխվում է. աշակերտ է գալիս, աշակերտ է հեռանում, ցուցակը պետք է այբբենական
կարգով։ Այսօր այդ ամենի մասին է։

## ԱՅՍՕՐ:

- **Ա մաս:** ավելացնել և հեռացնել
- **Բ մաս:** կա՞ ցուցակում
- **Գ մաս:** դասավորել և կտրել

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>class_grades = [9, 6, 10]</code> — մեկ անուն, շատ արժեք։<br/>
<code>len()</code> — քանիսն են։ <code>[0]</code> — առաջինը։ <code>[-1]</code> — վերջինը։
</p>
</div>

#%% code
student_names = ["Ani", "Davit", "Nare", "Aram", "Mariam"]

print(student_names)

#%% md
## Ա մաս: Ավելացնել և հեռացնել

Նոր աշակերտ եկավ դասարան։

#%% code
student_names.append("Tigran")

print(student_names)

#%% md
`.append(...)` — ավելացնում է **վերջում**։

Ուշադրություն կետին. `student_names.append(...)` կարդացվում է որպես
«`student_names`-ին ասա՝ ավելացրու»։ Այս ձևը՝ անուն, կետ, հրահանգ — շատ կհանդիպի։

Եվ ուշադրություն ևս մեկ բանի. բջիջը ոչինչ չտպեց, բայց **ցուցակը փոխվեց**։

#%% code
student_names.remove("Aram")

print(student_names)

#%% md
`.remove(...)` — հեռացնում է **արժեքով**, ոչ թե տեղով։ Գրում ես, թե ում ես հեռացնում,
ոչ թե որերորդին։

#%% md
## Բ մաս: Կա՞ ցուցակում

#%% code
print("Ani" in student_names)
print("Aram" in student_names)

#%% md
`in` — տալիս է `True` կամ `False`։ Իսկ դա նշանակում է, որ այն կարող է պայման դառնալ՝
վաղվանից։

Սա շատ օգտակար է `remove`-ից առաջ։ Եթե փորձես հեռացնել մեկին, ով ցուցակում չկա,
ծրագիրը կկանգնի սխալով։

#%% code
print("Vahe" in student_names)

#%% md
## Գ մաս: Դասավորել և կտրել

#%% code
student_names.sort()

print(student_names)

#%% md
`.sort()` — դասավորում է **տեղում**։ Ցուցակը ինքն է փոխվում, նոր ցուցակ չի ստեղծվում։

Թվերի համար՝ նույնը, փոքրից մեծ։

#%% code
class_grades = [9, 6, 10, 3, 8]
class_grades.sort()

print(class_grades)

#%% md
Իսկ եթե պետք է մեծից փոքր՝

#%% code
class_grades.sort(reverse=True)

print(class_grades)

#%% md
**Կտրել** — վերցնել ցուցակի մի մասը։

#%% code
student_names = ["Ani", "Davit", "Nare", "Aram", "Mariam"]

print(student_names[0:3])

#%% md
`[0:3]` նշանակում է «սկսած 0-ից, **մինչև** 3-ը, առանց 3-ի»։

Սա նույն տրամաբանությունն է, ինչ `range`-ինը, որ կտեսնենք 11-րդ օրը. **վերջին թիվը
ներառված չէ**։

#%% code
print(student_names[0:2])     # the first two
print(student_names[2:5])     # from the third to the fifth
print(student_names[-2:])     # the last two

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">📌 Մեկ բան, որ դեռ երկար է</h3>
<p style="color:#f71; margin-bottom:0;">
Մատյանը հիմա հարմար է՝ ավելացնում ենք, հեռացնում, դասավորում։<br/><br/>
Բայց բոլորին <b>տպելու</b> համար դեռ ամեն աշակերտի համար առանձին տող է պետք՝
<code>print(student_names[0])</code>, <code>[1]</code>, <code>[2]</code> ...<br/><br/>
<b>10-րդ օրը դա կդառնա երկու տող՝ ցանկացած թվով աշակերտի համար։</b> Երկու դաս հետո։
</p>
</div>

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Պարտադիր առաջադրանքներ</h3>
<p style="color:#900; margin-bottom:0;">
<b>1.</b> Վերցրո՛ւ քո դասարանի ցուցակը 6-րդ օրվանից։ Ավելացրո՛ւ մեկ նոր աշակերտ։<br/><br/>
<b>2.</b> Հեռացրո՛ւ մեկին։ <b>Նախ ստուգի՛ր <code>in</code>-ով, որ նա ցուցակում է։</b><br/><br/>
<b>3.</b> Դասավորի՛ր անունները այբբենական կարգով և տպի՛ր։<br/><br/>
<b>4.</b> Տպի՛ր միայն առաջին երեք աշակերտին՝ կտրելով։
</p>
</div>

#%% code
# Exercise 1 and 2 - add and remove

student_names = ["Ani", "Davit", "Nare"]
student_names.append("Tigran")

print(student_names)

#%% code
# Exercise 3 - sort

student_names.sort()

print(student_names)

#%% code
# Exercise 4 - the first three, by slicing

print(student_names[0:3])

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">🚀 Լրացուցիչ առաջադրանքներ</h3>
<p style="color:#f71; margin-bottom:0;">
<b>5.</b> Դասավորի՛ր միավորները մեծից փոքր և տպի՛ր ամենաբարձր երեքը։<br/><br/>
<b>6.</b> Ավելացրո՛ւ երեք աշակերտ միանգամից՝ երեք <code>.append()</code>-ով։
Հետո տպի՛ր, թե քանիսն են դարձել։<br/><br/>
<b>7.</b> Ի՞նչ է լինում, եթե <code>.remove()</code> անես աշակերտի, ով ցուցակում չկա։
Փորձի՛ր և կարդա՛ սխալը։ Ինչպե՞ս խուսափել։<br/><br/>
<b>8.</b> Ի՞նչ է լինում, եթե երկու աշակերտ ունեն նույն անունը և
<code>.remove()</code> անես։ Քանի՞սն է հեռանում։<br/><br/>
<b>9.</b> Փորձի՛ր <code>student_names[1:4]</code>։ Քանի՞ անուն ստացար։ Ինչո՞ւ։
</p>
</div>

#%% code
# Extra 5-9 - your space

class_grades = [9, 6, 10, 3, 8]
class_grades.sort(reverse=True)

print(class_grades[0:3])

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🧗 Մարտահրավեր</h3>
<p style="color:#06c; margin-bottom:0;">
<b>10.</b> Դասարանը բաժանվում է երկու խմբի։ Վերցրո՛ւ դասավորված ցուցակի առաջին կեսը
մեկ ցուցակի մեջ, երկրորդ կեսը՝ մյուսի։<br/><br/>
Հուշում՝ կեսը գտնելու համար պետք է <code>len(...)</code> և <code>//</code> նշանը
(ամբողջ բաժանում, որ տեսանք 3-րդ օրվա մարտահրավերում)։
</p>
</div>

#%% code
# Challenge 10 - split the class into two groups

student_names = ["Ani", "Davit", "Nare", "Aram", "Mariam", "Tigran"]
half = len(student_names) // 2

print(student_names[0:half])
print(student_names[half:])

#%% md
## Ինչի հասանք

- `.append(...)` — ավելացնում է վերջում։ `.remove(...)` — հեռացնում է արժեքով։
- `in` — կա՞ ցուցակում։ Տալիս է `True` կամ `False`։
- `.sort()` — դասավորում է տեղում։ `reverse=True` — հակառակ կարգով։
- `[0:3]` — կտրում է մի մասը։ **Վերջին թիվը ներառված չէ։**

## Հաջորդ անգամ

Մատյանը պատրաստ է։ Հաջորդ երկու դասին կսովորենք, թե ինչպես ծրագիրը կարող է **որոշում
ընդունել** — «անցա՞վ, թե՞ չանցավ»։ Իսկ 10-րդ օրը այդ որոշումը կկիրառենք ամբողջ
դասարանի վրա՝ չորս տողով։

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Դասավորի՛ր քո դասարանի միավորները մեծից փոքր և տպի՛ր ամենաբարձր երեքը։
