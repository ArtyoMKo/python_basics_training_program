#%% md
# Թեմա 9 — Ոչ միայն աշակերտներ

### Python 11-րդ դասարանի համար · Թեմա 9-ը 24-ից

Դպրոցում աշակերտներից բացի **ուսուցիչներ** էլ կան։ Նրանք ունեն անուն, դասարան և
հեռախոս՝ ինչպես աշակերտը։ Եվ ունեն առարկա ու աշխատավարձ՝ ինչպես աշակերտը չունի։

## ԱՅՍՕՐ:

- **Ա մաս:** ուսուցիչը՝ պատճենելով աշակերտին
- **Բ մաս:** «ամեն ինչ, ինչ ունի, գումարած»
- **Գ մաս:** երկու տարբերակը կողք կողքի

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>class Student</code> մեթոդներով · <code>class SchoolClass</code>, որի ներսում
<code>Student</code>-եր են<br/><br/>
<b>Այսօր երկու դաս կսովորեն կիսել ընդհանուրը։</b>
</p>
</div>

#%% md
## Ա մաս: Ուսուցիչը՝ պատճենով

Ահա աշակերտի դասը, ինչպես 7-րդ թեման։

#%% code
class Student:
    def __init__(self, name, class_name, phone, grades, attendance):
        self.name = name
        self.class_name = class_name
        self.phone = phone
        self.grades = grades
        self.attendance = attendance

    def surname(self):
        return self.name.split(" ")[1]

    def contact_line(self):
        return f"{self.name} ({self.class_name}) — {self.phone}"

    def average(self):
        return sum(self.grades) / len(self.grades)


ani = Student("Ani Hakobyan", "11A", "077-11-22-33", [7, 6, 8, 9, 8], 94)
print(ani.contact_line())
print(ani.surname(), ani.average())

#%% md
Հիմա պետք է ուսուցիչ։ Այն, ինչ գիտենք անել՝ **պատճենել դասը և խմբագրել**։

<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Այս ձևն աշխատում է, բայց կրկնվող է։</b> Դասի երկրորդ կեսին կսովորենք մի ձև,
որով ընդհանուր մասը գրվում է <b>մեկ անգամ</b>, և փոփոխությունը արվում է մեկ տեղում։
</p>
</div>

**Գործարկի՛ր։**

#%% code
class Teacher:
    def __init__(self, name, class_name, phone, subject, salary):
        self.name = name
        self.class_name = class_name
        self.phone = phone
        self.subject = subject
        self.salary = salary

    def surname(self):
        return self.name.split(" ")[1]

    def contact_line(self):
        return f"{self.name} ({self.class_name}) — {self.phone}"

    def is_experienced(self):
        return self.salary > 300000


tigran = Teacher("Tigran Mkrtchyan", "11A", "091-44-55-66", "Mathematics", 350000)
print(tigran.contact_line())
print(tigran.surname(), tigran.is_experienced())

#%% md
**Հիմա դու։** Ավելացրո՛ւ երրորդ դասը՝ `Parent` (ծնող)։ Նա ունի անուն, դասարան և
հեռախոս՝ ինչպես մյուսները, և երեխայի անուն՝ ինչպես նրանք չունեն։

Պատճենի՛ր `surname`-ը և `contact_line`-ը, ինչպես վերևում։

#%% code
class Parent:
    def __init__(self, name, class_name, phone, child_name):
        # five lines
        # ...
        pass

    # copy surname() here
    # copy contact_line() here


# mother = Parent("Lilit Hakobyan", "11A", "055-77-88-99", "Ani Hakobyan")
# print(mother.contact_line())

#%% md
### Եվ հիմա՝ տնօրենը զանգում է

Նոր կանոն. ազգանունը պետք է գրվի **մեծատառերով**, և կոնտակտի տողում պետք է
երևա դասարանը **առանց** փակագծերի։

Երկու փոքր փոփոխություն։ **Քանի՞ տեղում։**

#%% code
# Change surname() and contact_line() in Student.
# Then the same two in Teacher.
# Then the same two in Parent.
#
# Count the places you had to touch.

#%% md
## Բ մաս: Ամեն ինչ, ինչ ունի, գումարած

Նայի՛ր երեք դասին։ **Երեքն էլ ունեն** անուն, դասարան, հեռախոս, `surname()` և
`contact_line()`։

Python-ում կարելի է գրել այդ ընդհանուրը **մեկ անգամ**, առանձին դասում, և ասել
մյուսներին՝ «վերցրո՛ւ այնտեղից»։

#%% code
class Person:
    def __init__(self, name, class_name, phone):
        self.name = name
        self.class_name = class_name
        self.phone = phone

    def surname(self):
        return self.name.split(" ")[1]

    def contact_line(self):
        return f"{self.name} ({self.class_name}) — {self.phone}"


class Student(Person):
    def __init__(self, name, class_name, phone, grades, attendance):
        super().__init__(name, class_name, phone)
        self.grades = grades
        self.attendance = attendance

    def average(self):
        return sum(self.grades) / len(self.grades)


class Teacher(Person):
    def __init__(self, name, class_name, phone, subject, salary):
        super().__init__(name, class_name, phone)
        self.subject = subject
        self.salary = salary

    def is_experienced(self):
        return self.salary > 300000


ani = Student("Ani Hakobyan", "11A", "077-11-22-33", [7, 6, 8, 9, 8], 94)
tigran = Teacher("Tigran Mkrtchyan", "11A", "091-44-55-66", "Mathematics", 350000)

print(ani.contact_line())
print(tigran.contact_line())
print(ani.surname(), tigran.surname())

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#0a7; margin-top:0;">✅ Երկու բան, որ պետք է հասկանալ</h3>
<p style="color:#0a7; margin-bottom:0;">
<b><code>class Student(Person):</code></b> — փակագծերում գրվում է, թե որտեղից վերցնել
ընդհանուրը։ Ասում են՝ <code>Student</code>-ը <b>ժառանգում է</b> <code>Person</code>-ից։<br/><br/>
<b><code>super().__init__(name, class_name, phone)</code></b> — «կանչիր վերևինի
<code>__init__</code>-ը»։ Այն լրացնում է ընդհանուր դաշտերը, հետո մենք ավելացնում ենք մերը։<br/><br/>
<code>contact_line()</code> գրված չէ <code>Student</code>-ում։ Եվ այնուամենայնիվ աշխատում է։
</p>
</div>

#%% md
### Ի՞նչ է լինում, երբ `super()`-ը մոռանում ես

Սա ամենահաճախ հանդիպող սխալն է։ **Գործարկի՛ր և կարդա՛։**

#%% code expected-error: AttributeError
class Broken(Person):
    def __init__(self, name, class_name, phone, subject):
        self.subject = subject


broken = Broken("Sona Martirosyan", "11B", "093-00-11-22", "Physics")
print(broken.contact_line())

#%% md
<div style="border-left: 6px solid #d33; background: #fff5f5; padding: 12px 16px; margin: 12px 0;">
<p style="color:#d33; margin:0;">
🔍 <b><code>AttributeError: 'Broken' object has no attribute 'name'</code></b><br/><br/>
Դասը ժառանգեց <code>contact_line()</code>-ը և կարողացավ կանչել այն։ Բայց
<code>self.name</code>-ը երբեք չլրացվեց, որովհետև <code>Person.__init__</code>-ը
չկանչվեց։<br/><br/>
<b>Կանոն:</b> եթե գրում ես <code>__init__</code> ժառանգող դասում — <b>առաջին տողը</b>
գրեթե միշտ <code>super().__init__(...)</code> է։
</p>
</div>

#%% md
## Գ մաս: Նույն փոփոխությունը, նորից

Հիմա տնօրենի նույն խնդրանքը՝ ազգանունը մեծատառերով։

**Փոխի՛ր միայն `Person`-ը։**

#%% code
class Person:
    def __init__(self, name, class_name, phone):
        self.name = name
        self.class_name = class_name
        self.phone = phone

    def surname(self):
        return self.name.split(" ")[1].upper()

    def contact_line(self):
        return f"{self.name} {self.class_name} — {self.phone}"


class Student(Person):
    def __init__(self, name, class_name, phone, grades, attendance):
        super().__init__(name, class_name, phone)
        self.grades = grades
        self.attendance = attendance

    def average(self):
        return sum(self.grades) / len(self.grades)


class Teacher(Person):
    def __init__(self, name, class_name, phone, subject, salary):
        super().__init__(name, class_name, phone)
        self.subject = subject
        self.salary = salary


ani = Student("Ani Hakobyan", "11A", "077-11-22-33", [7, 6, 8, 9, 8], 94)
tigran = Teacher("Tigran Mkrtchyan", "11A", "091-44-55-66", "Mathematics", 350000)

print(ani.surname(), "|", ani.contact_line())
print(tigran.surname(), "|", tigran.contact_line())

#%% md
### Երկու տարբերակը կողք կողքի

| | Պատճենելով | Ժառանգելով |
|---|---|---|
| `surname()` գրված է | **3 անգամ** | **1 անգամ** |
| `contact_line()` գրված է | **3 անգամ** | **1 անգամ** |
| Տնօրենի փոփոխությունը | **6 տեղ** | **2 տեղ** |
| Չորրորդ դաս ավելացնելը | ևս 15 տող | 3 տող |
| Ի՞նչ է ընդհանուրը | ոչ մի տեղ գրված չէ | `class Person` |

<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<p style="color:#06c; margin:0;">
<b>Ե՞րբ օգտագործել։</b> Երբ կարող ես ասել՝ «<b>X-ը Y է</b>»։<br/>
Աշակերտը <b>մարդ է</b> → ժառանգում է։<br/>
Դասարանը <b>մարդ չէ</b> — այն <b>ունի</b> աշակերտներ → ցուցակ է, ոչ թե ժառանգում։
</p>
</div>

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Ծնողը՝ ժառանգելով

Վերագրի՛ր `Parent` դասը այնպես, որ այն ժառանգի `Person`-ից։

#%% code
class Parent(Person):
    def __init__(self, name, class_name, phone, child_name):
        # super() first, then child_name
        # ...
        pass


# mother = Parent("Lilit Hakobyan", "11A", "055-77-88-99", "Ani Hakobyan")
# print(mother.contact_line())
# print(mother.surname())

#%% md
### 2. Ընդհանուր մեթոդ ավելացնել

Ավելացրո՛ւ `Person`-ին `short_name()` մեթոդ, որը վերադարձնում է միայն առաջին
անունը։ Ստուգի՛ր, որ այն աշխատում է երեք դասի համար էլ՝ առանց որևէ տեղ
պատճենելու։

#%% code
# ...

#%% md
### 3. Երրորդ շերտ

Գրի՛ր `HeadTeacher` դաս, որը ժառանգում է **`Teacher`-ից** (ոչ թե `Person`-ից) և
ավելացնում `since_year` դաշտը։

Ստուգի՛ր, որ նա ունի և՛ `contact_line()`, և՛ `is_experienced()`։

#%% code
# ...

#%% md
### 4. Ո՞վ ումից

Ահա չորս օբյեկտ։ Ֆունկցիա գրի՛ր, որը տպում է ամեն մեկի անունը և այն, թե նա
`Person` է, թե ոչ։

**Հուշում:** `isinstance(x, Person)` վերադարձնում է `True` կամ `False`։

#%% code
people = [ani, tigran]

for person in people:
    # print the name and isinstance(person, Person)
    pass

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Աշխատավարձի բարձրացում

Ավելացրո՛ւ `Teacher`-ին `raise_salary(percent)` մեթոդ։ Ստուգի՛ր, որ
`is_experienced()`-ը դրանից հետո կարող է փոխվել։

#%% code
# ...

#%% md
### 6. Ընդհանուր հաշվիչ

Ավելացրո՛ւ `Person`-ին հաշվիչ, որը հաշվում է, թե քանի մարդ է ստեղծվել։ Ստուգի՛ր,
որ աշակերտ ստեղծելն էլ է հաշվիչը մեծացնում։

#%% code
# ...

#%% md
### 7. Հեռախոսների ցուցակ

Գրի՛ր ֆունկցիա, որը ստանում է `Person`-երի ցուցակ (խառը՝ աշակերտ, ուսուցիչ,
ծնող) և տպում է բոլորի կոնտակտային տողերը՝ դասավորված ըստ ազգանվան։

#%% code
# ...

#%% md
### 8. Ի՞նչ է `Person`-ը միայնակ

Ստեղծի՛ր `Person` օբյեկտ ուղղակիորեն՝ `Person("Nare Petrosyan", "11B", "094-...")`։

Աշխատո՞ւմ է։ Պե՞տք է արդյոք աշխատի։ Պատասխանը գրի՛ր markdown-ում։

#%% code
# ...

#%% md
## Մարտահրավեր

#%% md
### 9. Դպրոցի ամբողջ կազմը

Կառուցի՛ր `school.csv`-ից 36 `Student`, ապա ձեռքով ավելացրո՛ւ 5 `Teacher`։
Դի՛ր բոլորին մեկ ցուցակում և տպի՛ր կոնտակտային տեղեկատուն՝ դասավորված ըստ
ազգանվան։

Հեռախոսները կարող ես սարքել՝ `"077-00-00-" + str(10 + index)`։

#%% code
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

# ...

#%% md
### 10. Ժառանգե՞լ, թե՞ պարունակել

Ահա երկու տարբերակ նույն բանի համար։ Որ մեկն է ճիշտ, և ինչու՞։
Պատասխանը գրի՛ր markdown-ում։

```python
# A
class SchoolClass(Person):
    ...

# B
class SchoolClass:
    def __init__(self, name, students):
        self.students = students
```

#%% code
# No code needed -- the answer goes in a markdown cell.

#%% md
<div style="border-left: 6px solid #747; background: #f8f6fb; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#747; margin-top:0;">🏠 Տնային</h3>
<p style="color:#747; margin-bottom:0;">
Այս նոթատետրի <b>Լրացուցիչ</b> առաջադրանքները։<br/><br/>
<b>Նոր բան չկա</b> — ամեն առաջադրանք այս նոթատետրից է, և օգտագործում է միայն այն,
ինչ այսօր սովորեցինք։<br/>
Հաջորդ նիստը սկսվում է դրանց ստուգումով։
</p>
</div>

#%% md
## Ինչի հասանք

- `class Student(Person):` — **ժառանգում** է ընդհանուրը
- `super().__init__(...)` — կանչում է վերևինի `__init__`-ը։ **Առաջին տողն է**
- Մոռացած `super()` → `AttributeError`, որովհետև դաշտերը չեն լրացվել
- Ընդհանուր մեթոդը գրվում է **մեկ անգամ**, փոփոխվում է **մեկ տեղում**
- **«X-ը Y է»** → ժառանգում։ **«X-ը ունի Y»** → ցուցակ

## Ի՞նչ է գալիս հետո

Հիմա բոլոր մարդիկ ունեն նույն `contact_line()`-ը։ Բայց ուսուցչի տողում պետք է
երևա առարկան, իսկ աշակերտի տողում՝ միջինը։

Վաղը ժառանգող դասը կսովորի **փոխել** այն, ինչ ստացել է։
