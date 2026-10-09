#%% md
# Թեմա 13 — Ամբողջ զանգվածը՝ միանգամից

### Python 11-րդ դասարանի համար · Թեմա 13-ը 24-ից

Երեկ զանգվածը տվեց մեզ չորս թիվ։ Այսօր այն սովորում է **փոխվել ամբողջությամբ**՝
առանց ոչ մի ցիկլի։

## ԱՅՍՕՐ:

- **Ա մաս:** գործողություն ամբողջ զանգվածի վրա
- **Բ մաս:** ընտրել պայմանով
- **Գ մաս:** երկու չափում՝ աղյուսակ

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>import numpy as np</code> · <code>np.array(list)</code> ·
<code>.mean() .max() .min() .std()</code><br/><br/>
<b>Այսօր զանգվածը կաշխատի առանց ցիկլի։</b>
</p>
</div>

#%% md
## Ա մաս: Մեկ գործողություն, բոլոր թվերի վրա

#%% code
import numpy as np
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

grades = np.array([int(row[3]) for row in rows])
print(grades[:12])

#%% md
Տնօրենը որոշել է բոլորին **մեկ միավոր ավելացնել**։ Ահա այն, ինչ գիտենք անել։

#%% code
raised = []
for grade in grades:
    raised.append(grade + 1)

print(raised[:12])

#%% md
Իսկ ահա նույնը զանգվածով։

#%% code
raised = grades + 1
print(raised[:12])

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b><code>grades + 1</code></b> — գործողությունը կիրառվում է <b>ամեն թվի վրա</b>։<br/><br/>
Սովորական ցուցակի դեպքում սա սխալ կտար։ Զանգվածը հենց դրա համար է։
</p>
</div>

#%% code
print(grades * 10)
print(grades / 10)
print(grades ** 2)
print(np.round(grades / 10, 2))

#%% md
Եվ երկու զանգվածի միջև՝ տարր առ տարր։

#%% code
maths = np.array([int(r[3]) for r in rows if r[2] == "Mathematics"])
physics = np.array([int(r[3]) for r in rows if r[2] == "Physics"])

print("maths  ", maths[:8])
print("physics", physics[:8])
print("gap    ", (maths - physics)[:8])
print(f"average gap: {(maths - physics).mean():.2f}")

#%% md
## Բ մաս: Ընտրել պայմանով

Համեմատությունն էլ է կիրառվում ամեն թվի վրա — և տալիս է `True`/`False` զանգված։

#%% code
failing = grades < 4

print(failing[:12])
print("how many:", failing.sum())

#%% md
`True`-ն գումարելիս 1 է, `False`-ը՝ 0։ Այդ պատճառով `.sum()`-ը **հաշվում է**։

Եվ հիմա՝ ամենակարևորը։ Այդ `True`/`False` զանգվածը կարելի է դնել **փակագծերի մեջ**։

#%% code
print(grades[failing])
print(grades[grades < 4])
print(grades[grades == 10])

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b><code>grades[grades &lt; 4]</code></b> — «տուր ինձ այն թվերը, որոնց համար
պայմանը ճիշտ է»։<br/><br/>
Կարդա՛ այն ներսից դուրս՝ <code>grades &lt; 4</code> սարքում է <code>True</code>/<code>False</code>
զանգված, իսկ արտաքին փակագծերը դրանով <b>ընտրում են</b>։<br/><br/>
Սա ուղիղ նույնն է, ինչ 4-րդ թեմայի <code>[g for g in grades if g &lt; 4]</code>-ը —
պարզապես ավելի կարճ, և շատ ավելի արագ մեծ տվյալների վրա։
</p>
</div>

#%% md
Երկու պայման միասին՝ `&` («և») և `|` («կամ»)։ **Ամեն պայմանը իր փակագծերում։**

#%% code
middle = grades[(grades >= 5) & (grades <= 7)]
print(len(middle), "grades between 5 and 7")

edges = grades[(grades <= 2) | (grades >= 9)]
print(len(edges), "grades at the edges")

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Այստեղ <code>and</code> և <code>or</code> <b>չեն աշխատում</b>։</b> Զանգվածների
համար գրվում է <code>&</code> և <code>|</code>, և ամեն պայմանը <b>պարտադիր</b>
փակագծերի մեջ է։<br/><br/>
Սա ամենահաճախ հանդիպող սխալն է այս թեմայում։
</p>
</div>

#%% md
## Գ մաս: Աղյուսակ՝ երկու չափումով

Մինչ այժմ զանգվածը մեկ շարք էր։ Այն կարող է լինել նաև **աղյուսակ**։

#%% code
table = np.array([
    [7, 6, 8, 9, 8],
    [5, 3, 6, 5, 7],
    [10, 9, 10, 9, 10],
    [3, 2, 4, 3, 5],
])

print(table)
print("shape:", table.shape)

#%% md
`shape` ասում է՝ **4 տող, 5 սյունակ**։ Տողերը աշակերտներն են, սյունակները՝ առարկաները։

#%% code
# One student: a row
print("row 0:", table[0])

# One subject: a column
print("column 1:", table[:, 1])

# One number
print("row 0, column 1:", table[0, 1])

#%% md
Եվ ամենաօգտակարը՝ միջինը **ըստ ուղղության**։

#%% code
print("per student:", np.round(table.mean(axis=1), 2))
print("per subject:", np.round(table.mean(axis=0), 2))
print("everything: ", round(table.mean(), 2))

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<p style="color:#06c; margin:0;">
<b><code>axis=1</code></b> — անցնում է <b>տողի երկայնքով</b> → մեկ թիվ ամեն աշակերտի։<br/>
<b><code>axis=0</code></b> — անցնում է <b>սյունակի երկայնքով</b> → մեկ թիվ ամեն առարկայի։<br/><br/>
Հիշելու ձև՝ <code>axis</code>-ը ասում է, թե <b>որ չափումն է անհետանում</b>։
</p>
</div>

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Տոկոսային սանդղակ

Դպրոցը անցնում է 100-բալանոց համակարգի։ Վերածի՛ր բոլոր գնահատականները՝
բազմապատկելով 10-ով, և տպի՛ր առաջին տասը և նոր միջինը։

#%% code
# ...

#%% md
### 2. Քանի՞ գերազանց

Հաշվի՛ր, թե քանի գնահատական է 9 կամ 10, **առանց ցիկլի**։

#%% code
# ...

#%% md
### 3. Միայն անցածները

Ընտրի՛ր 4-ից բարձր բոլոր գնահատականները և տպի՛ր դրանց քանակը և միջինը։
Համեմատի՛ր ամբողջ դպրոցի միջինի հետ։

#%% code
# ...

#%% md
### 4. Երկու պայման

Ընտրի՛ր Mathematics-ի այն գնահատականները, որոնք **4-ից բարձր են և 8-ից ցածր**։

#%% code
# ...

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Դպրոցի աղյուսակը

Կառուցի՛ր 36×5 զանգված՝ տողերը աշակերտներն են, սյունակները՝ առարկաները։
Ստուգի՛ր `shape`-ը։

**Հուշում:** սկզբում սարքի՛ր ցուցակների ցուցակ, հետո՝ `np.array(...)`։

#%% code
# ...

#%% md
### 6. Ամեն աշակերտի միջինը

Վերևի աղյուսակից հաշվի՛ր ամեն աշակերտի միջինը մեկ տողով և տպի՛ր ամենաբարձր հինգը։

#%% code
# ...

#%% md
### 7. Ամեն առարկայի միջինը

Նույն աղյուսակից՝ առարկաների միջինները։

**Ստուգի՛ր:** Informatics 7.56, Physics 6.28։

#%% code
# ...

#%% md
### 8. Փոխարինել տեղում

`table[table < 4] = 4` փոխարինում է բոլոր ցածր գնահատականները չորսով։
Փորձի՛ր այն պատճենի վրա (`table.copy()`) և համեմատի՛ր միջինները։

#%% code
# ...

#%% md
## Մարտահրավեր

#%% md
### 9. Դասարանների աղյուսակը

Կառուցի՛ր 3×5 զանգված՝ տողերը դասարաններն են, սյունակները՝ առարկաները, իսկ
բջիջներում՝ միջինները։ Ապա գտի՛ր, թե **որ դասարանն է ամենաուժեղը որ առարկայից**։

#%% code
# ...

#%% md
### 10. Ցիկլն ընդդեմ զանգվածի

Սարքի՛ր 2 միլիոն պատահական թվից զանգված՝ `np.random.randint(1, 11, 2000000)`։

Հաշվի՛ր, թե քանիսն են 4-ից ցածր՝ **երկու ձևով**, և չափի՛ր ժամանակը։

#%% code
import time

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

- `grades + 1` — գործողությունը **ամեն թվի վրա**, առանց ցիկլի
- `grades < 4` — համեմատությունը տալիս է `True`/`False` **զանգված**
- `.sum()` այդ զանգվածի վրա — **հաշվում է**
- `grades[grades < 4]` — **ընտրում է** պայմանով
- `&` և `|`, ոչ թե `and` և `or`, և **ամեն պայմանը փակագծում**
- `shape`, `axis=0` սյունակներով, `axis=1` տողերով

## Ի՞նչ է գալիս հետո

Թվերը պատրաստ են։ Բայց մանկավարժական խորհրդին դրանք պետք չէ **կարդալ** —
պետք է **ցույց տալ**։

Վաղը կսարքենք գծապատկեր՝ սկզբում աստղանիշերով, հետո՝ իսկականը։
