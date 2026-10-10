# Հուշաթերթ — Python զրոյից

**Տպի՛ր այս էջերը և պահի՛ր կողքիդ։** Այստեղ գրված է այն ամենը, ինչ օգտագործում ենք
դասընթացում։ Ոչինչ անգիր անելու կարիք չկա — պետք է միայն իմանալ, թե որտեղ նայել։

---

## 1. Բառարան — հայերեն ու անգլերեն

**Կոդի ներսում ամեն բան անգլերեն է** — բառերը, փոփոխականների անունները,
մեկնաբանությունները և տպվող տեքստը։ Բացատրությունները հայերեն են։

Ստորև՝ ինչպես ենք կոչում այս հասկացությունները հայերեն, երբ խոսում ենք դասին։

| Անգլերեն | Հայերեն | Ինչ է դա |
|---|---|---|
| topic | թեմա | մեկ նոթատետր, մեկ գաղափար։ Դասընթացում 24-ն է |
| session | նիստ | 75 րոպե՝ միասին։ Դասընթացում 18-ն է, շաբաթական երկուսը |
| homework | տնային | **պարտադիր է։** Նիստից հետո՝ նույն նոթատետրի առաջադրանքները։ Նոր նյութ չի լինում |
| program | ծրագիր | Հրահանգների շարք, որը համակարգիչը կատարում է |
| code | կոդ | Այն, ինչ գրում ես |
| to run | գործարկել | Ասել համակարգչին՝ կատարի՛ր այս կոդը |
| notebook | տետր | `.ipynb` ֆայլը, որտեղ աշխատում ենք առաջին 15 նիստը |
| cell | բջիջ | Տետրի մեկ վանդակը, որը գործարկվում է առանձին |
| output | արդյունք | Այն, ինչ հայտնվում է բջիջի տակ |
| error | սխալ | Կարմիր տեքստը։ Ոչ թե աղետ, այլ հաղորդագրություն |
| comment | մեկնաբանություն | `#`-ից հետո գրվածը։ Python-ը չի կարդում այն |
| value | արժեք | Մեկ տվյալ՝ `9`, `"Ani"`, `6.5` |
| type | տիպ | Արժեքի տեսակը՝ տեքստ, ամբողջ թիվ, տասնորդական, ճիշտ/սխալ |
| text (string) | տեքստ | Չակերտների մեջ գրված արժեք՝ `"Ani"` |
| integer | ամբողջ թիվ | `9`, `12`, `0` |
| float | տասնորդական թիվ | `6.5`, `9.25` |
| boolean | ճիշտ կամ սխալ | Միայն երկու արժեք՝ `True` և `False` |
| variable | փոփոխական | Արժեքին տրված անուն |
| to assign | վերագրել | `grade = 9` — 9-ը վերագրում ենք `grade` անվանը |
| f-string | f-տող | `f"{name}: {grade}"` — տեքստ, որի մեջ արժեք ենք դնում |
| condition | պայման | Հարց, որի պատասխանը ճիշտ է կամ սխալ |
| indentation | ներդիր ⚠ | Տողի սկզբի չորս բացատը։ Python-ի համար իմաստ ունի |
| list | ցուցակ | Շատ արժեք՝ մեկ անվան տակ՝ `[9, 6, 10]` |
| element | տարր | Ցուցակի մեկ արժեքը |
| index | ինդեքս | Տարրի տեղը ցուցակում։ Հաշվարկը սկսվում է **0**-ից |
| to add (append) | ավելացնել | Ցուցակի վերջում նոր տարր դնել |
| loop | ցիկլ | Նույն գործողությունը կրկնել ամեն տարրի համար |
| dictionary | բառարան | Զույգեր՝ `{"Ani": 9}`. անուն ներս, գնահատական դուրս |
| key | բանալի | Բառարանի ձախ կողմը՝ `"Ani"` |
| function | ֆունկցիա | Կոդի կտոր, որին անուն ենք տալիս և կանչում ենք |
| to define | սահմանել | `def` բառով ֆունկցիա գրել |
| to call | կանչել | Ֆունկցիան աշխատեցնել՝ `average_of(grades)` |
| parameter | պարամետր | Ֆունկցիայի փակագծերում գրված անունը |
| to return | վերադարձնել | Ֆունկցիան արժեք է տալիս ետ |
| file | ֆայլ | Սկավառակի վրա պահված տվյալ |
| folder | թղթապանակ | Ֆայլերի պահոց |
| to save | պահպանել | Ctrl+S / Cmd+S |
| module | մոդուլ | Մեկ `.py` ֆայլ, որը կարող ենք ներմուծել |
| to import | ներմուծել | Այլ ֆայլից կոդ վերցնել |
| terminal | տերմինալ | Պատուհան, որտեղ հրամաններ ենք գրում |

**Դասարանի բառերը, որ օգտագործում ենք բոլոր օրինակներում**

| Անգլերեն | Հայերեն |
|---|---|
| student | աշակերտ |
| class | դասարան |
| grade | գնահատական |
| average | միջին |
| pass mark | անցողիկ միավոր |
| to pass | անցնել |
| attendance | հաճախում |
| report | հաշվետվություն |

> ⚠ **Ուշադրություն։** Նշված տերմինը դեռ ստուգման կարիք ունի։ Եթե քո դպրոցում այլ
> բառ է ընդունված, ասա՛ — կուղղենք։

---

## 2. Տպել

```python
print("Hello")                      # text
print(9)                            # a number
print("Ani", 9)                     # two values, with a space
print("Ani:", 9, "points")
print()                             # a blank line
print('He said "hello"')            # a quote inside text: use the other kind
```

## 3. Չորս տիպ

```python
name = "Ani"          # text              str
grade = 9             # whole number      int
average = 6.5         # decimal           float
passed = True         # true or false     bool

type(name)            # shows the type
```

**Տիպը փոխել**

```python
int("9")              # text to whole number   -> 9
float("6.5")          # text to decimal        -> 6.5
str(9)                # number to text         -> "9"
round(6.4762, 1)      # round it               -> 6.5
```

**`input()`-ը միշտ տեքստ է տալիս**

```python
answer = input("Grade: ")            # even if they type 9, you get "9"
grade = int(answer)                  # so convert it
```

## 4. Փոփոխականներ

```python
student_name = "Ani"
student_grade = 9

student_grade = 10          # a new value under the same name

print(f"{student_name}: {student_grade}")
print(f"Average: {average:.1f}")     # one digit after the point
```

Անվանման կանոններ՝ միայն անգլերեն տառեր, թվեր և `_`։ Թվով չի սկսվում։ Բացատ չկա։

## 5. Պայմաններ

```python
PASS_MARK = 4

if grade >= PASS_MARK:
    print("passed")
else:
    print("failed")
```

```python
if grade >= 9:
    print("excellent")
elif grade >= 7:
    print("good")
elif grade >= PASS_MARK:
    print("satisfactory")
else:
    print("unsatisfactory")
```

| Նշան | Իմաստ |
|---|---|
| `==` | հավասար է |
| `!=` | հավասար չէ |
| `>` `<` | մեծ է, փոքր է |
| `>=` `<=` | մեծ կամ հավասար, փոքր կամ հավասար |
| `and` | երկուսն էլ ճիշտ են |
| `or` | գոնե մեկը ճիշտ է |
| `not` | հակառակը |

**Չորս բացատը պարտադիր է։** `if`-ից հետո՝ երկու կետ, հաջորդ տողը՝ չորս բացատ ներս։

## 6. Ցուցակներ

```python
grades = [9, 6, 10, 3, 8]

grades[0]            # the first one   -> 9    (counting starts at 0)
grades[-1]           # the last one    -> 8
len(grades)          # how many        -> 5
grades[0:3]          # the first three -> [9, 6, 10]

grades.append(7)     # add at the end
grades.remove(3)     # remove the value 3
grades.sort()        # sort it
3 in grades          # is it there?    -> True or False
```

## 7. Ցիկլեր

```python
for grade in grades:
    print(grade)

for student_name in student_names:
    print(f"Hello, {student_name}")
```

**Հաշվել և գումարել**

```python
total = 0
for grade in grades:
    total = total + grade

average = total / len(grades)
```

**`range` — թվերի շարք**

```python
for number in range(1, 11):     # 1 to 10; 11 is not included
    print(number)
```

**Ցիկլ՝ պայմանով ներսում**

```python
failed = []
for name, grade in class_grades.items():
    if grade < PASS_MARK:
        failed.append(name)
```

**`while` — կրկնել մինչև կանգնեցնես**

```python
while True:
    answer = input("Command (or 'quit'): ")
    if answer == "quit":
        break
```

## 8. Բառարաններ

```python
class_grades = {"Ani": 9, "Davit": 6, "Nare": 10}

class_grades["Ani"]              # -> 9
class_grades["Gor"] = 4          # add
class_grades["Ani"] = 10         # correct
"Gor" in class_grades            # is it there? -> True

for name, grade in class_grades.items():
    print(f"{name}: {grade}")
```

## 9. Ֆունկցիաներ

```python
def average_of(grades):
    """Return the average of a list of grades."""
    total = 0
    for grade in grades:
        total = total + grade
    return round(total / len(grades), 1)


class_average = average_of([9, 6, 10])     # call it and keep the result
print(class_average)
```

```python
def has_passed(grade, pass_mark=PASS_MARK):    # a parameter with a default
    return grade >= pass_mark
```

**Սահմանելը և կանչելը տարբեր բաներ են։** `def`-ը ոչինչ չի անում, քանի դեռ չես կանչել։

## 10. Ֆայլեր

```python
from pathlib import Path

path = Path("data/my_class.csv")

# read
text = path.read_text(encoding="utf-8")
lines = text.strip().splitlines()

# write
path.write_text("name,grade\nAni,9\n", encoding="utf-8")

# does it exist yet?
if path.exists():
    ...
```

`encoding="utf-8"`-ը **պարտադիր է**, այլապես հայերեն տառերը կկոտրվեն։

> Աշակերտների դասագրքում կտեսնես նաև `open()`-ը՝ `with open(...) as file:`։
> Նույն գործն է անում։ Մենք `pathlib` ենք օգտագործում, որովհետև կարճ է և
> ֆայլը ինքն իրեն փակում է։

## 11. Մոդուլներ

```python
# in settings.py
PASS_MARK = 4

# in main.py
import settings
from grades import average_of

print(settings.PASS_MARK)
```

```python
if __name__ == "__main__":
    main()        # this part runs only when you run this file directly
```

## 12. Տերմինալ — ընդամենը երկու հրաման

```bash
cd Documents/python_course      # go to the folder
python main.py                  # run the program
```

VS Code-ում տերմինալը բացվում է **Ctrl + `** (Mac-ում՝ **Control + `**)։

---

## 13. Սխալները — ինչ են նշանակում

Կարմիր տեքստը սխալ չէ քո կողմից։ Այն հաղորդագրություն է։ **Կարդա՛ վերջին տողը** —
այնտեղ է սխալի անունը։

| Սխալի անունը | Ինչ է ասում | Ամենահավանական պատճառը |
|---|---|---|
| `SyntaxError` | Չեմ հասկանում այս տողը | Բաց մնացած չակերտ, փակագիծ կամ պակասող `:` |
| `IndentationError` | Բացատները սխալ են | Չորս բացատը մոռացվել է կամ խառնվել |
| `NameError` | Այս անունը չեմ ճանաչում | Տառասխալ, կամ բջիջը վերևում չի գործարկվել |
| `TypeError` | Այս երկուսը միասին չեն աշխատում | Տեքստ ու թիվ ես գումարում |
| `ValueError` | Տիպը ճիշտ է, արժեքը՝ ոչ | `int("nine")` - this is not a number |
| `IndexError` | Այդ տեղը ցուցակում չկա | Հաշվարկը 0-ից է. 12 տարրի վերջինը `[11]`-ն է |
| `KeyError` | Այդ բանալին բառարանում չկա | Տառասխալ անվան մեջ, կամ աշակերտը հեռացել է |
| `FileNotFoundError` | Այդ ֆայլը չգտա | Սխալ թղթապանակում ես, կամ անունը սխալ է |
| `ModuleNotFoundError` | Այդ ֆայլը ներմուծել չեմ կարող | Ֆայլը նույն թղթապանակում չէ |

**Երեք բան, որ ստուգել առաջին հերթին, երբ ինչ-որ բան չի աշխատում**

1. Բոլոր բջիջները գործարկե՞լ ես վերևից ներքև, հերթով։
2. VS Code-ի վերևի աջ անկյունում ճի՞շտ kernel-ն է ընտրված։
3. Ճի՞շտ թղթապանակում ես։
