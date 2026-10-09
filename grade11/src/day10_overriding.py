#%% md
# Օր 10 — Մեկ ցիկլ, շատ տեսակ

### Python 11-րդ դասարանի համար · Օր 10-ը 24-ից

Երեկ բոլոր մարդիկ ստացան նույն `contact_line()`-ը։ Բայց տնօրենին պետք է, որ
ուսուցչի տողում երևա **առարկան**, իսկ աշակերտի տողում՝ **միջինը**։

## ԱՅՍՕՐ:

- **Ա մաս:** փոխել ժառանգած մեթոդը
- **Բ մաս:** `super()` մեթոդի ներսում
- **Գ մաս:** մեկ ցիկլ, որը չի հարցնում՝ «սա ի՞նչ է»

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>class Student(Person)</code> · <code>super().__init__(...)</code><br/>
Ընդհանուրը գրվում է մեկ անգամ։<br/><br/>
<b>Այսօր ժառանգող դասը կսովորի փոխել այն, ինչ ստացել է։</b>
</p>
</div>

#%% md
## Ա մաս: Նույն անունով, այլ մարմնով

Ահա երեկվա վիճակը։

#%% code
class Person:
    def __init__(self, name, class_name, phone):
        self.name = name
        self.class_name = class_name
        self.phone = phone

    def label(self):
        return f"{self.name} ({self.class_name})"


class Student(Person):
    def __init__(self, name, class_name, phone, grades):
        super().__init__(name, class_name, phone)
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


class Teacher(Person):
    def __init__(self, name, class_name, phone, subject):
        super().__init__(name, class_name, phone)
        self.subject = subject


ani = Student("Ani Hakobyan", "11A", "077-11-22-33", [7, 6, 8, 9, 8])
tigran = Teacher("Tigran Mkrtchyan", "11A", "091-44-55-66", "Mathematics")

print(ani.label())
print(tigran.label())

#%% md
Երկու տողը նույնն են։ Տնօրենին պետք է՝

```
Ani Hakobyan (11A) — average 7.6
Tigran Mkrtchyan (11A) — Mathematics
```

Լուծումը՝ գրե՛լ `label()`-ը **նորից**, ժառանգող դասի ներսում։

#%% code
class Student(Person):
    def __init__(self, name, class_name, phone, grades):
        super().__init__(name, class_name, phone)
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def label(self):
        return f"{self.name} ({self.class_name}) — average {self.average():.1f}"


class Teacher(Person):
    def __init__(self, name, class_name, phone, subject):
        super().__init__(name, class_name, phone)
        self.subject = subject

    def label(self):
        return f"{self.name} ({self.class_name}) — {self.subject}"


ani = Student("Ani Hakobyan", "11A", "077-11-22-33", [7, 6, 8, 9, 8])
tigran = Teacher("Tigran Mkrtchyan", "11A", "091-44-55-66", "Mathematics")

print(ani.label())
print(tigran.label())

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b>Երբ ժառանգող դասում կա նույն անունով մեթոդ, Python-ը վերցնում է <b>նրան</b>։</b><br/><br/>
Սա ոչ մի հատուկ բառ չի պահանջում։ Պարզապես գրում ես մեթոդը նորից։<br/>
Ասում են՝ ժառանգող դասը <b>վերասահմանում է</b> (overrides) մեթոդը։
</p>
</div>

#%% md
## Բ մաս: Օգտագործել ժառանգածը, ոչ թե դեն նետել

Նկատի՛ր՝ երկու `label()`-ում էլ կրկնվում է `f"{self.name} ({self.class_name})"`։

Նորից նույն խնդիրը։ Լուծումը՝ կանչել **վերևինին** և ավելացնել։

#%% code
class Student(Person):
    def __init__(self, name, class_name, phone, grades):
        super().__init__(name, class_name, phone)
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def label(self):
        return super().label() + f" — average {self.average():.1f}"


class Teacher(Person):
    def __init__(self, name, class_name, phone, subject):
        super().__init__(name, class_name, phone)
        self.subject = subject

    def label(self):
        return super().label() + f" — {self.subject}"


ani = Student("Ani Hakobyan", "11A", "077-11-22-33", [7, 6, 8, 9, 8])
tigran = Teacher("Tigran Mkrtchyan", "11A", "091-44-55-66", "Mathematics")

print(ani.label())
print(tigran.label())

#%% md
Հիմա եթե տնօրենը ուզի փակագծերի փոխարեն գծիկ — փոխվում է **մեկ տեղ**՝ `Person`-ում։

#%% md
## Գ մաս: Ցիկլ, որը չի հարցնում

Ահա դպրոցի ամբողջ կազմը՝ մեկ ցուցակում։ Աշակերտներ և ուսուցիչներ՝ խառը։

#%% code
everyone = [
    Student("Ani Hakobyan", "11A", "077-11-22-33", [7, 6, 8, 9, 8]),
    Teacher("Tigran Mkrtchyan", "11A", "091-44-55-66", "Mathematics"),
    Student("Nare Petrosyan", "11B", "077-22-33-44", [10, 9, 10, 9, 10]),
    Teacher("Lilit Khachatryan", "11B", "091-55-66-77", "Physics"),
    Student("Aram Harutyunyan", "11C", "077-33-44-55", [3, 2, 4, 3, 5]),
]

for person in everyone:
    print(person.label())

#%% md
**Նայի՛ր ցիկլին ուշադիր։ Այնտեղ ոչ մի `if` չկա։**

Ոչ մի տեղ գրված չէ «եթե սա աշակերտ է՝ արա այսպես, եթե ուսուցիչ՝ այլ կերպ»։

#%% code
# What we would have had to write without overriding:
for person in everyone:
    if isinstance(person, Student):
        print(f"{person.name} ({person.class_name}) — average {person.average():.1f}")
    elif isinstance(person, Teacher):
        print(f"{person.name} ({person.class_name}) — {person.subject}")

#%% md
Այս ցիկլը աշխատում է։ Բայց ամեն նոր տեսակ ավելացնելիս պետք է **գտնել այն և
ավելացնել ևս մեկ `elif`**։ Իսկ եթե այդպիսի ցիկլ տասը տեղում կա՝ տասը խմբագրում։

Առաջին տարբերակում նոր տեսակ ավելացնելը ոչ մի ցիկլ չի փոխում։

#%% code
class Parent(Person):
    def __init__(self, name, class_name, phone, child_name):
        super().__init__(name, class_name, phone)
        self.child_name = child_name

    def label(self):
        return super().label() + f" — parent of {self.child_name}"


everyone.append(Parent("Sona Hakobyan", "11A", "055-77-88-99", "Ani Hakobyan"))

for person in everyone:
    print(person.label())

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<p style="color:#06c; margin:0;">
<b>Այս բանը անուն ունի՝ <b>բազմաձևություն</b> (polymorphism)։</b><br/><br/>
Բառը նշանակում է «շատ ձև»՝ մեկ կանչ, <code>person.label()</code>, և ամեն օբյեկտ
պատասխանում է իր ձևով։<br/><br/>
<b>Բառը հիմա ասացինք, որովհետև արդեն աշխատեց։</b> Առանց այս ցիկլը տեսնելու
սահմանումը ոչինչ չի տալիս։
</p>
</div>

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. `__str__` ժառանգությամբ

Ավելացրո՛ւ `Person`-ին `__str__`, որը վերադարձնում է `label()`-ը։ Ստուգի՛ր, որ
`print(person)` աշխատում է բոլոր չորս դասի համար։

#%% code
# ...

#%% md
### 2. Վերասահմանել `average`-ը

`HeadTeacher`-ը ուսուցիչ է, բայց նրա `label()`-ում պետք է գրվի `"head teacher"`
առարկայի փոխարեն։ Գրի՛ր այն՝ ժառանգելով `Teacher`-ից։

#%% code
# ...

#%% md
### 3. Հեռախոսագիրքը

Գրի՛ր ֆունկցիա `directory(people)`, որը տպում է բոլորի տողերը՝ դասավորված ըստ
անվան։ Ֆունկցիայի ներսում **ոչ մի `if` չպետք է լինի**։

#%% code
def directory(people):
    # ...
    pass


# directory(everyone)

#%% md
### 4. Ո՞վ է պատասխանում

Ահա չորս կանչ։ Առանց գործարկելու գրի՛ր markdown-ում, թե որ դասի `label()`-ն է
աշխատելու ամեն դեպքում։ Հետո գործարկի՛ր և ստուգի՛ր։

#%% code
p = Person("Gor Vardanyan", "11C", "093-11-11-11")
s = Student("Mane Avetisyan", "11C", "093-22-22-22", [8, 8, 8, 8, 8])
t = Teacher("Vahe Gevorgyan", "11C", "093-33-33-33", "History")

print(p.label())
print(s.label())
print(t.label())

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Ընդհանուր ամփոփում

Ավելացրո՛ւ `Person`-ին `summary()` մեթոդ, որը վերադարձնում է `"person"`։
Վերասահմանի՛ր այն երեք ժառանգող դասերում՝ `"student"`, `"teacher"`, `"parent"`։

Ապա հաշվի՛ր, թե ամեն տեսակից քանիսն են ցուցակում — **առանց `isinstance`-ի**։

#%% code
# ...

#%% md
### 6. Չվերասահմանված մեթոդ

Ավելացրո՛ւ `Person`-ին `can_vote()` մեթոդ, որը վերադարձնում է `True`։
Վերասահմանի՛ր այն **միայն** `Student`-ում՝ `False`։

Ստուգի՛ր բոլոր տեսակների վրա։

#%% code
# ...

#%% md
### 7. Երկու մակարդակ վերասահմանում

`HeadTeacher(Teacher)`-ում վերասահմանի՛ր `label()`-ը այնպես, որ այն կանչի
`super().label()`-ը — որը ինքն էլ կանչում է `Person.label()`-ը։

Տպի՛ր արդյունքը և հետևի՛ր շղթային։

#%% code
# ...

#%% md
### 8. Դպրոցի ֆայլից՝ խառը ցուցակ

Կառուցի՛ր 36 `Student` `school.csv`-ից, ավելացրո՛ւ 5 `Teacher`, և տպի՛ր բոլորի
տողերը մեկ ցիկլով։

#%% code
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

# ...

#%% md
## Մարտահրավեր

#%% md
### 9. Ցուցակը՝ ըստ տեսակի

Գրի՛ր ֆունկցիա, որը խառը ցուցակը բաժանում է բառարանի՝ տեսակի անունը → այդ
տեսակի օբյեկտների ցուցակ։ Օգտագործի՛ր 5-րդ վարժության `summary()`-ն, ոչ թե
`isinstance`։

#%% code
# ...

#%% md
### 10. Ե՞րբ չվերասահմանել

Ահա դաս, որը վերասահմանում է `average()`-ը այնպես, որ այն վերադարձնում է
**տող**, ոչ թե թիվ։

Գործարկի՛ր ցիկլը և նայի՛ր, թե ինչ է լինում։ Markdown-ում գրի՛ր, թե ինչու է սա
վտանգավոր, նույնիսկ երբ Python-ը սխալ չի տալիս։

#%% code
class StrangeStudent(Student):
    def average(self):
        return "very good"


group = [
    Student("Ani Hakobyan", "11A", "077-11-22-33", [7, 6, 8, 9, 8]),
    StrangeStudent("Hayk Hovhannisyan", "11A", "077-99-88-77", [2, 3, 2, 4, 3]),
]

for student in group:
    print(student.name, student.average())

# Now try to sort them by average and see what happens.

#%% md
## Ինչի հասանք

- Նույն անունով մեթոդ ժառանգող դասում → Python-ը վերցնում է **նրան**
- `super().label()` — օգտագործել ժառանգածը և **ավելացնել**, ոչ թե պատճենել
- Մեկ ցիկլ, **ոչ մի `if`** — ամեն օբյեկտ պատասխանում է իր ձևով
- Նոր տեսակ ավելացնելը **ոչ մի ցիկլ չի փոխում**
- Այս բանի անունը **բազմաձևություն** է — և բառն ասացինք վերջում, ոչ թե սկզբում

## Հաջորդ անգամ

Նոր շարահյուսություն չի լինի։ Վերցնելու ենք անցած դասընթացի մատյանը և
վերագրելու ենք այն **ամբողջությամբ օբյեկտներով** — կողք կողքի դնելով երկու
տարբերակը։

Դա նաև **միջանկյալ թեստից առաջ վերջին դասն է** — թեստը հանձնվում է 11-րդ օրից հետո։
