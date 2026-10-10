#%% md
# Թեմա 14 — Ցույց տալ տնօրենին

### Python 11-րդ դասարանի համար · Թեմա 14-ը 24-ից

Թվերը պատրաստ են. հինգ առարկա, հինգ միջին։ Բայց մանկավարժական խորհրդին
**ոչ ոք թվեր չի կարդում**։ Պետք է նկար։

## ԱՅՍՕՐ:

- **Ա մաս:** գծապատկեր՝ աստղանիշերով
- **Բ մաս:** իսկական գծապատկեր
- **Գ մաս:** պահպանել ֆայլում

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>grades[grades &lt; 4]</code> · <code>axis=0</code> և <code>axis=1</code> ·
միջիններ մեկ տողով<br/><br/>
<b>Այսօր թվերը դառնում են նկար։</b>
</p>
</div>

#%% md
## Ա մաս: Աստղանիշերով

Ահա հինգ առարկայի միջինները։

#%% code
import numpy as np
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

SUBJECTS = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]
averages = [np.array([int(r[3]) for r in rows if r[2] == s]).mean() for s in SUBJECTS]

for i in range(len(SUBJECTS)):
    print(f"{SUBJECTS[i]:<14} {averages[i]:.2f}")

#%% md
Այն, ինչ գիտենք անել՝ նկարել աստղանիշերով։

<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Այս ձևն աշխատում է, բայց հաշվետվության մեջ չի գնա։</b> Դասի երկրորդ կեսին
կսովորենք գործիք, որը նույն տվյալներից սարքում է <b>իսկական գծապատկեր</b> և
պահպանում այն որպես նկար։
</p>
</div>

**Գործարկի՛ր։**

#%% code
for i in range(len(SUBJECTS)):
    bar = "*" * int(averages[i] * 5)
    print(f"{SUBJECTS[i]:<14} {bar} {averages[i]:.2f}")

#%% md
Տնօրենը ասում է՝ «սանդղակը պետք է 0-ից 10 լինի, որ տարբերությունը երևա»։

Հիմա պետք է **ձեռքով հաշվել մասշտաբը**։

#%% code
WIDTH = 40
SCALE = 10

for i in range(len(SUBJECTS)):
    length = int(averages[i] / SCALE * WIDTH)
    bar = "#" * length + "." * (WIDTH - length)
    print(f"{SUBJECTS[i]:<14} |{bar}| {averages[i]:.2f}")

#%% md
**Հիմա դու։** Սարքի՛ր նույնը երեք դասարանի համար։ Ապա փորձի՛ր ավելացնել
առանցքի նշումներ՝ 0, 5, 10։

#%% code
CLASSES = ["11A", "11B", "11C"]
class_averages = [np.array([int(r[3]) for r in rows if r[0] == c]).mean()
                  for c in CLASSES]

# Same bars, for the three classes.
# ...

# Then a scale line under them: 0 at the left, 10 at the right.
# ...

#%% md
## Բ մաս: Իսկական գծապատկեր

#%% code
import matplotlib.pyplot as plt

plt.bar(SUBJECTS, averages)
plt.show()

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b><code>import matplotlib.pyplot as plt</code></b> — երկարությունից մի վախեցիր։
<code>matplotlib</code>-ը գրադարանն է, <code>pyplot</code>-ը՝ նրա այն մասը, որ
գծապատկեր է սարքում։<br/><br/>
<b><code>plt.bar(names, numbers)</code></b> — անունները ներքևում, թվերը՝ բարձրությունը։<br/>
<b><code>plt.show()</code></b> — ցույց տուր։
</p>
</div>

#%% md
Մեկ տող՝ նկարի փոխարեն։ Հիմա ավելացնենք այն, ինչ տնօրենն ուզում էր։

#%% code
plt.bar(SUBJECTS, averages)
plt.ylim(0, 10)
plt.ylabel("Average grade")
plt.title("Subject averages, term 1")
plt.show()

#%% md
`ylim(0, 10)` — ուղիղ այն, ինչ ձեռքով հաշվում էինք։ Մեկ տող։

#%% md
### Երբ թվերն ու անունները չեն համընկնում

**Գործարկի՛ր և կարդա՛ սխալը։**

#%% code expected-error: ValueError
plt.bar(SUBJECTS, averages[:3])
plt.show()

#%% md
<div style="border-left: 6px solid #d33; background: #fff5f5; padding: 12px 16px; margin: 12px 0;">
<p style="color:#d33; margin:0;">
🔍 <b><code>ValueError: shape mismatch</code></b><br/><br/>
Հինգ անուն, երեք թիվ։ Նույն տրամաբանությունը, ինչ 12-րդ թեմայի
<code>shapes (5,) (3,)</code>-ը։<br/><br/>
<b>Այս սխալը կհանդիպի քեզ հաճախ</b>, երբ զտում ես տվյալները մի տեղում և
մոռանում մյուսում։
</p>
</div>

#%% md
## Գ մաս: Պահպանել ֆայլում

Հաշվետվության մեջ դնելու համար նկարը պետք է ֆայլ դառնա։

#%% code
plt.figure(figsize=(8, 4))
plt.bar(SUBJECTS, averages, color="#4a7")
plt.ylim(0, 10)
plt.ylabel("Average grade")
plt.title("Subject averages, term 1")
plt.tight_layout()
plt.savefig("subject_averages.png", dpi=150)
plt.close()

print("saved")

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<p style="color:#06c; margin:0;">
<b>Չորս տող, որոնք միշտ նույնն են։</b><br/>
<code>plt.figure(figsize=(8, 4))</code> — որքան մեծ լինի նկարը, դյույմերով։<br/>
<code>plt.tight_layout()</code> — որ անունները չկտրվեն։<br/>
<code>plt.savefig("name.png", dpi=150)</code> — պահպանիր։<br/>
<code>plt.close()</code> — փակիր, որ հաջորդը մաքուր թղթի վրա սկսվի։<br/><br/>
<b>Բացի՛ր ֆայլը</b> — այն քո թղթապանակում է, նոթատետրի կողքին։
</p>
</div>

#%% md
### Երկու տարբերակը կողք կողքի

| | Աստղանիշերով | Matplotlib-ով |
|---|---|---|
| Գծապատկերը | 4 տող | 1 տող |
| Սանդղակը 0–10 | **ձեռքով հաշվարկ** | `plt.ylim(0, 10)` |
| Վերնագիր և առանցքներ | հնարավոր չէ | 3 տող |
| Գույն | չկա | `color="#4a7"` |
| Հաշվետվության մեջ դնել | **չի լինի** | `plt.savefig(...)` |

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Դասարանների գծապատկերը

Սարքի՛ր սյունակային գծապատկեր երեք դասարանի միջիններով։ Ավելացրո՛ւ վերնագիր,
առանցքի անուն և 0–10 սանդղակ։

#%% code
import matplotlib.pyplot as plt

# ...

#%% md
### 2. Հորիզոնական սյուներ

`plt.barh()` սարքում է հորիզոնական սյուներ։ Սարքի՛ր առարկաների գծապատկերը
հորիզոնական՝ երկար անունների համար ավելի հարմար է։

#%% code
# ...

#%% md
### 3. Պահպանել երկուսն էլ

Պահպանի՛ր երկու գծապատկերը որպես `classes.png` և `subjects.png`։ Բացի՛ր
ֆայլերը և ստուգի՛ր, որ անունները չեն կտրվել։

#%% code
# ...

#%% md
### 4. Գույնը՝ ըստ արդյունքի

Սարքի՛ր գծապատկեր, որտեղ 7-ից բարձր միջին ունեցող առարկաները կանաչ են, իսկ
մնացածը՝ նարնջագույն։

**Հուշում:** `color` պարամետրին կարելի է տալ **ցուցակ**՝ ամեն սյան համար մեկը։

#%% code
# ...

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Միջին գիծ

`plt.axhline(y=7.0, color="red")` քաշում է հորիզոնական գիծ։ Ավելացրո՛ւ դպրոցի
միջինը որպես կարմիր գիծ առարկաների գծապատկերի վրա։

#%% code
# ...

#%% md
### 6. Թվերը սյուների վրա

Ցիկլով ավելացրո՛ւ ամեն սյան վրա իր թիվը՝ `plt.text(x, y, "7.56")`։

#%% code
# ...

#%% md
### 7. Երկու գծապատկեր՝ կողք կողքի

`plt.subplot(1, 2, 1)` և `plt.subplot(1, 2, 2)` բաժանում են նկարը երկու մասի։
Դի՛ր առարկաները ձախում, դասարանները՝ աջում։

#%% code
# ...

#%% md
### 8. Չանցածների գծապատկերը

Հաշվի՛ր, թե ամեն առարկայից քանի գնահատական է 4-ից ցածր, և սարքի՛ր գծապատկեր։

**Ստուգի՛ր:** բոլորի գումարը պետք է լինի **18**։

#%% code
# ...

#%% md
## Մարտահրավեր

#%% md
### 9. Հայերեն անունները

Փորձի՛ր առարկաների անունները գրել հայերեն՝ ուղիղ `plt.bar`-ի մեջ։

Ամենայն հավանականությամբ կտեսնես **քառակուսիներ տառերի փոխարեն**։ Դա տառատեսակի
խնդիր է, ոչ թե քո կոդի։

Փորձի՛ր ավելացնել այս տողը **ներմուծումից հետո**.

```python
plt.rcParams["font.family"] = "Arial Unicode MS"
```

Եթե չօգնեց՝ փորձի՛ր `"DejaVu Sans"` կամ քո համակարգչում եղած այլ տառատեսակ։

**Սա պետք կգա 23-րդ թեմայում**, երբ բեռնես քո դպրոցի իսկական ֆայլը։

#%% code
# Keep the names in a list here, pasted from the markdown above.
# ...

#%% md
### 10. Ամբողջ դպրոցի պատկերը

Սարքի՛ր մեկ նկար, որում երեք գծապատկեր է՝ առարկաները, դասարանները, և
չանցածների թիվը ըստ առարկայի։ Պահպանի՛ր այն որպես `term_report.png`։

#%% code
# ...

#%% md
<div style="border-left: 6px solid #747; background: #f8f6fb; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#747; margin-top:0;">🏠 Տնային</h3>
<p style="color:#747; margin-bottom:0;">
Այս նոթատետրի <b>Լրացուցիչ</b> առաջադրանքները։<br/><br/>
<b>Նոր բան չկա</b> — ամեն առաջադրանք այս նոթատետրից է, նույն ձևի, ինչ դասին
արածները, և օգտագործում է միայն այն, ինչ այսօր սովորեցինք։<br/>
Հաջորդ նիստը սկսվում է դրանց ստուգումով։
</p>
</div>

#%% md
## Ինչի հասանք

- `import matplotlib.pyplot as plt` — **երկրորդ գրադարանը**
- `plt.bar(names, numbers)` — սյունակային գծապատկեր **մեկ տողով**
- `plt.ylim` `plt.title` `plt.ylabel` — այն, ինչ ձեռքով հաշվում էինք
- `plt.savefig("name.png", dpi=150)` — նկարը դառնում է ֆայլ
- `plt.close()` — որ հաջորդը մաքուր սկսվի
- Անունների և թվերի քանակը **պետք է համընկնի** → `ValueError`

## Ի՞նչ է գալիս հետո

Չորս գծապատկեր, որոնք դպրոցն իսկապես խնդրում է՝ առարկաները, գնահատականների
բաշխվածությունը, մեկ դասարանի ցրվածությունը, և երեք դասարանը կողք կողքի։
