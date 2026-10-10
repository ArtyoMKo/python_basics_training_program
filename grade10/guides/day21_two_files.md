# Թեմա 21 — Երկու ֆայլ, ամեն մեկը՝ մեկ գործով

**Python զրոյից · Թեմա 21-ը 24-ից**

> **Այս թեման անցնում ենք 20-րդի հետ՝ 16-րդ նիստում**, որի երկրորդ կեսն է։
> Առաջին կեսին `grades.py`-ն արդեն ստեղծել ես և գործարկել տերմինալից։

---

## Նախքան սկսելը

✅ `python grades.py`-ն աշխատում է և տպում քո դասարանի միջինը։

Եթե ոչ — կանգնի՛ր այստեղ և ձեռք բարձրացրու։ Առանց դրա այսօրվա մնացածը չի աշխատի։

---

## Ինչո՞ւ երկու ֆայլ

`grades.py`-ն հիմա երկու գործ է անում՝ **հաշվում է** և **տպում**։

Առայժմ դա խնդիր չէ։ Բայց երբ ուզենաս մենյու, հարցեր, ընտրություն՝ տպելու կոդը
կսկսի ծածկել հաշվարկները, և երկուսն էլ ավելի դժվար կդառնան գտնելը։

Այսօր բաժանում ենք դրանք։

| Ֆայլ | Ի՞նչ է անում |
|---|---|
| `grades.py` | Կարգավորումները և **հաշվարկները**։ Տպելու մասին ոչինչ չգիտի։ |
| `main.py` | **Խոսում է ուսուցչի հետ**՝ հարցնում, կանչում, տպում։ Ինքը ոչինչ չի հաշվում։ |

> **Ահա այն հարցը, որ այսուհետ որոշում է՝ որ ֆայլում գրել նոր կոդ։**
>
> **Հաշվո՞ւմ է → `grades.py`։ Մարդո՞ւ հետ է խոսում → `main.py`։**
>
> Հաջորդ նիստում կավելանա երրորդ պատասխան։ 11-րդ դասարանի դասընթացում՝ հինգ։
> Հարցը նույնն է։

---

## Քայլ 1 — `grades.py`-ի վերևը՝ կարգավորումները

Բացի՛ր `grades.py`-ն։ Ամենավերևում, ֆունկցիաներից **առաջ**, գրի՛ր՝

```python
# ----- կարգավորումներ -----

PASS_MARK = 4
DECIMAL_PLACES = 1
NAME_WIDTH = 12
```

`PASS_MARK`-ն արդեն այնտեղ է՝ առաջին կեսից։ Ավելացրո՛ւ մյուս երկուսը նրա կողքին։

> **Սա 9-րդ թեմայի դասն է՝ տեղը գտած։** Այնտեղ սովորեցինք, որ կարևոր թիվը անուն է
> ստանում։ Հիմա բոլոր այդ անունները **մեկ տեղում են**՝ ֆայլի վերևում, որ չփնտրես։

---

## Քայլ 2 — `grades.py`-ի մնացածը՝ հաշվարկները

Ֆունկցիաներից ներքև ավելացրո՛ւ ևս երեքը՝ 19-րդ թեմայի տետրից։

```python
def class_average(class_grades):
    """Return the average grade of the whole class."""
    if len(class_grades) == 0:
        return 0
    total = 0
    for name in class_grades:
        total = total + class_grades[name]
    return round(total / len(class_grades), DECIMAL_PLACES)


def failing_students(class_grades):
    """Return the names of the students below PASS_MARK."""
    names = []
    for name in class_grades:
        if class_grades[name] < PASS_MARK:
            names.append(name)
    return names


def highest_of(class_grades):
    """Return the highest grade in the class."""
    if len(class_grades) == 0:
        return 0
    return max(class_grades.values())
```

Նկատի՛ր՝ ոչ մեկը **չի տպում**։ Բոլորն էլ **վերադարձնում են**։ Տպելը `main.py`-ի գործն է։

✅ **ՍՏՈՒԳՈՒՄ։** `python grades.py` — դեռ աշխատում է, դեռ տպում է միջինը
(վերջի `if __name__ == "__main__":` բլոկի շնորհիվ)։

---

## Քայլ 3 — `main.py`

Ստեղծի՛ր **նոր** ֆայլ՝ `grades.py`-ի **կողքին**, նույն թղթապանակում՝ `main.py`։

```python
"""The menu: ask, call, print. This file calculates nothing itself."""

import grades


def show_register(class_grades):
    for name in class_grades:
        grade = class_grades[name]
        if grades.has_passed(grade):
            mark = "passed"
        else:
            mark = "failed"
        print(f"{name:<{grades.NAME_WIDTH}} {grade:>3}  {mark}")
    print(f"Class average: {grades.class_average(class_grades)}")


def show_failing(class_grades):
    names = grades.failing_students(class_grades)
    if len(names) == 0:
        print("Nobody is failing.")
        return
    print(f"Did not pass ({len(names)} students):")
    for name in names:
        print(" -", name)


def main():
    # For now the register lives here, exactly as it did in the notebook.
    # In the next session it moves into a file of its own.
    class_grades = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3, "Mariam": 8}

    while True:
        print()
        print("1 - show the register")
        print("2 - show who did not pass")
        print("3 - quit")
        answer = input("Choose: ")

        if answer == "1":
            show_register(class_grades)
        elif answer == "2":
            show_failing(class_grades)
        elif answer == "3":
            print("Goodbye.")
            return
        else:
            print("Type 1, 2 or 3.")


if __name__ == "__main__":
    main()
```

> **`import grades`** — մեկ տող, և `main.py`-ն կարող է կանչել `grades.py`-ի ամեն ինչ՝
> `grades.has_passed(...)`, `grades.class_average(...)`, `grades.NAME_WIDTH`։
>
> Ուշադի՛ր՝ **ոչ մի հաշվարկ չկա `main.py`-ում**։ Նա հարցնում է, կանչում և տպում։

---

## Քայլ 4 — Գործարկի՛ր

Տերմինալում, նույն թղթապանակից՝

```
python main.py
```

Սեղմի՛ր `1`։

✅ **ՍՏՈՒԳՈՒՄ։** Տպվում է հինգ աշակերտ, ամեն մեկի դիմաց `passed` կամ `failed`,
և վերջում՝ **`Class average: 7.2`**։

Սեղմի՛ր `2` → երևում է `Aram`։ Սեղմի՛ր `3` → ծրագիրը ավարտվում է։

> **Սա քո առաջին իսկական ծրագիրն է։** Ոչ թե տետր՝ բջիջներով, այլ ծրագիր, որը
> գործարկվում է տերմինալից և խոսում քեզ հետ։

---

## Քայլ 5 — Մեկ տող, ամբողջ ծրագիրը

Հիմա ամենակարևորը այսօրվա մեջ։

1. Բացի՛ր **`grades.py`**-ն և վերևում փոխի՛ր՝ `PASS_MARK = 8`
2. Պահի՛ր
3. Գործարկի՛ր `python main.py` և սեղմի՛ր `1`, հետո `2`

✅ **ՍՏՈՒԳՈՒՄ։** Հիմա `Davit`-ը (6) նույնպես `failed` է, և `2`-ը ցույց է տալիս
**երեք** աշակերտի։ **Իսկ `main.py`-ին ձեռք չես տվել։**

Վերադարձրո՛ւ `PASS_MARK = 4` և պահի՛ր։

> **Ահա թե ինչու են կարգավորումները ֆայլի վերևում։** Դպրոցը փոխում է անցողիկ նիշը՝
> փոխում ես **մեկ տող, մեկ տեղում**։ Ոչ թե փնտրում ես `4`-ը քսան տեղում։

---

## 📦 Այսօրվա արդյունքը

- **`python main.py`-ն աշխատում է** — երկու ֆայլ, մեկ ծրագիր
- `grades.py` հաշվում է, `main.py` խոսում է քեզ հետ
- Մեկ տող `grades.py`-ի վերևում փոխում է ամբողջ ծրագրի պահվածքը

---

## Եթե ինչ-որ բան չի աշխատում

| Սխալ | Ի՞նչ է նշանակում |
|---|---|
| `ModuleNotFoundError: No module named 'grades'` | Երկու ֆայլերը նույն թղթապանակում չեն, կամ տերմինալը այլ թղթապանակում է |
| `AttributeError: module 'grades' has no attribute ...` | Ֆունկցիայի անվան մեջ տառասխալ է, կամ այն `grades.py`-ում չկա |
| `NameError: name 'grades' is not defined` | `import grades` տողը բացակայում է `main.py`-ի վերևում |
| Ոչինչ չի տպվում | `if __name__ == "__main__":` բլոկը բացակայում է `main.py`-ի վերջում |

---

## Ի՞նչ է գալիս հետո

Ծրագիրդ աշխատում է, բայց դասարանը **գրված է կոդի մեջ**։ Ավելացնել աշակերտ
նշանակում է խմբագրել ծրագիրը, և փակելուց հետո ամեն փոփոխություն վերանում է։

Հաջորդ նիստում դա ուղղում ենք՝ և կհայտնվի **երրորդ ֆայլը**։
