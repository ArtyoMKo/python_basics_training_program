#%% md
# Օր 19 — Որքա՞ն խորն է

### Python 11-րդ դասարանի համար · Օր 19-ը 24-ից

Նախարարությունը ուղարկել է դպրոցի կառուցվածքը։ Այնտեղ դպրոցը բաժանված է
**հոսքերի**, հոսքերը՝ **դասարանների**, դասարանները՝ **խմբերի**։

Եվ ամեն ճյուղ նույն խորությունը չունի։

## ԱՅՍՕՐ:

- **Ա մաս:** ցիկլ ցիկլի մեջ ցիկլի մեջ
- **Բ մաս:** ֆունկցիա, որը կանչում է ինքն իրեն
- **Գ մաս:** երկու տարբերակը կողք կողքի

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
Կիսամյակի հաշվետվությունը՝ ֆայլից մինչև նկար։<br/><br/>
<b>Այսօր ֆունկցիան կսովորի կանչել ինքն իրեն։</b>
</p>
</div>

#%% md
## Ա մաս: Ցիկլ ցիկլի մեջ

Ահա նախարարության ֆայլը, պարզեցված։

#%% code
school = {
    "name": "School N 5",
    "parts": [
        {
            "name": "Science stream",
            "parts": [
                {"name": "11A", "students": ["Ani", "Davit", "Nare"]},
                {"name": "11B", "students": ["Aram", "Mariam"]},
            ],
        },
        {
            "name": "Humanities stream",
            "parts": [
                {"name": "11C", "students": ["Tigran", "Lilit", "Gor"]},
            ],
        },
    ],
}

print(school["name"])
for stream in school["parts"]:
    print(" ", stream["name"])
    for group in stream["parts"]:
        print("   ", group["name"], group["students"])

#%% md
Այն, ինչ գիտենք անել՝ ցիկլ ամեն մակարդակի համար։ Հաշվենք բոլոր աշակերտներին։

<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Այս ձևն աշխատում է, քանի դեռ խորությունը հայտնի է։</b> Դասի երկրորդ կեսին
կսովորենք մի ձև, որում <b>խորությունը ընդհանրապես չի հայտնվում կոդում</b>։
</p>
</div>

#%% code
def count_students(school):
    total = 0
    for stream in school["parts"]:
        for group in stream["parts"]:
            total = total + len(group["students"])
    return total


print(count_students(school), "students")

#%% md
**Հիմա դու։** Գրի՛ր ֆունկցիա, որը հավաքում է **բոլոր անունները** մեկ ցուցակում։

#%% code
def all_names(school):
    names = []
    # Two loops, like above.
    # ...
    return names


# print(all_names(school))

#%% md
### Եվ հիմա՝ նոր ֆայլը

Նախարարությունը ուղարկում է թարմացված կառուցվածքը։ Այս տարի գիտական հոսքը
բաժանվել է **ենթախմբերի**։

**Գործարկի՛ր հին ֆունկցիան նոր տվյալների վրա։**

#%% code
school = {
    "name": "School N 5",
    "parts": [
        {
            "name": "Science stream",
            "parts": [
                {
                    "name": "11A",
                    "parts": [
                        {"name": "group 1", "students": ["Ani", "Davit"]},
                        {"name": "group 2", "students": ["Nare"]},
                    ],
                },
                {"name": "11B", "students": ["Aram", "Mariam"]},
            ],
        },
        {
            "name": "Humanities stream",
            "parts": [
                {"name": "11C", "students": ["Tigran", "Lilit", "Gor"]},
            ],
        },
    ],
}

try:
    print(count_students(school))
except KeyError as problem:
    print("KeyError:", problem)

#%% md
`11A`-ն այլևս `students` չունի — նա ունի `parts`։ Ֆունկցիան փնտրում է այն, ինչ չկա։

Ուղղենք՝ ավելացնելով ևս մեկ ցիկլ և ստուգում։

#%% code
def count_students(school):
    total = 0
    for stream in school["parts"]:
        for group in stream["parts"]:
            if "students" in group:
                total = total + len(group["students"])
            else:
                for subgroup in group["parts"]:
                    total = total + len(subgroup["students"])
    return total


print(count_students(school), "students")

#%% md
Աշխատեց։ **Բայց վաղը ենթախումբը կբաժանվի ենթա-ենթախմբերի։**

Եվ այդ ժամանակ պետք կլինի ևս մեկ ցիկլ, ևս մեկ `if`, և ֆունկցիան կդառնա անընթեռնելի։

#%% md
## Բ մաս: Ֆունկցիա, որը կանչում է ինքն իրեն

Նայի՛ր խնդրին այլ կերպ։

Ամեն մաս կամ **ունի աշակերտներ**, կամ **ունի ուրիշ մասեր**։ Եթե ունի աշակերտներ՝
հաշվում ենք։ Եթե ունի մասեր՝ **նույն հարցը տալիս ենք ամեն մասին**։

#%% code
def count_students(part):
    if "students" in part:
        return len(part["students"])

    total = 0
    for smaller in part["parts"]:
        total = total + count_students(smaller)
    return total


print(count_students(school), "students")

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#0a7; margin-top:0;">✅ Երկու մաս, միշտ</h3>
<p style="color:#0a7; margin-bottom:0;">
<b>1. Հիմնային դեպք</b> — երբ կանգ առնել։ <code>if "students" in part:</code><br/>
<b>2. Կանչ ինքն իրեն</b> — ավելի փոքր խնդրի վրա։ <code>count_students(smaller)</code><br/><br/>
<b>Հիմնային դեպքը գրվում է առաջինը։ Միշտ։</b> Առանց դրա ֆունկցիան երբեք չի կանգնի։<br/><br/>
Նկատի՛ր՝ կոդում <b>ոչ մի տեղ չկա, թե որքան խորն է</b> կառուցվածքը։
</p>
</div>

#%% md
### Երբ կանչը չի մոտենում հիմնային դեպքին

Ահա ֆունկցիա, որում **հիմնային դեպքը կա**։ Բայց նայի՛ր ուշադիր վերջին տողին։

**Գործարկի՛ր և կարդա՛ սխալը։**

#%% code expected-error: RecursionError
def count_broken(part):
    if "students" in part:
        return len(part["students"])

    # The call forgets to go one level down -- it asks the same question again.
    return count_broken(part)


print(count_broken(school))

#%% md
<div style="border-left: 6px solid #d33; background: #fff5f5; padding: 12px 16px; margin: 12px 0;">
<p style="color:#d33; margin:0;">
🔍 <b><code>RecursionError: maximum recursion depth exceeded</code></b><br/><br/>
Ֆունկցիան կանչեց ինքն իրեն, նա՝ նորից, և այդպես մինչև Python-ը կանգնեցրեց։<br/><br/>
Python-ը թույլ է տալիս մոտ <b>1000 մակարդակ</b>։ Սա պաշտպանություն է — առանց
դրա համակարգիչը կկախվեր։<br/><br/>
<b>Այս սխալը նշանակում է երկու բանից մեկը.</b><br/>
1. հիմնային դեպք <b>չկա</b>, կամ<br/>
2. հիմնային դեպքը կա, բայց կանչը <b>չի մոտենում</b> նրան — ինչպես այստեղ.
<code>count_broken(part)</code>-ը տալիս է <b>նույն</b> հարցը, ոչ թե ավելի փոքրը։<br/><br/>
Երկրորդը ավելի հաճախ է լինում, և ավելի դժվար է նկատել։
</p>
</div>

#%% md
## Գ մաս: Նույնը, ցանկացած խորության

Ամենակարևոր ստուգումը՝ ավելացնենք **ևս մեկ մակարդակ** և ոչինչ չփոխենք կոդում։

#%% code
deeper = {
    "name": "School N 5",
    "parts": [
        {
            "name": "Science stream",
            "parts": [
                {
                    "name": "11A",
                    "parts": [
                        {
                            "name": "group 1",
                            "parts": [
                                {"name": "pair A", "students": ["Ani"]},
                                {"name": "pair B", "students": ["Davit"]},
                            ],
                        },
                        {"name": "group 2", "students": ["Nare"]},
                    ],
                },
                {"name": "11B", "students": ["Aram", "Mariam"]},
            ],
        },
        {
            "name": "Humanities stream",
            "parts": [
                {"name": "11C", "students": ["Tigran", "Lilit", "Gor"]},
            ],
        },
    ],
}

print(count_students(deeper), "students")

#%% md
**Նույն ֆունկցիան։ Ոչ մի տող չփոխվեց։**

Հիմա հավաքենք անունները և տպենք կառուցվածքը։

#%% code
def collect_names(part):
    if "students" in part:
        return part["students"]

    names = []
    for smaller in part["parts"]:
        names = names + collect_names(smaller)
    return names


print(collect_names(deeper))


def show(part, indent=0):
    print(" " * indent + part["name"])
    if "students" in part:
        for name in part["students"]:
            print(" " * (indent + 2) + "- " + name)
        return
    for smaller in part["parts"]:
        show(smaller, indent + 2)


show(deeper)

#%% md
### Երկու տարբերակը կողք կողքի

| | Ցիկլերով | Ռեկուրսիայով |
|---|---|---|
| Երեք մակարդակ | 2 ցիկլ | 1 ֆունկցիա |
| Չորս մակարդակ | **3 ցիկլ և `if`** | **նույն ֆունկցիան** |
| Հինգ մակարդակ | 4 ցիկլ և 2 `if` | **նույն ֆունկցիան** |
| Խորությունը կոդում | **գրված է** | **չկա** |
| Տողերի թիվ | 9 և աճում | 6, միշտ |

<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<p style="color:#06c; margin:0;">
<b>Ե՞րբ օգտագործել։</b> Երբ տվյալը <b>իր մեջ պարունակում է նույն ձևի տվյալ</b> —
թղթապանակ թղթապանակի մեջ, մեկնաբանություն մեկնաբանության տակ, դպրոց→հոսք→դասարան։<br/><br/>
<b>Ե՞րբ ոչ։</b> Երբ սովորական ցուցակ է։ <code>for grade in grades</code> ռեկուրսիայով
գրելը <b>ավելի վատ է</b>, ոչ ավելի լավ։
</p>
</div>

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Ամենախոր մակարդակը

Գրի՛ր ֆունկցիա `depth(part)`, որը վերադարձնում է կառուցվածքի խորությունը։
Աշակերտներով մասը խորություն **1** է։

#%% code
def depth(part):
    # Base case first.
    # ...
    return 0


# print(depth(deeper))

#%% md
### 2. Քանի՞ խումբ կա

Գրի՛ր ֆունկցիա, որը հաշվում է, թե **քանի մաս** կա ընդհանուր՝ ներառյալ
դպրոցը ինքը։

#%% code
# ...

#%% md
### 3. Գտնել աշակերտին

Գրի՛ր ֆունկցիա `find(part, name)`, որը վերադարձնում է այն մասի անունը, որտեղ
տվյալ աշակերտն է։ Եթե չկա՝ `None`։

#%% code
# print(find(deeper, "Nare"))
# print(find(deeper, "Someone"))

#%% md
### 4. Ամենամեծ խումբը

Գրի՛ր ֆունկցիա, որը վերադարձնում է ամենաշատ աշակերտ ունեցող մասի անունը
և աշակերտների թիվը։

#%% code
# ...

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Ճանապարհը մինչև աշակերտը

Վերագրի՛ր `find`-ը այնպես, որ այն վերադարձնի **ամբողջ ճանապարհը**՝
`["School N 5", "Science stream", "11A", "group 1", "pair A"]`։

#%% code
# ...

#%% md
### 6. Հարթեցնել ցուցակը

Ահա ցուցակ, որի ներսում ցուցակներ են, ցանկացած խորության։ Գրի՛ր ֆունկցիա, որը
վերադարձնում է բոլոր թվերը մեկ հարթ ցուցակում։

#%% code
nested = [1, [2, 3, [4, [5, 6]], 7], [8], 9]

def flatten(items):
    # ...
    return []


# print(flatten(nested))

#%% md
### 7. Գումարը

Գրի՛ր ֆունկցիա, որը հաշվում է բոլոր աշակերտների գնահատականների գումարը, եթե
ամեն մասում `"grades"` բանալի կա թվերի ցուցակով։

#%% code
# ...

#%% md
### 8. Թղթապանակները

`Path(".").iterdir()` տալիս է թղթապանակի պարունակությունը, իսկ
`path.is_dir()` ասում է՝ թղթապանակ է, թե ֆայլ։

Գրի՛ր ֆունկցիա, որը տպում է քո թղթապանակի ամբողջ ծառը։

**Ուշադի՛ր:** սահմանափակի՛ր խորությունը, որ չընկնես շատ խորը։

#%% code
from pathlib import Path

# ...

#%% md
## Մարտահրավեր

#%% md
### 9. Ռեկուրսիան՝ ցիկլով

Ամեն ռեկուրսիա կարելի է գրել ցիկլով՝ օգտագործելով **ցուցակ որպես հերթ**։

Վերագրի՛ր `count_students`-ը առանց ռեկուրսիայի. սկսի՛ր `queue = [school]`-ից,
և ցիկլում ամեն անգամ վերցրո՛ւ մեկ տարր, ավելացրո՛ւ նրա մասերը հերթին։

#%% code
def count_with_queue(school):
    queue = [school]
    total = 0
    # while queue: ...
    return total


# print(count_with_queue(deeper))

#%% md
### 10. Որքա՞ն խորն է Python-ը թույլ տալիս

`import sys` և `sys.getrecursionlimit()` ցույց է տալիս սահմանը։

Գրի՛ր ֆունկցիա, որը կանչում է ինքն իրեն և հաշվում, թե քանի մակարդակ հասավ՝
բռնելով `RecursionError`-ը։

Markdown-ում գրի՛ր՝ ինչո՞ւ է այդ սահմանը ընդհանրապես գոյություն ունի։

#%% code
import sys

print("limit:", sys.getrecursionlimit())
# ...

#%% md
## Ինչի հասանք

- Ֆունկցիան կարող է **կանչել ինքն իրեն** — դրան ասում են ռեկուրսիա
- **Հիմնային դեպքը գրվում է առաջինը** — առանց դրա ֆունկցիան չի կանգնի
- `RecursionError` → հիմնային դեպք չկա, **կամ** կանչը չի մոտենում նրան
- Խորությունը **չի հայտնվում կոդում** — նոր մակարդակ, նույն ֆունկցիան
- Օգտագործվում է, երբ տվյալը **իր մեջ պարունակում է նույն ձևի տվյալ**
- Սովորական ցուցակի համար ռեկուրսիան **ավելի վատ է**, ոչ ավելի լավ

> **Ֆակտորիալ և Ֆիբոնաչի այսօր չկան։** Դրանք ռեկուրսիայի *ալգորիթմական* կողմն են,
> և դրանք դասընթացի երկրորդ մասի թեման են։ Այսօրվանը **կառուցվածքն էր**։

## Հաջորդ անգամ

Երեք գրադարան ներմուծեցինք՝ numpy, matplotlib, pandas։ Բայց որտեղի՞ց են դրանք
եկել, և ի՞նչ անել, երբ պետք է չորրորդը։

Վաղը՝ `pip`, `requirements.txt`, միջավայրեր, և Google Colab։
**Միակ դասն է, որին ինտերնետ է պետք։**
