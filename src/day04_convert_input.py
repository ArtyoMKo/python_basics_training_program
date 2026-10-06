#%% md
# Օր 4 — Տեսակը փոխել, և հարց տալ

### Python զրոյից · Օր 4-ը 24-ից

Երեկ տեսանք, որ `"9"`-ը և `9`-ը տարբեր բաներ են։ Այսօր սովորում ենք մեկը մյուսին
վերածել — և պարզում ենք, թե ինչու է դա **անհրաժեշտ**։

## ԱՅՍՕՐ:

- **Ա մաս:** `int()`, `str()`, `float()` — տեսակը փոխել
- **Բ մաս:** `input()` — հարցնել օգտվողից
- **Գ մաս:** `input()`-ը **միշտ** տեքստ է տալիս

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
Չորս տեսակ՝ <code>str</code>, <code>int</code>, <code>float</code>, <code>bool</code>։
<code>"9" + 1</code> տալիս է <code>TypeError</code>։
</p>
</div>

#%% md
## Ա մաս: Տեսակը փոխել

Երեք հրահանգ, և ամբողջ դասընթացում ուրիշ բան պետք չի գա։

#%% code
print(int("9"))
print(str(9))
print(float("6.5"))

#%% md
Ամեն մեկը տալիս է **նոր** արժեք։ Բնօրինակը չի փոխվում։

Հիմա երեկվա խնդիրը լուծված է։

#%% code
print(int("9") + 1)

#%% md
Կա նաև չորրորդ օգտակար հրահանգ՝ `round()` — կլորացնում է։

#%% code
print(round(6.4762, 1))
print(round(6.4762))

#%% md
Երկրորդ թիվը ասում է՝ քանի նիշ թողնել ստորակետից հետո։ Սա պետք կգա 12-րդ օրը, երբ
միջին ենք հաշվելու։

#%% md
## Բ մաս: `input()` — հարցնել օգտվողից

Մինչև հիմա բոլոր արժեքները մենք ինքներս էինք գրում կոդի մեջ։ `input()`-ը թույլ է տալիս
**հարցնել**։

Գործարկի՛ր ներքևի բջիջը։ Վերևում կհայտնվի դաշտ — գրի՛ր անունդ և սեղմի՛ր Enter։

#%% code interactive: Anahit
teacher_name = input("What is your name? ")

print("Hello,", teacher_name)

#%% md
Երկու բան կատարվեց.

- `input("...")` — ցույց տվեց հարցը և սպասեց, մինչև գրես։
- `teacher_name = ` — գրածդ **պահեց** այդ անվան տակ։ Վաղը այս մասին երկար կխոսենք։

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🛑 Երբ բջիջը «կախվում է»</h3>
<p style="color:#900; margin-bottom:0;">
Երբ բջիջը <code>input()</code> ունի, նրա կողքին հայտնվում է <b>[*]</b> և տետրը սպասում է
քեզ։ Ուրիշ բջիջ այդ ընթացքում չի աշխատի։<br/><br/>
Եթե մոռացել ես պատասխանել՝ գրի՛ր ինչ-որ բան և սեղմի՛ր Enter։ Կամ սեղմի՛ր վերևի
<b>■</b> (Interrupt) կոճակը։
</p>
</div>

#%% md
## Գ մաս: `input()`-ը միշտ տեքստ է տալիս

Այսօրվա ամենակարևոր նախադասությունը մեկն է.

> **Ինչ էլ գրի օգտվողը, `input()`-ը քեզ տալիս է տեքստ։**

Նույնիսկ եթե գրի `9`, դու ստանում ես `"9"`։ Ստուգենք։

#%% code interactive: 9
answer = input("Grade: ")

print(answer)
print(type(answer))

#%% md
`str`։ Ոչ թե `int`։

Իսկ հիմա փորձենք այդ գնահատականին մեկ միավոր ավելացնել։

#%% code expected-error: TypeError
answer = "9"           # exactly what input() would have given us

print(answer + 1)

#%% md
Նույն `TypeError`-ն է, ինչ երեկ։ Բայց հիմա այն հանդիպում է **իրական իրավիճակում** —
ամեն անգամ, երբ ինչ-որ բան հարցնում ես և ուզում ես հաշվարկ անել։

Լուծումը՝ վերածի՛ր թվի։

#%% code
answer = "9"
grade = int(answer)

print(grade + 1)

#%% md
Սովորաբար դա գրում են մեկ տողում՝ `input()`-ը ուղղակի փաթաթում են `int()`-ի մեջ։

#%% code interactive: 9
grade = int(input("Grade: "))

print("One point more:", grade + 1)

#%% md
### Հիմա կոտրենք

Իսկ ի՞նչ է լինում, եթե օգտվողը թիվ չգրի։

#%% code expected-error: ValueError
print(int("nine"))

#%% md
### Ինչ գրված է այնտեղ

```
ValueError: invalid literal for int() with base 10: 'nine'
```

| Մասը | Ի՞նչ է ասում |
|---|---|
| `ValueError` | «Տեսակը ճիշտ է, բայց արժեքը՝ ոչ» |
| `invalid literal for int()` | «Սա թիվ դարձնել չեմ կարող» |
| `'nine'` | ուղիղ այն, ինչ չհասկացա |

**`TypeError`-ի և `ValueError`-ի տարբերությունը.** `TypeError` — սխալ **տեսակի** բան ես
տվել։ `ValueError` — տեսակը ճիշտ է (տեքստ), բայց բովանդակությունը թիվ չէ։

16-րդ օրը կսովորենք, թե ինչպես ստուգել՝ նախքան վերածելը։

#%% md
<div style="border-left: 6px solid #181; background: #f2fff5; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#181; margin-top:0;">🏫 Քո դասարանում</h3>
<p style="color:#181; margin-bottom:0;">
Ամեն ծրագիր, որին տվյալ ես մուտքագրում — էլեկտրոնային մատյան, հարցաթերթ, բանկի կայք —
ստանում է <b>տեքստ</b> և ինքն է այն վերածում թվի։ Ահա թե ինչու է կայքը երբեմն ասում՝
«խնդրում ենք մուտքագրել թիվ»։ Այդ պահին ինչ-որ տեղ ուղիղ այս <code>ValueError</code>-ն է։
</p>
</div>

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Պարտադիր առաջադրանքներ</h3>
<p style="color:#900; margin-bottom:0;">
<b>1.</b> Հարցրո՛ւ աշակերտի անունը և տպի՛ր ողջույն։<br/><br/>
<b>2.</b> Հարցրո՛ւ գնահատականը, վերածի՛ր թվի և տպի՛ր այն՝ մեկ միավոր ավելացրած։<br/><br/>
<b>3.</b> Հարցրո՛ւ երկու գնահատական և տպի՛ր դրանց միջինը՝ մեկ նիշով կլորացրած։<br/><br/>
<b>4.</b> <b>Կոտրի՛ր դիտավորյալ։</b> Առաջադրանք 2-ում գնահատականի փոխարեն գրի՛ր
տառերով։ Կարդա՛ սխալը։
</p>
</div>

#%% code interactive: Ani
# Exercise 1

student_name = input("Student name: ")

print("Hello,", student_name)

#%% code interactive: 9
# Exercise 2 - do not forget int()

grade = int(input("Grade: "))

print(grade + 1)

#%% code interactive: 9; 6
# Exercise 3 - the average of two grades

first_grade = int(input("First grade: "))
second_grade = int(input("Second grade: "))

print(round((first_grade + second_grade) / 2, 1))

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">🚀 Լրացուցիչ առաջադրանքներ</h3>
<p style="color:#f71; margin-bottom:0;">
<b>5.</b> Ի՞նչ է լինում, եթե <code>int("9.5")</code> գրես։ Նախ գուշակի՛ր, հետո
ստուգի՛ր։ Ինչպե՞ս ճիշտ անել։<br/><br/>
<b>6.</b> Հարցրո՛ւ երեք գնահատական և տպի՛ր միջինը։<br/><br/>
<b>7.</b> Հարցրո՛ւ աշակերտի անունը և գնահատականը, հետո տպի՛ր մեկ տողով՝
<code>Ani: 9</code> ձևաչափով։<br/><br/>
<b>8.</b> Ի՞նչ է տալիս <code>str(9) + str(1)</code>։ Ինչո՞ւ է այն տարբեր
<code>9 + 1</code>-ից։
</p>
</div>

#%% code
# Extra 5-8 - your space

print(float("9.5"))

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🧗 Մարտահրավեր</h3>
<p style="color:#06c; margin-bottom:0;">
<b>9.</b> Հարցրո՛ւ դասարանի աշակերտների թիվը և միավորների գումարը, հետո տպի՛ր միջինը՝
երկու նիշով։<br/><br/>
<b>10.</b> Ի՞նչ է լինում, եթե դատարկ պատասխանես (ուղղակի Enter)։ Ի՞նչ սխալ է լինում
<code>int("")</code>-ի դեպքում։
</p>
</div>

#%% code
# Challenge 9-10

total = 78
how_many = 12

print(round(total / how_many, 2))

#%% md
## Ինչի հասանք

- `int()`, `str()`, `float()` — փոխում են տեսակը։ `round()` — կլորացնում է։
- `input("question")` — հարցնում է և սպասում պատասխանի։
- **`input()`-ը միշտ տեքստ է տալիս։** Հաշվարկից առաջ վերածի՛ր թվի։
- `ValueError` — տեսակը ճիշտ է, արժեքը՝ ոչ։

## Հաջորդ անգամ

Այսօր երկու անգամ գրեցինք `grade = ...` և ասացինք՝ «այս մասին վաղը»։ Վաղը հենց այդ
մասին է՝ **փոփոխականներ**։

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Գրի՛ր բջիջ, որը հարցնում է երեք գնահատական և տպում դրանց միջինը։
