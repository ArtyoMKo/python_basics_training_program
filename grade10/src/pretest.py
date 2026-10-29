#%% md
# Նախնական թեստ

### Python զրոյից · 1-ին նիստից առաջ · 45 րոպե

Սա **քննություն չէ**։ Դասընթացը դեռ չի սկսվել, և ոչ ոք չի սպասում, որ բոլոր
առաջադրանքները կլուծես։ Թեստը ցույց է տալիս, թե որտեղից ենք սկսում։ Նույն առաջադրանքները
կհանդիպեն դասընթացի կեսին, և այդ ժամանակ կտեսնենք՝ որքան ենք առաջ գնացել։

**Չգիտե՞ս ինչպես լուծել — անցիր հաջորդին։** Դա նորմալ է, և դա էլ է օգտակար տեղեկություն։

| Մաս | Ինչ է պետք անել | Մոտավոր ժամանակ |
|---|---|---|
| Ա | աշխատել բջջի և աղյուսակի հետ | 10 րոպե |
| Բ | կարդալ կոդը և գուշակել, թե ինչ կտպի | 15 րոպե |
| Գ | գրել կոդ | 20 րոպե |

#%% md
## Կանոններ

- **Սկզբում.** մենյուից ընտրիր **File → Save a copy in Drive**։ Աշխատիր քո պատճենում։
- Բջիջը գործարկելու համար սեղմիր ▶ կոճակը բջջի ձախ կողմում կամ **Shift + Enter**։
- Գրիր միայն այնտեղ, որտեղ առաջադրանքն է ասում։ Բջիջներ մի՛ ջնջիր։
- Թեստի ընթացքում **չի կարելի** օգտվել ինտերնետից, AI-ից կամ ուրիշի օգնությունից։
- Ամեն առաջադրանք կամ արված է, կամ՝ ոչ։ Միավորներ չկան։
- Կոդի ներսում ամեն բան անգլերեն է։ Հայերեն գրում ենք միայն այս տեքստային բջիջներում։

#%% md teacher
> **Instructor copy — never hand this notebook out.** Give participants
> `pretest/pretest.ipynb`. Each grey `teacher` cell below holds the reference answer for the
> task above it. Marking rules: `pretest/README.md`.

#%% md
---
# Ա մաս — Բջիջ և աղյուսակ

Ծրագրավորում պետք չէ։

#%% md
## Առաջադրանք 1 — Փոխիր և գործարկիր

`"Ani"`-ի փոխարեն գրիր **քո անունը** (լատինատառ, չակերտների մեջ) և գործարկիր բջիջը։

#%% code
teacher_name = "Ani"
print("Hello,", teacher_name)

#%% md
## Առաջադրանք 2 — Կարդա աղյուսակը

Անցողիկ գնահատականը **4** է. 4 և ավելի՝ անցել է։

| Աշակերտ | Գնահատական |
|---|---|
| Ani | 9 |
| Davit | 6 |
| Nare | 10 |
| Aram | 3 |
| Mariam | 4 |

Լրացրու երկու պատասխանը և գործարկիր բջիջը.
- `best_student` — ո՞վ ունի ամենաբարձր գնահատականը (անունը՝ չակերտների մեջ)
- `failed_count` — քանի՞ աշակերտ **չի** անցել (թիվը՝ առանց չակերտների)

#%% code
best_student = ""
failed_count = 0

print(best_student, failed_count)

#%% code teacher
best_student = "Nare"
failed_count = 1

print(best_student, failed_count)

#%% md
## Առաջադրանք 3 — Կիրառիր կանոնը

Կանոն. եթե գնահատականը **5 կամ ավելի** է՝ `"passed"`, հակառակ դեպքում՝ `"failed"`։

Ամեն գնահատականի համար գրիր `"passed"` կամ `"failed"` և գործարկիր բջիջը։

#%% code
result_for_3 = ""
result_for_5 = ""
result_for_8 = ""

print(result_for_3, result_for_5, result_for_8)

#%% code teacher
result_for_3 = "failed"
result_for_5 = "passed"
result_for_8 = "passed"

print(result_for_3, result_for_5, result_for_8)

#%% md
---
# Բ մաս — Կարդա կոդը

Ամեն առաջադրանքում կա մի քանի տող կոդ։ **Մի՛ գործարկիր այն** և մի՛ պատճենիր բջջի մեջ.
պարզապես կարդա և գուշակիր, թե ինչ կհայտնվի էկրանին։

Գրիր քո պատասխանը չակերտների մեջ, ճիշտ այնպես, ինչպես կերևա էկրանին, և գործարկիր բջիջը։
Ոչ մի բան չի՞ տպվի, կամ կլինի սխալ — գրիր `"error"`։

Եթե երբեք կոդ չես տեսել, միևնույն է՝ փորձիր գուշակել։

#%% md
## Առաջադրանք 4

```python
print("Ani:", 9)
```

#%% code
answer_4 = ""

print(answer_4)

#%% code teacher
answer_4 = "Ani: 9"

print(answer_4)

#%% md
## Առաջադրանք 5

```python
grade = 7
grade = grade + 2
print(grade)
```

#%% code
answer_5 = ""

print(answer_5)

#%% code teacher
answer_5 = "9"

print(answer_5)

#%% md
## Առաջադրանք 6

```python
print("9" + "1")
```

#%% code
answer_6 = ""

print(answer_6)

#%% code teacher
answer_6 = "91"

print(answer_6)

#%% md
## Առաջադրանք 7

```python
names = ["Ani", "Davit", "Nare"]
print(names[1])
```

#%% code
answer_7 = ""

print(answer_7)

#%% code teacher
answer_7 = "Davit"

print(answer_7)

#%% md
## Առաջադրանք 8

```python
grade = 4
if grade >= 5:
    print("passed")
else:
    print("failed")
```

#%% code
answer_8 = ""

print(answer_8)

#%% code teacher
answer_8 = "failed"

print(answer_8)

#%% md
## Առաջադրանք 9

```python
total = 0
for grade in [3, 5, 2]:
    total = total + grade
print(total)
```

#%% code
answer_9 = ""

print(answer_9)

#%% code teacher
answer_9 = "10"

print(answer_9)

#%% md
---
# Գ մաս — Գրիր կոդ

Եթե երբեք կոդ չես գրել, **շատ նորմալ է**, որ այստեղ ոչինչ չլուծես։ Կարդա առաջադրանքը,
փորձիր, եթե գաղափար ունես, և անցիր հաջորդին։

Ամեն բջջում `# your code here` տողից հետո գրիր քո կոդը։

#%% md
## Առաջադրանք 10 — Տպիր

Տպիր ճիշտ այս տողը.

```
7-B class - biology
```

#%% code
# your code here

#%% code teacher
print("7-B class - biology")

#%% md
## Առաջադրանք 11 — Փոփոխական

Ստեղծիր երկու փոփոխական.
- `student_name`, արժեքը՝ `"Ani"`
- `grade`, արժեքը՝ `9`

Հետո **մեկ** `print`-ով տպիր երկուսը։ Պետք է տպվի `Ani 9`։

#%% code
# your code here

#%% code teacher
student_name = "Ani"
grade = 9

print(student_name, grade)

#%% md
## Առաջադրանք 12 — Միջին գնահատական

Երեք գնահատականն արդեն գրված են։ **Կոդով** հաշվիր դրանց միջինը և տպիր այն։
Պետք է տպվի `8.0`։

#%% code
grade_1 = 9
grade_2 = 6
grade_3 = 9

# your code here

#%% code teacher
grade_1 = 9
grade_2 = 6
grade_3 = 9

average = (grade_1 + grade_2 + grade_3) / 3
print(average)

#%% md
## Առաջադրանք 13 — Տեքստից թիվ

`grade_text`-ը չակերտների մեջ է, ուրեմն տեքստ է։ Տպիր `grade_text`-ին **1 գումարած**
արդյունքը։ Պետք է տպվի `9` (թիվ), ոչ թե `81` կամ սխալ։

#%% code
grade_text = "8"

# your code here

#%% code teacher
grade_text = "8"

print(int(grade_text) + 1)

#%% md
## Առաջադրանք 14 — Ցուցակ

1. Ավելացրու **Mariam**-ին `names` ցուցակի վերջում
2. Տպիր, թե քանի անուն կա հիմա ցուցակում (պետք է տպվի `5`) — թիվը **հաշվիր կոդով**
3. Տպիր ցուցակի **առաջին** անունը (պետք է տպվի `Ani`)

#%% code
names = ["Ani", "Davit", "Nare", "Aram"]

# your code here

#%% code teacher
names = ["Ani", "Davit", "Nare", "Aram"]

names.append("Mariam")
print(len(names))
print(names[0])

#%% md
## Առաջադրանք 15 — Բառարան

`grades`-ում ամեն աշակերտի անունը կապված է իր գնահատականին։
1. Տպիր **Nare**-ի գնահատականը (պետք է տպվի `10`)
2. **Aram**-ի գնահատականը փոխիր **5**-ի
3. Տպիր **Aram**-ի նոր գնահատականը (պետք է տպվի `5`)

#%% code
grades = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3}

# your code here

#%% code teacher
grades = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3}

print(grades["Nare"])
grades["Aram"] = 5
print(grades["Aram"])

#%% md
## Առաջադրանք 16 — Պարզ պայման

Եթե `grade`-ը **9 կամ ավելի** է, տպիր `excellent`։ Հակառակ դեպքում ոչինչ պետք չէ տպել։

Ստուգիր. փոխիր `10`-ը `5`-ով և նորից գործարկիր — ոչինչ չպետք է տպվի։

#%% code
grade = 10

# your code here

#%% code teacher
grade = 10

if grade >= 9:
    print("excellent")

#%% md
## Առաջադրանք 17 — Պայման

Եթե `grade`-ը **4 կամ ավելի** է, տպիր `passed`, հակառակ դեպքում՝ `failed`։

Կոդը պետք է ճիշտ աշխատի **ցանկացած** գնահատականի համար։ Ստուգիր. փոխիր `3`-ը `7`-ով
և նորից գործարկիր։

#%% code
grade = 3

# your code here

#%% code teacher
grade = 3

if grade >= 4:
    print("passed")
else:
    print("failed")

#%% md
## Առաջադրանք 18 — Ամբողջ դասարանը

Անցողիկը **4** է։ `class_grades` ցուցակի **յուրաքանչյուր** գնահատականի համար տպիր
գնահատականը և `passed` կամ `failed`։ Պետք է տպվի.

```
9 passed
6 passed
10 passed
3 failed
```

Կոդը պետք է աշխատի նաև, եթե դասարանում 30 աշակերտ լինի. մի՛ գրիր չորս առանձին `print`։

#%% code
class_grades = [9, 6, 10, 3]

# your code here

#%% code teacher
class_grades = [9, 6, 10, 3]

for grade in class_grades:
    if grade >= 4:
        print(grade, "passed")
    else:
        print(grade, "failed")

#%% md
---
# Վերջում

Մեկ հարց քո մասին. սա առաջադրանք **չէ** և չի մտնում արդյունքի մեջ։

Նախկինում կոդ գրե՞լ ես։ Գրիր `"no"`, `"a little"` կամ `"yes"`։ Եթե գրել ես, `language`-ում գրիր
ծրագրավորման լեզուն (օրինակ՝ `"Pascal"`)։

#%% code
experience = ""
language = ""

print(experience, language)

#%% md
## Ինչպես հանձնել

1. Մենյուից ընտրիր **Runtime → Run all**, որպեսզի բոլոր բջիջները գործարկվեն։ Եթե ինչ-որ բջջում
   սխալ լինի, դա խնդիր չէ։
2. Վերևի աջ անկյունում սեղմիր **Share**։
3. **General access**-ում ընտրիր **Anyone with the link**, դերը թող **Viewer**։
4. Սեղմիր **Copy link** և ուղարկիր հղումը դասավանդողին։

**Շնորհակալություն։ Կհանդիպենք դասընթացում։**
