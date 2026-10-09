#%% md
# Թեմա 5 — Արժեքին անուն տալ

### Python զրոյից · Թեմա 5-ը 24-ից

Երեկ գրեցինք `grade = int(input(...))` և ասացինք՝ «այս մասին վաղը»։ Այսօր է այդ վաղը։

**Փոփոխականը դասընթացի ամենակարևոր գաղափարն է։**

## ԱՅՍՕՐ:

- **Ա մաս:** անուն և արժեք
- **Բ մաս:** անունը կարող է նոր արժեք ստանալ
- **Գ մաս:** f-տողեր — արժեքը տեքստի մեջ դնել

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>input()</code>-ը միշտ տեքստ է տալիս, ուստի հաշվարկից առաջ՝ <code>int()</code>։
</p>
</div>

#%% md
## Ա մաս: Անուն և արժեք

#%% code
student_name = "Ani"

#%% md
Այս բջիջը ոչինչ չտպեց — և դա ճիշտ է։ Մենք ոչինչ չենք խնդրել տպել։ Մենք պարզապես ասացինք.

> «`"Ani"` արժեքին տուր `student_name` անունը»։

`=` նշանը **հավասար** չի նշանակում։ Այն նշանակում է **«վերագրի՛ր»** — աջ կողմի արժեքը
դիր ձախ կողմի անվան տակ։

#%% code
print(student_name)

#%% md
Տետրում կա մի հարմարություն. եթե բջիջի **վերջին տողը** պարզապես անուն է, տետրը ինքն է
ցույց տալիս արժեքը՝ առանց `print`-ի։

#%% code
student_name

#%% md
Սա տետրի հատկությունն է, ոչ թե Python-ի։ 20-րդ թեմայինից, երբ սովորական ֆայլերի անցնենք,
այն այլևս չի աշխատի — այնտեղ `print` է պետք։

#%% code
student_name = "Ani"
student_grade = 9
class_average = 6.5

print(student_name, student_grade, class_average)

#%% md
### Անվանման կանոնները

| Կանոն | Ճիշտ | Սխալ |
|---|---|---|
| Միայն անգլերեն տառեր, թվեր և `_` | `student_name` | `աշակերտ` |
| Բացատ չկա — օգտագործի՛ր `_` | `student_grade` | `student grade` |
| Թվով չի սկսվում | `grade_1` | `1_grade` |
| Մեծատառ-փոքրատառը կարևոր է | `name` ≠ `Name` | |

**Անունը գրի՛ր ամբողջական բառերով։** `student_name`, ոչ թե `sn`։ Երեք շաբաթ հետո
`sn`-ը ոչինչ չի նշանակի։

#%% md
### Հիմա կոտրենք

Ի՞նչ է լինում, եթե անուն օգտագործես, որը դեռ չես սահմանել։

#%% code expected-error: NameError
print(student_surname)

#%% md
### Ինչ գրված է այնտեղ

```
NameError: name 'student_surname' is not defined
```

«Այս անունը չեմ ճանաչում»։ Երկու հնարավոր պատճառ, և երկուսն էլ հաճախ են հանդիպում.

1. **Տառասխալ է։** `student_name` գրելու փոխարեն գրել ես `student_nmae`։
2. **Վերևի բջիջը չի գործարկվել։** Տետրում սա ամենահաճախն է։

> **Երբ `NameError` ես տեսնում տետրում՝ նախ գործարկի՛ր բոլոր բջիջները վերևից ներքև։**
> Ընտրացանկում՝ **Run → Run All Above**։

#%% md
## Բ մաս: Անունը կարող է նոր արժեք ստանալ

Դրա համար է կոչվում «փոփոխական»։

#%% code
student_grade = 9
print(student_grade)

student_grade = 10
print(student_grade)

#%% md
Հին արժեքը կորչում է։ Անունը մատնացույց է անում նոր արժեքին։

#%% code
student_grade = 9
student_grade = student_grade + 1

print(student_grade)

#%% md
`student_grade = student_grade + 1` մաթեմատիկորեն անհեթեթ է։ Բայց `=`-ը հավասար չի
նշանակում — այն նշանակում է «վերագրի՛ր»։ Ուստի կարդացվում է այսպես.

> «Վերցրու `student_grade`-ի հիմիկվա արժեքը, ավելացրու 1, և արդյունքը դիր նույն անվան տակ»։

**Հիշի՛ր այս տողը։** 12-րդ թեման դասարանի միջինը հենց այսպես ենք հաշվելու։

#%% md
## Գ մաս: f-տողեր

Մինչև հիմա արժեքները տպում էինք ստորակետով։ Դա աշխատում է, բայց տողի տեսքը լավ չի
ստացվում։

#%% code
student_name = "Ani"
student_grade = 9

print(student_name, ":", student_grade, "points")

#%% md
Նկատի՛ր ավելորդ բացատը երկու կետից առաջ։ Python-ը ամեն ստորակետի տեղում բացատ է դնում։

Ավելի լավ ձևն է **f-տողը**՝ չակերտից առաջ դրվում է `f` տառը, իսկ արժեքները գրվում են
ձևավոր փակագծերի մեջ՝ ուղիղ այնտեղ, որտեղ պետք են։

#%% code
print(f"{student_name}: {student_grade} points")

#%% md
Փակագծերի ներսում կարելի է նաև հաշվարկ անել։

#%% code
print(f"{student_name}: {student_grade} points, one more is {student_grade + 1}")

#%% md
Իսկ տասնորդական թվերի համար կարելի է ասել, թե քանի նիշ թողնել։

#%% code
class_average = 6.4762

print(f"Average: {class_average}")
print(f"Average: {class_average:.1f}")

#%% md
`:.1f` նշանակում է «մեկ նիշ ստորակետից հետո»։ Այս մեկը հիշելու կարիք չկա — կա հուշաթերթում։

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🛑 Անձնական տվյալների մասին — կարդա՛ սա</h3>
<p style="color:#900; margin-bottom:0;">
Այս պահից սկսած առաջադրանքները խնդրում են քո <b>իրական դասարանի</b> տվյալները։
Դասընթացի ֆայլերը մնում են քո համակարգչում, բայց սովորությունը կարևոր է.<br/><br/>
✅ <b>Միայն անուն կամ սկզբնատառեր։</b> «Ani», «A. M.»<br/>
❌ <b>Առանց ազգանունների։</b><br/>
❌ <b>Առանց իրական գնահատականների</b> — փոխի՛ր դրանք։<br/>
❌ <b>Առանց ծննդյան ամսաթվերի, հասցեների, փաստաթղթերի համարների։</b><br/><br/>
Ծրագիրը սովորեցնելու համար տվյալները իրական լինելու կարիք չունեն։ Դրանք պետք է միայն
<b>ծանոթ</b> լինեն։
</p>
</div>

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Պարտադիր առաջադրանքներ</h3>
<p style="color:#900; margin-bottom:0;">
<b>1.</b> Սահմանի՛ր երեք փոփոխական՝ աշակերտի անուն, գնահատական և քո առարկան։<br/><br/>
<b>2.</b> Տպի՛ր դրանք մեկ f-տողով՝ <code>Ani - biology - 9 points</code>։<br/><br/>
<b>3.</b> Ավելացրո՛ւ գնահատականին մեկ միավոր և տպի՛ր նորից։<br/><br/>
<b>4.</b> <b>Կոտրի՛ր դիտավորյալ։</b> Տպի՛ր անուն, որը չես սահմանել։ Կարդա՛
<code>NameError</code>-ը, հետո ուղղի՛ր։
</p>
</div>

#%% code
# Exercise 1 - three variables. The first one is written.

student_name = "Ani"

#%% code
# Exercise 2 - one f-string

print(f"{student_name}")

#%% code
# Exercise 4 - break it on purpose, then fix it

print(student_name)

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">🚀 Լրացուցիչ առաջադրանքներ</h3>
<p style="color:#f71; margin-bottom:0;">
<b>5.</b> Հաշվի՛ր երկու գնահատականի միջինը փոփոխականի մեջ և տպի՛ր այն մեկ նիշով։<br/><br/>
<b>6.</b> Գրի՛ր երեք աշակերտի համար երեք զույգ փոփոխական և տպի՛ր դրանք երեք f-տողով։<br/><br/>
<b>7.</b> Ի՞նչ է լինում, եթե <code>student_name</code>-ին վերագրես թիվ՝
<code>student_name = 9</code>։ Աշխատո՞ւմ է։ Ինչո՞ւ։<br/><br/>
<b>8.</b> Փորձի՛ր <code>{class_average:.2f}</code> և <code>{class_average:.0f}</code>։
Ի՞նչ է փոխվում։
</p>
</div>

#%% code
# Extra 5-8 - your space

first_grade = 9
second_grade = 6
average = (first_grade + second_grade) / 2

print(f"Average: {average:.1f}")

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🧗 Մարտահրավեր</h3>
<p style="color:#06c; margin-bottom:0;">
<b>9.</b> Գրի՛ր <b>հինգ</b> աշակերտի համար հինգ զույգ փոփոխական և տպի՛ր ամբողջական
մատյան՝ վերնագրով և հինգ տողով։<br/><br/>
Ուշադրություն դարձրու՝ որքա՞ն ժամանակ տարավ և քանի՞ տող ստացվեց։ <b>Վաղը այս
աշխատանքը շատ ավելի կարճ կդառնա։</b>
</p>
</div>

#%% code
# Challenge 9 - a five-student register with variables

student_1_name = "Ani"
student_1_grade = 9

print(f"{student_1_name}: {student_1_grade}")

#%% md
## Ինչի հասանք

- `name = value` — արժեքին անուն է տալիս։ `=`-ը նշանակում է «վերագրի՛ր»։
- Անունը կարող է նոր արժեք ստանալ, նույնիսկ իր հին արժեքի հիման վրա։
- `f"{name}: {grade}"` — արժեքը դնում է տեքստի ներսում։
- `NameError` — կամ տառասխալ է, կամ վերևի բջիջը չի գործարկվել։

## Ի՞նչ է գալիս հետո

Հիմա գիտես, թե ինչպես անուն տալ արժեքին։ **Վաղը դրանով կկառուցենք իսկական բան՝
ամբողջ դասարանի մատյան** — և դասի երկրորդ կեսին կսովորենք մի ձև, որը այդ մատյանը
դարձնում է ընդամենը երկու տող։

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Գրի՛ր երեք աշակերտի համար փոփոխականներ և տպի՛ր դրանք f-տողերով։
