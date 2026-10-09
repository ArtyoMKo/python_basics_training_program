#%% md
# Թեմա 14 — Հաշվետվություններ մատյանից

### Python զրոյից · Թեմա 14-ը 24-ից

8-րդ թեմայում մատյանը դարձրեցինք բառարան, բայց այդ ժամանակ ցիկլեր դեռ չգիտեինք։
Հիմա գիտենք։

Այսօր միացնում ենք երկուսը և տպում **ամբողջ մատյանը** — և տեսնում ենք, որ 11-րդ և
13-րդ թեմայի ամեն ցիկլ դառնում է ավելի կարճ։

## ԱՅՍՕՐ:

- **Ա մաս:** ցիկլ բառարանի վրայով
- **Բ մաս:** ամեն ինչ նորից, բայց ավելի կարճ
- **Գ մաս:** սյունակները հավասարեցնել

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<b>8-րդ թեմայից՝</b> <code>class_grades = {"Ani": 9}</code> — բանալի → արժեք։<br/>
<b>11-րդ թեմայից՝</b> <code>for grade in class_grades:</code> — ցիկլ։<br/><br/>
Այսօր՝ երկուսը միասին։
</p>
</div>

#%% code
PASS_MARK = 4

class_grades = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3,
                "Mariam": 8, "Tigran": 5, "Lilit": 8, "Gor": 4,
                "Anahit": 9, "Hayk": 2, "Sona": 8, "Vahe": 6}

print(len(class_grades), "students")

#%% md
## Ա մաս: Ցիկլ բառարանի վրայով

Բառարանի ամեն տարրը **երկու** բան է՝ անուն և միավոր։ Ուստի ցիկլում երկու անուն ենք գրում։

#%% code
for student_name, grade in class_grades.items():
    print(f"{student_name}: {grade}")

#%% md
Կարդանք.

- `.items()` — «տուր ինձ զույգերը»
- `student_name, grade` — **երկու անուն, ստորակետով**։ Առաջինը ստանում է բանալին,
  երկրորդը՝ արժեքը
- մնացածը՝ սովորական `for`, ինչպես 11-րդ թեմայում

Անունները մերն են։ Կարող էինք գրել `a, b`, բայց այդ դեպքում ոչինչ չէր կարդացվի։

#%% md
## Բ մաս: Ամեն ինչ նորից, բայց ավելի կարճ

Հիմա 10-րդ և 13-րդ թեմայի բոլոր առաջադրանքները՝ բառարանով։

**Ամբողջ մատյանը.**

#%% code
for student_name, grade in class_grades.items():
    if grade >= PASS_MARK:
        print(f"{student_name}: passed")
    else:
        print(f"{student_name}: failed")

#%% md
Համեմատի՛ր 11-րդ թեմայի տարբերակի հետ.

```python
for position in range(len(student_names)):
    if class_grades[position] >= PASS_MARK:
        print(f"{student_names[position]}: passed")
```

Նույն արդյունքը՝ առանց `position`-ի, առանց `range`-ի, առանց `len`-ի, և առանց
այն վտանգի, որ երկու ցուցակը իրարից անջատվեն։

**Չանցածները.**

#%% code
failing_students = []

for student_name, grade in class_grades.items():
    if grade < PASS_MARK:
        failing_students.append(student_name)

print("Did not pass:", failing_students)

#%% md
**Միջինը** — ուղիղ 12-րդ թեմայի ձևով։

#%% code
total = 0

for student_name, grade in class_grades.items():
    total = total + grade

print(f"Class average: {total / len(class_grades):.1f}")

#%% md
**Ամենաբարձրը** — 13-րդ թեմայի ձևով, բայց հիմա անունն ու միավորը միասին են գալիս։

#%% code
best_name = ""
best_grade = -1

for student_name, grade in class_grades.items():
    if grade > best_grade:
        best_grade = grade
        best_name = student_name

print(f"highest: {best_name} - {best_grade}")

#%% md
Երբեմն միայն արժեքներն են պետք, առանց անունների։ Դրա համար կա `.values()`։

#%% code
print(list(class_grades.values()))
print(list(class_grades.keys()))

#%% md
## Գ մաս: Սյունակները հավասարեցնել

Մատյանը պետք է կարդալի լինի։ Մինչ այժմ անունները տարբեր երկարության են և սյունակները
չեն համընկնում։

#%% code
for student_name, grade in class_grades.items():
    print(f"{student_name}: {grade}")

#%% md
f-տողի ներսում կարելի է ասել, թե որքան լայն լինի սյունակը։

#%% code
for student_name, grade in class_grades.items():
    print(f"{student_name:<10} {grade:>3}")

#%% md
- `:<10` — «գրի՛ր ձախից և լրացրո՛ւ բացատներով մինչև 10 նիշ»
- `:>3` — «գրի՛ր աջից, 3 նիշ լայնությամբ»

Սա միակ ձևավորման հնարքն է, որ պետք կգա, և այն կա հուշաթերթում։

Հիմա ամբողջական մատյան.

#%% code
print("=== REGISTER ===")
print()

for student_name, grade in class_grades.items():
    if grade >= PASS_MARK:
        result = "passed"
    else:
        result = "failed"
    print(f"{student_name:<10} {grade:>3}   {result}")

print()
print(f"{len(class_grades)} students")
print(f"Class average: {total / len(class_grades):.1f}")

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Պարտադիր առաջադրանքներ</h3>
<p style="color:#900; margin-bottom:0;">
Այս բոլորը՝ <b>քո դասարանի բառարանով</b>։<br/><br/>
<b>1.</b> Տպի՛ր բոլորին <code>.items()</code> ցիկլով։<br/><br/>
<b>2.</b> Տպի՛ր ամեն աշակերտի դիմաց <code>passed</code>/<code>failed</code>։<br/><br/>
<b>3.</b> Հաշվի՛ր դասարանի միջինը և չանցածների թիվը։<br/><br/>
<b>4.</b> Տպի՛ր ամբողջական մատյան՝ հավասարեցված սյունակներով և ամփոփիչ տողերով։
</p>
</div>

#%% code
# Exercise 1 and 2 - the whole register

class_grades = {"Ani": 9, "Davit": 6, "Nare": 10}

for student_name, grade in class_grades.items():
    print(f"{student_name}: {grade}")

#%% code
# Exercise 4 - a full register with aligned columns

for student_name, grade in class_grades.items():
    print(f"{student_name:<10} {grade:>3}")

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">🚀 Լրացուցիչ առաջադրանքներ</h3>
<p style="color:#f71; margin-bottom:0;">
<b>5.</b> Տպի՛ր միայն անցածներին։<br/><br/>
<b>6.</b> Գտի՛ր ամենացածր միավորը և ում է այն պատկանում։<br/><br/>
<b>7.</b> Հաշվի՛ր, թե քանի աշակերտի միավոր է դասարանի միջինից բարձր։<br/><br/>
<b>8.</b> Տպի՛ր մատյանը՝ ամեն տողի սկզբում համարով (<code>1.</code>, <code>2.</code> ...)։
Հուշում՝ հաշվիչ փոփոխական ցիկլից առաջ։<br/><br/>
<b>9.</b> Օգտագործի՛ր 10-րդ թեմայի չորս մակարդակի շղթան ամեն աշակերտի համար։<br/><br/>
<b>10.</b> Տպի՛ր միայն այն աշակերտներին, որոնց անունը սկսվում է «A» տառով։
Հուշում՝ <code>student_name[0] == "A"</code>։
</p>
</div>

#%% code
# Extra 5-10 - your space

for student_name, grade in class_grades.items():
    if grade >= PASS_MARK:
        print(student_name)

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🧗 Մարտահրավեր</h3>
<p style="color:#06c; margin-bottom:0;">
<b>11.</b> Տպի՛ր մատյանը՝ <b>միավորով դասավորված</b>՝ բարձրից ցածր։<br/><br/>
Հուշում՝ դեռ չգիտենք, թե ինչպես դասավորել բառարանը։ Բայց գիտենք <code>range(10, 0, -1)</code>։
Ամեն միավորի համար անցի՛ր բառարանով և տպի՛ր նրանց, ում միավորը հենց այդքան է։<br/><br/>
<b>12.</b> Կազմի՛ր ամփոփիչ աղյուսակ՝ քանի աշակերտ ունի ամեն միավոր, 10-ից 1։
</p>
</div>

#%% code
# Challenge 11 - the register sorted by grade, high to low

for mark in range(10, 0, -1):
    for student_name, grade in class_grades.items():
        if grade == mark:
            print(f"{student_name:<10} {grade:>3}")

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

- `for name, grade in class_grades.items():` — ցիկլ բառարանի վրայով, **երկու անուն**։
- Ինդեքսն ու `range`-ը այլևս պետք չեն։
- `.values()` և `.keys()` — միայն արժեքները կամ միայն անունները։
- `{name:<10}` — հավասարեցնում է սյունակները։

## Ի՞նչ է գալիս հետո

Իրական մատյանում աշակերտը մեկ միավոր չունի — նա ունի մի քանիսը։ Ընդմիջումից հետո
կսովորենք, թե ինչպես պահել դրանք։

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Տպի՛ր քո դասարանի ամբողջական մատյանը հավասարեցված սյունակներով։
