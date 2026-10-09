#%% md
# Թեմա 15 — Չորս գծապատկեր, որ դպրոցը խնդրում է

### Python 11-րդ դասարանի համար · Թեմա 15-ը 24-ից

Նախորդ թեմայում սովորեցինք սյունակային գծապատկերը։ Այսօր՝ մնացած երեքը, որոնք իսկապես
պետք են գալիս, և այն, ինչ նրանք **ցույց են տալիս**։

## ԱՅՍՕՐ:

- **Ա մաս:** բաշխվածությունը — հիստոգրամ
- **Բ մաս:** գիծ
- **Գ մաս:** երեք դասարանը՝ կողք կողքի

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>plt.bar</code> · <code>plt.ylim</code> · <code>plt.title</code> ·
<code>plt.savefig</code> · <code>plt.close</code><br/><br/>
<b>Այսօր նոր գրադարան չկա — միայն երեք նոր տեսակի գծապատկեր։</b>
</p>
</div>

#%% code
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

SUBJECTS = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]
CLASSES = ["11A", "11B", "11C"]
grades = np.array([int(r[3]) for r in rows])

print(len(grades), "grades, average", round(grades.mean(), 2))

#%% md
## Ա մաս: Բաշխվածությունը

Միջինը **7.0** է։ Բայց դա չի ասում, թե **ինչպես են բաշխված** գնահատականները։

Երկու դպրոց կարող են ունենալ նույն միջինը՝ մեկում բոլորը 7 են, մյուսում՝ կեսը 10,
կեսը՝ 4։

Հիստոգրամը ցույց է տալիս հենց դա։

#%% code
plt.figure(figsize=(7, 4))
plt.hist(grades, bins=range(1, 12), edgecolor="white")
plt.xlabel("Grade")
plt.ylabel("How many")
plt.title("All grades in the school")
plt.tight_layout()
plt.savefig("distribution.png", dpi=150)
plt.close()

print("saved distribution.png")

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b><code>plt.hist(numbers, bins=...)</code></b> — ինքն է հաշվում, թե ամեն
արժեքից քանիսն են։ Դու ոչինչ չես հաշվում։<br/><br/>
<code>bins=range(1, 12)</code> — սահմանները՝ 1-ից 11։ Տասնմեկը պետք է, որպեսզի
տասը <b>ներսում մնա</b>։
</p>
</div>

#%% md
Եվ մեկ դասարանի համար՝ նույնը։

#%% code
eleven_b = np.array([int(r[3]) for r in rows if r[0] == "11B"])

plt.figure(figsize=(7, 4))
plt.hist(eleven_b, bins=range(1, 12), edgecolor="white", color="#c74")
plt.xlabel("Grade")
plt.ylabel("How many")
plt.title(f"11B — average {eleven_b.mean():.2f}")
plt.tight_layout()
plt.savefig("class_11b.png", dpi=150)
plt.close()

print("11B average:", round(eleven_b.mean(), 2))
print("11B spread: ", round(eleven_b.std(), 3))

#%% md
## Բ մաս: Գիծ

Գիծը օգտագործվում է, երբ կետերի **կարգը նշանակություն ունի** — օրինակ,
քանի գնահատական կա ամեն մակարդակում, 1-ից 10։

#%% code
levels = list(range(1, 11))
counts = [int((grades == level).sum()) for level in levels]

for level in levels:
    print(f"{level:>3}  {counts[level - 1]:>3}")

#%% code
plt.figure(figsize=(7, 4))
plt.plot(levels, counts, marker="o")
plt.xlabel("Grade")
plt.ylabel("How many")
plt.title("Grade distribution, whole school")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("levels.png", dpi=150)
plt.close()

print("saved levels.png")

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Գի՞ծ, թե՞ սյուներ։</b><br/>
Սյուներ — երբ կատեգորիաներ են (առարկաներ, դասարաններ)։ Նրանց կարգը կարելի է փոխել։<br/>
Գիծ — երբ կարգը <b>բնական է</b> (1, 2, 3 … 10, կամ ամիսները)։<br/><br/>
Առարկաները գծով նկարելը սխալ կլիներ՝ «Mathematics-ից Physics» անցում չկա։
</p>
</div>

#%% md
## Գ մաս: Երեք դասարանը, կողք կողքի

Ամենաօգտակար գծապատկերը՝ երեք դասարանը, հինգ առարկայով, մեկ նկարում։

Դրա համար սյուները պետք է **տեղաշարժվեն** իրար կողքի։

#%% code
width = 0.25
positions = np.arange(len(SUBJECTS))

plt.figure(figsize=(9, 4))

for index in range(len(CLASSES)):
    class_name = CLASSES[index]
    averages = [np.array([int(r[3]) for r in rows
                          if r[0] == class_name and r[2] == s]).mean()
                for s in SUBJECTS]
    plt.bar(positions + index * width, averages, width, label=class_name)

plt.xticks(positions + width, SUBJECTS, rotation=20)
plt.ylim(0, 10)
plt.ylabel("Average grade")
plt.title("Three classes, five subjects")
plt.legend()
plt.tight_layout()
plt.savefig("three_classes.png", dpi=150)
plt.close()

print("saved three_classes.png")

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<p style="color:#06c; margin:0;">
<b>Երեք նոր բան այստեղ.</b><br/>
<code>np.arange(5)</code> — 0, 1, 2, 3, 4 — սյուների հիմնական տեղերը։<br/>
<code>positions + index * width</code> — ամեն դասարանը տեղաշարժվում է աջ։<br/>
<code>plt.xticks(...)</code> — անունները դնում է մեջտեղում, <code>rotation=20</code>-ով՝ թեք։<br/>
<code>plt.legend()</code> — բացատրում է, թե որ գույնը որ դասարանն է։ Աշխատում է,
որովհետև ամեն <code>plt.bar</code>-ին տվել ենք <code>label=</code>։
</p>
</div>

#%% md
### Չորս գծապատկերը՝ ե՞րբ որը

| Գծապատկեր | Ցույց է տալիս | Երբ |
|---|---|---|
| `plt.bar` | համեմատություն | կատեգորիաներ՝ առարկա, դասարան |
| `plt.hist` | **բաշխվածություն** | մեկ շարք թվեր — «ինչպե՞ս են ցրված» |
| `plt.plot` | ընթացք | բնական կարգ — 1…10, ամիսներ |
| խմբավորված `bar` | **երկու չափում** | կատեգորիա × կատեգորիա |

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Երեք դասարանի հիստոգրամները

Սարքի՛ր երեք հիստոգրամ՝ մեկը ամեն դասարանի համար, և պահպանի՛ր դրանք։
Վերնագրում գրի՛ր դասարանի անունը և միջինը։

#%% code
# ...

#%% md
### 2. Չանցածների գիծը

Հաշվի՛ր, թե ամեն առարկայից քանի գնահատական է 4-ից ցածր, և սարքի՛ր **սյունակային**
գծապատկեր։ Ինչո՞ւ սյուներ, ոչ թե գիծ։

#%% code
# ...

#%% md
### 3. Կարմիր գիծը

Ավելացրո՛ւ առարկաների գծապատկերին հորիզոնական կարմիր գիծ դպրոցի միջինի վրա՝
`plt.axhline(y=..., color="red", linestyle="--")`։

#%% code
# ...

#%% md
### 4. Չորսը՝ մեկ նկարում

Օգտագործի՛ր `plt.subplot(2, 2, n)` և դի՛ր չորս գծապատկերը մեկ նկարում։
Պահպանի՛ր այն որպես `term_report.png`։

#%% code
# ...

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Հաճախումների գծապատկերը

Սարքի՛ր հաճախումների թվեր՝ `85 + (index % 15)` բանաձևով 36 աշակերտի համար, և
նկարի՛ր դրանց հիստոգրամը։

#%% code
# ...

#%% md
### 6. Ամենաուժեղ և ամենաթույլ առարկան

Նկարի՛ր առարկաների գծապատկերը այնպես, որ ամենաբարձրը կանաչ լինի, ամենացածրը՝
կարմիր, մնացածը՝ մոխրագույն։

#%% code
# ...

#%% md
### 7. Երկու դասարան, մեկ հիստոգրամ

`plt.hist` կարող է ստանալ **երկու զանգված** և նկարել դրանք կողք կողքի՝
`plt.hist([a, b], bins=..., label=["11A", "11B"])`։ Փորձի՛ր։

#%% code
# ...

#%% md
### 8. Կարգավորված գծապատկեր

Սարքի՛ր առարկաների գծապատկերը **դասավորված ըստ միջինի**, ամենաբարձրից սկսած։

#%% code
# ...

#%% md
## Մարտահրավեր

#%% md
### 9. Ամեն աշակերտի պատկերը

Սարքի՛ր հորիզոնական գծապատկեր 36 աշակերտի միջիններով, դասավորված, գունավորված
ըստ դասարանի։ Նկարի բարձրությունը պետք է բավարարի, որ բոլոր անունները երևան։

#%% code
# ...

#%% md
### 10. Հայերեն անունները՝ նորից

14-րդ թեմայի 9-րդ Մարտահրավերը շարունակելով՝ սարքի՛ր գծապատկեր, որտեղ դասարանների
անունները հայերեն են՝ `11Ա`, `11Բ`, `11Գ`։

Գրի՛ր դրանք **markdown բջիջում** և պատճենի՛ր կոդի մեջ ինքդ։ Ապա գտի՛ր այն
տառատեսակը, որն աշխատում է քո համակարգչում։

**Այս մեկը պետք կգա 23-րդ թեմայում։** Գրի՛ր պատասխանը՝ տառատեսակի անունը, որ չմոռանաս։

#%% code
# Paste the Armenian class names here yourself, then set the font.
# plt.rcParams["font.family"] = "..."
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

- `plt.hist(numbers, bins=...)` — **բաշխվածություն**, ինքն է հաշվում
- `plt.plot(x, y, marker="o")` — գիծ, երբ կարգը **բնական** է
- Խմբավորված սյուներ՝ `positions + index * width` և `plt.xticks`
- `plt.legend()` աշխատում է, եթե ամեն շարքին տվել ես `label=`
- `plt.subplot(2, 2, n)` — չորս գծապատկեր մեկ նկարում
- **Միջինը մեկ թիվ է։ Բաշխվածությունը՝ պատմություն**

## Ի՞նչ է գալիս հետո

Մինչ այժմ ֆայլը կարդում էինք `split(",")`-ով, և 1-ին օրվանից գիտենք, որ մեկ
տող սխալ է կարդացվում։

Հաջորդ նիստում կուղղենք այն՝ ձեռքով։ Եվ նույն նիստում կստանանք մի գործիք, որը այդ ամբողջ
կոդը դարձնում է **մեկ տող**։
