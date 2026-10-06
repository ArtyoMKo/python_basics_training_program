#%% md
# Օր 13 — Ցիկլեր, որոնք որոշում են

### Python զրոյից · Օր 13-ը 24-ից

Այսօր պատասխանում ենք այն հարցերին, որ ամեն ուսուցիչ տալիս է եռամսյակի վերջում.
ո՞վ չի անցել, քանի՞սն են անցել, ո՞վ է ամենալավը։

## ԱՅՍՕՐ:

- **Ա մաս:** հաշվել միայն որոշներին
- **Բ մաս:** հավաքել նոր ցուցակ
- **Գ մաս:** գտնել ամենաբարձրը

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
Կուտակիչի ձևը՝ <code>total = 0</code> մինչ ցիկլը, <code>total = total + ...</code>
ներսում։<br/>
Եվ 11-րդ օրվանից՝ <code>if</code> ցիկլի ներսում։
</p>
</div>

#%% code
student_names = ["Ani", "Davit", "Nare", "Aram", "Mariam", "Tigran",
                 "Lilit", "Gor", "Anahit", "Hayk", "Sona", "Vahe"]
class_grades = [9, 6, 10, 3, 8, 5, 8, 4, 9, 2, 8, 6]

PASS_MARK = 4

print(len(student_names), "students")

#%% md
## Ա մաս: Հաշվել միայն որոշներին

Երեկ հաշվեցինք բոլորին։ Հիմա հաշվում ենք **միայն նրանց, ովքեր բավարարում են պայմանին**։

Ձևը նույնն է — պարզապես ավելացնում ենք `if`։

#%% code
how_many_passed = 0

for grade in class_grades:
    if grade >= PASS_MARK:
        how_many_passed = how_many_passed + 1

print(f"{how_many_passed} students passed out of {len(class_grades)}")

#%% md
Կարող ենք երկուսն էլ հաշվել միանգամից՝ երկու հաշվիչով։

#%% code
how_many_passed = 0
how_many_failed = 0

for grade in class_grades:
    if grade >= PASS_MARK:
        how_many_passed = how_many_passed + 1
    else:
        how_many_failed = how_many_failed + 1

print(f"passed: {how_many_passed}")
print(f"failed: {how_many_failed}")

#%% md
## Բ մաս: Հավաքել նոր ցուցակ

Թիվը լավ է, բայց մեզ **անունները** պետք են։

Ձևը նույնն է, բայց `0`-ի փոխարեն սկսում ենք **դատարկ ցուցակից**, և գումարելու փոխարեն
օգտագործում ենք `.append()`-ը՝ 7-րդ օրվանից։

#%% code
failing_students = []

for position in range(len(class_grades)):
    if class_grades[position] < PASS_MARK:
        failing_students.append(student_names[position])

print(failing_students)

#%% md
Երեք մասից բաղկացած նույն ձևը.

1. **Մինչ ցիկլը՝** `failing_students = []` — դատարկ ցուցակ
2. **Ցիկլի ներսում՝** `if` և `.append(...)`
3. **Ցիկլից հետո՝** նայում ենք արդյունքին

Իսկ նոր ցուցակը սովորական ցուցակ է — կարող ենք նրա վրայով նոր ցիկլ գրել։

#%% code
print("Did not pass:")

for student_name in failing_students:
    print(" -", student_name)

print(f"Total: {len(failing_students)} students")

#%% md
## Գ մաս: Գտնել ամենաբարձրը

Նույն գաղափարը, ուրիշ հարցի համար։ Սկսում ենք առաջին արժեքից և ամեն պտույտում
համեմատում ենք։

#%% code
highest_grade = class_grades[0]

for grade in class_grades:
    if grade > highest_grade:
        highest_grade = grade

print("highest grade:", highest_grade)

#%% md
Կարդանք. «եթե այս միավորը մեծ է, քան մինչ այժմ տեսած ամենաբարձրը — ուրեմն հիմա
**սա** է ամենաբարձրը»։

Իսկ ո՞ւմ միավորն է դա։ Հիշենք ինդեքսը։

#%% code
best_position = 0

for position in range(len(class_grades)):
    if class_grades[position] > class_grades[best_position]:
        best_position = position

print(f"highest: {student_names[best_position]} - {class_grades[best_position]} points")

#%% md
> **Ի դեպ.** Python-ում կա նաև պատրաստի `max(class_grades)`, որը նույն բանն է անում։
> Բայց ցիկլով գրելը սովորեցնում է **ձևը**, որը կաշխատի ցանկացած հարցի համար՝
> ամենացածրը, ամենաերկար անունը, ամենամոտը միջինին։

#%% md
<div style="border-left: 6px solid #181; background: #f2fff5; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#181; margin-top:0;">🏫 Քո դասարանում</h3>
<p style="color:#181; margin-bottom:0;">
Այս երեք ձևը — <b>հաշվել պայմանով</b>, <b>հավաքել նոր ցուցակ</b>, <b>գտնել
ամենաբարձրը</b> — ծածկում են այն հարցերի մեծ մասը, որ ուսուցիչը տալիս է իր դասարանի
մասին։ Դասընթացի մնացած մասում նոր ձև գրեթե չի լինելու, միայն նույն երեքի կիրառում։
</p>
</div>

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Պարտադիր առաջադրանքներ</h3>
<p style="color:#900; margin-bottom:0;">
Այս բոլորը՝ <b>քո իրական դասարանի ցուցակներով</b>։<br/><br/>
<b>1.</b> Քանի՞ աշակերտ է անցել, քանի՞սը՝ ոչ։<br/><br/>
<b>2.</b> Հավաքի՛ր չանցածների անունները նոր ցուցակում և տպի՛ր դրանք։<br/><br/>
<b>3.</b> Գտի՛ր ամենաբարձր միավորը և ում է այն պատկանում։<br/><br/>
<b>4.</b> Տպի՛ր ամբողջ մատյանը՝ ամեն աշակերտի դիմաց արդյունքը, ամփոփիչ տողերով։
</p>
</div>

#%% code
# Exercise 1 - how many passed

how_many_passed = 0

for grade in class_grades:
    if grade >= PASS_MARK:
        how_many_passed = how_many_passed + 1

print(how_many_passed)

#%% code
# Exercise 2 - the names of those who did not pass

failing_students = []

for position in range(len(class_grades)):
    if class_grades[position] < PASS_MARK:
        failing_students.append(student_names[position])

print(failing_students)

#%% code
# Exercise 4 - the whole register with a summary

for position in range(len(student_names)):
    if class_grades[position] >= PASS_MARK:
        print(f"{student_names[position]}: passed")
    else:
        print(f"{student_names[position]}: failed")

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">🚀 Լրացուցիչ առաջադրանքներ</h3>
<p style="color:#f71; margin-bottom:0;">
<b>5.</b> Գտի՛ր ամենացածր միավորը։ Ձևը նույնն է՝ փոխի՛ր <code>&gt;</code>-ը
<code>&lt;</code>-ի։<br/><br/>
<b>6.</b> Հավաքի՛ր <b>անցածների</b> անունները նոր ցուցակում։<br/><br/>
<b>7.</b> Հաշվի՛ր անցածների միջինը և չանցածների միջինը առանձին։<br/><br/>
<b>8.</b> Գտի՛ր, թե քանի աշակերտի միավոր է դասարանի միջինից բարձր։<br/><br/>
<b>9.</b> Հավաքի՛ր նոր ցուցակ, որտեղ բոլոր միավորները մեկով ավելի են։<br/><br/>
<b>10.</b> Գտի՛ր ամենաերկար անունը ցուցակում։ (Հուշում՝ <code>len(student_name)</code>։)
</p>
</div>

#%% code
# Extra 5-10 - your space

lowest_grade = class_grades[0]

for grade in class_grades:
    if grade < lowest_grade:
        lowest_grade = grade

print(lowest_grade)

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🧗 Մարտահրավեր</h3>
<p style="color:#06c; margin-bottom:0;">
<b>11.</b> Գտի՛ր այն աշակերտին, ում միավորը <b>ամենամոտն է</b> դասարանի միջինին։<br/><br/>
Հուշում՝ «որքան հեռու է միջինից» = <code>grade - average</code>, բայց դա կարող է
բացասական լինել։ Փորձի՛ր <code>abs(...)</code>-ը, որը հանում է մինուսը։<br/><br/>
<b>12.</b> Կազմի՛ր երկու նոր ցուցակ միանգամից՝ անցածներ և չանցածներ, մեկ ցիկլով։
</p>
</div>

#%% code
# Challenge 11 - the student closest to the average

total = 0
for grade in class_grades:
    total = total + grade
average = total / len(class_grades)

closest_position = 0
for position in range(len(class_grades)):
    if abs(class_grades[position] - average) < abs(class_grades[closest_position] - average):
        closest_position = position

print(f"average {average:.1f}, closest: {student_names[closest_position]}")

#%% md
## Ինչի հասանք

- **Հաշվել պայմանով՝** `how_many = 0`, ցիկլ, `if`, `how_many = how_many + 1`։
- **Հավաքել նոր ցուցակ՝** `new_list = []`, ցիկլ, `if`, `.append(...)`։
- **Գտնել ամենաբարձրը՝** սկսիր առաջինից, համեմատիր, փոխարինիր։

## Հաջորդ անգամ

Բոլոր ցիկլերը, որ մինչ այժմ գրել ենք, գիտեին, թե քանի անգամ պետք է կրկնվեն —
այնքան, որքան ցուցակում տարր կա։ Հաջորդ դասին՝ ցիկլ, որը **չգիտի**, և կանգնում է
միայն այն ժամանակ, երբ դու ասես։

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Հաշվի՛ր, թե քո դասարանի աշակերտների քանի՞ տոկոսն է անցել։
