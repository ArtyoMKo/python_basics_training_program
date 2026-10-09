#%% md
# Թեմա 10 — Երկուսից ավելի ելք

### Python զրոյից · Թեմա 10-ը 24-ից

Այս նիստի սկզբում երկու ելք ունեինք։ Իրական մատյանում չորս մակարդակ կա։

## ԱՅՍՕՐ:

- **Ա մաս:** `elif` — երրորդ, չորրորդ, հինգերորդ ելքը
- **Բ մաս:** հերթականությունը կարևոր է
- **Գ մաս:** `and`, `or`, `not`

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>if condition:</code> ... <code>else:</code> — երկու ելք։ Երկու կետ, չորս բացատ։<br/>
<code>PASS_MARK</code> — անցողիկ միավորը մեկ տեղում։
</p>
</div>

#%% md
## Ա մաս: `elif`

`elif` նշանակում է «else if» — «իսկ եթե ոչ, ապա եթե...»։

#%% code
grade = 8

if grade >= 9:
    print("excellent")
elif grade >= 7:
    print("good")
elif grade >= 4:
    print("satisfactory")
else:
    print("unsatisfactory")

#%% md
Կարդանք վերևից ներքև, ուղիղ այնպես, ինչպես Python-ը.

1. `8 >= 9`? Ոչ։ Անցնում ենք հաջորդին։
2. `8 >= 7`? Այո։ **Տպում ենք «good» և կանգ առնում։**

**Առաջին ճիշտ պայմանը հաղթում է։** Մնացածը նույնիսկ չեն ստուգվում։ Փոխի՛ր `grade`-ը
10-ի, 5-ի, 2-ի և գործարկի՛ր ամեն անգամ։

#%% md
## Բ մաս: Հերթականությունը կարևոր է

Հիմա նույն չորս պայմանը՝ **սխալ հերթականությամբ**։

**Նախ գուշակի՛ր։** Ի՞նչ կտպի սա 10-ի համար։

#%% code
grade = 10

if grade >= 4:
    print("satisfactory")
elif grade >= 7:
    print("good")
elif grade >= 9:
    print("excellent")

#%% md
«satisfactory»։ Գերազանց աշակերտը ստացավ «բավարար»։

Որովհետև `10 >= 4` ճիշտ է, և առաջին ճիշտ պայմանը հաղթում է։ Մյուս երկուսը երբեք չեն
ստուգվի — ոչ մի միավորի համար։

> **Ուշադրություն։ Այստեղ ոչ մի սխալ չհայտնվեց։** Ոչ մի կարմիր տեքստ։ Ծրագիրը
> հանգիստ աշխատեց և տվեց սխալ պատասխան։
>
> Սա ամենավտանգավոր տեսակի սխալն է. **այն, որ չի բողոքում**։ Ահա թե ինչու պետք է
> ամեն `elif` շղթա ստուգել մի քանի տարբեր թվով։

#%% md
**Կանոնը պարզ է՝ ամենախիստ պայմանը դիր առաջինը։** Նեղից դեպի լայն։

#%% code
grade = 10

if grade >= 9:
    print("excellent")
elif grade >= 7:
    print("good")
elif grade >= 4:
    print("satisfactory")
else:
    print("unsatisfactory")

#%% md
## Գ մաս: `and`, `or`, `not`

Իրական դպրոցական կանոնները հաճախ երկու պայման ունեն միանգամից։

> «Աշակերտը ստանում է վկայական, եթե անցել է **և** հաճախել է դասերի 80 տոկոսին»։

#%% code
PASS_MARK = 4

grade = 8
attendance = 90

if grade >= PASS_MARK and attendance >= 80:
    print("certificate granted")
else:
    print("certificate not granted")

#%% md
`and` — **երկուսն էլ** պետք է ճիշտ լինեն։ Փոխի՛ր `attendance`-ը 50-ի և գործարկի՛ր։

#%% code
grade = 8
attendance = 50

if grade >= 4 and attendance >= 80:
    print("certificate granted")
else:
    print("certificate not granted")

#%% md
`or` — **գոնե մեկը** ճիշտ լինի։

#%% code
grade = 3
has_retaken_exam = True

if grade >= 4 or has_retaken_exam:
    print("moves to the next year")
else:
    print("does not move")

#%% md
`not` — հակառակը։

#%% code
attended = False

if not attended:
    print("absent")

#%% md
Ուշադրություն՝ սրանք **բառեր** են, ոչ թե նշաններ։ Python-ում `&&` և `||` չկան։

Երեքն էլ կարելի է ստուգել առանձին, առանց `if`-ի — հիշի՛ր, պայմանը պարզապես արժեք է։

#%% code
print(True and False)
print(True or False)
print(not True)

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">📌 Հաջորդ նիստում</h3>
<p style="color:#f71; margin-bottom:0;">
Այս պայմանները մինչ այժմ կիրառում ենք <b>մեկ</b> աշակերտի վրա։<br/><br/>
Հաջորդ նիստում դրանք կկիրառենք <b>ամբողջ դասարանի վրա միանգամից</b> — և կսովորենք մի
ձև, որով դա արվում է չորս տողով՝ անկախ նրանից, քսան աշակերտ ունես, թե երեք հարյուր։
</p>
</div>

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Պարտադիր առաջադրանքներ</h3>
<p style="color:#900; margin-bottom:0;">
<b>1.</b> Գրի՛ր չորս մակարդակի շղթա <b>քո դպրոցի</b> սահմաններով։<br/><br/>
<b>2.</b> Ստուգի՛ր այն <b>չորս տարբեր միավորով</b> — մեկը ամեն մակարդակից։<br/><br/>
<b>3.</b> Գրի՛ր մեկ կանոն <code>and</code>-ով՝ քո դասարանից վերցրած իրական կանոն։<br/><br/>
<b>4.</b> <b>Խառնի՛ր հերթականությունը դիտավորյալ։</b> Տեղափոխի՛ր
<code>elif grade &gt;= 4</code>-ը ամենավերև և գործարկի՛ր 10-ով։ Տեսի՛ր սխալ պատասխանը
առանց սխալի հաղորդագրության։
</p>
</div>

#%% code
# Exercise 1 and 2 - four bands, your school's boundaries

grade = 8

if grade >= 9:
    print("excellent")
elif grade >= 7:
    print("good")
elif grade >= 4:
    print("satisfactory")
else:
    print("unsatisfactory")

#%% code
# Exercise 3 - your own rule with and

grade = 8
attendance = 90

if grade >= 4 and attendance >= 80:
    print("yes")

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">🚀 Լրացուցիչ առաջադրանքներ</h3>
<p style="color:#f71; margin-bottom:0;">
<b>5.</b> Ի՞նչ է տալիս <code>not (grade &gt;= 4)</code>։ Համեմատի՛ր
<code>grade &lt; 4</code>-ի հետ։<br/><br/>
<b>6.</b> Գրի՛ր կանոն <code>or</code>-ով՝ «անցնում է, եթե միավորը 4-ից բարձր է
<b>կամ</b> վերահանձնել է»։<br/><br/>
<b>7.</b> Գրի՛ր կանոն երեք պայմանով՝ <code>and</code>-ը երկու անգամ օգտագործելով։<br/><br/>
<b>8.</b> Ի՞նչ է <code>True and False or True</code>։ Նախ գուշակի՛ր։ Հետո փորձի՛ր
փակագծերով՝ <code>(True and False) or True</code> և <code>True and (False or True)</code>։<br/><br/>
<b>9.</b> Գրի՛ր <code>elif</code> շղթա, որը միավորը վերածում է հայերեն
բառի, բայց տեքստը գրի՛ր անգլերեն՝ <code>excellent</code>, <code>good</code> ...
</p>
</div>

#%% code
# Extra 5-9 - your space

grade = 3

print(not (grade >= 4))
print(grade < 4)

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🧗 Մարտահրավեր</h3>
<p style="color:#06c; margin-bottom:0;">
<b>10.</b> Գրի՛ր դպրոցի իրական վկայականի կանոնը՝ երեք պայմանով.
միավորը անցողիկ է, հաճախումը 80%-ից բարձր է, <b>և</b> վարքը բավարար է։
Ստուգի՛ր այն ութ տարբեր համակցությամբ և համոզվի՛ր, որ բոլորը ճիշտ են։<br/><br/>
<b>11.</b> Գրի՛ր նույն կանոնը՝ օգտագործելով <code>not</code> և <code>or</code>՝
առանց <code>and</code>-ի։ Նույն արդյո՞ւնքն է ստացվում։
</p>
</div>

#%% code
# Challenge 10-11 - the real certificate rule

grade = 8
attendance = 90
behaviour_ok = True

if grade >= 4 and attendance >= 80 and behaviour_ok:
    print("certificate granted")
else:
    print("certificate not granted")

#%% md
<div style="border-left: 6px solid #747; background: #f8f6fb; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#747; margin-top:0;">🏠 Տնային</h3>
<p style="color:#747; margin-bottom:0;">
Այս նոթատետրի <b>Պարտադիր</b> առաջադրանքները — այս նիստում երկու նոթատետր ենք անցնում, և դրանք դասին չեն տեղավորվում — ապա <b>Լրացուցիչ</b>-ը, որքան հասցնես։<br/><br/>
<b>Նոր բան չկա</b> — ամեն առաջադրանք այս նոթատետրից է, և օգտագործում է միայն այն,
ինչ այսօր սովորեցինք։<br/>
Հաջորդ նիստը սկսվում է դրանց ստուգումով։
</p>
</div>

#%% md
## Ինչի հասանք

- `elif` — որքան ուզես ելք։ **Առաջին ճիշտ պայմանը հաղթում է։**
- Սխալ հերթականությունը տալիս է **սխալ պատասխան առանց սխալի հաղորդագրության**։
  Ամենախիստ պայմանը՝ առաջինը։
- `and` — երկուսն էլ։ `or` — գոնե մեկը։ `not` — հակառակը։ Բառեր, ոչ թե նշաններ։

## Ի՞նչ է գալիս հետո

Հաջորդ նիստում այս պայմանները կկիրառենք **ամբողջ դասարանի վրա** — և կտեսնենք, թե ինչպես
է դա արվում չորս տողով։

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Գրի՛ր քո չորս մակարդակի շղթան և ստուգի՛ր բոլոր տասը միավորով՝ 1-ից 10։
