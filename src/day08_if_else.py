#%% md
# Օր 8 — Առաջին որոշումը

### Python զրոյից · Օր 8-ը 24-ից

Մինչև հիմա ծրագիրը միշտ նույն բանն էր անում։ Այսօր նա սկսում է **որոշում ընդունել**։

## ԱՅՍՕՐ:

- **Ա մաս:** համեմատել՝ `>` `<` `==`
- **Բ մաս:** `if` և `else`
- **Գ մաս:** չորս բացատը

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
Մատյանը՝ երկու ցուցակ։ <code>.append()</code>, <code>.remove()</code>,
<code>.sort()</code>, <code>in</code>։
</p>
</div>

#%% md
## Ա մաս: Համեմատել

3-րդ օրը տեսանք `True` և `False` արժեքները և ասացինք, որ դրանք առայժմ անօգուտ են։
Այսօր դրանք դառնում են ամենակարևորը։

#%% code
print(9 > 4)
print(2 > 4)

#%% md
Համեմատությունը արժեք է — ուղիղ այնպես, ինչպես `9`-ը կամ `"Ani"`-ն։ Այն կամ `True` է,
կամ `False`։

#%% code
grade = 9

print(grade > 4)
print(type(grade > 4))

#%% md
Վեց նշան, և ամբողջ դասընթացում ուրիշ բան պետք չի գա։

#%% code
print(9 > 4)      # greater than
print(9 < 4)      # less than
print(9 >= 9)     # greater than or equal
print(9 <= 4)     # less than or equal
print(9 == 9)     # equal to
print(9 != 4)     # not equal to

#%% md
> **Ուշադրություն՝ `==` երկու նշան։**
>
> `=` (մեկ նշան) — **վերագրում է**. `grade = 9` նշանակում է «դիր 9-ը `grade`-ի մեջ»։
> `==` (երկու նշան) — **հարցնում է**. `grade == 9` նշանակում է «արդյո՞ք 9 է»։
>
> Սա ամենահաճախ շփոթվող բանն է ծրագրավորման սկզբում։

#%% code
print("Ani" == "Ani")
print("Ani" == "ani")

#%% md
Մեծատառը և փոքրատառը տարբեր տառեր են։ Սա 22-րդ օրը կարևոր կդառնա, երբ ֆայլից ենք
անուններ կարդալու։

#%% md
## Բ մաս: `if` և `else`

#%% code
PASS_MARK = 4
grade = 9

if grade >= PASS_MARK:
    print("passed")

#%% md
Կարդանք բառ առ բառ.

- `if` — «եթե»
- `grade >= PASS_MARK` — պայմանը։ Այն կամ `True` է, կամ `False`
- `:` — երկու կետ։ **Պարտադիր է։**
- չորս բացատ — ասում է, թե որ տողերն են պայմանի ներսում

> **Ինչո՞ւ է `PASS_MARK`-ը մեծատառերով։** Python-ում մեծատառ անունը նշանակում է
> «սա որոշում է, ոչ թե տվյալ. դնում ենք մեկ անգամ և այլևս չենք փոխում ծրագրի ընթացքում»։
>
> Եվ ավելի կարևորը՝ **անցողիկ միավորը հիմա մեկ տեղում է գրված**։ Եթե դպրոցի կանոնը
> փոխվի, փոխում ես մեկ տող։ 21-րդ օրը այս գաղափարը կդառնա առանձին ֆայլ։

Փոխի՛ր `grade`-ը 2-ի և գործարկի՛ր նորից։ Ոչինչ չի տպվի — և դա ճիշտ է։

#%% md
Սովորաբար ուզում ենք, որ մյուս դեպքում **ուրիշ** բան լինի։ Դրա համար կա `else`։

#%% code
PASS_MARK = 4
grade = 2

if grade >= PASS_MARK:
    print("passed")
else:
    print("failed")

#%% md
`else`-ը պայման չունի։ Այն նշանակում է պարզապես «մնացած բոլոր դեպքերում»։

#%% code
PASS_MARK = 4
student_name = "Hayk"
grade = 2

if grade >= PASS_MARK:
    print(f"{student_name}: {grade} - passed")
else:
    print(f"{student_name}: {grade} - failed")

#%% md
## Գ մաս: Չորս բացատը

Այն, ինչ Word-ում ձևավորում է, Python-ում **իմաստ** է։

#%% code
grade = 2

if grade >= 4:
    print("This line is inside the condition")
print("This line is not")

#%% md
Երկրորդ տողը տպվեց, չնայած պայմանը `False` էր։ Որովհետև այն **ներսում չէ** —
բացատներ չունի։

Բացատները ցույց են տալիս, թե ինչն է ինչի ներսում։ Դա ամբողջ կանոնը։

#%% md
### Հիմա կոտրենք — երկու անգամ

Առաջինը՝ մոռացված երկու կետ։

#%% code expected-error: SyntaxError
if grade >= 4
    print("passed")

#%% md
```
SyntaxError: expected ':'
```

Python-ը ուղիղ ասում է, թե ինչ է պակասում։

#%% md
Երկրորդը՝ մոռացված բացատներ։

#%% code expected-error: IndentationError
if grade >= 4:
print("passed")

#%% md
```
IndentationError: expected an indented block after 'if' statement
```

«`if`-ից հետո սպասում էի ներս տեղաշարժված տող, բայց չգտա»։

**Չորս բացատ։** Ոչ թե երկու, ոչ թե ութ, և **ոչ թե Tab-ի և բացատների խառնուրդ**։
VS Code-ը դա ինքն է անում, երբ երկու կետից հետո սեղմում ես Enter։

#%% md
<div style="border-left: 6px solid #181; background: #f2fff5; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#181; margin-top:0;">🏫 Քո դասարանում</h3>
<p style="color:#181; margin-bottom:0;">
Excel-ի <code>ԵԹԵ(A1&gt;=4; "անցավ"; "չանցավ")</code> բանաձևը ուղիղ նույն բանն է։
Տարբերությունն այն է, որ Python-ում պայմանի ներսում կարող ես դնել <b>որքան ուզես կոդ</b>,
ոչ թե մեկ արժեք։ Դա է պատճառը, որ բացատներ են պետք։
</p>
</div>

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Պարտադիր առաջադրանքներ</h3>
<p style="color:#900; margin-bottom:0;">
<b>1.</b> Գրի՛ր <code>PASS_MARK</code>-ը <b>քո դպրոցի</b> անցողիկ միավորով։<br/><br/>
<b>2.</b> Վերցրո՛ւ քո դասարանի երեք աշակերտ և ամեն մեկի համար տպի՛ր
<code>passed</code> կամ <code>failed</code>։<br/><br/>
<b>3.</b> Ավելացրո՛ւ երկրորդ պայման՝ եթե միավորը 10 է, տպի՛ր <code>excellent</code>։<br/><br/>
<b>4.</b> <b>Կոտրի՛ր դիտավորյալ։</b> Ջնջի՛ր չորս բացատը մի տողից և գործարկի՛ր։
Կարդա՛ սխալը, հետո ուղղի՛ր։
</p>
</div>

#%% code
# Exercise 1 - your school's pass mark

PASS_MARK = 4

#%% code
# Exercise 2 - three students. The first one is written.

student_name = "Ani"
grade = 9

if grade >= PASS_MARK:
    print(f"{student_name}: passed")
else:
    print(f"{student_name}: failed")

#%% code
# Exercise 4 - break it on purpose by deleting the indentation, then fix it

if 9 >= PASS_MARK:
    print("passed")

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">🚀 Լրացուցիչ առաջադրանքներ</h3>
<p style="color:#f71; margin-bottom:0;">
<b>5.</b> Ի՞նչ կլինի, եթե <code>==</code>-ի փոխարեն գրես <code>=</code> պայմանի մեջ։
Նախ գուշակի՛ր, հետո փորձի՛ր։<br/><br/>
<b>6.</b> Գրի՛ր պայման, որը ստուգում է՝ միավորը ճի՞շտ 10 է։<br/><br/>
<b>7.</b> Գրի՛ր պայման, որը համեմատում է երկու աշակերտի միավոր և ասում, թե ում
միավորն է բարձր։<br/><br/>
<b>8.</b> Գրի՛ր պայման, որը ստուգում է անունը՝ <code>if student_name == "Ani":</code>։
Հետո փորձի՛ր փոքրատառով։ Ի՞նչ է լինում։<br/><br/>
<b>9.</b> Ի՞նչ է լինում, եթե <code>if</code>-ի ներսում ոչինչ չգրես։ Փորձի՛ր։
</p>
</div>

#%% code
# Extra 5-9 - your space

first_grade = 9
second_grade = 6

if first_grade > second_grade:
    print("the first one is higher")
else:
    print("the second one is higher or equal")

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🧗 Մարտահրավեր</h3>
<p style="color:#06c; margin-bottom:0;">
<b>10.</b> Գրի՛ր պայման, որը ստուգում է, արդյոք աշակերտը կա ցուցակում
(<code>in</code>, 7-րդ օրվանից), և միայն այդ դեպքում տպում է նրա միավորը։<br/><br/>
<b>11.</b> Ներդի՛ր մեկ <code>if</code> մյուսի ներսում՝ ութ բացատով։ Օրինակ՝ եթե
աշակերտը ցուցակում է, <b>և</b> միավորը 10 է — տպի՛ր հատուկ հաղորդագրություն։
</p>
</div>

#%% code
# Challenge 10-11 - a condition inside a condition

student_names = ["Ani", "Davit"]
student_name = "Ani"
grade = 10

if student_name in student_names:
    if grade == 10:
        print(f"{student_name} is in the class and has a perfect grade")

#%% md
## Ինչի հասանք

- Համեմատությունը արժեք է՝ `True` կամ `False`։
- `=` վերագրում է, `==` հարցնում է։ Երկու տարբեր բան։
- `if condition:` ... `else:` — ծրագիրը որոշում է ընդունում։
- `PASS_MARK` — անցողիկ միավորը **մեկ տեղում**։
- **Չորս բացատը իմաստ ունի**, ոչ թե գեղեցկություն։

## Հաջորդ անգամ

Այսօր երկու ելք ունեինք։ Բայց իրական մատյանում չորս մակարդակ կա։ Հաջորդ դասին՝ `elif`,
և ինչպես երկու պայման միացնել իրար։

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Գրի՛ր պայման, որը ստուգում է՝ աշակերտի միավորը 10 է, թե ոչ։
