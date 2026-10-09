# Հուշաթերթ — 11-րդ դասարանի դասընթաց

Տպի՛ր և պահի՛ր կողքիդ։ Այստեղ **միայն այն է, ինչ սովորել ենք այս դասընթացում** —
10-րդ դասարանի հիմունքները այնտեղի հուշաթերթում են։

---

## Ֆունկցիաներ

```python
def report(name, grade, pass_mark=4):     # կանխադրված արժեքը ՎԵՐՋՈՒՄ է
    return f"{name}: {grade}"

report("Ani", 9)                          # pass_mark-ը 4 է
report("Ani", 9, 7)                       # ըստ դիրքի
report("Ani", 9, pass_mark=7)             # ըստ անվան — ավելի պարզ

def stats(grades):
    return min(grades), max(grades)       # մի քանի արժեք

lowest, highest = stats([7, 9, 3])        # unpacking

def total(*numbers):                      # ցանկացած թվով արգումենտ
    return sum(numbers)
```

> **Երբեք** `def f(items=[])` — կանխադրված ցուցակը **կիսվում է բոլոր կանչերի միջև**։
> Գրի՛ր `def f(items=None)` և ներսում՝ `if items is None: items = []`։

## Մեկ տողով ցուցակ և բառարան

```python
[name for name in register]                      # բոլորը
[name for name in register if register[name] > 7]   # զտել   — if ՎԵՐՋՈՒՄ
["+" if register[n] >= 4 else "-" for n in register]  # ընտրել — if ՍԿԶԲՈՒՄ

{name: register[name] for name in register}      # բառարան — երկու կետով
{row[1] for row in rows}                         # set — առանց երկու կետի

sorted(register, key=lambda name: register[name])              # ըստ գնահատականի
sorted(register, key=lambda name: register[name], reverse=True)[:5]   # լավագույն 5
```

| `if`-ը որտեղ է | Ի՞նչ է անում |
|---|---|
| **վերջում** | **զտում** — չհամապատասխանողները ցուցակում չեն |
| **ձախում**, `else`-ով | **ընտրում** — բոլորը ցուցակում են |

## Բառարան

```python
grades["Physics"]            # չկա՞ → KeyError
grades.get("Physics")        # չկա՞ → None
grades.get("Physics", 0)     # չկա՞ → 0
```

## Դասեր

```python
class Student:
    def __init__(self, name, grades):     # կանչվում է Student(...) գրելիս
        self.name = name                  # self = այն մեկը, որ հիմա սարքվում է
        self.grades = grades

    def average(self):                    # մեթոդ
        return sum(self.grades) / len(self.grades)

    def __str__(self):                    # կանչվում է print(student) գրելիս
        return f"{self.name}: {self.average():.1f}"

ani = Student("Ani", [7, 9])
ani.average()         # փակագծերը ՊԱՐՏԱԴԻՐ են
ani.average           # առանց դրանց՝ ֆունկցիան ինքը, ոչ թե պատասխանը
```

## Ժառանգականություն

```python
class Person:
    def __init__(self, name):
        self.name = name

    def label(self):
        return self.name


class Student(Person):                    # ժառանգում է Person-ից
    def __init__(self, name, grades):
        super().__init__(name)            # ԱՌԱՋԻՆ ՏՈՂԸ — գրեթե միշտ
        self.grades = grades

    def label(self):                      # վերասահմանում
        return super().label() + " (student)"
```

> **«X-ը Y է»** → ժառանգում։ **«X-ը ունի Y»** → ցուցակ, ոչ թե ժառանգում։

## NumPy

```python
import numpy as np

a = np.array([7, 6, 8, 9])
a.mean()   a.max()   a.min()   a.std()     # չորս թիվ, չորս տող

a + 1          a * 10          a ** 2      # ամբողջ զանգվածի վրա
a < 4                                      # True/False զանգված
(a < 4).sum()                              # քանիսն են
a[a < 4]                                   # միայն դրանք

a[(a >= 5) & (a <= 7)]     # ԵՎ  — & , ոչ թե and, ամեն պայմանը փակագծում
a[(a <= 2) | (a >= 9)]     # ԿԱՄ — |

table.shape                 # (տողեր, սյունակներ)
table.mean(axis=0)          # սյունակների երկայնքով → մեկ թիվ ամեն սյունակի
table.mean(axis=1)          # տողերի երկայնքով     → մեկ թիվ ամեն տողի
```

## pandas

```python
import pandas as pd

data = pd.read_csv("school.csv")

data.shape                  data.head()            data.columns.tolist()
data["grade"].mean()        data["grade"].describe()
data["subject"].unique()    data["student"].nunique()
data.isna().sum()           # որտեղ են դատարկ բջիջները

data[data["class"] == "11A"]                            # զտել
data[(data["class"] == "11A") & (data["grade"] < 4)]    # երկու պայման

data.groupby("class")["grade"].mean()
data.groupby("class")["grade"].agg(["mean", "min", "max", "std"])
data.pivot_table(index="class", columns="subject", values="grade")

data.to_csv("out.csv")
```

## Matplotlib

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4))
plt.bar(names, values)          # կատեգորիաներ
plt.barh(names, values)         # հորիզոնական — երկար անունների համար
plt.hist(numbers, bins=range(1, 12))   # բաշխվածություն
plt.plot(x, y, marker="o")      # բնական կարգ

plt.ylim(0, 10)
plt.title("...")    plt.xlabel("...")    plt.ylabel("...")
plt.axhline(y=7.0, color="red", linestyle="--", label="average")
plt.legend()
plt.tight_layout()
plt.savefig("chart.png", dpi=150)
plt.close()                     # ՄԻՇՏ, որ հաջորդը մաքուր սկսվի
```

| Գծապատկեր | Ե՞րբ |
|---|---|
| `bar` | կատեգորիաներ՝ առարկա, դասարան |
| `hist` | մեկ շարք թվեր — «ինչպե՞ս են ցրված» |
| `plot` | բնական կարգ՝ 1…10, ամիսներ |

## Ռեկուրսիա

```python
def count(part):
    if "students" in part:              # ՀԻՄՆԱՅԻՆ ԴԵՊՔԸ ԱՌԱՋԻՆՆ Է
        return len(part["students"])
    total = 0
    for smaller in part["parts"]:
        total = total + count(smaller)  # կանչ ինքն իրեն՝ ԱՎԵԼԻ ՓՈՔՐ խնդրի վրա
    return total
```

> `RecursionError` → կա՛մ հիմնային դեպք չկա, կա՛մ կանչը **չի մոտենում** նրան։

## Վրիպազերծում

```python
assert len(rows) > 0, "no rows for this class"     # լուռ սխալը դարձնել բարձրաձայն
```

**Traceback-ը կարդա՛ ներքևից վերև.** վերջին տողը՝ *ի՞նչ*, նախավերջինը՝ *որտե՞ղ*,
վերևինները՝ *ինչպե՞ս հասանք այնտեղ*։ Երկար traceback-ում գտի՛ր **քո ֆայլի անունը**։

---

## Բառարան

| Հայերեն | English | Ի՞նչ է |
|---|---|---|
| դաս | class | ձևանմուշ՝ ինչ ունի և ինչ կարող է անել օբյեկտը |
| օբյեկտ | object | դասից սարքված մեկ օրինակ |
| մեթոդ | method | դասի ներսում գրված ֆունկցիա |
| հատկություն | attribute | օբյեկտի տվյալը՝ `student.name` |
| ժառանգականություն | inheritance | «ամեն ինչ, ինչ ունի, գումարած» |
| վերասահմանում | overriding | ժառանգած մեթոդը նորից գրել |
| բազմաձևություն | polymorphism | մեկ կանչ, ամեն օբյեկտ պատասխանում է իր ձևով |
| ռեկուրսիա | recursion | ֆունկցիա, որը կանչում է ինքն իրեն |
| հիմնային դեպք | base case | այնտեղ, որտեղ ռեկուրսիան կանգնում է |
| զանգված | array | NumPy-ի թվերի շարք |
| գրադարան | library | ուրիշի գրած կոդ, որը ներմուծում ես |
| փաթեթ | package | տեղադրվող գրադարան |
| միջավայր | environment | առանձին տեղ՝ մեկ ծրագրի փաթեթների համար |
| բաշխվածություն | distribution | ինչպես են թվերը ցրված |
| վրիպազերծում | debugging | սխալը գտնելու աշխատանք |
