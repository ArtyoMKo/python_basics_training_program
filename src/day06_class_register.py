#%% md
# Օր 6 — Մատյան ամբողջ դասարանի համար

### Python զրոյից · Օր 6-ը 24-ից

Այսօր առաջին անգամ իսկական բան ենք կառուցում։

Ուսուցիչը պետք է ինչ-որ տեղ պահի ամբողջ դասարանը՝ ամեն աշակերտի անունը և միավորը,
որպեսզի ծրագիրը կարողանա աշխատել բոլորի հետ։ Դա մեր **թվային մատյանն** է, և
դասընթացի վերջում ուղիղ այն կդառնա քո ծրագիրը։

## ԱՅՍՕՐ:

- **Ա մաս:** մատյանը՝ այն ձևով, որ արդեն գիտենք
- **Բ մաս:** մեկ անուն՝ շատ արժեքի համար
- **Գ մաս:** երկու տարբերակը կողք կողքի

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>student_name = "Ani"</code> — արժեքին անուն ենք տալիս։<br/>
<code>f"{student_name}: {student_grade}"</code> — արժեքը դնում ենք տեքստի մեջ։
</p>
</div>

#%% md
## Ա մաս: Մատյանը՝ այն ձևով, որ արդեն գիտենք

Մեզ պետք է քսան աշակերտի անուն և միավոր։ Այն, ինչ գիտենք մինչև հիմա, մեկ բան է՝
ամեն արժեքի համար առանձին անուն։

Ներքևի բջիջում քսան աշակերտ է՝ քառասուն փոփոխական։ **Գործարկի՛ր և կարդա՛։**

<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Այս ձևն աշխատում է, բայց երկար է։</b> Դասի երկրորդ կեսին կսովորենք մի բան,
որը այս ամբողջ բջիջը դարձնում է <b>երկու տող</b>։ Առայժմ շարունակի՛ր այսպես —
կեսժամից կհամեմատենք։
</p>
</div>

#%% code
student_01_name = "Ani"
student_01_grade = 9
student_02_name = "Davit"
student_02_grade = 6
student_03_name = "Nare"
student_03_grade = 10
student_04_name = "Aram"
student_04_grade = 3
student_05_name = "Mariam"
student_05_grade = 8
student_06_name = "Tigran"
student_06_grade = 5
student_07_name = "Lilit"
student_07_grade = 8
student_08_name = "Gor"
student_08_grade = 4
student_09_name = "Anahit"
student_09_grade = 9
student_10_name = "Hayk"
student_10_grade = 2
student_11_name = "Sona"
student_11_grade = 8
student_12_name = "Vahe"
student_12_grade = 6
student_13_name = "Mane"
student_13_grade = 7
student_14_name = "Samvel"
student_14_grade = 5
student_15_name = "Elen"
student_15_grade = 9
student_16_name = "Narek"
student_16_grade = 4
student_17_name = "Alis"
student_17_grade = 10
student_18_name = "Artur"
student_18_grade = 6
student_19_name = "Siranush"
student_19_grade = 7
student_20_name = "Vardan"
student_20_grade = 3

#%% md
Քսան աշակերտ, և արդեն տեսնում ես, թե որքան տեղ է դա զբաղեցնում։

Հիմա տպենք առաջին երեքը՝ ուղիղ այնպես, ինչպես երեկ սովորեցինք։

#%% code
print(f"{student_01_name}: {student_01_grade}")
print(f"{student_02_name}: {student_02_grade}")
print(f"{student_03_name}: {student_03_grade}")

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Առաջադրանք 1 — պարտադիր</h3>
<p style="color:#900; margin-bottom:0;">
Ներքևի բջիջում ավելացրո՛ւ <b>հինգ աշակերտ քո դասարանից</b>՝ 21-ից 25 համարներով։<br/><br/>
Առաջինը գրված է որպես օրինակ։ Շարունակի՛ր ուղիղ նույն ձևով.<br/><br/>
<code>student_22_name = "..."</code><br/>
<code>student_22_grade = ...</code><br/><br/>
<b>Միայն անուններ՝ լատինատառ, առանց ազգանունների։ Գնահատականները փոխի՛ր։</b>
</p>
</div>

#%% code
# Exercise 1 - five students from your own class. The first one is written.

student_21_name = "Anna"
student_21_grade = 7

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Առաջադրանք 2 — պարտադիր</h3>
<p style="color:#900; margin-bottom:0;">
Քննությունից հետո միավորները վերանայվեցին և բոլորը ստացան մեկ միավոր ավելի։<br/><br/>
Թարմացրո՛ւ <b>առաջին հինգ աշակերտի</b> միավորները ներքևի բջիջում։ Առաջին երկուսը
գրված են։<br/><br/>
Ուշադրություն դարձրու, թե ինչպես է դա ընթանում — դասի վերջում կհամեմատենք։
</p>
</div>

#%% code
# Exercise 2 - everyone gets one more point. The first two are done.

student_01_grade = student_01_grade + 1
student_02_grade = student_02_grade + 1

print(student_01_grade, student_02_grade)

#%% md
## Բ մաս: Մեկ անուն՝ շատ արժեքի համար

Հիմա նայի՛ր վերևի բջիջներին և մի բան նկատի՛ր.

`student_01_grade`, `student_02_grade`, `student_03_grade` ... սրանք բոլորը **նույն
բանն են**։ Բոլորը գնահատական են։ Միակ տարբերությունը համարն է։

Python-ում կա ձև, որով շատ արժեք պահվում է **մեկ** անվան տակ։ Այն կոչվում է **ցուցակ**։

#%% code
class_grades = [9, 6, 10, 3, 8]

print(class_grades)

#%% md
Քառակուսի փակագծերի մեջ, ստորակետով բաժանված։ Մեկ անուն՝ հինգ արժեք։

Ահա ամբողջ մատյանը՝ քսան աշակերտը՝ **երկու տողով**։

#%% code
student_names = ["Ani", "Davit", "Nare", "Aram", "Mariam", "Tigran", "Lilit", "Gor",
                 "Anahit", "Hayk", "Sona", "Vahe", "Mane", "Samvel", "Elen", "Narek",
                 "Alis", "Artur", "Siranush", "Vardan"]
class_grades = [9, 6, 10, 3, 8, 5, 8, 4, 9, 2, 8, 6, 7, 5, 9, 4, 10, 6, 7, 3]

print(student_names)

#%% md
Երկար ցուցակը կարելի է գրել մի քանի տողով։ Python-ը կարդում է մինչև փակող `]`-ը։

Եվ ամենակարևոր հարցին այժմ պատասխան կա՝ **քանի՞ հոգի է**։

#%% code
print(len(class_grades))

#%% md
`len` — «length», երկարություն։ Վերևի քառասուն փոփոխականի դեպքում այս հարցի պատասխանը
չկար — պետք էր հաշվել ձեռքով։

#%% md
### Ինչպես հասնել մեկ արժեքի

#%% code
class_grades = [9, 6, 10, 3, 8]

print(class_grades[0])

#%% md
Քառակուսի փակագծերի մեջ գրում ենք **տեղը** — ինդեքսը։

Եվ ահա այսօրվա միակ շփոթեցնող բանը.

> **Հաշվարկը սկսվում է զրոյից։**

#%% code
class_grades = [9, 6, 10, 3, 8]

print(class_grades[0])     # the first one
print(class_grades[1])     # the second one
print(class_grades[4])     # the fifth one

#%% md
| Ինդեքսը | Որերորդն է | Արժեքը |
|---|---|---|
| `[0]` | առաջինը | 9 |
| `[1]` | երկրորդը | 6 |
| `[2]` | երրորդը | 10 |
| `[3]` | չորրորդը | 3 |
| `[4]` | հինգերորդը | 8 |

Հինգ տարր, ինդեքսները՝ **0-ից 4**։ Ոչ թե 1-ից 5։

Վերջինին հասնելու համար կա հարմարություն՝ `-1`։

#%% code
print(class_grades[-1])

#%% md
### Հիմա կոտրենք

Հինգ տարր ունեցող ցուցակում ի՞նչ կա `[5]` տեղում։ **Նախ գուշակի՛ր։**

#%% code expected-error: IndexError
class_grades = [9, 6, 10, 3, 8]

print(class_grades[5])

#%% md
```
IndexError: list index out of range
```

«Այդ տեղը ցուցակում չկա»։ Հինգ տարր՝ ինդեքսները 0, 1, 2, 3, 4։ `[5]`-ը **վեցերորդն**
է, իսկ վեցերորդ չկա։

> **Կանոն.** եթե ցուցակում `n` տարր կա, վերջինի ինդեքսը `n - 1` է։ Կամ պարզապես գրի՛ր
> `[-1]` և չմտածես։

#%% md
## Գ մաս: Երկու տարբերակը կողք կողքի

Ահա նույն մատյանը՝ երկու ձևով։

**Ձև 1 — առանձին փոփոխականներ (այն, ինչով սկսեցինք).**

```python
student_01_name = "Ani"
student_01_grade = 9
student_02_name = "Davit"
student_02_grade = 6
...                          # 40 lines for 20 students
```

**Ձև 2 — ցուցակներ.**

#%% code
student_names = ["Ani", "Davit", "Nare", "Aram", "Mariam"]
class_grades = [9, 6, 10, 3, 8]

print(f"{len(student_names)} students in the register")

#%% md
| | Առանձին փոփոխականներ | Ցուցակ |
|---|---|---|
| 20 աշակերտի համար | 40 տող | **2 տող** |
| «Քանի՞սն են» | հաշվի՛ր ձեռքով | `len(...)` |
| Նոր աշակերտ ավելացնել | 2 նոր տող | վաղը՝ մեկ հրահանգ |
| 300 աշակերտի համար | 600 տող | **2 տող** |

#%% md
<div style="border-left: 6px solid #181; background: #f2fff5; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#181; margin-top:0;">🏫 Քո դասարանում</h3>
<p style="color:#181; margin-bottom:0;">
Ցուցակը ուղիղ այն է, ինչ Excel-ի <b>սյունակն</b> է։ Մեկ անուն՝ վերևում, շատ արժեք՝
ներքևում։ Տարբերությունն այն է, որ Excel-ում տողերը 1-ից են համարակալված, իսկ
Python-ում՝ 0-ից։ Դա միակ բանն է, որ պետք է հիշել։
</p>
</div>

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Պարտադիր առաջադրանքներ</h3>
<p style="color:#900; margin-bottom:0;">
<b>3.</b> Գրի՛ր <b>քո ամբողջ դասարանը երկու ցուցակով</b>՝ անունները և միավորները,
<b>նույն հերթականությամբ</b>։<br/><br/>
<b>4.</b> Տպի՛ր՝ քանի աշակերտ կա, առաջինի անունը, վերջինի անունը։<br/><br/>
<b>5.</b> <b>Կոտրի՛ր դիտավորյալ։</b> Խնդրի՛ր այնպիսի ինդեքս, որ ցուցակում չկա։
Կարդա՛ սխալը, հետո ուղղի՛ր։
</p>
</div>

#%% code
# Exercise 3 - your whole class, in two lists

student_names = ["Ani", "Davit"]
class_grades = [9, 6]

#%% code
# Exercise 4 - how many, first, last

print(len(student_names))

#%% code
# Exercise 5 - break it on purpose, then fix it

print(student_names[0])

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">🚀 Լրացուցիչ առաջադրանքներ</h3>
<p style="color:#f71; margin-bottom:0;">
<b>6.</b> Տպի՛ր երրորդ աշակերտի անունը և միավորը մեկ f-տողով։<br/><br/>
<b>7.</b> Հաշվի՛ր ձեռքով առաջին երեք աշակերտի միավորների գումարը՝
<code>class_grades[0] + ...</code> ձևով։<br/><br/>
<b>8.</b> Գրի՛ր երրորդ ցուցակ՝ աշակերտների հաճախումների տոկոսը, նույն
հերթականությամբ։<br/><br/>
<b>9.</b> Ի՞նչ է լինում, եթե ցուցակում խառը դնես՝ <code>[9, "Ani", 6.5]</code>։
Աշխատո՞ւմ է։ Լա՞վ գաղափար է։
</p>
</div>

#%% code
# Extra 6-9 - your space

print(f"{student_names[0]}: {class_grades[0]}")

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🧗 Մարտահրավեր</h3>
<p style="color:#06c; margin-bottom:0;">
<b>10.</b> Տպի՛ր քո ամբողջ դասարանի մատյանը՝ ամեն աշակերտի համար մեկ տող, ինդեքսներով՝
<code>[0]</code>, <code>[1]</code>, <code>[2]</code> ...<br/><br/>
Հաշվի՛ր, թե քանի տող գրեցիր։ <b>Հիշի՛ր այդ թիվը</b> — 10-րդ օրը այն կդառնա չորս։
</p>
</div>

#%% code
# Challenge 10 - the whole register, one index at a time

print(f"{student_names[0]}: {class_grades[0]}")

#%% md
## Ինչի հասանք

- **Մատյան ամբողջ դասարանի համար** — երկու ցուցակով, ոչ թե քառասուն փոփոխականով։
- `[9, 6, 10]` — մեկ անուն, շատ արժեք։
- `len(list)` — քանիսն են։ `list[0]` — առաջինը։ **Հաշվարկը զրոյից է։** `list[-1]` — վերջինը։
- `IndexError` — այդ տեղը ցուցակում չկա։

## Հաջորդ անգամ

Մատյանը հիմա մեկ տեղում է։ Հաջորդ դասին այն կդառնա **կենդանի** — աշակերտ ավելացնել,
հեռացնել, դասավորել այբբենական կարգով։

Իսկ այն, որ ամեն աշակերտի տպելու համար դեռ առանձին տող է պետք, **10-րդ օրը կդառնա
չորս տող ամբողջ դասարանի համար**։

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Գրի՛ր քո ամբողջ դասարանը երկու ցուցակով և տպի՛ր, թե քանի հոգի է։
