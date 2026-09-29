#%% md
# Ստուգողական 4 — Ծրագիրը

### Օրեր 19–24 · Տնային · Մոտ 35 րոպե

Վերջին ստուգողականը։ Առաջին մասը տետրում է, երկրորդը՝ քո **իսկական ծրագրի** մասին։

Նույն կանոնները. հուշաթերթը կարելի է, ինտերնետը՝ ոչ, անավարտը՝ նորմալ է։

#%% code
# Run this cell first.

PASS_MARK = 4

class_grades = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3,
                "Mariam": 8, "Tigran": 5, "Lilit": 8, "Gor": 2}

print(len(class_grades), "students")

#%% md
### Հարց 1 — ֆունկցիա, որը վերադարձնում է

Գրի՛ր `class_average(class_grades)` ֆունկցիան, որը **վերադարձնում** է դասարանի
միջինը՝ մեկ նիշով։

#%% code
# Question 1

# your code here

#%% md
### Հարց 2 — լռելյայն արժեք

Գրի՛ր `has_passed(grade, pass_mark=PASS_MARK)` ֆունկցիան։

Կանչի՛ր այն երկու անգամ՝ մեկ անգամ առանց երկրորդ արժեքի, մեկ անգամ՝ `pass_mark=7`-ով։

#%% code
# Question 2

# your code here

#%% md
### Հարց 3 — ֆունկցիան կանչում է ֆունկցիա

Գրի՛ր `print_register(class_grades)`, որը տպում է ամբողջ մատյանը և ներսում
**կանչում է** `has_passed`-ը։

#%% code
# Question 3

# your code here

#%% md
### Հարց 4 — տողը բաժանել

Ստորև մեկ տող է՝ ուղիղ այնպես, ինչպես ֆայլում է գրված։

Բաժանի՛ր այն ստորակետով և տպի՛ր անունն ու միավորը առանձին։
**Ուշադի՛ր** — միավորը պետք է թիվ լինի, ոչ թե տեքստ։

#%% code
# Question 4

line = "Ani,9"

# your code here

#%% md
### Հարց 5 — ֆայլից բառարան

Ստորև `lines`-ը ցուցակ է՝ ուղիղ այնպես, ինչպես ֆայլից կկարդայինք
(առաջին տողը վերնագիրն է)։

Կազմի՛ր դրանից բառարան՝ `{"Ani": 9, ...}`։

#%% code
# Question 5

lines = ["name,grade", "Ani,9", "Davit,6", "Nare,10"]
class_from_file = {}

# your code here

print(class_from_file)

#%% md
### Հարց 6 — քո ծրագրի մասին

Պատասխանի՛ր մեկնաբանության մեջ, **առանց ֆայլերը բացելու** — հիշողությամբ։

#%% code
# Question 6
#
# (a) Which file holds PASS_MARK?
#
# (b) Which file reads data/my_class.csv?
#
# (c) Which file does the calculations?
#
# (d) Why does grades.py NOT import storage.py?
#
# (e) What are the two terminal commands you have used in this course?

#%% md
### Հարց 7 — սխալը գտնել

Ներքևի կոդը սխալ է տալիս։ Գործարկի՛ր, կարդա՛, և մեկնաբանության մեջ գրի՛ր՝
սխալի անունը և ինչու է այն տեղի ունենում։ Հետո **ուղղի՛ր** այն։

#%% code expected-error: KeyError
# Question 7 - run, read, explain, then fix.
#
# The error is called:
# It happens because:

print(class_grades["Vahe"])

#%% md
---

## Վերջին հարցը

Այս հարցը մի քիչ տարբեր է։ **Այսպիսի բան դասին չենք արել։**

Բոլոր գործիքները, որ պետք են, արդեն գիտես — ցիկլ, պայման, բառարան, փոփոխական։
Նոր շարահյուսություն պետք չէ։

**Կարևորն այն չէ, թե կստացվի, թե ոչ։** Կարևորն այն է, թե ինչ ես անում, երբ
նայում ես հարցին։ Ուստի՝

- Նախ **մեկնաբանության մեջ գրի՛ր**, թե ինչպես կմոտենաս խնդրին՝ հայերեն, սովորական
  բառերով, նախքան կոդ գրելը։
- Հետո փորձի՛ր գրել այն։
- Եթե չստացվի, **թող մնա անավարտ** և գրի՛ր, թե որտեղ կանգնեցիր։

Ազնիվ անավարտ պատասխանը այստեղ ավելի արժեքավոր է, քան ճիշտը։

#%% md
### Հարց 8

Գտի՛ր այն աշակերտին, ում միավորը **ամենամոտն է դասարանի միջինին**։

Օրինակ՝ եթե միջինը 6.4 է, և միավորները 9, 6, 10, 3 են, ապա ամենամոտը 6-ն է։

#%% code
# Question 8
#
# First, in plain words: how would you solve this? Write it here before any code.
#
# My approach:
#
#
# Now try to write it. If you get stuck, leave it and say where you stopped.

class_grades = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3,
                "Mariam": 8, "Tigran": 5, "Lilit": 8, "Gor": 2}

# your code here

#%% md
---

**Վերջ — և դասընթացի վերջը։**

Պահպանի՛ր և ուղարկի՛ր։ Շնորհակալություն քսանչորս օրվա համար։
