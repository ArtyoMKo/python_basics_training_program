#%% md
# Թեմա 18 — Պատասխանը ետ ուղարկել

### Python զրոյից · Թեմա 18-ը 24-ից

Երեկ օգտագործեցինք `return`-ը։ Այսօր նայում ենք նրան ուշադիր և կառուցում ենք
**չորս ֆունկցիայից բաղկացած գործիքակազմ**, որը 20-րդ թեման կդառնա քո ծրագրի սիրտը։

## ԱՅՍՕՐ:

- **Ա մաս:** տպել կամ վերադարձնել
- **Բ մաս:** լռելյայն արժեք
- **Գ մաս:** քո գործիքակազմը

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>def name(parameter):</code> — կոդին անուն։ Սահմանելը և կանչելը տարբեր բաներ են։<br/>
<code>return</code> — վերադարձնում է արժեքը։
</p>
</div>

#%% md
## Ա մաս: Տպել կամ վերադարձնել

Երկու գրեթե նույն ֆունկցիա։

#%% code
def print_average(grades):
    total = 0
    for grade in grades:
        total = total + grade
    print(f"Average: {total / len(grades):.1f}")


def average_of(grades):
    total = 0
    for grade in grades:
        total = total + grade
    return round(total / len(grades), 1)

#%% code
print_average([9, 10, 8])

#%% md
Սա տպեց միջինը։ Հիմա փորձի՛ր պատասխանել հարցին՝ «արդյո՞ք Անիի միջինը 8-ից բարձր է»։

Չես կարող։ **Թիվը գնաց էկրան, ոչ թե քեզ։**

#%% code
ani_average = average_of([9, 10, 8])

print(ani_average)
print(ani_average > 8)
print(ani_average * 2)

#%% md
| | Տպող ֆունկցիա | Վերադարձնող ֆունկցիա |
|---|---|---|
| Ի՞նչ է անում | ցույց է տալիս էկրանին | տալիս է քեզ արժեքը |
| Կարո՞ղ ես օգտագործել | ոչ | այո |
| Կարո՞ղ ես տպել | արդեն տպված է | `print(average_of(...))` |

> **Կանոն, որը գործում է մինչև դասընթացի վերջը.**
> ֆունկցիան կա՛մ **հաշվում է** (և վերադարձնում), կա՛մ **տպում է**։ Ոչ թե երկուսը։
>
> 21-րդ թեման դա կդառնա երկու առանձին ֆայլ։

#%% md
`return`-ից հետո ֆունկցիան **անմիջապես ավարտվում է**։

#%% code
def has_passed(grade):
    if grade >= 4:
        return True
    return False


print(has_passed(9))
print(has_passed(2))

#%% md
Այստեղ `else` պետք չէ. եթե պայմանը ճիշտ է, `return True`-ն արդեն ավարտել է ֆունկցիան։

Բայց այս ֆունկցիան իրականում ավելի կարճ է գրվում, որովհետև `grade >= 4`-ը **արդեն**
`True` կամ `False` է — դա 9-րդ թեմայի դասն էր։

#%% code
def has_passed(grade):
    return grade >= 4


print(has_passed(9))
print(has_passed(2))

#%% md
## Բ մաս: Լռելյայն արժեք

Անցողիկ միավորը 4 է, բայց ուրիշ դպրոցում կարող է ուրիշ լինել։ Կարող ենք պարամետրին
**լռելյայն արժեք** տալ։

#%% code
PASS_MARK = 4


def has_passed(grade, pass_mark=PASS_MARK):
    return grade >= pass_mark


print(has_passed(5))
print(has_passed(5, 6))

#%% md
Առաջին կանչում երկրորդ արժեքը չգրեցինք, ուստի օգտագործվեց `PASS_MARK`-ը՝ 4։
Երկրորդում գրեցինք 6, ուստի օգտագործվեց 6։

**Լռելյայն արժեք ունեցող պարամետրերը գրվում են վերջում։**

#%% md
## Գ մաս: Քո գործիքակազմը

Հիմա գրում ենք չորս ֆունկցիա, որոնք **20-րդ թեման դառնալու են քո ծրագրի սիրտը**։

#%% code
PASS_MARK = 4


def average_of(grades):
    """Return the average of a list of grades, rounded to one decimal place."""
    total = 0
    for grade in grades:
        total = total + grade
    return round(total / len(grades), 1)


def has_passed(grade, pass_mark=PASS_MARK):
    """Return True if this grade is a pass."""
    return grade >= pass_mark


def highest_of(class_grades):
    """Return the name of the student with the highest grade."""
    best_name = ""
    best_grade = -1
    for student_name, grade in class_grades.items():
        if grade > best_grade:
            best_grade = grade
            best_name = student_name
    return best_name


def failing_students(class_grades, pass_mark=PASS_MARK):
    """Return a list of the names of the students who did not pass."""
    failing = []
    for student_name, grade in class_grades.items():
        if grade < pass_mark:
            failing.append(student_name)
    return failing

#%% md
> Երեք չակերտի մեջ գրված տողը ֆունկցիայի **նկարագրությունն** է։ Այն պարտադիր չէ,
> բայց երեք շաբաթ հետո ինքդ քեզ շնորհակալ կլինես։ Այն գրում ենք անգլերեն, ինչպես
> մնացած կոդը։

Հիմա ստուգենք դրանք։

#%% code
class_grades = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3,
                "Mariam": 8, "Tigran": 5, "Lilit": 8, "Gor": 4,
                "Anahit": 9, "Hayk": 2, "Sona": 8, "Vahe": 6}

print("average:", average_of(list(class_grades.values())))
print("highest:", highest_of(class_grades))
print("failing:", failing_students(class_grades))
print("did Ani pass?", has_passed(class_grades["Ani"]))

#%% md
> `class_grades.values()` — տալիս է միայն արժեքները՝ 14-րդ թեմայինից։ `list(...)`-ը
> դրանք դարձնում է ցուցակ, որպեսզի `average_of`-ը կարողանա աշխատել։

Եվ հիմա՝ ամբողջ մատյանը, չորս ֆունկցիայով։

#%% code
print("=== REGISTER ===")

for student_name, grade in class_grades.items():
    if has_passed(grade):
        result = "passed"
    else:
        result = "failed"
    print(f"{student_name:<10} {grade:>3}   {result}")

print()
print(f"average: {average_of(list(class_grades.values()))}")
print(f"highest: {highest_of(class_grades)}")
print(f"failing: {len(failing_students(class_grades))} students")

#%% md
**Նայի՛ր այս բջիջին։** Դա իրական ծրագիր է։ Այն անում է այն, ինչի համար կգրեիր գործիք
քեզ համար։

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Պարտադիր առաջադրանքներ</h3>
<p style="color:#900; margin-bottom:0;">
<b>Այսօրվա առաջադրանքը կարևոր է. 20-րդ թեման այս կոդն է տեղափոխվելու ֆայլ։</b><br/><br/>
<b>1.</b> Գրի՛ր չորս ֆունկցիաները քո տետրում՝ քո դասարանի բառարանով։<br/><br/>
<b>2.</b> Ստուգի՛ր բոլոր չորսը և համեմատի՛ր մատյանիդ հետ։<br/><br/>
<b>3.</b> Տպի՛ր ամբողջական մատյանը չորս ֆունկցիաներով։<br/><br/>
<b>4.</b> Փոխի՛ր <code>PASS_MARK</code>-ը և համոզվի՛ր, որ ամեն ինչ փոխվեց։
</p>
</div>

#%% code
# Exercise 1 - your four functions, your class
# Keep this cell - on day 20 it moves into a file.

PASS_MARK = 4


def average_of(grades):
    """Return the average of a list of grades."""
    total = 0
    for grade in grades:
        total = total + grade
    return round(total / len(grades), 1)


def has_passed(grade, pass_mark=PASS_MARK):
    """Return True if this grade is a pass."""
    return grade >= pass_mark


my_class = {"Ani": 9, "Davit": 6, "Nare": 10}

print(average_of(list(my_class.values())))
print(has_passed(my_class["Davit"]))

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#f71; margin-top:0;">🚀 Լրացուցիչ առաջադրանքներ</h3>
<p style="color:#f71; margin-bottom:0;">
<b>5.</b> Գրի՛ր <code>lowest_of(class_grades)</code>։ Ձևը նույնն է՝ փոխի՛ր
<code>&gt;</code>-ը <code>&lt;</code>-ի և սկզբնական արժեքը։<br/><br/>
<b>6.</b> Գրի՛ր <code>how_many_passed(class_grades)</code>, որը վերադարձնում է թիվը։<br/><br/>
<b>7.</b> Գրի՛ր <code>passing_students(class_grades)</code>՝ անցածների ցուցակը։<br/><br/>
<b>8.</b> Գրի՛ր <code>grade_band(grade)</code>, որը վերադարձնում է
<code>"excellent"</code>, <code>"good"</code>, <code>"satisfactory"</code> կամ
<code>"unsatisfactory"</code>։ Կանչի՛ր այն մատյանի ցիկլում։<br/><br/>
<b>9.</b> Ի՞նչ է վերադարձնում ֆունկցիան, որը <code>return</code> չունի։
Փորձի՛ր՝ <code>print(print_average([9]))</code>։
</p>
</div>

#%% code
# Extra 5-9 - your space

def grade_band(grade):
    """Return the name of the band this grade falls into."""
    if grade >= 9:
        return "excellent"
    elif grade >= 7:
        return "good"
    elif grade >= 4:
        return "satisfactory"
    return "unsatisfactory"


print(grade_band(9))
print(grade_band(2))

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🧗 Մարտահրավեր</h3>
<p style="color:#06c; margin-bottom:0;">
<b>10.</b> Գրի՛ր <code>students_above(class_grades, mark)</code>, որը վերադարձնում է
այն աշակերտների ցուցակը, ում միավորը տրված թվից բարձր է։ Կանչի՛ր այն երեք տարբեր
թվով։<br/><br/>
<b>11.</b> Գրի՛ր <code>class_summary(class_grades)</code>, որը վերադարձնում է
<b>բառարան</b>՝ <code>{"average": ..., "passed": ..., "failed": ...}</code>։<br/><br/>
Ֆունկցիան կարող է վերադարձնել ցանկացած բան՝ թիվ, ցուցակ, նույնիսկ բառարան։
</p>
</div>

#%% code
# Challenge 10-11

def students_above(class_grades, mark):
    """Return the names of students whose grade is above the given mark."""
    above = []
    for student_name, grade in class_grades.items():
        if grade > mark:
            above.append(student_name)
    return above


print(students_above(class_grades, 8))

#%% md
<div style="border-left: 6px solid #747; background: #f8f6fb; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#747; margin-top:0;">🏠 Տնային</h3>
<p style="color:#747; margin-bottom:0;">
Այս նոթատետրի <b>Լրացուցիչ</b> առաջադրանքները, և ցանկացած <b>Պարտադիր</b>, որ չհասցրիր։<br/><br/>
<b>Նոր բան չկա</b> — ամեն առաջադրանք այս նոթատետրից է, և օգտագործում է միայն այն,
ինչ այսօր սովորեցինք։<br/>
Հաջորդ նիստը սկսվում է դրանց ստուգումով։
</p>
</div>

#%% md
## Ինչի հասանք

- `return` — ֆունկցիան **տալիս է արժեքը**, ոչ թե տպում։ Հետո կարող ես օգտագործել այն։
- Ֆունկցիան կա՛մ հաշվում է, կա՛մ տպում։ **Ոչ թե երկուսը։**
- `def f(a, b=5)` — լռելյայն արժեք։ Գրվում է վերջում։
- Չորս ֆունկցիա, որոնք 20-րդ թեման դառնալու են ծրագրի սիրտը։

## Ի՞նչ է գալիս հետո

Հաջորդ դասին **նոր բան չենք սովորելու**։ Հավաքելու ենք տասնութ դասի ամեն ինչ մեկ
տետրում և կստանանք ամբողջական մատյանի ծրագիր։

Դա նաև հասնելու օրն է. եթե ինչ-որ բան բաց ես թողել, վաղը ժամանակ կլինի։

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Համոզվի՛ր, որ այսօրվա չորս ֆունկցիան պահպանված է։ Վաղը և հատկապես 20-րդ թեման պետք կգան։
