# Թեմա 22 — Հինգ ֆայլ, ամեն մեկը՝ մեկ գործով

**Python 11-րդ դասարանի համար · Թեմա 22-ը 24-ից**

Քսանմեկ օր աշխատեցինք նոթատետրում։ Նոթատետրը **արհեստանոց** է — այնտեղ փորձում
ես, սխալվում, նորից փորձում։

Բայց գործընկերոջդ դու չես տալիս արհեստանոցը։ Տալիս ես **պատրաստի գործիքը**։

Այսօր ամեն ինչ դուրս է գալիս նոթատետրից։

---

## Ինչո՞ւ հինգ ֆայլ, ոչ թե մեկ

Ամբողջ ծրագիրը կարելի էր գրել մեկ `main.py`-ում՝ մոտ 200 տող։ Կաշխատեր։

Բայց երբ կիսամյակի վերջում տնօրենը խնդրի նոր գծապատկեր, դու պետք է գտնես այն
20 տողը 200-ի մեջ։ Իսկ երբ նախարարությունը փոխի ֆայլի ձևը — ևս 30 տող, ուրիշ տեղում։

**Հինգ ֆայլ, հինգ գործ։ Ամեն փոփոխություն ունի իր հասցեն։**

```
school_report/
├── settings.py     ամեն թիվ և անուն — ոչ մի հաշվարկ
├── people.py       Person · Student · Teacher · SchoolClass · School
├── loading.py      ՄԻԱԿ ֆայլը, որը գիտի, որ CSV-ն գոյություն ունի
├── charts.py       երկու գծապատկեր, երկու ֆունկցիա
├── main.py         մուտքի կետը — կարդա, տպիր, պահպանիր
├── data/
│   └── school.csv
└── output/         գծապատկերները գրվում են այստեղ
```

### Ո՞ր ֆայլում է գրվում նոր կոդը

Մեկ հարց է որոշում.

| Հարցը | Ֆայլը |
|---|---|
| Թիվ է, որը կարող է փոխվել։ | `settings.py` |
| Մարդու կամ դասարանի մասին է։ | `people.py` |
| Ֆայլ է կարդում կամ գրում։ | `loading.py` |
| Նկար է սարքում։ | `charts.py` |
| Մարդու հետ է խոսում՝ տպում, հարցնում։ | `main.py` |

> **Եթե երկու պատասխան է համապատասխանում** — նշանակում է գործը երկուսն է, և պետք է
> բաժանել։ Օրինակ՝ «կարդա ֆայլը և նկարիր» = `loading.py` **և** `charts.py`։

---

## Ա մաս — Պատրաստվել (5 րոպե)

1. VS Code-ում սարքի՛ր նոր թղթապանակ՝ `school_report`
2. Ներսում՝ ևս երկուսը՝ `data` և `output`
3. Պատճենի՛ր `school.csv`-ը `data`-ի մեջ
4. Բացի՛ր տերմինալը՝ **Terminal → New Terminal**
5. `cd school_report`

---

## Բ մաս — `settings.py` (8 րոպե)

Սկսում ենք ամենահեշտից։ Այս ֆայլում **ոչ մի հաշվարկ չկա** — միայն արժեքներ։

```python
"""Every number and name the report depends on, in one place."""

from pathlib import Path

SCHOOL_NAME = "School N 5"
TERM = "Term 1"

PASS_MARK = 4
LOWEST_GRADE = 1
HIGHEST_GRADE = 10

SUBJECTS = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]

HERE = Path(__file__).resolve().parent
DATA_FILE = HERE / "data" / "school.csv"
OUTPUT_DIR = HERE / "output"

FIGURE_SIZE = (8, 4)
DPI = 150
BAR_COLOUR = "#44aa77"
HISTOGRAM_COLOUR = "#4477aa"
```

**Գործարկի՛ր՝ `python settings.py`**

Ոչինչ չի տպվում։ **Դա ճիշտ է։** Ֆայլը միայն արժեքներ է սահմանում։

> `Path(__file__).resolve().parent` նշանակում է «այն թղթապանակը, որտեղ այս ֆայլն է»։
> Առանց դրա ծրագիրը կաշխատեր միայն այն դեպքում, երբ տերմինալը ճիշտ թղթապանակում է։

---

## Գ մաս — `people.py` (10 րոպե)

Տեղափոխի՛ր 11-րդ թեմայի դասերը։ Վերևում՝ մեկ ներմուծում.

```python
import settings
```

Հետո՝ `Person`, `Student`, `Teacher`, `SchoolClass`, `School` — ուղիղ այնպես, ինչպես
նոթատետրում։ Երկու տարբերություն.

- `PASS_MARK`-ի փոխարեն գրի՛ր `settings.PASS_MARK`
- `SUBJECT_NAMES`-ի փոխարեն՝ `settings.SUBJECTS`

**Գործարկի՛ր՝ `python people.py`** → նորից ոչինչ։ Նորից ճիշտ է։

> **Ստուգո՞ւմ ես, թե աշխատում է։** Տերմինալում՝ `python`, հետո՝
> `import people`, հետո՝ `people.Student("Ani Hakobyan", "11A", {"Physics": 8})`։
> Դուրս գալու համար՝ `exit()`։

---

## Դ մաս — `loading.py` և `charts.py` (18 րոպե)

### `loading.py`

Սա **միակ ֆայլն է, որը գիտի, որ CSV գոյություն ունի**։ Եթե վաղը նախարարությունը
անցնի Excel-ի, փոխվում է միայն այս ֆայլը։

```python
import pandas as pd

import settings
from people import School, SchoolClass, Student

REQUIRED_COLUMNS = ["class", "student", "subject", "grade"]
```

Երկու ֆունկցիա՝

- `read_table(path=None)` — կարդում է և **ստուգում**. սյունակները տեղո՞ւմ են,
  գնահատականները 1–10 միջակայքո՞ւմ են։ Սա 21-րդ թեմայի `assert`-ի գաղափարն է։
- `build_school(path=None)` — տողերից սարքում է `School` → `SchoolClass` → `Student`

### `charts.py`

```python
import matplotlib.pyplot as plt

import settings
```

Երկու ֆունկցիա, 18-րդ թեմայինից՝ `save_subject_chart(school, path)` և
`save_distribution_chart(school, path)`։

Ամեն մեկը ստանում է դպրոցը և ֆայլի անունը, և **ոչինչ չի վերադարձնում**։

> **Ինչո՞ւ են գծապատկերները ֆունկցիա, ոչ թե ուղիղ կոդ։** Որովհետև վաղը նույն
> գծապատկերը պետք կլինի 11A-ի համար առանձին։ Ֆունկցիան կանչում ես նորից։ Կոդը
> պատճենում ես։

---

## Ե մաս — `main.py` (16 րոպե)

Վերջին ֆայլը։ Այն **միակն է, որը խոսում է մարդու հետ**։

```python
import sys

import settings
from charts import save_distribution_chart, save_subject_chart
from loading import build_school


def print_summary(school):
    ...


def main():
    try:
        school = build_school()
    except FileNotFoundError:
        print(f"Could not find {settings.DATA_FILE}")
        return 1
    except ValueError as problem:
        print(f"The file is not in the expected shape: {problem}")
        return 1

    print_summary(school)

    settings.OUTPUT_DIR.mkdir(exist_ok=True)
    save_subject_chart(school, settings.OUTPUT_DIR / "subjects.png")
    save_distribution_chart(school, settings.OUTPUT_DIR / "distribution.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

### Եվ հիմա՝

```bash
python main.py
```

**Պետք է տեսնես.**

```
School N 5 — Term 1
==============================================
classes:            3
students:          36
school average:   7.0
```

Եվ `output/` թղթապանակում՝ երկու PNG։ **Բացի՛ր դրանք։**

---

## Ստուգի՛ր ինքդ քեզ

- [ ] `python main.py` աշխատում է
- [ ] Դպրոցի միջինը **7.0** է
- [ ] Ռիսկի տակ **12** աշակերտ է
- [ ] `output/`-ում երկու նկար կա, և դրանք բացվում են
- [ ] Փոխի՛ր `PASS_MARK`-ը 5-ի `settings.py`-ում → ռիսկի թիվը փոխվում է
- [ ] Վերադարձրո՛ւ 4-ը

> **Վերջին կետը ամենակարևորն է։** Մեկ տող փոխեցիր մեկ ֆայլում, և ամբողջ
> հաշվետվությունը փոխվեց։ Հենց դրա համար են հինգ ֆայլը։

---

## Եթե չաշխատեց

| Սխալ | Պատճառ |
|---|---|
| `ModuleNotFoundError: No module named 'settings'` | տերմինալը այլ թղթապանակում է — `cd school_report` |
| `FileNotFoundError` | `school.csv`-ը `data/`-ում չէ |
| `ImportError: cannot import name ...` | ֆունկցիայի անունը այլ է գրված երկու ֆայլում |
| Ոչինչ չի տպվում | `if __name__ == "__main__":` բլոկը բացակայում է |

**Դասի վերջում դասավանդողը ստուգում է ամեն մասնակցի `python main.py`-ն
առանձին, ընդհանուր էկրանի վրա։** Ոչ ոք չի հեռանում կոտրված ծրագրով։
