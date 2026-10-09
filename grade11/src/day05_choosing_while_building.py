
#%% md
# Թեմա 5 — Ընտրել կառուցելու ընթացքում

### Python 11-րդ դասարանի համար · Թեմա 5-ը 24-ից

Երեկ ցուցակը սովորեց **զտել** — վերցնել միայն նրանց, ովքեր բավարարում են պայմանին։

Այսօր այն սովորում է **ընտրել**. ամեն տարրի համար՝ մեկը կամ մյուսը։

## ԱՅՍՕՐ:

- **Ա մաս:** `if`/`else` մեկ տողում
- **Բ մաս:** բառարան՝ մեկ տողով
- **Գ մաս:** դասավորել ըստ քո կանոնի

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>[name for name in register if register[name] >= 4]</code> — զտել։<br/>
<b>Զգո՛ւյշ:</b> երեկվա <code>if</code>-ը <b>վերջում</b> էր և <b>դեն էր նետում</b> տարրերը։<br/>
Այսօրվա <code>if</code>-ը <b>սկզբում</b> է և <b>ոչինչ չի նետում</b> — ընտրում է։
</p>
</div>

#%% md
## Ա մաս: `if`/`else` մեկ տողում

Ահա ծանոթ ֆունկցիա։

#%% code
def status(grade, pass_mark=4):
    if grade >= pass_mark:
        return "passed"
    else:
        return "failed"


print(status(9), status(3))

#%% md
Չորս տող՝ մեկ ընտրության համար։ Python-ը թույլ է տալիս գրել նույնը մեկ տողում։

#%% code
def status(grade, pass_mark=4):
    return "passed" if grade >= pass_mark else "failed"


print(status(9), status(3))

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b>Կարդա՛ այն այնպես, ինչպես հայերեն կասեիր.</b><br/><br/>
<code>"passed"</code> &nbsp; <b>եթե</b> &nbsp; <code>grade >= pass_mark</code> &nbsp;
<b>այլապես</b> &nbsp; <code>"failed"</code><br/><br/>
Պատասխանը <b>առջևում</b> է, պայմանը՝ մեջտեղում։ Սա միակ տեղն է Python-ում, որտեղ
<code>if</code>-ը արժեք է վերադարձնում, ոչ թե որոշում է՝ ինչ գործարկել։
</p>
</div>

#%% md
Իսկ հիմա՝ միասին երեկվա ցուցակի հետ։

#%% code
register = {
    "Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3, "Mariam": 8, "Tigran": 7,
    "Lilit": 5, "Gor": 4, "Anahit": 9, "Hayk": 2, "Sona": 8, "Vahe": 6,
}
PASS_MARK = 4

marks = [status(register[name]) for name in register]
print(marks)

lines = [f"{name}: {status(register[name])}" for name in register]
for line in lines:
    print(line)

#%% md
**Ուշադի՛ր եղիր տարբերությանը։**

| | Որտեղ է `if`-ը | Ի՞նչ է անում |
|---|---|---|
| `[n for n in reg if reg[n] >= 4]` | **վերջում** | **զտում է** — չանցածները ցուցակում չեն |
| `[status(reg[n]) for n in reg]` | **ձախում**, `else`-ով | **ընտրում է** — բոլորը ցուցակում են |

#%% code
# Filtering: 9 names out of 12
print(len([name for name in register if register[name] >= PASS_MARK]))

# Choosing: all 12, each one labelled
print(len(["ok" if register[name] >= PASS_MARK else "-" for name in register]))

#%% md
## Բ մաս: Բառարան՝ մեկ տողով

Նույն ձևը աշխատում է բառարանի համար։ Տարբերությունը՝ **ձևավոր փակագծեր** և
**երկու կետ**։

#%% code
# From a dictionary to a dictionary
rounded = {name: register[name] for name in register}
print(rounded)

# The value can be anything you build
labels = {name: status(register[name]) for name in register}
print(labels)

#%% md
Եվ հիմա՝ իսկական օրինակ։ Դպրոցի ֆայլից ամեն աշակերտի համար՝ ցուցակ
գնահատականներով։

#%% code
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

students = {row[1] for row in rows}
grades_of = {name: [int(row[3]) for row in rows if row[1] == name] for name in students}

print(len(grades_of), "students")
print(grades_of["Ani Hakobyan"])

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Նկատի՛ր ձևավոր փակագծերը երկու տեղում։</b><br/>
<code>{row[1] for row in rows}</code> — երկու կետ չկա → սա <b>set</b> է,
կրկնություններ չկան։<br/>
<code>{name: ... for name in students}</code> — երկու կետ կա → սա <b>բառարան</b> է։
</p>
</div>

#%% md
## Բ մաս, շարունակություն: Երբ բանալին կարող է չլինել

Բառարանից արժեք վերցնելը քառակուսի փակագծերով **սխալ է տալիս**, եթե բանալին չկա։

#%% code
grades = {"Mathematics": 8, "Physics": 6}

try:
    print(grades["History"])
except KeyError as problem:
    print("KeyError:", problem)

#%% md
Երբեմն դա հենց այն է, ինչ պետք է՝ բացակայող բանալին սխալ է։

Բայց հաճախ ուզում ես ասել՝ «**վերցրու, իսկ եթե չկա՝ տուր սա**»։ Դրա համար կա `.get()`։

#%% code
print(grades.get("History"))
print(grades.get("History", 0))
print(grades.get("Mathematics", 0))

# Useful in a comprehension, where a KeyError would stop everything:
SUBJECTS = ["Mathematics", "Physics", "Armenian"]
marks = [grades.get(subject, 0) for subject in SUBJECTS]
print(marks)

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b><code>grades.get(key)</code></b> — եթե բանալին չկա, վերադարձնում է
<code>None</code>, ոչ թե սխալ։<br/>
<b><code>grades.get(key, 0)</code></b> — եթե չկա, վերադարձնում է <code>0</code>։<br/><br/>
<b>Ե՞րբ որը։</b> Քառակուսի փակագիծ, երբ բանալին <b>պետք է</b> լինի և բացակայությունը
սխալ է։ <code>.get()</code>, երբ բացակայությունը նորմալ է։
</p>
</div>

#%% md
## Գ մաս: Դասավորել ըստ քո կանոնի

Անցած դասընթացում `sorted()`-ը դասավորում էր ըստ իրերի բնական կարգի։

#%% code
names = ["Davit", "Ani", "Nare", "Aram"]
print(sorted(names))

grades = [9, 3, 10, 6]
print(sorted(grades))

#%% md
Իսկ եթե պետք է դասավորել աշակերտներին **ըստ գնահատականի**, ոչ թե ըստ անվան։

`sorted()`-ը ունի պարամետր `key` — այնտեղ գրվում է **ֆունկցիա**, որը ամեն տարրից
հանում է այն, ինչով դասավորելու ենք։

#%% code
def grade_of(name):
    return register[name]


by_grade = sorted(register, key=grade_of)
print(by_grade)

by_grade_down = sorted(register, key=grade_of, reverse=True)
print(by_grade_down)

#%% md
Աշխատում է։ Բայց `grade_of`-ը **միայն այստեղ է պետք** և երբեք այլուր չի կանչվի։

Այդպիսի փոքրիկ ֆունկցիայի համար Python-ը ունի կարճ ձև՝ **`lambda`**։

#%% code
by_grade = sorted(register, key=lambda name: register[name])
print(by_grade)

top_three = sorted(register, key=lambda name: register[name], reverse=True)[:3]
print("top three:", top_three)

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<p style="color:#06c; margin:0;">
<b><code>lambda name: register[name]</code></b> նշանակում է ուղիղ նույնը, ինչ<br/>
<code>def grade_of(name): return register[name]</code> — պարզապես անուն չունի։<br/><br/>
<b>Այս դասընթացում <code>lambda</code>-ն կօգտագործենք միայն այստեղ՝
<code>sorted()</code>-ի <code>key</code>-ի մեջ։</b> Ուրիշ տեղ պետք չէ, և աշակերտների
ծրագրում էլ հենց այսպես է հանդիպում։
</p>
</div>

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Անցած / չանցած նշան

Կառուցի՛ր ցուցակ, որտեղ ամեն աշակերտի դիմաց `"+"` է, եթե անցել է, և `"-"`՝ եթե ոչ։
Մեկ տողով։

#%% code
marks = []
print(marks)

#%% md
### 2. Կլորացնել կամ թողնել

Կառուցի՛ր ցուցակ, որտեղ 5-ից ցածր գնահատականները դառնում են `0`, իսկ մնացածը
մնում են իրենց տեղում։

#%% code
adjusted = []
print(adjusted)

#%% md
### 3. Բառարան՝ անուն → բառ

Կառուցի՛ր բառարան, որտեղ ամեն անվան դիմաց գրված է `"excellent"` (9–10),
`"good"` (7–8) կամ `"ok"` (մնացածը)։

**Հուշում:** մեկ տողում երկու `if`/`else` կարելի է դնել իրար մեջ, բայց եթե
կարդալը դժվարանում է — գրի՛ր սովորական ֆունկցիա և կանչի՛ր այն։

#%% code
words = {}
print(words)

#%% md
### 4. Դասավորել ըստ երկարության

Դասավորի՛ր աշակերտների անունները **ըստ անվան երկարության**, ամենակարճից սկսած։

#%% code
by_length = []
print(by_length)

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Լավագույն հինգը

Տպի՛ր լավագույն հինգ աշակերտի անունն ու գնահատականը՝ հաշվետվության տողերով։

#%% code
# sorted(..., key=..., reverse=True) then [:5]
top_five = []
for name in top_five:
    print(f"{name}: {register[name]}")

#%% md
### 6. Բառարանը՝ շրջված

Կառուցի՛ր բառարան, որտեղ բանալին գնահատականն է, իսկ արժեքը՝ այդ գնահատականն
ստացած աշակերտների ցուցակը։

#%% code
by_grade = {}
for grade in sorted(by_grade):
    print(grade, by_grade[grade])

#%% md
### 7. Ամեն աշակերտի միջինը

Վերևի `grades_of` բառարանից կառուցի՛ր նոր բառարան՝ անուն → միջին, մեկ տողով։
Ապա տպի՛ր ամենաբարձր միջինով երեք աշակերտին։

#%% code
average_of = {}
# ...
print(len(average_of))

#%% md
### 8. Դասավորել երկու բանով

Դասավորի՛ր աշակերտներին ըստ գնահատականի՝ նվազման կարգով, իսկ նույն գնահատական
ունեցողներին՝ ըստ անվան այբբենական կարգով։

**Հուշում:** `key`-ն կարող է վերադարձնել tuple։ Երեկ սովորեցինք, որ tuple-ները
համեմատվում են՝ սկզբում առաջին տարրը, հետո երկրորդը։

#%% code
ordered = []
print(ordered)

#%% md
## Մարտահրավեր

#%% md
### 9. Դպրոցի ամփոփ աղյուսակը

`grades_of`-ից կառուցի՛ր տող ամեն աշակերտի համար՝ անուն, միջին, և քանի առարկայից
է չանցել։ Ապա դասավորի՛ր ըստ չանցած առարկաների թվի՝ նվազման կարգով, և տպի՛ր
առաջին տասը։

#%% code
# One comprehension builds the list of tuples.
# One sorted() with a lambda orders it.
summary = []
for row in summary[:10]:
    print(row)

#%% md
### 10. Ե՞րբ չօգտագործել

Ահա մեկ տող, որը **աշխատում է, բայց վատ է գրված**։

Վերագրի՛ր այն սովորական ցիկլով, և markdown բջիջում գրի՛ր, թե ինչու է ցիկլն
այստեղ ավելի լավ։

#%% code
result = [f"{n}: {'ok' if register[n] >= 4 else ('low' if register[n] >= 2 else 'bad')}"
          for n in register if len(n) > 3]
print(result)

#%% md
## Ինչի հասանք

- `"a" if condition else "b"` — ընտրություն **մեկ տողում**, արժեք է վերադարձնում
- `if`-ը **ձախում** = ընտրում է · `if`-ը **վերջում** = զտում է
- `{name: value for ... }` — **բառարան** մեկ տողով
- `{x for ... }` — առանց երկու կետի՝ **set**, առանց կրկնությունների
- `grades.get(key, default)` — բանալին չկա՞, վերադարձրու կանխադրվածը, ոչ թե սխալ
- `sorted(items, key=...)` — դասավորել **ըստ քո կանոնի**
- `lambda x: ...` — անանուն ֆունկցիա։ **Միայն `key`-ի մեջ, այս դասընթացում**

## Ի՞նչ է գալիս հետո

Մեր աշակերտը մինչ այժմ մեկ թիվ էր։ Վաղը նա դառնում է **անուն, դասարան, հինգ
գնահատական, հաճախումներ և ծանոթագրություն** — և բառարանը սկսում է չդիմանալ։

Նույն դասին կստանանք այն, ինչով աշակերտը նկարագրվում է **մեկ անգամ**։
