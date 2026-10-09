#%% md
# Թեմա 17 — Զտել, խմբավորել, նկարագրել

### Python 11-րդ դասարանի համար · Թեմա 17-ը 24-ից

Նախորդ թեմայում ֆայլը բացվեց մեկ տողով։ Այսօր՝ երեք գործողություն, որոնք ծածկում են
դպրոցի հարցերի մեծ մասը։

## ԱՅՍՕՐ:

- **Ա մաս:** խմբավորել
- **Բ մաս:** նկարագրել
- **Գ մաս:** աղյուսակ՝ երկու չափումով

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>pd.read_csv</code> · <code>.shape</code> · <code>.head()</code> ·
<code>data[data["class"] == "11B"]</code><br/><br/>
<b>Այսօր նոր գրադարան չկա — երեք նոր գործողություն։</b>
</p>
</div>

#%% code
import pandas as pd

data = pd.read_csv("school.csv")
print(data.shape)
data.head(3)

#%% md
## Ա մաս: Խմբավորել

Ահա այն, ինչ արեցինք նախորդ թեմայում՝ երեք դասարանի միջինը, երեք անգամ։

#%% code
for class_name in ["11A", "11B", "11C"]:
    part = data[data["class"] == class_name]
    print(class_name, round(part["grade"].mean(), 2))

#%% md
Ցիկլը պետք է **իմանա դասարանների անունները**։ Եթե վաղը նոր դասարան ավելանա՝
ցիկլը չի իմանա այդ մասին։

pandas-ը ունի մեկ գործողություն, որը **ինքն է գտնում խմբերը**։

#%% code
print(data.groupby("class")["grade"].mean().round(2))

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b>Կարդա՛ ձախից աջ.</b><br/>
<code>data.groupby("class")</code> — բաժանիր տողերը ըստ դասարանի<br/>
<code>["grade"]</code> — ինձ հետաքրքրում է գնահատականների սյունակը<br/>
<code>.mean()</code> — ամեն խմբի համար՝ միջինը<br/><br/>
<b>Դասարանների անունները ոչ մի տեղ չենք գրել։</b> pandas-ը դրանք գտավ տվյալների մեջ։
</p>
</div>

#%% md
Նույնը՝ ցանկացած սյունակով, ցանկացած հաշվարկով։

#%% code
print(data.groupby("subject")["grade"].mean().round(2).sort_values())
print()
print(data.groupby("subject")["grade"].max())
print()
print(data.groupby("student")["grade"].mean().round(2).head())

#%% md
Եվ մի քանի հաշվարկ միանգամից՝ `.agg()`-ով։

#%% code
print(data.groupby("class")["grade"].agg(["mean", "min", "max", "std"]).round(2))

#%% md
## Բ մաս: Նկարագրել

Երբ նոր ֆայլ ես բացում, առաջին հարցը՝ «ի՞նչ կա այստեղ»։

#%% code
print(data["grade"].describe())

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<p style="color:#06c; margin:0;">
<b>Ութ թիվ՝ մեկ կանչով։</b><br/>
<code>count</code> քանակ · <code>mean</code> միջին · <code>std</code> ցրվածություն ·
<code>min</code> և <code>max</code><br/>
<code>25%</code> <code>50%</code> <code>75%</code> — <b>քառորդները</b>։
<code>50%</code>-ը միջնակետն է. կեսը ցածր է, կեսը՝ բարձր։<br/><br/>
Եթե <code>mean</code>-ը և <code>50%</code>-ը իրարից հեռու են — բաշխվածությունը
<b>թեք է</b>, և միջինը միայնակ խաբում է։
</p>
</div>

#%% code
# describe() works per group too
print(data.groupby("class")["grade"].describe().round(2))

#%% md
## Գ մաս: Աղյուսակ՝ երկու չափումով

Տնօրենին պետք է աղյուսակ՝ տողերը դասարաններն են, սյունակները՝ առարկաները։

Երկու խմբավորում միանգամից՝ `pivot_table`։

#%% code
table = data.pivot_table(index="class", columns="subject", values="grade",
                         aggfunc="mean").round(2)
print(table)

#%% md
Սա ուղիղ այն աղյուսակն է, որ 13-րդ թեմայում կառուցում էինք NumPy-ով՝ ցիկլերով։

#%% code
print("highest cell:", table.max().max())
print("best class per subject:")
print(table.idxmax())

#%% md
Եվ քանի որ `table`-ը սովորական աղյուսակ է, այն ուղիղ գնում է գծապատկերի մեջ։

#%% code
import matplotlib.pyplot as plt

table.T.plot(kind="bar", figsize=(9, 4))
plt.ylim(0, 10)
plt.ylabel("Average grade")
plt.title("Three classes, five subjects")
plt.tight_layout()
plt.savefig("pivot_chart.png", dpi=150)
plt.close()

print("saved pivot_chart.png")

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Համեմատի՛ր 15-րդ թեմայի Գ մասի հետ։</b> Այնտեղ խմբավորված սյուները պահանջում
էին <code>np.arange</code>, <code>width</code>, տեղաշարժ և <code>xticks</code> —
ինը տող։<br/><br/>
Այստեղ՝ <code>table.T.plot(kind="bar")</code>։ <b>Քանի որ տվյալն արդեն աղյուսակ է։</b><br/>
<code>.T</code>-ն շրջում է աղյուսակը՝ որ առարկաները լինեն ներքևում։
</p>
</div>

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Երեք խմբավորում

Տպի՛ր միջինը՝ ըստ դասարանի, ըստ առարկայի, և ըստ աշակերտի (առաջին տասը)։

#%% code
import pandas as pd

data = pd.read_csv("school.csv")
# ...

#%% md
### 2. Չանցածները՝ ըստ դասարանի

Զտի՛ր 4-ից ցածր տողերը, ապա խմբավորի՛ր ըստ դասարանի և հաշվի՛ր քանակը։

**Հուշում:** `.count()` կամ `.size()`։

**Ստուգի՛ր:** բոլորի գումարը պետք է լինի 18։

#%% code
# ...

#%% md
### 3. Ամեն աշակերտի նկարագրությունը

Խմբավորի՛ր ըստ աշակերտի և վերցրո՛ւ միջինը, նվազագույնը և առավելագույնը `.agg()`-ով։
Տպի՛ր ամենաբարձր միջինով հինգ աշակերտին։

#%% code
# ...

#%% md
### 4. Աղյուսակը

Սարքի՛ր `pivot_table` աշակերտ × առարկա։ Քանի՞ տող և սյունակ ունի այն։

#%% code
# ...

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Երկու մակարդակի խմբավորում

`data.groupby(["class", "subject"])["grade"].mean()` խմբավորում է **երկու
սյունակով**։ Փորձի՛ր և համեմատի՛ր `pivot_table`-ի հետ։

#%% code
# ...

#%% md
### 6. Անցումների տոկոսը

Ավելացրո՛ւ `passed` սյունակ և խմբավորի՛ր ըստ առարկայի՝ միջինը վերցնելով։
Քանի որ `True`-ն 1 է, միջինը կլինի **անցման տոկոսը**։

#%% code
# ...

#%% md
### 7. Ամենաանհավասար առարկան

Խմբավորի՛ր ըստ առարկայի և վերցրո՛ւ `.std()`-ը։ Որ առարկայի գնահատականներն են
ամենաշատը ցրված։

#%% code
# ...

#%% md
### 8. Խմբավորում և գծապատկեր

Սարքի՛ր `groupby("subject")["grade"].mean()` և ուղիղ դրանից՝ գծապատկեր
`.plot(kind="barh")`-ով։

#%% code
# ...

#%% md
## Մարտահրավեր

#%% md
### 9. Ռիսկի ցուցակը

Կառուցի՛ր աղյուսակ այն 12 աշակերտի համար, ովքեր ունեն գոնե մեկ չանցած
գնահատական։ Ամեն տողում՝ անունը, դասարանը, միջինը, և չանցած առարկաների թիվը։

Դասավորի՛ր ըստ չանցած առարկաների թվի՝ նվազման կարգով։

#%% code
# ...

#%% md
### 10. Ցիկլն ընդդեմ `groupby`-ի

Գրի՛ր **երկու** ֆունկցիա, որոնք հաշվում են ամեն առարկայի միջինը՝ մեկը ցիկլով,
մյուսը `groupby`-ով։ Ստուգի՛ր, որ պատասխանները նույնն են։

Ապա markdown-ում գրի՛ր՝ ո՞րն է ավելի հեշտ կարդալ, և ո՞րը ավելի հեշտ **սխալ գրել**։

#%% code
# ...

#%% md
<div style="border-left: 6px solid #747; background: #f8f6fb; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#747; margin-top:0;">🏠 Տնային</h3>
<p style="color:#747; margin-bottom:0;">
Այս նոթատետրի <b>Պարտադիր</b> առաջադրանքները — այս նիստում երկու նոթատետր ենք անցնում, և դրանք դասին չեն տեղավորվում։<br/><b>Լրացուցիչը տանը պետք չէ անել։</b><br/><br/>
<b>Նոր բան չկա</b> — ամեն առաջադրանք այս նոթատետրից է, նույն ձևի, ինչ դասին
արածները, և օգտագործում է միայն այն, ինչ այսօր սովորեցինք։<br/>
Հաջորդ նիստը սկսվում է դրանց ստուգումով։
</p>
</div>

#%% md
## Ինչի հասանք

- `data.groupby("class")["grade"].mean()` — խմբերը **ինքն է գտնում**
- `.agg(["mean", "min", "max", "std"])` — մի քանի հաշվարկ միանգամից
- `.describe()` — ութ թիվ, երբ նոր ֆայլ ես բացում
- `mean`-ը և `50%`-ը հեռու են → բաշխվածությունը **թեք է**
- `pivot_table(index=..., columns=..., values=...)` — աղյուսակ երկու չափումով
- `table.T.plot(kind="bar")` — ինը տող Matplotlib-ի փոխարեն մեկ տող

## Ի՞նչ է գալիս հետո

Նոր գրադարան չի լինի։ Վերցնելու ենք այն ամենը, ինչ ունենք — pandas, NumPy,
Matplotlib — և սարքելու ենք **կիսամյակի ամբողջական հաշվետվությունը**՝ ֆայլից
մինչև պատրաստի նկարներ։
