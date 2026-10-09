#%% md
# Թեմա 15 — Մի քանի միավոր մեկ աշակերտի համար

### Python զրոյից · Թեմա 15-ը 24-ից

Իրական մատյանում աշակերտը մեկ միավոր չունի։ Նա ունի մի քանիսը՝ եռամսյակի ընթացքում։

## ԱՅՍՕՐ:

- **Ա մաս:** բառարան, որի արժեքը ցուցակ է
- **Բ մաս:** նոր միավոր ավելացնել
- **Գ մաս:** ամեն աշակերտի միջինը

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>for name, grade in class_grades.items():</code> — ցիկլ բառարանի վրայով։<br/>
<code>{name:&lt;10}</code> — հավասարեցնում է սյունակները։
</p>
</div>

#%% md
## Ա մաս: Բառարան, որի արժեքը ցուցակ է

Մինչ այժմ բառարանի արժեքը թիվ էր։ Բայց այն կարող է լինել **ցուցակ**։

#%% code
class_grades = {
    "Ani": [9, 10, 8],
    "Davit": [6, 5, 7],
    "Nare": [10, 10, 9],
    "Aram": [3, 4, 2],
}

print(class_grades["Ani"])

#%% md
`class_grades["Ani"]` այժմ ցուցակ է։ Ուրեմն նրա հետ կարելի է անել այն ամենը, ինչ
ցուցակի հետ՝ 6-րդ և 7-րդ թեմայից։

#%% code
print(len(class_grades["Ani"]))
print(class_grades["Ani"][0])
print(class_grades["Ani"][-1])

#%% md
Երկու քառակուսի փակագիծ. առաջինը՝ բառարանից աշակերտին, երկրորդը՝ ցուցակից միավորը։

Կարդացվում է ձախից աջ. «վերցրու `class_grades`-ից `Ani`-ին, հետո վերցրու նրա
առաջին միավորը»։

#%% md
## Բ մաս: Նոր միավոր ավելացնել

#%% code
class_grades["Ani"].append(7)

print(class_grades["Ani"])

#%% md
`.append()` — ուղիղ 7-րդ թեմայի ձևով։ Ոչ մի նոր բան։

Նոր աշակերտ ավելացնելը՝ ցուցակով։

#%% code
class_grades["Tigran"] = [5, 6]

print(class_grades)

#%% md
## Գ մաս: Ամեն աշակերտի միջինը

Հիմա ամեն աշակերտի համար հաշվում ենք իր միջինը՝ 12-րդ թեմայի կուտակիչի ձևով։

#%% code
for student_name, grades in class_grades.items():
    total = 0
    for grade in grades:
        total = total + grade
    student_average = total / len(grades)

    print(f"{student_name:<10} {grades}  average {student_average:.1f}")

#%% md
Ցիկլ ցիկլի ներսում. արտաքինը՝ աշակերտների վրայով, ներքինը՝ մեկ աշակերտի
միավորների վրայով։

Ուշադրություն՝ `total = 0`-ն **արտաքին ցիկլի ներսում** է։ Ամեն աշակերտի համար
սկսում ենք զրոյից։ Եթե դուրս լիներ, բոլորի միավորները կգումարվեին իրար։

#%% md
Ավելացնենք նաև «անցավ/չանցավ»-ը՝ լրիվ հաշվետվության քարտ։

#%% code
PASS_MARK = 4

print("=== REPORT CARDS ===")
print()

for student_name, grades in class_grades.items():
    total = 0
    for grade in grades:
        total = total + grade
    student_average = total / len(grades)

    if student_average >= PASS_MARK:
        result = "passed"
    else:
        result = "failed"

    print(f"{student_name:<10} {str(grades):<16} average {student_average:.1f}   {result}")

print()
print(f"{len(class_grades)} students")

#%% md
> `str(grades)` — ցուցակը վերածում է տեքստի, որպեսզի `:<16`-ը կարողանա այն հավասարեցնել։
> Առանց դրա Python-ը չի կարող ցուցակը լայնացնել։

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Պարտադիր առաջադրանքներ</h3>
<p style="color:#900; margin-bottom:0;">
<b>1.</b> Գրի՛ր քո դասարանը բառարանով, որտեղ ամեն աշակերտ ունի <b>երեք միավոր</b>։<br/><br/>
<b>2.</b> Տպի՛ր բոլորին <code>.items()</code> ցիկլով։<br/><br/>
<b>3.</b> Ավելացրո՛ւ նոր միավոր երկու աշակերտի և տպի՛ր նորից։<br/><br/>
<b>4.</b> Հաշվի՛ր և տպի՛ր ամեն աշակերտի միջինը։<br/><br/>
<b>5.</b> Տպի՛ր ամբողջական հաշվետվության քարտերը՝ անուն, միավորներ, միջին, արդյունք։
</p>
</div>

#%% code
# Exercise 1 - your class, three grades each

class_grades = {
    "Ani": [9, 10, 8],
    "Davit": [6, 5, 7],
}

print(class_grades)

#%% code
# Exercise 4 - each student's average

for student_name, grades in class_grades.items():
    total = 0
    for grade in grades:
        total = total + grade
    print(f"{student_name}: {total / len(grades):.1f}")

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">🚀 Լրացուցիչ առաջադրանքներ</h3>
<p style="color:#f71; margin-bottom:0;">
<b>6.</b> Հաշվի՛ր, թե քանի աշակերտի միջինն է դասարանի միջինից բարձր։<br/><br/>
<b>7.</b> Գտի՛ր ամենաբարձր միջինը և ում է այն պատկանում։<br/><br/>
<b>8.</b> Տպի՛ր ամեն աշակերտի <b>ամենաբարձր</b> միավորը։<br/><br/>
<b>9.</b> Հաշվի՛ր, թե ընդհանուր քանի՞ միավոր է գրանցված ամբողջ դասարանում։<br/><br/>
<b>10.</b> Գտի՛ր այն աշակերտներին, ում բոլոր միավորները անցողիկ են։<br/><br/>
<b>11.</b> Ի՞նչ է լինում, եթե աշակերտի ցուցակը դատարկ է՝ <code>[]</code>։
Փորձի՛ր հաշվել միջինը։ Կարդա՛ սխալը։
</p>
</div>

#%% code
# Extra 6-11 - your space

for student_name, grades in class_grades.items():
    highest = grades[0]
    for grade in grades:
        if grade > highest:
            highest = grade
    print(f"{student_name}: best {highest}")

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🧗 Մարտահրավեր</h3>
<p style="color:#06c; margin-bottom:0;">
<b>12.</b> Գտի՛ր այն աշակերտին, ում միավորները ամենաշատն են բարելավվել՝
վերջին միավորը մինուս առաջին միավորը։<br/><br/>
<b>13.</b> Ուշադրություն դարձրու՝ միջին հաշվելու վեց տողը այսօր քանի՞ անգամ գրեցիր
այս տետրում։ Հաշվի՛ր։<br/><br/>
<b>17-րդ թեմայում այդ վեց տողը կգրենք մեկ անգամ և կօգտագործենք ամենուր։</b>
</p>
</div>

#%% code
# Challenge 12 - who improved the most

for student_name, grades in class_grades.items():
    improvement = grades[-1] - grades[0]
    print(f"{student_name}: {improvement:+d}")

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

- Բառարանի արժեքը կարող է լինել **ցուցակ**՝ մեկ աշակերտ, մի քանի միավոր։
- `class_grades["Ani"][0]` — երկու փակագիծ, ձախից աջ։
- `.append()` աշխատում է ուղիղ այնպես, ինչպես սովորական ցուցակում։
- Ցիկլ ցիկլի ներսում. `total = 0`-ն **արտաքին ցիկլի ներսում** է։

## Ի՞նչ է գալիս հետո

Այսօր միջին հաշվելու նույն վեց տողը գրեցինք մի քանի անգամ։ **Հաջորդ նիստում կսովորենք
այն գրել մեկ անգամ և կանչել ամենուր, որտեղ պետք է։**

Դա դասընթացի վերջին մեծ գաղափարն է։

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Հաշվի՛ր, թե քո դասարանում որ աշակերտն ունի ամենաբարձր միջինը։
