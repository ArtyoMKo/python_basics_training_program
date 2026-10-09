#%% md
# Թեմա 21 — Սխալ, առանց սխալի

### Python 11-րդ դասարանի համար · Թեմա 21-ը 24-ից

Երբ Python-ը սխալ է տալիս — դա **լավ օր** է։ Նա ասում է, թե որտեղ է խնդիրը։

Վատ օրը այն է, երբ ծրագիրը աշխատում է, պատասխան է տալիս, և **պատասխանը սխալ է**։

## ԱՅՍՕՐ:

- **Ա մաս:** կարդալ traceback-ը
- **Բ մաս:** լուռ սխալը
- **Գ մաս:** կանգնեցնել ծրագիրը մեջտեղում

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Այս դասընթացում արդեն տեսել ես</h3>
<p style="color:#06c; margin-bottom:0;">
<code>TypeError</code> · <code>KeyError</code> · <code>AttributeError</code> ·
<code>NameError</code> · <code>ValueError</code> · <code>RecursionError</code><br/><br/>
<b>Այսօր սովորում ենք կարդալ դրանք համակարգված, և գտնել այն սխալը, որը ոչինչ չի ասում։</b>
</p>
</div>

#%% md
## Ա մաս: Կարդալ traceback-ը

Ահա երեք ֆունկցիա, որոնք կանչում են միմյանց։ Վերջինը սխալ է տալիս։

#%% code
import traceback


def average(grades):
    return sum(grades) / len(grades)


def student_line(student):
    return f"{student['name']}: {average(student['grades']):.1f}"


def class_report(students):
    for student in students:
        print(student_line(student))


students = [
    {"name": "Ani", "grades": [7, 6, 8]},
    {"name": "Davit", "grades": []},
]

try:
    class_report(students)
except ZeroDivisionError:
    traceback.print_exc()

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#0a7; margin-top:0;">✅ Կարդա՛ ներքևից վերև</h3>
<p style="color:#0a7; margin-bottom:0;">
<b>Վերջին տողը</b> — <b>ի՞նչ</b> է պատահել. <code>ZeroDivisionError: division by zero</code><br/>
<b>Նախավերջինը</b> — <b>որտե՞ղ</b>. <code>return sum(grades) / len(grades)</code><br/>
<b>Վերևի տողերը</b> — <b>ինչպե՞ս հասանք այնտեղ</b>. <code>class_report</code> →
<code>student_line</code> → <code>average</code><br/><br/>
<b>Ամենավերևի տողը քո գրած առաջին կանչն է։ Ամենաներքևինը՝ այնտեղ, որտեղ կոտրվեց։</b>
</p>
</div>

#%% md
Երեք հարց, ամեն traceback-ի համար.

| Հարց | Որտեղ նայել |
|---|---|
| Ի՞նչ տեսակի սխալ է | **վերջին տող**, կետից ձախ |
| Ի՞նչ է ասում | վերջին տող, կետից աջ |
| Ո՞ր տողում | նախավերջին զույգ տող |
| Ինչպե՞ս հասանք այնտեղ | ամբողջ շղթան, վերևից ներքև |

#%% md
### Երբ սխալը գրադարանի ներսում է

Հաճախ traceback-ի ներքևի տողերը **numpy-ի կամ pandas-ի ներսից են**։

#%% code
import pandas as pd

data = pd.read_csv("school.csv")

try:
    print(data["grades"].mean())
except KeyError:
    traceback.print_exc()

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Մի՛ վախեցիր երկար traceback-ից։</b><br/><br/>
Գտի՛ր այն տողը, որտեղ **քո ֆայլի անունն է**։ Դա է քո սխալը։ Մնացածը pandas-ի
ներսն է, և այնտեղ սխալ չկա։<br/><br/>
VS Code-ում քո ֆայլի տողերը <b>սեղմելի են</b> — սեղմի՛ր և կհայտնվես այնտեղ։
</p>
</div>

#%% md
## Բ մաս: Լուռ սխալը

Հիմա ամենավտանգավորը։ Ահա ֆունկցիա, որը հաշվում է դասարանի միջինը։

**Գործարկի՛ր։ Սխալ չկա։**

#%% code
def class_average(data, class_name):
    total = 0
    count = 0
    for index in range(len(data)):
        row = data.iloc[index]
        if row["class"] == class_name:
            total = total + row["grade"]
        count = count + 1
    return total / count


print("11A average:", round(class_average(data, "11A"), 2))

#%% md
Պատասխանը՝ **2.33**։

Բայց 17-րդ թեմայում `groupby`-ով ստացանք **6.98**։

#%% code
print("groupby says:", round(data.groupby("class")["grade"].mean()["11A"], 2))

#%% md
<div style="border-left: 6px solid #d33; background: #fff5f5; padding: 12px 16px; margin: 12px 0;">
<p style="color:#d33; margin:0;">
🔍 <b>Ոչ մի սխալի հաղորդագրություն։ Ոչ մի կարմիր տող։ Պարզապես սխալ թիվ։</b><br/><br/>
Եթե 17-րդ թեմայի պատասխանը չունենայինք, այս թիվը կգնար հաշվետվության մեջ։
</p>
</div>

**Գտի՛ր սխալը ինքդ, նախքան շարունակելը։**

#%% md
### Ինչպես գտնել՝ առաջին գործիքը, `print`

Ամենապարզ ձևը՝ տպել այն, ինչ կասկածում ես։

#%% code
def class_average_with_prints(data, class_name):
    total = 0
    count = 0
    for index in range(len(data)):
        row = data.iloc[index]
        if row["class"] == class_name:
            total = total + row["grade"]
        count = count + 1
    print("total:", total)
    print("count:", count)
    return total / count


print("11A average:", round(class_average_with_prints(data, "11A"), 2))

#%% md
**`total` 419 է, `count`՝ 180։**

419-ը ճիշտ է՝ դա 11A-ի գումարն է։ Բայց 180-ը **ամբողջ ֆայլի տողերի թիվն է**։

Սխալը՝ `count = count + 1` գրված է `if`-ից **դուրս**։ Մեկ ներս ընկած տարածություն։

#%% code
def class_average(data, class_name):
    total = 0
    count = 0
    for index in range(len(data)):
        row = data.iloc[index]
        if row["class"] == class_name:
            total = total + row["grade"]
            count = count + 1
    return total / count


print("11A average:", round(class_average(data, "11A"), 2))

#%% md
### Երկրորդ գործիքը՝ ստուգում, որը բողոքում է

`print`-ը պետք է **կարդալ**։ Ավելի լավ է ստուգում, որը ինքը բողոքում է։

#%% code
def class_average(data, class_name):
    rows = data[data["class"] == class_name]
    assert len(rows) > 0, f"no rows for class {class_name}"
    assert len(rows) < len(data), "the filter did not filter anything"
    return rows["grade"].mean()


print("11A:", round(class_average(data, "11A"), 2))

try:
    class_average(data, "11Z")
except AssertionError as problem:
    print("AssertionError:", problem)

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b><code>assert condition, "message"</code></b> — եթե պայմանը սխալ է, ծրագիրը
կանգնում է և ասում ինչու։<br/><br/>
<b>Սա լուռ սխալը դարձնում է բարձրաձայն։</b> Եվ հենց դա է, ինչ պետք է. սխալ
պատասխանը ավելի վատ է, քան կանգնած ծրագիրը։
</p>
</div>

#%% md
## Գ մաս: Կանգնեցնել ծրագիրը մեջտեղում

`print`-ը լավ է, բայց պետք է նախապես իմանաս, **ինչ** տպել։

Debugger-ը թույլ է տալիս կանգնեցնել ծրագիրը և նայել **ամեն ինչ** այդ պահին։

### VS Code-ում

1. Սեղմի՛ր տողի համարի **ձախ կողմում** — հայտնվում է կարմիր կետ։ Դա **breakpoint** է
2. Սեղմի՛ր **Run and Debug** (ձախ սյունակում, միջատի նշան) → **Run and Debug**
3. Ծրագիրը կանգնում է կարմիր կետի վրա
4. Ձախում՝ **VARIABLES** — բոլոր փոփոխականները, այդ պահին
5. Վերևում՝ չորս կոճակ.

| Կոճակ | Ինչ է անում |
|---|---|
| **Continue** | գնա մինչև հաջորդ breakpoint |
| **Step Over** | հաջորդ տող, առանց ֆունկցիայի ներս մտնելու |
| **Step Into** | հաջորդ տող, **ֆունկցիայի ներսում** |
| **Step Out** | դուրս եկ այս ֆունկցիայից |

<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Նոթատետրում breakpoint չի աշխատում այնպես, ինչպես <code>.py</code> ֆայլում։</b><br/>
Դրա համար այսօրվա գործնական մասը անում ենք <b>առանձին ֆայլում</b>։<br/><br/>
Python-ում կա նաև <code>breakpoint()</code> ֆունկցիան, որը գրվում է ուղիղ կոդում
և կանգնեցնում է ծրագիրը տերմինալում։ <b>Նոթատետրում այն մի՛ գրիր</b> — բջիջը
կկախվի։
</p>
</div>

#%% md
**Հիմա դու։** Ներքևի բջիջը սարքում է ֆայլ՝ սխալով ներսում։

Գործարկի՛ր բջիջը, հետո բացի՛ր `broken_report.py`-ը VS Code-ում, դի՛ր breakpoint
և գտի՛ր սխալը **debugger-ով**, ոչ թե կարդալով։

#%% code
from pathlib import Path

Path("broken_report.py").write_text('''import pandas as pd

PASS_MARK = 4


def failing_count(data, class_name):
    """How many failing grades does this class have?"""
    rows = data[data["class"] == class_name]
    count = 0
    for grade in rows["grade"]:
        if grade < PASS_MARK:
            count = count + 1
        return count


def main():
    data = pd.read_csv("school.csv")
    for class_name in ["11A", "11B", "11C"]:
        print(class_name, failing_count(data, class_name))
    print("total should be 18")


if __name__ == "__main__":
    main()
''', encoding="utf-8")

print("written -- now open it in VS Code")

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Կարդա՛ traceback-ը

Գործարկի՛ր ներքևի բջիջը և պատասխանի՛ր չորս հարցին markdown-ում՝ ի՞նչ տեսակի
սխալ, ի՞նչ է ասում, ո՞ր տողում, ինչպե՞ս հասանք այնտեղ։

#%% code
import traceback


def grade_word(grade):
    words = {9: "excellent", 7: "good", 4: "ok"}
    return words[grade]


def report(grades):
    return [grade_word(g) for g in grades]


try:
    print(report([9, 7, 5]))
except KeyError:
    traceback.print_exc()

#%% md
### 2. Գտի՛ր լուռ սխալը

Ահա ֆունկցիա, որը պետք է վերադարձնի ամենաբարձր գնահատականը։ Այն սխալ է։
Գտի՛ր ինչու՝ `print`-երով։

#%% code
def highest(grades):
    best = 0
    for grade in grades:
        if grade > best:
            best = grade
    return best


print(highest([7, 6, 8]))
print(highest([-3, -6, -1]))

#%% md
### 3. Երկրորդ լուռ սխալը

Այս ֆունկցիան պետք է հաշվի անցածների տոկոսը։ Ստուգի՛ր `school.csv`-ի վրա՝
պատասխանը պետք է լինի **90.0**։

#%% code
import pandas as pd

data = pd.read_csv("school.csv")


def pass_rate(data):
    passed = data[data["grade"] >= 4]
    return len(passed) / len(data)


print(pass_rate(data))

#%% md
### 4. Ավելացրո՛ւ ստուգումներ

Վերցրո՛ւ 3-րդ վարժության ուղղված ֆունկցիան և ավելացրո՛ւ երկու `assert`՝
արդյունքը 0-ի և 100-ի միջև է, և տվյալները դատարկ չեն։

#%% code
# ...

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Debugger-ով

Ուղղի՛ր `broken_report.py`-ը։ Գրի՛ր markdown-ում, թե **որ տողում** է սխալը և
**ինչ ես տեսել** VARIABLES-ում։

#%% code
# No code -- this one is done in VS Code.

#%% md
### 6. Երեք սխալ՝ մեկ ֆունկցիայում

Ահա ֆունկցիա երեք սխալով։ Ճիշտ պատասխանը 11A-ի համար՝ **6.98**։

```python
def broken_average(data, class_name):
    rows = data[data["class"] = class_name]
    total = 0
    for grade in rows["grade"]:
        total + grade
    return total / len(data)
```

**Պատճենի՛ր այն ներքևի բջիջ և ուղղի՛ր մեկ առ մեկ**, ամեն ուղղումից հետո
գործարկելով։ Առաջին սխալը շարահյուսական է — Python-ը բջիջը ընդհանրապես չի
կարդա, քանի դեռ այն չես ուղղել։

#%% code
# Paste the function here and fix it. Then:
# print(round(broken_average(data, "11A"), 2))   ->  6.98

#%% md
### 7. Ո՞ր տողն է դանդաղ

Ահա երկու ֆունկցիա՝ նույն պատասխանով։ Չափի՛ր ժամանակը և պարզի՛ր, թե որն է
դանդաղ և ինչու։

#%% code
import time

def slow(data):
    total = 0
    for index in range(len(data)):
        total = total + data.iloc[index]["grade"]
    return total


def fast(data):
    return data["grade"].sum()


# Time both, print both answers.
# ...

#%% md
### 8. Սխալը, որ ոչ մի տեղ չի երևում

Ահա ծրագիր, որը աշխատում է **ճիշտ** հիմա, բայց կկոտրվի, երբ ֆայլում նոր
դասարան ավելանա։ Գտի՛ր այդ տեղը և ավելացրո՛ւ `assert`։

#%% code
CLASSES = ["11A", "11B", "11C"]

def report(data):
    for class_name in CLASSES:
        rows = data[data["class"] == class_name]
        print(class_name, round(rows["grade"].mean(), 2))

report(data)

#%% md
## Մարտահրավեր

#%% md
### 9. Քո սեփական սխալը

Վերցրո՛ւ **քո** գրած կոդը նախորդ թեմաներից և միտումնավոր կոտրի՛ր այն՝ փոխելով
մեկ նիշ։ Ապա տո՛ւր գործընկերոջդ և թող նա գտնի՝ debugger-ով։

Հետո փոխվե՛ք տեղերով։

#%% code
# ...

#%% md
### 10. Ստուգումների շերտ

Գրի՛ր ֆունկցիա `check_data(data)`, որը ստուգում է դպրոցի ֆայլը և բողոքում, եթե՝

- տողերի թիվը 180 չէ
- գնահատականներից որևէ մեկը 1–10 միջակայքից դուրս է
- որևէ աշակերտ ունի 5-ից տարբեր թվով գնահատական
- դասարանների թիվը 3 չէ

Ապա գործարկի՛ր այն խաթարված ֆայլի վրա։

**Սա այն է, ինչ իսկական ծրագրերը անում են ամեն անգամ, երբ տվյալ են կարդում։**

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

- Traceback-ը կարդացվում է **ներքևից վերև**՝ ի՞նչ, որտե՞ղ, ինչպե՞ս հասանք
- Երկար traceback-ում գտի՛ր **քո ֆայլի անունը** — մնացածը գրադարանի ներսն է
- **Լուռ սխալը ամենավտանգավորն է** — պատասխան կա, սխալ հաղորդագրություն՝ ոչ
- `print` — առաջին գործիքը։ Պետք է իմանաս, ինչ տպել
- `assert condition, "message"` — լուռ սխալը դարձնում է բարձրաձայն
- **Breakpoint** և VARIABLES — նայել ամեն ինչ, առանց նախապես իմանալու ինչ փնտրել
- Նոթատետրում `breakpoint()` մի՛ գրիր

## Ի՞նչ է գալիս հետո

Նոթատետրը արհեստանոց է։ Հաջորդ նիստում ամեն ինչ դուրս է գալիս այնտեղից և դառնում
**հինգ ֆայլ**, որոնցից ամեն մեկը մեկ գործ է անում։

Եվ օրվա վերջում՝ `python main.py`։
