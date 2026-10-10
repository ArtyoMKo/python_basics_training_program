# Թեմա 22 — Քո դասարանը, պահպանված

**Python զրոյից · Թեմա 22-ը 24-ից**

> **17-րդ նիստ։** Ծրագիրդ աշխատում է, բայց դասարանը գրված է կոդի մեջ։

---

## 🛑 Կարդա՛ սա նախքան քո տվյալները մուտքագրելը

Այսօր ներս ես բերելու **քո իսկական դասարանը**։

- Օգտագործի՛ր **միայն անուն և գնահատական**։ Ոչ ազգանուն, ոչ ծննդյան տարեթիվ, ոչ հասցե։
- Ֆայլը մնում է **քո համակարգչում**։ Ոչ ոք այն չի տեսնում, ներառյալ դասավանդողը։
- Եթե նախընտրում ես՝ օգտագործի՛ր հորինված անուններ։ Վարժությունը նույնն է։

---

## Քայլ 1 — Այն, ինչ հիմա ունենք

Բացի՛ր `main.py`-ն և նայի՛ր այս տողին՝

```python
class_grades = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3, "Mariam": 8}
```

**Դասարանը ծրագրի ներսում է։**

Արա՛ հետևյալը, ուշադիր նայելով, թե ինչ է լինում՝

1. Ավելացրո՛ւ երեք աշակերտ՝ ուղիղ այդ տողում։ Պահի՛ր։ Գործարկի՛ր՝ երևում են։
2. Սեղմի՛ր `3` և դուրս արի։
3. Գործարկի՛ր նորից։ Երեքն էլ տեղում են։
4. Հիմա **ջնջի՛ր** դրանք տողից, պահի՛ր, գործարկի՛ր։ Չկան։

Ամեն փոփոխություն նշանակում է **խմբագրել ծրագիրը**։ Իսկ ուսուցիչը գնահատական է
ավելացնում ամեն շաբաթ։

<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Այս ձևն աշխատում է, բայց ծրագիրը հարմար չէ։</b> Այս նիստի երկրորդ կեսին
կսովորենք, թե ինչպես դասարանը պահել <b>ծրագրից դուրս</b> — և այն ժամանակ
գնահատական ավելացնելը կոդ խմբագրել չի նշանակի։
</p>
</div>

---

## Քայլ 2 — Ֆայլ կարդալ և գրել

Python-ում ֆայլը կարդալու և գրելու ամենակարճ ձևը երկու հրաման է։

```python
from pathlib import Path

path = Path("data/my_class.csv")

# գրել
path.write_text("name,grade\nAni,9\nDavit,6\n", encoding="utf-8")

# կարդալ
text = path.read_text(encoding="utf-8")
print(text)
```

> `encoding="utf-8"`-ը **պարտադիր է**։ Առանց դրա հայերեն անունները կկոտրվեն։

Սարքի՛ր `data` թղթապանակը ծրագրիդ կողքին՝ VS Code-ում, աջ սեղմում → **New Folder** →
**`data`**։

---

## Քայլ 3 — Երրորդ ֆայլը՝ `storage.py`

Ֆայլ կարդալը **հաշվարկ չէ** և **ուսուցչի հետ խոսել չէ**։ Դա երրորդ գործ է։

Հիշո՞ւմ ես անցած նիստի հարցը։ Հիմա նա ունի երեք պատասխան՝

| Եթե կոդը... | ապա այն գնում է... |
|---|---|
| հաշվում է | `grades.py` |
| **ֆայլի հետ է աշխատում** | **`storage.py`** |
| մարդու հետ է խոսում | `main.py` |

Ստեղծի՛ր **`storage.py`** մյուս երկուսի կողքին՝

```python
"""Reading and writing the class file. Calculates nothing, prints nothing."""

from pathlib import Path

import grades


def load_class(file_name=grades.CLASS_FILE):
    """Read the class from a file. An empty dictionary if the file is not there."""
    path = Path(file_name)
    if not path.exists():
        print(f"Could not find {file_name}")
        return {}

    class_grades = {}
    for line in path.read_text(encoding="utf-8").strip().splitlines()[1:]:
        if line == "":
            continue
        name, grade = line.split(",")
        class_grades[name] = int(grade)
    return class_grades


def save_class(class_grades, file_name=grades.CLASS_FILE):
    """Write the class back to the file, header first."""
    lines = ["name,grade"]
    for name in class_grades:
        lines.append(f"{name},{class_grades[name]}")
    Path(file_name).write_text("\n".join(lines) + "\n", encoding="utf-8")
```

`storage.py` **ներմուծում է `grades`-ը** մեկ բանի համար՝ ֆայլի անունը իմանալու։
Ավելացրո՛ւ այդ անունը `grades.py`-ի կարգավորումներին՝

```python
CLASS_FILE = "data/my_class.csv"
```

✅ **ՍՏՈՒԳՈՒՄ։** `python storage.py` — ոչինչ չի տպվում, և դա ճիշտ է։ Ֆայլը միայն
սահմանում է ֆունկցիաներ։

---

## Քայլ 4 — Կապի՛ր այն `main.py`-ին

Երեք փոփոխություն, բոլորն էլ `main.py`-ում։

**1.** Վերևում, `import grades`-ի կողքին՝

```python
import storage
```

**2.** `main()`-ի ներսում, հարդկոդ տողի **փոխարեն**՝

```python
    class_grades = storage.load_class()
    print(f"Opened {grades.CLASS_FILE} - {len(class_grades)} students")
```

**3.** Մենյուին ավելացրո՛ւ պահպանելու տարբերակ՝

```python
        print("1 - show the register")
        print("2 - show who did not pass")
        print("3 - add or correct a grade")
        print("4 - save")
        print("5 - quit")
```

և `if`-երի շղթային՝

```python
        elif answer == "3":
            name = input("Name: ")
            grade = int(input("Grade: "))
            class_grades[name] = grade
            print(f"{name}: {grade}")
        elif answer == "4":
            storage.save_class(class_grades)
            print("Saved.")
        elif answer == "5":
            print("Goodbye.")
            return
```

(հինը, որտեղ `3`-ը դուրս էր գալիս, փոխի՛ր `5`-ի։)

---

## Քայլ 5 — Քո դասարանը

Սարքի՛ր `data/my_class.csv` և գրի՛ր ներսում՝

```
name,grade
Անի,9
Դավիթ,6
Նարե,10
```

Առաջին տողը **պարտադիր է** և պետք է լինի ուղիղ `name,grade`։

Հիմա՝ **այն պահը, որի համար այսօրվա ամբողջ նիստն էր**՝

1. `python main.py` → `1` → քո դասարանն է, ոչ թե Ani-ն և Davit-ը
2. `3` → ավելացրո՛ւ նոր աշակերտ
3. `4` → `Saved.`
4. `5` → դուրս
5. **`python main.py` նորից → `1`**

✅ **ՍՏՈՒԳՈՒՄ։** Նոր աշակերտը տեղում է։ Ծրագիրը փակվեց, և տվյալները **մնացին**։

> Բացի՛ր `data/my_class.csv`-ն VS Code-ում։ Նոր աշակերտը այնտեղ է՝ ֆայլում, որը
> ծրագիրը գրեց։

---

## Քայլ 6 — Կոտրի՛ր դիտավորյալ

Բացի՛ր `grades.py`-ն և ֆայլի անունը սխալ գրի՛ր՝ `"data/my_clas.csv"` (մեկ `s`)։
Գործարկի՛ր։

```
Could not find data/my_clas.csv
Opened data/my_clas.csv - 0 students
```

Ծրագիրը **չկանգնեց**։ Ասաց, թե ինչ չգտավ, և շարունակեց դատարկ դասարանով։

> Այդ տարբերությունը `storage.py`-ի `if not path.exists():` տողն է։ Առանց դրա
> ծրագիրը կկանգներ `FileNotFoundError`-ով։

Ուղղի՛ր անունը ետ և ստուգի՛ր, որ դասարանդ վերադարձավ։

---

## 📦 Այսօրվա արդյունքը

- **`storage.py`** — երրորդ ֆայլը, որը ֆայլերի հետ է աշխատում և ուրիշ ոչինչ
- **Քո դասարանը** ապրում է `data/my_class.csv`-ում, ոչ թե կոդի մեջ
- Գնահատական ավելացնելը այլևս **կոդ խմբագրել չէ**
- Բացակայող ֆայլը ծրագիրը չի կոտրում

---

## Ի՞նչ ես սովորել այսօր

- `path.read_text(encoding="utf-8")` և `path.write_text(...)`
- `path.exists()` — ստուգել նախքան կարդալը
- `line.split(",")` — մեկ տողից երկու արժեք
- **Երրորդ պատասխանը** այն հարցին, թե որ ֆայլում գրել նոր կոդ

---

## Ի՞նչ է գալիս հետո

Երեք ֆայլ, քո տվյալները, աշխատող ծրագիր։ Հաջորդ նիստում այն **դարձնում ես քոնը** —
մեկ հատկություն, որը դու ես ընտրում։
