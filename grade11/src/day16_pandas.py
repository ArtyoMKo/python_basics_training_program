#%% md
# Թեմա 16 — Դպրոցի սեփական ֆայլը

### Python 11-րդ դասարանի համար · Թեմա 16-ը 24-ից

Առաջին օրը նկատեցինք մի բան. `school.csv`-ում կա տող, որը `split(",")`-ը
**սխալ է կարդում**։ Թվերը ճիշտ ստացվեցին պատահաբար։

Այսօր ուղղում ենք այն։ Սկզբում՝ ձեռքով։

## ԱՅՍՕՐ:

- **Ա մաս:** ֆայլը՝ ձեռքով, ճիշտ
- **Բ մաս:** մեկ տող
- **Գ մաս:** երկու տարբերակը կողք կողքի

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
NumPy՝ թվերի համար։ Matplotlib՝ նկարների համար։<br/>
Ֆայլը դեռ կարդում ենք այնպես, ինչպես անցած դասընթացում։<br/><br/>
<b>Այսօր երրորդ և վերջին գրադարանը։</b>
</p>
</div>

#%% md
## Ա մաս: Ֆայլը՝ ձեռքով

Ահա այն, ինչ գրել ենք տասնհինգ օր։

#%% code
from pathlib import Path

lines = Path("school.csv").read_text(encoding="utf-8").strip().splitlines()
rows = [line.split(",") for line in lines[1:] if line != ""]

print(len(rows), "rows")

broken = [r for r in rows if len(r) != 5]
print(len(broken), "rows split into the wrong number of pieces")
print(broken[0])

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Ահա այն։</b> Ծանոթագրության մեջ ստորակետ կա, և <code>split(",")</code>-ը
տողը բաժանեց <b>վեց</b> մասի։<br/><br/>
Դասի երկրորդ կեսին կստանանք գործիք, որը այս ամբողջ բջիջը դարձնում է <b>մեկ տող</b>
և ստորակետն ինքն է ճիշտ կարդում։
</p>
</div>

**Ուղղե՛նք ձեռքով։** Քանի որ ծանոթագրությունը վերջին սյունակն է, կարելի է
միացնել ավելցուկը ետ։

#%% code
fixed = []
for row in rows:
    if len(row) > 5:
        row = row[:4] + [",".join(row[4:])]
    fixed.append(row)

broken = [r for r in fixed if r is None or len(r) != 5]
print(len(broken), "still broken")
print(fixed[41])

#%% md
Աշխատեց։ Բայց նկատի՛ր՝ այդ ծանոթագրությունը հիմա պարունակում է **չակերտներ**։

#%% code
print(repr(fixed[41][4]))

#%% md
Ուղղենք նաև դա։ Եվ հետո՝ վերնագիրը, դատարկ տողերը, և թվերը՝ տեքստից։

#%% code
HEADER = lines[0].split(",")
print("columns:", HEADER)

cleaned = []
for row in fixed:
    note = row[4]
    if note.startswith('"') and note.endswith('"'):
        note = note[1:-1]
    cleaned.append({
        "class": row[0],
        "student": row[1],
        "subject": row[2],
        "grade": int(row[3]),
        "note": note,
    })

print(len(cleaned), "rows")
print(cleaned[41])

#%% md
**Քսաներկու տող։** Եվ սա դեռ պարզ ֆայլ է։ Իսկական դպրոցական ֆայլում կլինեն
դատարկ բջիջներ, ամսաթվեր, և մեկ սյունակ, որը երբեմն թիվ է, երբեմն՝ գծիկ։

**Հիմա դու։** Գրի՛ր ֆունկցիա, որը այս ամբողջը անում է, և ստուգի՛ր, որ միջինը
7.0 է։

#%% code
def read_school(path):
    # Everything above, in one function.
    # ...
    return []


# data = read_school("school.csv")
# print(len(data))

#%% md
## Բ մաս: Մեկ տող

#%% code
import pandas as pd

data = pd.read_csv("school.csv")

print(data.shape)
data.head()

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b><code>pd.read_csv("school.csv")</code></b> — մեկ տող։<br/><br/>
Վերնագիրը՝ ճանաչեց։ Դատարկ տողը՝ բաց թողեց։ Չակերտների մեջ եղած ստորակետը՝
ճիշտ կարդաց։ Թվերը՝ թիվ դարձրեց։<br/><br/>
<code>.head()</code> — առաջին հինգ տողը։ <code>.shape</code> — <b>180 տող, 5 սյունակ</b>։
</p>
</div>

#%% md
Ստուգենք հենց այն տողը, որի վրա քսաներկու տող ծախսեցինք։

#%% code
print(data.loc[41, "note"])
print(data.loc[41, "grade"], type(data.loc[41, "grade"]))

#%% md
Ծանոթագրությունը ամբողջական է, առանց չակերտների։ Գնահատականը **թիվ** է, ոչ թե
տեքստ — ոչ մի `int()` չենք գրել։

#%% md
### Սյունակն ու տողը

#%% code
print(data.columns.tolist())
print()
print(data["grade"].head(8).tolist())
print()
print(data["grade"].mean())
print(data["grade"].std())

#%% md
Սյունակը իրեն պահում է **ինչպես NumPy-ի զանգված**։ Նույն `.mean()`, նույն `.std()`։

Դա պատահական չէ՝ pandas-ը ներսում NumPy է օգտագործում։

#%% md
### Երբ սյունակի անունը սխալ է

**Գործարկի՛ր և կարդա՛ սխալը։**

#%% code expected-error: KeyError
print(data["grades"].mean())

#%% md
<div style="border-left: 6px solid #d33; background: #fff5f5; padding: 12px 16px; margin: 12px 0;">
<p style="color:#d33; margin:0;">
🔍 <b><code>KeyError: 'grades'</code></b><br/><br/>
Սյունակը կոչվում է <code>grade</code>, ոչ թե <code>grades</code>։<br/><br/>
Երբ կասկածում ես՝ <code>data.columns.tolist()</code> ցույց է տալիս բոլոր
անունները։ Սա առաջին բանն է, որ պետք է անես նոր ֆայլ բացելիս։
</p>
</div>

#%% md
## Գ մաս: Զտել տողերը

#%% code
# One class
eleven_b = data[data["class"] == "11B"]
print(eleven_b.shape)

# One subject
maths = data[data["subject"] == "Mathematics"]
print(maths["grade"].mean())

# Failing grades
failing = data[data["grade"] < 4]
print(len(failing), "failing grades")

# Two conditions -- same rule as NumPy: & and |, each in brackets
both = data[(data["class"] == "11B") & (data["grade"] < 4)]
print(len(both), "failing grades in 11B")

#%% md
**Նույն շարահյուսությունը, ինչ 13-րդ թեման։** `&`, `|`, և ամեն պայմանը փակագծում։

### Երկու տարբերակը կողք կողքի

| | Ձեռքով | pandas-ով |
|---|---|---|
| Ֆայլը կարդալ | **22 տող** | `pd.read_csv(path)` |
| Վերնագիրը | ձեռքով | ինքն է |
| Դատարկ տողը | `if line != ""` | ինքն է |
| Չակերտների մեջ ստորակետը | **8 տող** | ինքն է |
| Թվերը | `int(...)` ամեն տեղ | ինքն է |
| Մեկ դասարան ընտրել | ցիկլ | `data[data["class"] == "11B"]` |
| Սխալվելու տեղ | **ամենուր** | սյունակի անունը |

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Առաջին հարցերը

Բացի՛ր ֆայլը և տպի՛ր՝ տողերի քանակը, սյունակների անունները, առաջին երեք տողը,
և գնահատականների միջինը։

#%% code
import pandas as pd

# ...

#%% md
### 2. Մեկ դասարանի միջինը

Տպի՛ր երեք դասարանի միջինները՝ երեք առանձին տողով։

**Ստուգի՛ր:** 11A 6.98 · 11B 6.33 · 11C 7.68

#%% code
# ...

#%% md
### 3. Չանցածները

Ընտրի՛ր 4-ից ցածր բոլոր տողերը։ Քանի՞սն են։ Քանի՞ **տարբեր աշակերտ** է դրանց
հետևում։

**Ստուգի՛ր:** 18 գնահատական, 12 աշակերտ։

#%% code
# ...

#%% md
### 4. Մեկ աշակերտի տողերը

Ընտրի՛ր մեկ աշակերտի բոլոր հինգ տողը և տպի՛ր նրա միջինը։

#%% code
# ...

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Նոր սյունակ

`data["passed"] = data["grade"] >= 4` ավելացնում է նոր սյունակ։ Սարքի՛ր այն և
տպի՛ր, թե քանի `True` կա։

#%% code
# ...

#%% md
### 6. Դասավորել

`data.sort_values("grade")` դասավորում է։ Տպի՛ր տասը ամենացածր գնահատականը՝
աշակերտի անունով։

#%% code
# ...

#%% md
### 7. Եզակի արժեքներ

`data["subject"].unique()` տալիս է առարկաների ցուցակը առանց կրկնության։
Օգտագործի՛ր այն և ցիկլով տպի՛ր ամեն առարկայի միջինը։

#%% code
# ...

#%% md
### 8. Ծանոթագրություններով տողերը

Ընտրի՛ր այն տողերը, որոնց ծանոթագրությունը դատարկ չէ։

**Հուշում:** դատարկ բջիջները pandas-ում դառնում են `NaN`, ոչ թե `""`։
Օգտագործի՛ր `data["note"].notna()`։

#%% code
# ...

#%% md
## Մարտահրավեր

#%% md
### 9. Աղյուսակ՝ աշակերտ × առարկա

`data.pivot(index="student", columns="subject", values="grade")` վերածում է
երկար ֆայլը **աղյուսակի**՝ 36 տող, 5 սյունակ։

Սարքի՛ր այն, տպի՛ր `shape`-ը և առաջին հինգ տողը։

#%% code
# ...

#%% md
### 10. Համեմատի՛ր քո ֆունկցիայի հետ

Վերցրո՛ւ Ա մասի `read_school` ֆունկցիան և ստուգի՛ր, որ այն տալիս է **ուղիղ նույն**
միջինը, ինչ pandas-ը։

Ապա markdown-ում գրի՛ր՝ ի՞նչ կլիներ, եթե ֆայլում լիներ նաև ամսաթվի սյունակ
`"12.03.2026"` տեսքով, և մեկ բջիջ դատարկ լիներ։ Որ տարբերակը կկոտրվեր։

#%% code
# ...

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

- `import pandas as pd` — **երրորդ և վերջին գրադարանը**
- `pd.read_csv(path)` — վերնագիր, դատարկ տողեր, չակերտներ, թվեր — **ամեն ինչ ինքը**
- `.shape` `.head()` `.columns.tolist()` — առաջին երեք հարցը նոր ֆայլին
- `data["grade"].mean()` — սյունակը իրեն պահում է ինչպես NumPy զանգված
- `data[data["class"] == "11B"]` — զտել տողերը
- `&` և `|`, ամեն պայմանը փակագծում — **նույնը, ինչ 13-րդ թեման**
- Սխալ սյունակի անուն → `KeyError`

## Ի՞նչ է գալիս հետո

Մինչ այժմ ամեն դասարանի միջինը հաշվում էինք ցիկլով՝ երեք անգամ։

Վաղը կսովորենք **մեկ տող**, որը դա անում է բոլորի համար միանգամից։
