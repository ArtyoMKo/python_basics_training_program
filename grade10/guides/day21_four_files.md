# Թեմա 21 — Չորս ֆայլ, ամեն մեկը՝ մեկ գործով

**Python զրոյից · Թեմա 21-ը 24-ից**

Այսօր դասընթացի առանցքային օրն է։ Վերջում ունենալու ես **աշխատող ծրագիր**։

---

## Նախքան սկսելը

✅ **ՍՏՈՒԳՈՒՄ։** Տերմինալում գործարկի՛ր՝

```
python grades.py
```

Պետք է տպի միջինը։ **Եթե չի աշխատում — ասա՛ հիմա**, նախքան որևէ բան փոխելը։

---

## Ինչո՞ւ չորս ֆայլ

Այս պահին քո `grades.py`-ն երեք տարբեր գործ է անում՝ հաշվում է, պահում է տվյալները,
և տպում է։

Երբ ամեն ինչ մեկ տեղում է, երկու բան է լինում.

- Երբ ուզում ես փոխել, թե **ինչպես է տպվում**, ստիպված ես դիպչել հաշվարկներին։
- Երբ ինչ-որ բան սխալ է, չգիտես՝ **որտեղ** փնտրել։

Ուստի բաժանում ենք։ **Ամեն ֆայլ՝ մեկ գործ, մեկ նախադասությամբ բացատրելի։**

| Ֆայլ | Ի՞նչ է անում |
|---|---|
| `settings.py` | Բոլոր թվերը, որ կարող ես ուզենալ փոխել։ **Տրամաբանություն չկա։** |
| `storage.py` | Կարդում է դասարանը ֆայլից և գրում ետ։ **Գնահատականների մասին ոչինչ չգիտի։** |
| `grades.py` | Հաշվարկները։ **Ֆայլերի մասին ոչինչ չգիտի։** |
| `main.py` | Խոսում է ուսուցչի հետ։ **Ինքը ոչինչ չի հաշվում։** |

> **Կարևոր կանոն.** `grades.py`-ն **չպետք է** ներմուծի `storage.py`-ն։
>
> Ինչո՞ւ. որովհետև այդպես կարող ես ստուգել հաշվարկները՝ առանց ֆայլ ունենալու։
> Եթե միջինը սխալ է, գործարկում ես `python grades.py` և գիտես, որ ֆայլը մեղավոր չէ։

---

## Քայլ 1 — `settings.py`

Ստեղծի՛ր նոր ֆայլ՝ **`settings.py`**, և գրի՛ր՝

```python
"""Every number the program uses, in one place."""

# The pass mark. Change it to match your school.
PASS_MARK = 4

# Which file holds the class?
CLASS_FILE = "data/sample_class.csv"

# How many digits after the decimal point?
DECIMAL_PLACES = 1

# How wide is the name column when printing?
NAME_WIDTH = 12
```

✅ **ՍՏՈՒԳՈՒՄ։** Գործարկի՛ր՝ `python settings.py`

**Ոչինչ չի տպվի, և սխալ չի լինի։** Դա ճիշտ է։ Այս ֆայլը գործ չի անում —
այն **որոշումներ է պահում**։

> Հիշո՞ւմ ես 9-րդ թեման՝ քսանհինգ տեղում գրված `4`-ը։ Այս ֆայլը այդ դասն է։
> Երբ ուզում ես ինչ-որ բան փոխել ծրագրում, **նախ նայի՛ր այստեղ**։

---

## Քայլ 2 — `data` թղթապանակը

`python_course`-ի ներսում ստեղծի՛ր թղթապանակ՝ **`data`**։

Դի՛ր այնտեղ `sample_class.csv`-ը, որ ուսուցիչը տվել է։ Բացի՛ր և նայի՛ր՝

```
name,grade
Ani,9
Davit,6
```

Առաջին տողը վերնագիրն է։ Հետո՝ մեկ տող՝ մեկ աշակերտի համար, ստորակետով բաժանված։

✅ **ՍՏՈՒԳՈՒՄ։** `data/sample_class.csv`-ը կա և ունի 13 տող (վերնագիր + 12 աշակերտ)։

---

## Քայլ 3 — `storage.py`

Ստեղծի՛ր **`storage.py`**՝

```python
"""Read the class from a file and write it back."""

from pathlib import Path

import settings


def load_class(file_name=settings.CLASS_FILE):
    """Read the file and return a dictionary, like {"Ani": 9}."""
    path = Path(file_name)

    if not path.exists():
        print(f"Could not find {file_name}")
        return {}

    lines = path.read_text(encoding="utf-8").strip().splitlines()

    class_grades = {}

    for line in lines[1:]:
        parts = line.split(",")
        student_name = parts[0].strip()
        class_grades[student_name] = int(parts[1].strip())

    return class_grades


if __name__ == "__main__":
    print(load_class())
```

Երեք նոր բան, և միայն երեքը.

- `import settings` — վերցնում է մյուս ֆայլից։ Օգտագործում ենք որպես `settings.PASS_MARK`։
- `path.read_text(encoding="utf-8")` — կարդում է ամբողջ ֆայլը։ **`encoding="utf-8"`-ը
  պարտադիր է**, այլապես հայերեն անունները կկոտրվեն։
- `line.split(",")` — կտրում է տողը ստորակետով և տալիս ցուցակ՝ `["Անի", "9"]`։

Իսկ `lines[1:]`-ը 7-րդ թեմայի կտրելն է՝ «առաջինից բացի բոլորը», որովհետև առաջինը
վերնագիրն է։

✅ **ՍՏՈՒԳՈՒՄ։** `python storage.py` տպում է բառարանը՝ 12 աշակերտով, հայերեն
անուններով։

> **Եթե հայերենը կոտրված է** — ստուգի՛ր `encoding="utf-8"`-ը։
> **Եթե `FileNotFoundError` է** — `data` թղթապանակը սխալ տեղում է։

---

## Քայլ 4 — `grades.py`-ն կապել `settings.py`-ին

Բացի՛ր երեկվա `grades.py`-ն։ Վերևում ջնջի՛ր `PASS_MARK = 4` տողը և փոխարենը գրի՛ր՝

```python
import settings
```

Հետո ամենուր, որտեղ գրված է `PASS_MARK`, գրի՛ր `settings.PASS_MARK`։

```python
def has_passed(grade, pass_mark=settings.PASS_MARK):
    return grade >= pass_mark
```

Ավելացրո՛ւ նաև մեկ նոր ֆունկցիա, որը վաղը պետք կգա՝

```python
def class_average(class_grades):
    """Return the average grade of the whole class."""
    return average_of(list(class_grades.values()))
```

✅ **ՍՏՈՒԳՈՒՄ։** `python grades.py` դեռ աշխատում է։

✅ **ԵՐԿՐՈՐԴ ՍՏՈՒԳՈՒՄ։** Բացի՛ր `settings.py`-ն, փոխի՛ր `PASS_MARK`-ը 8-ի, պահի՛ր,
գործարկի՛ր `python grades.py` նորից։ **Արդյունքը պետք է փոխվի։**

Հետո փոխի՛ր ետ 4-ի։ **Մեկ խմբագրում, ամբողջ ծրագրի համար։**

---

## Քայլ 5 — `main.py`

Վերջին ֆայլը։ Ստեղծի՛ր **`main.py`**՝

```python
"""Register - a program for teachers."""

import grades
import settings
import storage


def show_register(class_grades):
    """Print the whole register."""
    print()
    print("=== REGISTER ===")

    for student_name, grade in class_grades.items():
        if grades.has_passed(grade):
            result = "passed"
        else:
            result = "failed"
        print(f"{student_name:<{settings.NAME_WIDTH}} {grade:>3}   {result}")

    print()
    print(f"students:      {len(class_grades)}")
    print(f"class average: {grades.class_average(class_grades)}")


def main():
    class_grades = storage.load_class()

    while True:
        print()
        print("1 - show the register")
        print("2 - quit")

        choice = input("Choose: ").strip()

        if choice == "1":
            show_register(class_grades)
        elif choice == "2":
            print("Goodbye.")
            break
        else:
            print("No such command.")


if __name__ == "__main__":
    main()
```

Ուշադրություն՝ **`main.py`-ն ինքը ոչինչ չի հաշվում**։ Նա հարցնում է, հետո խնդրում է
`storage`-ին կարդալ և `grades`-ին հաշվել։

Եվ ուշադրություն՝ `grades.has_passed(...)` — ֆայլի անունը, կետ, ֆունկցիայի անունը։
Ուղիղ այնպես, ինչպես `student_names.append(...)`-ը 7-րդ թեման։

---

## Քայլ 6 — Գործարկի՛ր

```
python main.py
```

✅ **ՍՏՈՒԳՈՒՄ։** Տեսնում ես մենյուն։ Գրի՛ր `1` → տպվում է մատյանը՝ 12 աշակերտ,
միջինը 6.5։ Գրի՛ր `2` → դուրս ես գալիս։

**Սա ծրագիր է։ Դու գրեցիր այն։**

---

## 📦 Այսօրվա արդյունքը

**Աշխատող `python main.py`** — չորս ֆայլից բաղկացած իսկական ծրագիր, գործարկված
տերմինալից։

> **Ուսուցիչը այսօր անձամբ ստուգում է ամեն մասնակցի մոտ, որ `python main.py`-ն
> աշխատում է, նախքան դասը ավարտելը։** Եթե քոնը չի աշխատում — ասա՛։ Դա այսօրվա
> միակ կարևոր բանն է։

---

## Եթե ինչ-որ բան չի աշխատում

| Սխալը | Ի՞նչ է նշանակում |
|---|---|
| `ModuleNotFoundError: No module named 'settings'` | Չորս ֆայլերը նույն թղթապանակում չեն |
| `FileNotFoundError` | `data` թղթապանակը սխալ տեղում է, կամ սխալ թղթապանակից ես գործարկում |
| Հայերենը կոտրված է | `encoding="utf-8"`-ը մոռացվել է |
| `AttributeError: module 'grades' has no attribute ...` | Ֆունկցիայի անվան մեջ տառասխալ է |
| Ոչինչ չի տպվում | `main()`-ը չի կանչվել՝ ստուգի՛ր վերջին երկու տողը |

**Եթե շատ ես ետ մնացել՝** ուսուցիչը ունի պատրաստի `gradebook/` թղթապանակը։
Վերցրո՛ւ այն, **կարդա՛ ամեն ֆայլը**, հասկացի՛ր, և հետո գրի՛ր քոնը։ Պատճենելը առանց
կարդալու օգուտ չի տա։

## Ի՞նչ է գալիս հետո

Ծրագիրը աշխատում է, բայց այն **ուրիշի դասարանով** է։ Հաջորդ դասին այնտեղ կդնես
քո դասարանը — և կսովորես, թե ինչպես պահպանել փոփոխությունները։
