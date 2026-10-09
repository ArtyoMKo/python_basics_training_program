#%% md
# Թեմա 17 — Միջինը՝ ամեն քարտի վրա

### Python զրոյից · Թեմա 17-ը 24-ից

Հաշվետվության քարտը պատրաստ է։ Բայց միջինը պետք է **չորս տարբեր տեղում**՝ քարտի վրա,
ամփոփիչ տողում, անցողիկության ստուգման մեջ, և դասարանի ընդհանուր հաշվարկում։

Այսօր սովորում ենք, թե ինչպես այդ հաշվարկը գրել **մեկ անգամ**։

## ԱՅՍՕՐ:

- **Ա մաս:** չորս տեղում՝ այն ձևով, որ արդեն գիտենք
- **Բ մաս:** կոդին անուն տալ
- **Գ մաս:** մեկ սխալ, մեկ ուղղում

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
Բառարան՝ ցուցակներով։ Ցիկլ ցիկլի ներսում՝ ամեն աշակերտի միջինը։
</p>
</div>

#%% code
PASS_MARK = 4

class_grades = {
    "Ani": [9, 10, 8],
    "Davit": [6, 5, 7],
    "Nare": [10, 10, 9],
    "Aram": [3, 4, 2],
}

print(len(class_grades), "students")

#%% md
## Ա մաս: Չորս տեղում՝ այն ձևով, որ արդեն գիտենք

<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Այս ձևն աշխատում է, բայց կրկնվում է։</b> Դասի երկրորդ կեսին կսովորենք, թե
ինչպես այս վեց տողը գրել <b>մեկ անգամ</b> և օգտագործել ամենուր։
</p>
</div>

**Տեղ 1 — հաշվետվության քարտը.**

#%% code
for student_name, grades in class_grades.items():
    total = 0
    for grade in grades:
        total = total + grade
    student_average = total / len(grades)

    print(f"{student_name:<10} average {student_average:.1f}")

#%% md
**Տեղ 2 — ո՞վ չի անցել.**

#%% code
failing_students = []

for student_name, grades in class_grades.items():
    total = 0
    for grade in grades:
        total = total + grade
    student_average = total / len(grades)

    if student_average < PASS_MARK:
        failing_students.append(student_name)

print("Did not pass:", failing_students)

#%% md
**Տեղ 3 — ամենաբարձր միջինը.**

#%% code
best_name = ""
best_average = -1

for student_name, grades in class_grades.items():
    total = 0
    for grade in grades:
        total = total + grade
    student_average = total / len(grades)

    if student_average > best_average:
        best_average = student_average
        best_name = student_name

print(f"best: {best_name} - {best_average:.1f}")

#%% md
**Տեղ 4 — դասարանի ընդհանուր միջինը.**

#%% code
all_averages = []

for student_name, grades in class_grades.items():
    total = 0
    for grade in grades:
        total = total + grade
    student_average = total / len(grades)

    all_averages.append(student_average)

total = 0
for one_average in all_averages:
    total = total + one_average

print(f"class average: {total / len(all_averages):.1f}")

#%% md
Չորս բջիջ, և չորսում էլ **ուղիղ նույն չորս տողը**.

```python
total = 0
for grade in grades:
    total = total + grade
student_average = total / len(grades)
```

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Առաջադրանք 1 — պարտադիր</h3>
<p style="color:#900; margin-bottom:0;">
Տնօրինությունը որոշեց, որ միջինը պետք է գրվի <b>երկու նիշով</b>, ոչ թե մեկով։<br/><br/>
Փոխի՛ր <code>:.1f</code>-ը <code>:.2f</code>-ի <b>բոլոր չորս բջիջում</b> և գործարկի՛ր
դրանք նորից։<br/><br/>
Ուշադրություն դարձրու, թե քանի տեղում պետք եղավ փոխել — և արդյոք վստա՞հ ես, որ
ոչ մեկը բաց չթողեցիր։
</p>
</div>

#%% md
## Բ մաս: Կոդին անուն տալ

5-րդ թեման **արժեքին** անուն տվեցինք՝ `PASS_MARK = 4`։

Հիմա **կոդին** ենք անուն տալիս։ Դա կոչվում է **ֆունկցիա**։

#%% code
def say_hello():
    print("Hello, teacher")

#%% md
Այս բջիջը ոչինչ չտպեց։ **Եվ դա ճիշտ է։**

Մենք ոչինչ չենք արել — մենք միայն ասացինք. «այս տողը այսուհետ կոչվում է `say_hello`»։

Կոդը աշխատեցնելու համար պետք է այն **կանչել**։

#%% code
say_hello()

#%% md
> **Սահմանելը և կանչելը տարբեր բաներ են։**
>
> `def say_hello():` — սահմանում է։ Ոչինչ չի կատարվում։
> `say_hello()` — կանչում է։ Հիմա կատարվում է։
>
> Եթե ֆունկցիան «չի աշխատում», առաջին հարցը՝ **կանչե՞լ ես այն**։

#%% md
Ֆունկցիան օգտակար է դառնում, երբ ամեն կանչի ժամանակ **ուրիշ արժեքով** է աշխատում։
Արժեքը գրում ենք փակագծերի մեջ։

#%% code
def greet_student(student_name):
    print(f"Hello, {student_name}")

greet_student("Ani")
greet_student("Davit")

#%% md
`student_name`-ը **պարամետր** է. անուն, որը գոյություն ունի միայն ֆունկցիայի ներսում։
Ամեն կանչի ժամանակ այն ստանում է այն արժեքը, որ գրել ես փակագծերում։

Դա նույն գաղափարն է, ինչ ցիկլի փոփոխականը 11-րդ թեման։

#%% md
### Հիմա՝ մեր չորս տողը

Բայց մեզ պետք է ոչ թե տպել միջինը, այլ **ստանալ այն**, որպեսզի կարողանանք
համեմատել, ավելացնել ցուցակին, և այլն։

Դրա համար կա `return`։

#%% code
def average_of(grades):
    total = 0
    for grade in grades:
        total = total + grade
    return round(total / len(grades), 1)

#%% md
`return` — «վերադարձրու այս արժեքը նրան, ով կանչեց»։

Հիմա կանչենք։

#%% code
print(average_of([9, 10, 8]))
print(average_of([6, 5, 7]))

#%% md
Եվ քանի որ այն **արժեք է վերադարձնում**, կարող ենք այն օգտագործել ամեն տեղ, որտեղ
թիվ է պետք։

#%% code
ani_average = average_of(class_grades["Ani"])

print(ani_average)
print(ani_average > 8)
print(ani_average * 2)

#%% md
## Գ մաս: Չորս տեղը՝ նորից

Ահա նույն չորս բջիջը, բայց հիմա ֆունկցիայով։

#%% code
# Place 1 - report cards
for student_name, grades in class_grades.items():
    print(f"{student_name:<10} average {average_of(grades):.1f}")

#%% code
# Place 2 - who did not pass
failing_students = []

for student_name, grades in class_grades.items():
    if average_of(grades) < PASS_MARK:
        failing_students.append(student_name)

print("Did not pass:", failing_students)

#%% code
# Place 3 - the best average
best_name = ""
best_average = -1

for student_name, grades in class_grades.items():
    if average_of(grades) > best_average:
        best_average = average_of(grades)
        best_name = student_name

print(f"best: {best_name} - {best_average}")

#%% code
# Place 4 - the class average
all_averages = []

for student_name, grades in class_grades.items():
    all_averages.append(average_of(grades))

print(f"class average: {average_of(all_averages)}")

#%% md
Ուշադրություն վերջին տողին. **`average_of`-ը կանչեցինք միջինների ցուցակի վրա**։
Ֆունկցիան չգիտի և չի հետաքրքրվում, թե որտեղից են եկել թվերը։

#%% md
### Մեկ սխալ, մեկ ուղղում

**Ահա այսօրվա իրական դասը։**

Տնօրինությունը նորից փոխեց միտքը՝ միջինը պետք է երկու նիշով։

Առաջին կեսում դա չորս խմբագրում էր։ Հիմա՝ **մեկ**։ Փոխի՛ր ներքևի բջիջում
`1`-ը `2`-ի, գործարկի՛ր այն, հետո գործարկի՛ր վերևի չորս բջիջը՝ **առանց դրանք դիպչելու**։

#%% code
def average_of(grades):
    total = 0
    for grade in grades:
        total = total + grade
    return round(total / len(grades), 2)

#%% md
Բոլոր չորս տեղում փոխվեց։ Որովհետև **տեղը մեկն էր**։

> **Կանոն, զույգ 9-րդ թեմայի կանոնին.**
> 9-րդ թեմա՝ եթե **թիվը** կարևոր է, տո՛ւր նրան անուն (`PASS_MARK`)։
> Այսօր՝ եթե **կոդը** կրկնվում է, տո՛ւր նրան անուն։

#%% md
<div style="border-left: 6px solid #181; background: #f2fff5; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#181; margin-top:0;">🏫 Քո դասարանում</h3>
<p style="color:#181; margin-bottom:0;">
Ֆունկցիան այն է, ինչ անում ես, երբ դասի պլան ես գրում մեկ անգամ և օգտագործում
չորս դասարանում։ Պլանը մեկն է։ Դասարանը՝ պարամետրը։ Երբ պլանում սխալ ես գտնում,
ուղղում ես <b>պլանը</b>, ոչ թե չորս անգամ նույն բանը։
</p>
</div>

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Պարտադիր առաջադրանքներ</h3>
<p style="color:#900; margin-bottom:0;">
<b>2.</b> Գրի՛ր <code>average_of(grades)</code> ֆունկցիան և կանչի՛ր քո դասարանի
երեք աշակերտի համար։<br/><br/>
<b>3.</b> Գրի՛ր <code>greet_student(student_name)</code> և կանչի՛ր ցիկլի ներսում։<br/><br/>
<b>4.</b> Տպի՛ր ամբողջական հաշվետվության քարտերը՝ <code>average_of</code>-ով։<br/><br/>
<b>5.</b> Փոխի՛ր <code>average_of</code>-ի կլորացումը <b>մեկ տեղում</b> և համոզվի՛ր,
որ բոլոր տողերը փոխվեցին։
</p>
</div>

#%% code
# Exercise 2 - your own average_of

def average_of(grades):
    total = 0
    for grade in grades:
        total = total + grade
    return round(total / len(grades), 1)


print(average_of([9, 10, 8]))

#%% code
# Exercise 4 - full report cards using the function

for student_name, grades in class_grades.items():
    print(f"{student_name:<10} {average_of(grades)}")

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">🚀 Լրացուցիչ առաջադրանքներ</h3>
<p style="color:#f71; margin-bottom:0;">
<b>6.</b> Գրի՛ր <code>highest_of(grades)</code>, որը վերադարձնում է ամենաբարձր միավորը։<br/><br/>
<b>7.</b> Գրի՛ր <code>lowest_of(grades)</code>։ Ձևը նույնն է։<br/><br/>
<b>8.</b> Գրի՛ր <code>print_report_card(student_name, grades)</code>, որը տպում է
մեկ ամբողջական տող։ Կանչի՛ր ցիկլի ներսում։<br/><br/>
<b>9.</b> Գրի՛ր <code>how_many_passed(class_grades)</code>, որը վերադարձնում է թիվը։<br/><br/>
<b>10.</b> Ի՞նչ է լինում, եթե <code>average_of([])</code> կանչես դատարկ ցուցակով։
Կարդա՛ սխալը։ Ինչպե՞ս պաշտպանվել։
</p>
</div>

#%% code
# Extra 6-10 - your space

def highest_of(grades):
    highest = grades[0]
    for grade in grades:
        if grade > highest:
            highest = grade
    return highest


print(highest_of([9, 10, 8]))

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🧗 Մարտահրավեր</h3>
<p style="color:#06c; margin-bottom:0;">
<b>11.</b> Գրի՛ր <code>class_report(class_grades)</code>, որը տպում է ամբողջ
մատյանը՝ վերնագրով, բոլոր քարտերով և ամփոփիչ տողերով։ Այն պետք է կանչի
<code>average_of</code>-ը ներսում։<br/><br/>
Հետո կանչի՛ր այն <b>մեկ տողով</b>։ Այդ մեկ տողը 21-րդ թեման կդառնա քո ծրագրի մենյուի
առաջին հրամանը։
</p>
</div>

#%% code
# Challenge 11 - the whole register as one function

def class_report(class_grades):
    print("=== REGISTER ===")
    for student_name, grades in class_grades.items():
        print(f"{student_name:<10} {average_of(grades)}")
    print(f"{len(class_grades)} students")


class_report(class_grades)

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

- `def name(parameter):` — կոդին անուն է տալիս։ **Ոչինչ չի կատարվում, քանի դեռ չես կանչել։**
- `return` — վերադարձնում է արժեքը, որպեսզի կարողանաս օգտագործել այն։
- Պարամետրերը թույլ են տալիս ամեն կանչին ուրիշ արժեք տալ։
- **Չորս տեղում կրկնվող վեց տողը՝ մեկ ֆունկցիա։ Մեկ ուղղում՝ չորս տեղում։**

## Ի՞նչ է գալիս հետո

Այսօր տեսանք `return`-ը գործի մեջ։ Հաջորդ դասին նայենք նրան ուշադիր՝ ի՞նչ է
նշանակում «վերադարձնել», ինչո՞վ է տարբերվում տպելուց, և կկառուցենք չորս ֆունկցիայից
բաղկացած գործիքակազմ, որը 20-րդ թեման կդառնա քո ծրագրի սիրտը։

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Գրի՛ր ֆունկցիա, որը տպում է մատյանի վերնագիրը՝ դասարանի անունը որպես պարամետր։
