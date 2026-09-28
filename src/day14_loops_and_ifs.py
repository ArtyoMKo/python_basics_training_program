#%% md
# Օր 14 — Ցիկլեր, որոնք որոշում են

### Python զրոյից · Օր 14-ը 24-ից

Այսօր փակում ենք **9-րդ օրվա պարտքը**։ Այն քսանհինգ բլոկը այսօր դառնում է չորս տող,
և մենք դրանք կդնենք կողք կողքի։

## ԱՅՍՕՐ:

- **Ա մաս:** հաշվել միայն որոշներին
- **Բ մաս:** հավաքել նոր ցուցակ
- **Գ մաս:** գտնել ամենաբարձրը
- **Դ մաս:** 9-րդ օրվա պարտքը

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
Կուտակիչի ձևը՝ <code>total = 0</code> մինչ ցիկլը, <code>total = total + ...</code>
ներսում։<br/>
Եվ 12-րդ օրվանից՝ <code>if</code> ցիկլի ներսում։
</p>
</div>

#%% code
student_names = ["Անի", "Դավիթ", "Նարե", "Արամ", "Մարիամ", "Տիգրան",
                 "Լիլիթ", "Գոռ", "Անահիտ", "Հայկ", "Սոնա", "Վահե"]
class_grades = [9, 6, 10, 3, 8, 5, 8, 4, 9, 2, 8, 6]

PASS_MARK = 4

print(len(student_names), "աշակերտ")

#%% md
## Ա մաս: Հաշվել միայն որոշներին

Երեկ հաշվեցինք բոլորին։ Հիմա հաշվում ենք **միայն նրանց, ովքեր բավարարում են պայմանին**։

Ձևը նույնն է — պարզապես ավելացնում ենք `if`։

#%% code
how_many_passed = 0

for grade in class_grades:
    if grade >= PASS_MARK:
        how_many_passed = how_many_passed + 1

print(f"Անցել է {how_many_passed} աշակերտ {len(class_grades)}-ից")

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

print(f"Անցել է՝ {how_many_passed}")
print(f"Չի անցել՝ {how_many_failed}")

#%% md
## Բ մաս: Հավաքել նոր ցուցակ

Թիվը լավ է, բայց մեզ **անունները** պետք են։

Ձևը նույնն է, բայց `0`-ի փոխարեն սկսում ենք **դատարկ ցուցակից**, և գումարելու փոխարեն
օգտագործում ենք `.append()`-ը՝ 11-րդ օրվանից։

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
print("Չեն անցել՝")

for student_name in failing_students:
    print(" -", student_name)

print(f"Ընդամենը՝ {len(failing_students)} աշակերտ")

#%% md
## Գ մաս: Գտնել ամենաբարձրը

Նույն գաղափարը, ուրիշ հարցի համար։ Սկսում ենք առաջին արժեքից և ամեն պտույտում
համեմատում ենք։

#%% code
highest_grade = class_grades[0]

for grade in class_grades:
    if grade > highest_grade:
        highest_grade = grade

print("Ամենաբարձր գնահատականը՝", highest_grade)

#%% md
Կարդանք. «եթե այս գնահատականը մեծ է, քան մինչ այժմ տեսած ամենաբարձրը — ուրեմն հիմա
**սա** է ամենաբարձրը»։

Իսկ ո՞ւմ գնահատականն է դա։ Հիշենք ինդեքսը։

#%% code
best_position = 0

for position in range(len(class_grades)):
    if class_grades[position] > class_grades[best_position]:
        best_position = position

print(f"Ամենաբարձրը՝ {student_names[best_position]} — {class_grades[best_position]} միավոր")

#%% md
> **Ի դեպ.** Python-ում կա նաև պատրաստի `max(class_grades)`, որը նույն բանն է անում։
> Բայց ցիկլով գրելը սովորեցնում է **ձևը**, որը կաշխատի ցանկացած հարցի համար՝
> ամենացածրը, ամենաերկար անունը, ամենամոտը միջինին։

#%% md
## Դ մաս: 9-րդ օրվա պարտքը

Հիշո՞ւմ ես 9-րդ օրը։ Քսանհինգ բլոկ, ավելի քան հարյուր տող։ Ահա դրա սկիզբը.

#%% code
grade = 9
if grade >= 4:
    print("Անի: անցավ")
else:
    print("Անի: չանցավ")

grade = 6
if grade >= 4:
    print("Դավիթ: անցավ")
else:
    print("Դավիթ: չանցավ")

grade = 10
if grade >= 4:
    print("Նարե: անցավ")
else:
    print("Նարե: չանցավ")

#%% md
Երեք աշակերտ՝ տասնհինգ տող։ Քսանհինգ աշակերտի համար՝ **հարյուր քսանհինգ տող**։

Եվ ահա նույնը՝ **բոլոր տասներկուսի համար**։

#%% code
for position in range(len(student_names)):
    if class_grades[position] >= PASS_MARK:
        print(f"{student_names[position]}: անցավ")
    else:
        print(f"{student_names[position]}: չանցավ")

#%% md
**Չորս տող։**

Եվ հիմա փորձի՛ր այն, ինչ 9-րդ օրը անհնար էր.

- «անցավ»-ը փոխի՛ր «բավարար»-ի։ **Մեկ խմբագրում**, ոչ թե քսանհինգ։
- Ավելացրո՛ւ նոր աշակերտ երկու ցուցակին։ **Ցիկլում ոչինչ չես փոխում։**
- Փոխի՛ր `PASS_MARK`-ը։ **Մեկ խմբագրում** — դա արդեն 9-րդ օրը լուծեցինք։

| | 9-րդ օր | Այսօր |
|---|---|---|
| Տողերի թիվը 25 աշակերտի համար | ~125 | 4 |
| «անցավ»-ը փոխել | 25 խմբագրում | 1 |
| Նոր աշակերտ ավելացնել | 5 նոր տող | 0 |
| 300 աշակերտի համար | ~1500 տող | **4** |

#%% md
<div style="border-left: 6px solid #181; background: #f2fff5; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#181; margin-top:0;">🏫 Քո դասարանում</h3>
<p style="color:#181; margin-bottom:0;">
Այս չորս տողը այն է, ինչ անում է դպրոցի էլեկտրոնային մատյանը, երբ սեղմում ես
«չանցածների ցուցակ»։ Ոչ մի ավելի բարդ բան այնտեղ չկա — ցիկլ, պայման, և նոր ցուցակ։
</p>
</div>

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Առաջադրանքներ</h3>
<p style="color:#900; margin-bottom:0;">
Այս բոլորը՝ <b>քո իրական դասարանի ցուցակներով</b>։<br/><br/>
<b>1. Պարտադիր։</b> Քանի՞ աշակերտ է անցել, քանի՞սը՝ ոչ։<br/><br/>
<b>2. Պարտադիր։</b> Հավաքի՛ր չանցածների անունները նոր ցուցակում և տպի՛ր դրանք։<br/><br/>
<b>3. Պարտադիր։</b> Գտի՛ր ամենաբարձր գնահատականը և ում է այն պատկանում։<br/><br/>
<b>4. Պարտադիր։</b> Տպի՛ր ամբողջ մատյանը՝ ամեն աշակերտի դիմաց «անցավ»/«չանցավ»։
<b>Չորս տողով։</b><br/><br/>
<b>5. Ցանկության դեպքում։</b> Գտի՛ր ամենացածր գնահատականը։ Ձևը նույնն է՝ փոխի՛ր
<code>&gt;</code>-ը <code>&lt;</code>-ի։
</p>
</div>

#%% code
# Առաջադրանք 1 — քանիսն են անցել

how_many_passed = 0

for grade in class_grades:
    if grade >= PASS_MARK:
        how_many_passed = how_many_passed + 1

print(how_many_passed)

#%% code
# Առաջադրանք 2 — չանցածների անունները

failing_students = []

for position in range(len(class_grades)):
    if class_grades[position] < PASS_MARK:
        failing_students.append(student_names[position])

print(failing_students)

#%% code
# Առաջադրանք 4 — ամբողջ մատյանը, չորս տողով

for position in range(len(student_names)):
    if class_grades[position] >= PASS_MARK:
        print(f"{student_names[position]}: անցավ")
    else:
        print(f"{student_names[position]}: չանցավ")

#%% md
## Ինչի հասանք

- **Հաշվել պայմանով՝** `how_many = 0`, ցիկլ, `if`, `how_many = how_many + 1`։
- **Հավաքել նոր ցուցակ՝** `new_list = []`, ցիկլ, `if`, `.append(...)`։
- **Գտնել ամենաբարձրը՝** սկսիր առաջինից, համեմատիր, փոխարինիր։
- **9-րդ օրվա 125 տողը՝ 4 տող։** Պարտքը փակված է։

## Հաջորդ անգամ

Բոլոր ցիկլերը, որ մինչ այժմ գրել ենք, գիտեին, թե քանի անգամ պետք է կրկնվեն —
այնքան, որքան ցուցակում տարր կա։ Հաջորդ դասին՝ ցիկլ, որը **չգիտի**, և կանգնում է
միայն այն ժամանակ, երբ դու ասես։

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Հաշվի՛ր, թե քո դասարանի աշակերտների քանի՞ տոկոսն է անցել։
