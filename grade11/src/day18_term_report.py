#%% md
# Թեմա 18 — Կիսամյակի հաշվետվությունը

### Python 11-րդ դասարանի համար · Թեմա 18-ը 24-ից

Այսօր **նոր գրադարան չկա**։ Երեքն էլ ունենք. pandas ֆայլի համար, NumPy թվերի,
Matplotlib նկարների։

Այսօր դրանք դառնում են **մեկ աշխատանք**՝ ֆայլից մինչև պատրաստի հաշվետվություն։

## ԱՅՍՕՐ:

- **Ա մաս:** կարդալ և ստուգել
- **Բ մաս:** հաշվել
- **Գ մաս:** նկարել և պահպանել

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Երեք գրադարանը</h3>
<p style="color:#06c; margin-bottom:0;">
<b>pandas</b> — ֆայլը կարդալ, զտել, խմբավորել<br/>
<b>NumPy</b> — թվերի վրա հաշվարկ<br/>
<b>Matplotlib</b> — նկար<br/><br/>
<b>Այսօր երեքն էլ՝ մեկ ծրագրում։</b>
</p>
</div>

#%% md
## Ա մաս: Կարդալ և ստուգել

Առաջին քայլը **միշտ** նույնն է՝ բացել և նայել։ Երբեք չսկսես հաշվել, մինչև
չտեսնես, թե ինչ կա ֆայլում։

#%% code
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PASS_MARK = 4

data = pd.read_csv("school.csv")

print("rows and columns:", data.shape)
print("columns:", data.columns.tolist())
print("classes:", sorted(data["class"].unique()))
print("subjects:", sorted(data["subject"].unique()))
print("students:", data["student"].nunique())
print("missing values per column:")
print(data.isna().sum())

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b>Վեց հարց, որ միշտ տալիս ես նոր ֆայլին.</b> չափը, սյունակները, եզակի
արժեքները, քանի օբյեկտ, և <b>որտեղ են դատարկ բջիջները</b>։<br/><br/>
<code>.isna().sum()</code> — ամեն սյունակում քանի դատարկ բջիջ կա։ Այստեղ
<code>note</code>-ում շատ են, և դա նորմալ է. ծանոթագրությունը ոչ բոլորն ունեն։
</p>
</div>

#%% md
## Բ մաս: Հաշվել

#%% code
summary = {
    "students": data["student"].nunique(),
    "grades": len(data),
    "average": round(data["grade"].mean(), 2),
    "spread": round(data["grade"].std(), 3),
    "failing_grades": int((data["grade"] < PASS_MARK).sum()),
    "students_at_risk": data[data["grade"] < PASS_MARK]["student"].nunique(),
}

for key in summary:
    print(f"{key:<18} {summary[key]}")

#%% md
Երեք աղյուսակ, որ հաշվետվության մեջ են գնում։

#%% code
by_subject = data.groupby("subject")["grade"].mean().round(2).sort_values()
by_class = data.groupby("class")["grade"].mean().round(2)
table = data.pivot_table(index="class", columns="subject", values="grade",
                         aggfunc="mean").round(2)

print(by_subject)
print()
print(by_class)
print()
print(table)

#%% md
Եվ ռիսկի ցուցակը՝ նրանք, ում վրա պետք է ուշադրություն դարձնել։

#%% code
failing = data[data["grade"] < PASS_MARK]

at_risk = failing.groupby("student").agg(
    failed=("grade", "size"),
    lowest=("grade", "min"),
).sort_values("failed", ascending=False)

at_risk["average"] = data.groupby("student")["grade"].mean().round(2)
at_risk["class"] = data.groupby("student")["class"].first()

print(at_risk)

#%% md
## Գ մաս: Նկարել և պահպանել

#%% code
def save_subject_chart(data, filename):
    averages = data.groupby("subject")["grade"].mean().sort_values()
    plt.figure(figsize=(8, 4))
    plt.barh(averages.index, averages.values, color="#4a7")
    plt.xlim(0, 10)
    plt.axvline(x=data["grade"].mean(), color="red", linestyle="--",
                label="school average")
    plt.xlabel("Average grade")
    plt.title("Subject averages")
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()


def save_distribution_chart(data, filename):
    plt.figure(figsize=(8, 4))
    plt.hist(data["grade"], bins=range(1, 12), edgecolor="white", color="#47a")
    plt.xlabel("Grade")
    plt.ylabel("How many")
    plt.title("Grade distribution")
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()


save_subject_chart(data, "report_subjects.png")
save_distribution_chart(data, "report_distribution.png")
print("two charts saved")

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Նկատի՛ր՝ երկու գծապատկերը ֆունկցիաներ են։</b><br/><br/>
Ամեն մեկը ստանում է տվյալները և ֆայլի անունը, և ոչինչ չի վերադարձնում։ Այսպես
նույն գծապատկերը կարելի է սարքել 11A-ի, 11B-ի և ամբողջ դպրոցի համար՝
<b>առանց կոդը պատճենելու</b>։<br/><br/>
<b>Սա ուղիղ այն է, ինչ 22-րդ թեմայում կտեղափոխենք առանձին ֆայլ։</b>
</p>
</div>

#%% md
Եվ վերջում՝ տեքստային հաշվետվությունը, որը պահպանվում է ֆայլում։

#%% code
from pathlib import Path

report = []
report.append("TERM REPORT")
report.append("=" * 40)
report.append(f"Students:          {summary['students']}")
report.append(f"Grades recorded:   {summary['grades']}")
report.append(f"School average:    {summary['average']}")
report.append(f"Failing grades:    {summary['failing_grades']}")
report.append(f"Students at risk:  {summary['students_at_risk']}")
report.append("")
report.append("Subject averages")
report.append("-" * 40)
for subject in by_subject.index:
    report.append(f"  {subject:<16} {by_subject[subject]:.2f}")

text = "\n".join(report)
Path("term_report.txt").write_text(text, encoding="utf-8")

print(text)

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Վեց հարցը

Գրի՛ր ֆունկցիա `inspect(data)`, որը տպում է Ա մասի վեց պատասխանը։ Կանչի՛ր այն։

#%% code
import pandas as pd

data = pd.read_csv("school.csv")

def inspect(data):
    # ...
    pass

#%% md
### 2. Մեկ դասարանի հաշվետվությունը

Գրի՛ր ֆունկցիա `class_summary(data, class_name)`, որը վերադարձնում է բառարան՝
այդ դասարանի աշակերտների թիվը, միջինը, ցրվածությունը և չանցածների թիվը։

Կանչի՛ր այն երեք դասարանի համար։

#%% code
# ...

#%% md
### 3. Գծապատկեր ամեն դասարանի համար

Օգտագործի՛ր Գ մասի `save_distribution_chart`-ը և սարքի՛ր երեք նկար՝ մեկը ամեն
դասարանի համար։ Ֆայլերի անունները՝ `dist_11A.png` և այլն։

#%% code
# ...

#%% md
### 4. Ամբողջ հաշվետվությունը՝ մեկ ֆունկցիայով

Գրի՛ր `build_report(path)`, որը կարդում է ֆայլը, հաշվում, սարքում երկու
գծապատկեր և գրում տեքստային հաշվետվությունը։

**Սա քո վերջնական ծրագրի սկիզբն է։**

#%% code
# ...

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Ռիսկի ցուցակը՝ ֆայլում

Պահպանի՛ր `at_risk` աղյուսակը CSV ֆայլում՝ `data.to_csv("at_risk.csv")`։
Բացի՛ր ֆայլը և ստուգի՛ր։

#%% code
# ...

#%% md
### 6. Առարկայի հաշվետվություն

Գրի՛ր ֆունկցիա, որը մեկ առարկայի համար սարքում է հաշվետվություն՝ միջին ըստ
դասարանի, բաշխվածության գծապատկեր, և չանցածների ցուցակ։

#%% code
# ...

#%% md
### 7. Համեմատել երկու դասարան

Սարքի՛ր մեկ գծապատկեր, որում 11A-ի և 11C-ի բաշխվածությունները կողք կողքի են։

#%% code
# ...

#%% md
### 8. Հաշվետվությունը՝ ամսաթվով

Ավելացրո՛ւ հաշվետվության վերնագրին այսօրվա ամսաթիվը։

**Հուշում:** `from datetime import date` և `date.today()`։

#%% code
# ...

#%% md
## Մարտահրավեր

#%% md
### 9. Հաշվետվություն ցանկացած ֆայլի համար

Դարձրո՛ւ `build_report`-ը այնպես, որ այն աշխատի **ցանկացած** նույն ձևի ֆայլի
հետ՝ տարբեր դասարաններով և առարկաներով։

Ստուգի՛ր այն՝ սարքելով փոքր ֆայլ ձեռքով՝ երկու դասարան, երեք առարկա։

#%% code
# ...

#%% md
### 10. Ի՞նչ է լինում, երբ տվյալը վատն է

Սարքի՛ր ֆայլի պատճեն, որտեղ.

- մեկ գնահատական դատարկ է
- մեկ գնահատական `"-"` է թվի փոխարեն
- մեկ դասարանի անունը սխալ է գրված՝ `"11a"` փոքրատառով

Գործարկի՛ր `build_report`-ը դրա վրա և տես, թե ինչ է լինում։ Ի՞նչ սխալ է տալիս,
և որտե՞ղ։ Ի՞նչը **չի** սխալ տալիս, բայց պատասխանը սխալ է։

Պատասխանը գրի՛ր markdown-ում։ **Սա 21-րդ թեմայի նյութն է։**

#%% code
# ...

#%% md
<div style="border-left: 6px solid #747; background: #f8f6fb; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#747; margin-top:0;">🏠 Տնային</h3>
<p style="color:#747; margin-bottom:0;">
Այս նոթատետրի <b>Պարտադիր</b> առաջադրանքները, որ չհասցրիր, ապա <b>Լրացուցիչ</b>-ը։<br/><br/>
<b>Նոր բան չկա</b> — ամեն առաջադրանք այս նոթատետրից է, և օգտագործում է միայն այն,
ինչ այսօր սովորեցինք։<br/>
Հաջորդ նիստը սկսվում է դրանց ստուգումով։
</p>
</div>

#%% md
## Ինչի հասանք

- Երեք գրադարանը՝ **մեկ աշխատանքում**
- Առաջին քայլը միշտ՝ **բացել և նայել**, ոչ թե հաշվել
- `.isna().sum()` — որտեղ են դատարկ բջիջները
- Գծապատկերը՝ **ֆունկցիա**, որը ստանում է տվյալ և ֆայլի անուն
- `to_csv` և `write_text` — հաշվետվությունը դուրս է գալիս նոթատետրից
- Ամբողջ կիսամյակի հաշվետվությունը՝ **մեկ ֆունկցիայի կանչ**

## Ի՞նչ է գալիս հետո

Նախարարությունը ուղարկել է ֆայլ, որտեղ դպրոցը բաժանված է հոսքերի, հոսքերը՝
դասարանների, դասարանները՝ խմբերի։ Եվ ամեն ճյուղ **նույն խորությունը չունի**։

Ցիկլ ներսում ցիկլ ներսում ցիկլ կգրենք։ Հետո նույն նիստում կստանանք այն, ինչով
դա գրվում է **առանց իմանալու խորությունը**։
