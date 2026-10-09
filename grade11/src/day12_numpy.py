#%% md
# Օր 12 — Կիսամյակի թվերը

### Python 11-րդ դասարանի համար · Օր 12-ը 24-ից

Նախարարությունը խնդրում է կիսամյակի հաշվետվությունը. **միջին, ամենաբարձր,
ամենացածր**, և թե **որքան ցրված** են գնահատականները՝ ամեն առարկայի և ամեն
դասարանի համար։

Դա 180 թիվ է, 5 առարկա և 3 դասարան։

## ԱՅՍՕՐ:

- **Ա մաս:** թվերը՝ ցիկլով
- **Բ մաս:** առաջին գրադարանը
- **Գ մաս:** երկու տարբերակը կողք կողքի

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
Դպրոցը՝ օբյեկտներով։ <code>Person</code> → <code>Student</code>, <code>Teacher</code>։<br/>
Միջանկյալ թեստը հանձնված է։<br/><br/>
<b>Այսօր առաջին անգամ ներմուծելու ենք բան, որ մենք չենք գրել։</b>
</p>
</div>

#%% md
## Ա մաս: Ցիկլով

Վերցնենք դպրոցի բոլոր գնահատականները մեկ ցուցակում։

#%% code
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

grades = [int(row[3]) for row in rows]

print(len(grades), "grades")
print(grades[:12])

#%% md
Առաջին երեք թիվը հեշտ են՝ դրանք գիտենք անել։

#%% code
total = 0
highest = grades[0]
lowest = grades[0]

for grade in grades:
    total = total + grade
    if grade > highest:
        highest = grade
    if grade < lowest:
        lowest = grade

average = total / len(grades)

print(f"average {average:.2f} · highest {highest} · lowest {lowest}")

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Չորրորդ թիվը ավելի դժվար է։</b> «Որքան ցրված են» նշանակում է՝ միջինից միջին
շեղումը։ Բանաձևը՝ ամեն թվի և միջինի տարբերությունը քառակուսի, գումարել, բաժանել
քանակի վրա, և արմատ։<br/><br/>
Դասի երկրորդ կեսին կստանանք գործիք, որը <b>այս չորսն էլ</b> անում է չորս տողով։
</p>
</div>

**Գործարկի՛ր։**

#%% code
difference_total = 0
for grade in grades:
    difference = grade - average
    difference_total = difference_total + difference * difference

spread = (difference_total / len(grades)) ** 0.5

print(f"spread: {spread:.3f}")

#%% md
Աշխատեց։ Հիմա՝ **նույնը ամեն առարկայի համար**։

Հինգ առարկա × չորս թիվ = քսան հաշվարկ։ Եվ ամեն մեկի համար՝ նոր ցիկլ։

**Հիմա դու։** Լրացրո՛ւ ֆունկցիան, և կանչի՛ր հինգ առարկայի համար։

#%% code
SUBJECTS = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]


def four_numbers(numbers):
    # Return average, highest, lowest and spread -- all four.
    # ...
    return 0, 0, 0, 0


for subject in SUBJECTS:
    subject_grades = [int(row[3]) for row in rows if row[2] == subject]
    # print(subject, four_numbers(subject_grades))

#%% md
## Բ մաս: Առաջին գրադարանը

Այս գործը՝ «շատ թվերի վրա նույն հաշվարկը» — այնքան հաճախ է պետք, որ մարդիկ
գրել են այն **մեկ անգամ, բոլորի համար**։

Գրադարանի անունն է **NumPy**։ Այն արդեն քո համակարգչում է՝ Anaconda-ն բերել է։

#%% code
import numpy as np

numbers = np.array(grades)

print(type(numbers))
print(numbers[:12])

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b><code>import numpy as np</code></b> — ներմուծում ենք և տալիս կարճ անուն։<br/>
<code>as np</code>-ը պարտադիր չէ, բայց <b>այսպես է գրում ամբողջ աշխարհը</b>, և
աշակերտների դասագրքում էլ այդպես է։<br/><br/>
<code>np.array(grades)</code> — սովորական ցուցակից սարքում է <b>զանգված</b>։
</p>
</div>

#%% md
Եվ հիմա՝ չորս թիվը։

#%% code
print(f"average {numbers.mean():.2f}")
print(f"highest {numbers.max()}")
print(f"lowest  {numbers.min()}")
print(f"spread  {numbers.std():.3f}")

#%% md
**Չորս տող։** Եվ `spread`-ը ճիշտ նույն թիվն է, որ հաշվեցինք ցիկլով։

#%% code
print("our loop:", round(spread, 6))
print("numpy:   ", round(numbers.std(), 6))
print("the same?", round(spread, 6) == round(numbers.std(), 6))

#%% md
### Զանգվածը ցուցակ չէ

Մի բան, որ պետք է իմանալ հիմա՝ **զանգվածի բոլոր թվերը պետք է նույն երկարության
լինեն գործողության ժամանակ**։

**Գործարկի՛ր և կարդա՛ սխալը։**

#%% code expected-error: ValueError
first = np.array([7, 6, 8, 9, 8])
second = np.array([10, 9, 10])

print(first + second)

#%% md
<div style="border-left: 6px solid #d33; background: #fff5f5; padding: 12px 16px; margin: 12px 0;">
<p style="color:#d33; margin:0;">
🔍 <b><code>ValueError: operands could not be broadcast together with shapes (5,) (3,)</code></b><br/><br/>
<code>shapes (5,) (3,)</code> — հինգ թիվ և երեք թիվ։ NumPy-ը չգիտի, թե ինչ անի։<br/><br/>
Սովորական ցուցակների դեպքում <code>+</code>-ը դրանք <b>միացնում</b> էր։ Զանգվածի
դեպքում այն <b>գումարում</b> է՝ տարր առ տարր։ Սա կարևոր տարբերություն է։
</p>
</div>

#%% md
## Գ մաս: Հինգ առարկան, չորս տողով

#%% code
print(f"{'subject':<14} {'avg':>6} {'high':>5} {'low':>4} {'spread':>7}")
print("-" * 40)

for subject in SUBJECTS:
    subject_grades = np.array([int(row[3]) for row in rows if row[2] == subject])
    print(f"{subject:<14} {subject_grades.mean():>6.2f} {subject_grades.max():>5} "
          f"{subject_grades.min():>4} {subject_grades.std():>7.3f}")

#%% md
Եվ նույնը՝ դասարանների համար։

#%% code
for class_name in ["11A", "11B", "11C"]:
    class_grades = np.array([int(row[3]) for row in rows if row[0] == class_name])
    print(f"{class_name}  {class_grades.mean():.2f}  spread {class_grades.std():.3f}")

#%% md
### Երկու տարբերակը կողք կողքի

| | Ցիկլով | NumPy-ով |
|---|---|---|
| Միջին | 4 տող | `numbers.mean()` |
| Ամենաբարձր | 3 տող | `numbers.max()` |
| Ամենացածր | 3 տող | `numbers.min()` |
| Ցրվածություն | **6 տող և բանաձև** | `numbers.std()` |
| Հինգ առարկայի համար | **80 տող** | **4 տող ցիկլում** |
| Սխալվելու տեղ | բանաձևում | չկա |

<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<p style="color:#06c; margin:0;">
<b>Ի՞նչ սովորեցինք այսօր՝ բացի NumPy-ից։</b><br/><br/>
Որ կան բաներ, որոնք <b>ուրիշներն արդեն գրել են ճիշտ</b>։ Ցրվածության բանաձևը
գրելու կարիք չկա — կա՛ և ստուգված է։<br/><br/>
Դա չի նշանակում, որ չպետք է իմանալ բանաձևը։ Հենց դրա համար այսօր <b>սկսեցինք
ցիկլից</b>։
</p>
</div>

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Զանգվածից՝ թվեր

Սարքի՛ր զանգված 11A դասարանի գնահատականներից և տպի՛ր չորս թիվը։

#%% code
import numpy as np

# ...

#%% md
### 2. Քանի՞ գնահատական է 4-ից ցածր

Զանգվածի մեջ կարելի է հարցնել՝ «որո՞նք են 4-ից ցածր»։ Պատասխանը նոր զանգված է՝
`True`/`False` արժեքներով։

Գործարկի՛ր առաջին երկու տողը, հետո լրացրո՛ւ երրորդը։

#%% code
numbers = np.array(grades)

below = numbers < 4
print(below[:12])

# sum() on a True/False array counts the Trues. How many are below 4?
# ...

#%% md
### 3. Միայն չանցած գնահատականները

Օգտագործի՛ր `numbers[below]`, որպեսզի ստանաս **միայն** 4-ից ցածր գնահատականները։
Տպի՛ր դրանց քանակը և միջինը։

#%% code
# ...

#%% md
### 4. Ամեն առարկայի աղյուսակը

Գրի՛ր ֆունկցիա, որը ստանում է առարկայի անունը և վերադարձնում է չորս թիվը՝
NumPy-ով։ Կանչի՛ր հինգ առարկայի համար։

#%% code
def subject_numbers(subject):
    # ...
    return 0, 0, 0, 0


# for subject in SUBJECTS:
#     print(subject, subject_numbers(subject))

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Միջնակետը

`np.median()` վերադարձնում է միջնակետը՝ այն թիվը, որից կեսը ցածր է, կեսը՝ բարձր։
Համեմատի՛ր այն միջինի հետ ամբողջ դպրոցի համար։ Ինչո՞ւ են տարբեր։

#%% code
# ...

#%% md
### 6. Կլորացում

`np.round(array, 1)` կլորացնում է **ամբողջ զանգվածը**։ Սարքի՛ր ամեն աշակերտի
միջինների զանգված և կլորացրո՛ւ այն։

#%% code
# ...

#%% md
### 7. Ամենաբարձրի տեղը

`numbers.argmax()` վերադարձնում է ամենամեծ թվի **տեղը**, ոչ թե թիվը։
Օգտագործի՛ր այն՝ գտնելու, թե որ տողում է ամենաբարձր գնահատականը, և տպի՛ր
այդ աշակերտի անունը։

#%% code
# ...

#%% md
### 8. Երկու առարկայի տարբերությունը

Սարքի՛ր երկու զանգված՝ Mathematics-ի և Physics-ի գնահատականները, նույն
աշակերտների համար և նույն կարգով։ Հանի՛ր մեկը մյուսից և տպի՛ր տարբերությունների
միջինը։

**Ուշադի՛ր:** երկու զանգվածը պետք է նույն երկարության լինեն, այլապես՝
այսօրվա `ValueError`-ը։

#%% code
# ...

#%% md
## Մարտահրավեր

#%% md
### 9. Ամբողջ աղյուսակը

Տպի՛ր 3×5 աղյուսակ՝ տողերը դասարաններն են, սյունակները՝ առարկաները, իսկ
բջիջներում՝ միջինները։

```
          Math  Phys   Arm  Hist  Info
11A       7.17  6.50  7.00  7.42  7.75
...
```

#%% code
# ...

#%% md
### 10. Ե՞րբ NumPy-ը չի օգնում

Գրի՛ր երկու ցուցակ՝ 180 թվով, և չափի՛ր, թե որքան է տևում միջինի հաշվարկը
ցիկլով և NumPy-ով։ Օգտագործի՛ր `time.time()`։

Հետո նույնը՝ 2 միլիոն թվով։

Markdown-ում գրի՛ր, թե ե՞րբ արժե NumPy-ը, և ե՞րբ՝ ոչ։

#%% code
import time

# ...

#%% md
## Ինչի հասանք

- `import numpy as np` — **առաջին գրադարանը**, որ մենք չենք գրել
- `np.array(list)` — ցուցակից **զանգված**
- `.mean() .max() .min() .std()` — չորս թիվ, չորս տող
- `+` զանգվածների վրա **գումարում է**, ոչ թե միացնում
- Տարբեր երկարության զանգվածներ → `ValueError: ... shapes (5,) (3,)`
- **Սկսեցինք ցիկլից դիտավորյալ** — որպեսզի իմանաս, թե ինչ է անում գործիքը

## Հաջորդ անգամ

Զանգվածը կսովորի աշխատել **ամբողջությամբ, մեկ տողով** — բոլոր գնահատականները
մեկով բարձրացնել, բոլոր չանցածները առանձնացնել, առանց ոչ մի ցիկլի։
