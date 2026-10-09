#%% md
# Օր 16 — Միավորները մուտքագրել մեկ առ մեկ

### Python զրոյից · Օր 16-ը 24-ից

Մինչ այժմ միավորները գրում էինք ուղիղ կոդի մեջ։ Այսօր ծրագիրը սկսում է **հարցնել**։

Սա վերջին նոր տեսակի ցիկլն է դասընթացում։

Դա այն է, ինչ անում ես, երբ գրիչով մատյան ես լրացնում. մուտքագրում ես մեկը, հետո
մյուսը, մինչև վերջանան։

## ԱՅՍՕՐ:

- **Ա մաս:** `while` և `break`
- **Բ մաս:** ստուգել, թե ինչ է գրել օգտվողը
- **Գ մաս:** անվերջ ցիկլ — և ինչպես կանգնեցնել

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>for</code>-ը կրկնվում է ցուցակի ամեն տարրի համար՝ ոչ ավել, ոչ պակաս։<br/>
Եվ 4-րդ օրվանից՝ <code>input()</code>-ը միշտ տեքստ է տալիս։
</p>
</div>

#%% md
## Ա մաս: `while`

`for`-ը կապված է ցուցակի հետ։ Իսկ երբ ուզում ենք կրկնել, մինչև ինչ-որ բան **տեղի
ունենա**, պետք է `while`։

#%% code
count = 0

while count < 3:
    print("round number", count)
    count = count + 1

print("done")

#%% md
`while condition:` — «քանի դեռ պայմանը ճիշտ է, կրկնի՛ր»։

Ամեն պտույտից առաջ Python-ը ստուգում է պայմանը։ Երբ այն դառնում է `False`, ցիկլը կանգ
է առնում։

**Ուշադրություն `count = count + 1` տողին։** Առանց դրա պայմանը երբեք չէր փոխվի և ցիկլը
երբեք չէր կանգնի։

#%% md
Իրական օգտագործումը՝ ցիկլ, որը սպասում է ուսուցչին։ Դրա համար կա երկու բառ՝
`while True` և `break`։

#%% code interactive: 9; 6; quit
class_grades = []

while True:
    answer = input("Grade (or 'quit'): ")

    if answer == "quit":
        break

    class_grades.append(int(answer))

print("collected:", class_grades)

#%% md
- `while True:` — «կրկնի՛ր միշտ»։ Պայմանը բառացիորեն `True` է, ուստի երբեք չի ավարտվի ինքն իրեն։
- `break` — «դուրս արի ցիկլից հիմա»։ Դա միակ ելքն է։

**Այս ձևը՝ `while True` + `break` — ամբողջ դասընթացում օգտագործում ենք միայն այսպես։**

#%% md
## Բ մաս: Ստուգել, թե ինչ է գրել օգտվողը

4-րդ օրը տեսանք, որ `int("nine")`-ը տալիս է `ValueError` և ծրագիրը կանգնում է։

Իսկական ծրագիրը չպետք է կանգնի այդ պատճառով։ Python-ում կա պատրաստի ստուգում.

#%% code
print("9".isdigit())
print("nine".isdigit())
print("".isdigit())

#%% md
`.isdigit()` — «արդյո՞ք սա միայն թվանշաններից է բաղկացած»։ Տալիս է `True` կամ `False`,
ուստի կարող է `if`-ի մեջ մտնել։

#%% code interactive: nine; 15; 9; quit
class_grades = []

while True:
    answer = input("Grade from 1 to 10 (or 'quit'): ")

    if answer == "quit":
        break

    if not answer.isdigit():
        print("That is not a number. Try again.")
        continue

    grade = int(answer)

    if grade < 1 or grade > 10:
        print("The grade must be between 1 and 10. Try again.")
        continue

    class_grades.append(grade)
    print(f"Added. Now there are {len(class_grades)} grades.")

print("final list:", class_grades)

#%% md
Նոր բառ՝ `continue` — «բաց թող մնացածը և անցի՛ր հաջորդ պտույտին»։

`break`-ը դուրս է գալիս ցիկլից։ `continue`-ն մնում է ցիկլում, բայց սկսում է նորից։

Ուշադրություն երեք ստուգման հերթականությանը.

1. Ուզո՞ւմ է դուրս գալ։
2. Թի՞վ է ընդհանրապես։
3. Ճիշտ միջակայքո՞ւմ է։

**Ամեն ստուգում ունի իր առանձին հաղորդագրությունը։** «Սխալ մուտք» ոչինչ չի ասում։
«The grade must be between 1 and 10» ասում է, թե ինչ անել։

#%% md
## Գ մաս: Անվերջ ցիկլ

Ամենահաճախ հանդիպող սխալը `while`-ի հետ՝ պայմանը երբեք չի փոխվում։

```python
count = 0

while count < 3:
    print("hello")        # count never changes
```

Այս կոդը կտպի «hello» **անվերջ**։

**Մի՛ գործարկիր այն։** Փոխարենը իմացի՛ր, թե ինչպես կանգնեցնել.

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🛑 Ինչպես կանգնեցնել ցիկլը, որը չի կանգնում</h3>
<p style="color:#900; margin-bottom:0;">
Բջիջի կողքին կտեսնես <b>[*]</b> և այն չի ավարտվում։<br/><br/>
<b>Սեղմի՛ր ■ կոճակը</b> (Interrupt) տետրի վերևի գոտում։<br/><br/>
Եթե չօգնի՝ <b>Restart</b> կոճակը։ Այդ դեպքում բոլոր փոփոխականները կջնջվեն և պետք է
նորից գործարկես բջիջները վերևից։<br/><br/>
<b>Համակարգիչը չի կոտրվել։</b> Այն ուղիղ այն է անում, ինչ գրել ես։
</p>
</div>

#%% md
Անվերջ ցիկլից խուսափելու կանոնը մեկն է.

> Ամեն `while`-ի ներսում պետք է լինի կա՛մ `break`, կա՛մ տող, որը փոխում է պայմանը։
> **Եթե չկա — ցիկլը երբեք չի ավարտվի։**

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Պարտադիր առաջադրանքներ</h3>
<p style="color:#900; margin-bottom:0;">
<b>1.</b> Գրի՛ր ցիկլ, որը հարցնում է միավորներ և կանգնում <code>quit</code> բառից։<br/><br/>
<b>2.</b> Ավելացրո՛ւ ստուգում՝ եթե թիվ չէ, ասա՛ դա և հարցրո՛ւ նորից։<br/><br/>
<b>3.</b> Ցիկլից հետո տպի՛ր, թե քանի միավոր հավաքվեց և ինչ է միջինը։<br/><br/>
<b>4.</b> Ավելացրո՛ւ ստուգում, որ միավորը 1-ից 10 է։
</p>
</div>

#%% code interactive: 9; 6; quit
# Exercise 1, 2, 3 - collect grades until 'quit'

class_grades = []

while True:
    answer = input("Grade (or 'quit'): ")

    if answer == "quit":
        break

    if not answer.isdigit():
        print("That is not a number.")
        continue

    class_grades.append(int(answer))

print(f"Collected {len(class_grades)} grades")

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">🚀 Լրացուցիչ առաջադրանքներ</h3>
<p style="color:#f71; margin-bottom:0;">
<b>5.</b> Ավելացրո՛ւ <code>undo</code> հրաման, որը հանում է վերջին միավորը։<br/><br/>
<b>6.</b> Ավելացրո՛ւ երկրորդ հարց՝ աշակերտի անունը, և հավաքի՛ր <b>երկու</b> ցուցակ
միաժամանակ։<br/><br/>
<b>7.</b> Ցիկլից հետո տպի՛ր ամբողջ մատյանը՝ 11-րդ օրվա ձևով։<br/><br/>
<b>8.</b> Ավելացրո՛ւ <code>count</code> հրաման, որը ասում է, թե քանիսն են մինչ այժմ։<br/><br/>
<b>9.</b> Ի՞նչ է լինում, եթե ուղղակի Enter սեղմես։ Ավելացրո՛ւ ստուգում դրա համար։
</p>
</div>

#%% code interactive: 9; undo; 7; quit
# Extra 5-9 - your space

class_grades = []

while True:
    answer = input("Grade, 'undo' or 'quit': ")

    if answer == "quit":
        break

    if answer == "undo":
        if class_grades:
            removed = class_grades.pop()
            print("removed", removed)
        else:
            print("nothing to remove")
        continue

    if answer.isdigit():
        class_grades.append(int(answer))

print(class_grades)

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🧗 Մարտահրավեր</h3>
<p style="color:#06c; margin-bottom:0;">
<b>10.</b> Գրի՛ր ամբողջական մենյու՝ չորս հրամանով.<br/>
<code>add</code> — ավելացնել միավոր, <code>list</code> — ցույց տալ բոլորը,
<code>average</code> — միջինը, <code>quit</code> — դուրս գալ։<br/><br/>
Սա ուղիղ այն մենյուն է, որ 21-րդ օրը կունենա քո ծրագիրը։ Եթե այսօր գրես, այդ օրը
շատ ավելի հեշտ կլինի։
</p>
</div>

#%% code interactive: add; 9; list; average; quit
# Challenge 10 - a full menu

class_grades = []

while True:
    command = input("Command (add / list / average / quit): ")

    if command == "quit":
        break
    elif command == "add":
        answer = input("Grade: ")
        if answer.isdigit():
            class_grades.append(int(answer))
    elif command == "list":
        print(class_grades)
    elif command == "average":
        if class_grades:
            total = 0
            for grade in class_grades:
                total = total + grade
            print(f"average: {total / len(class_grades):.1f}")
        else:
            print("no grades yet")
    else:
        print("no such command")

#%% md
## Ինչի հասանք

- `while condition:` — կրկնում է, քանի դեռ պայմանը ճիշտ է։
- **`while True:` + `break`** — սա է այն ձևը, որ օգտագործում ենք։
- `continue` — բաց թողնել մնացածը և անցնել հաջորդ պտույտին։
- `.isdigit()` — թի՞վ է տեքստը։ Ստուգում ենք **նախքան** `int()`-ը։
- Անվերջ ցիկլը կանգնեցվում է **■** կոճակով։

## Հաջորդ անգամ

Հաջորդ դասին պատասխանում ենք մի հարցի, որ ամեն օր տալիս են ուսուցչին՝
**«Արամի միավորը քանի՞սն է»**։ Կտեսնենք, որ երկու ցուցակով դա վտանգավոր է — և
կսովորենք ավելի ապահով ձև։

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Գրի՛ր ցիկլ, որը հարցնում է անուններ և կանգնում դատարկ պատասխանից։
