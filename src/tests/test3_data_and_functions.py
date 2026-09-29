#%% md
# Ստուգողական 3 — Տվյալներ և ֆունկցիաներ

### Օրեր 13–18 · Տնային · Մոտ 30 րոպե

Նույն կանոնները։

#%% code
# Run this cell first.

PASS_MARK = 4

class_grades = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3,
                "Mariam": 8, "Tigran": 5, "Lilit": 8, "Gor": 2}

print(len(class_grades), "students")

#%% md
### Հարց 1 — բառարանից կարդալ

Տպի՛ր Նարեի միավորը՝ անունով փնտրելով։

#%% code
# Question 1

# your code here

#%% md
### Հարց 2 — բառարան փոփոխել

Արա՛ երեք բան և ամեն անգամ տպի՛ր բառարանը՝

1. ավելացրո՛ւ նոր աշակերտ
2. ուղղի՛ր Դավիթի միավորը 8-ի
3. հանի՛ր Գորին

#%% code
# Question 2

# your code here

#%% md
### Հարց 3 — անվտանգ որոնում

Գրի՛ր կոդ, որը փնտրում է `"Vahe"` աշակերտին։ Եթե նա կա — տպի՛ր միավորը։
Եթե չկա — տպի՛ր `no such student`։

**Ծրագիրը չպետք է սխալով կանգնի։**

#%% code
# Question 3

# your code here

#%% md
### Հարց 4 — ցիկլ բառարանի վրայով

Տպի՛ր ամբողջ մատյանը՝ ամեն տողում անուն և միավոր, `.items()`-ով։

#%% code
# Question 4

# your code here

#%% md
### Հարց 5 — ցիկլ, պայման, հաշվիչ

Հաշվի՛ր, թե քանի աշակերտ է անցել, և տպի՛ր թիվը։

#%% code
# Question 5

# your code here

#%% md
### Հարց 6 — ֆունկցիա գրել

Գրի՛ր `average_of(grades)` ֆունկցիան, որը **վերադարձնում** է ցուցակի միջինը՝
մեկ նիշով կլորացրած։

Հետո կանչի՛ր այն և տպի՛ր արդյունքը։

#%% code
# Question 6

# your code here

#%% md
### Հարց 7 — ֆունկցիա պարամետրով

Գրի՛ր `has_passed(grade)` ֆունկցիան, որը վերադարձնում է `True` կամ `False`։

Կանչի՛ր այն **երեք տարբեր միավորով** և տպի՛ր արդյունքները։

#%% code
# Question 7

# your code here

#%% md
### Հարց 8 — ֆունկցիա, որը ցուցակ է վերադարձնում

Գրի՛ր `failing_students(class_grades)` ֆունկցիան, որը վերադարձնում է չանցած
աշակերտների **անունների ցուցակը**։

Կանչի՛ր այն և տպի՛ր արդյունքը։

#%% code
# Question 8

# your code here

#%% md
### Հարց 9 — while ցիկլ

Ստորև `answers`-ը ցուցակ է՝ ուղիղ այն, ինչ ուսուցիչը կմուտքագրեր։

Գրի՛ր ցիկլ, որը անցնում է դրանց վրայով և կանգնում է `quit` բառից։
Թվերը հավաքի՛ր `collected` ցուցակում։ Այն, ինչ թիվ չէ, բաց թո՛ղ։

#%% code
# Question 9

answers = ["9", "6", "nine", "8", "quit", "10"]
collected = []

# your code here

print(collected)

#%% md
### Հարց 10 — տպել կամ վերադարձնել

Ներքևում երկու ֆունկցիա է։ Մեկնաբանության մեջ գրի՛ր՝ **ո՞րն է տարբերությունը**,
և ո՞րն է ավելի օգտակար, եթե ուզում ես արդյունքը համեմատել 8-ի հետ։

#%% code
# Question 10 - what is the difference? Which one can you compare with 8?
#
# Your answer:

def print_average(grades):
    print(sum(grades) / len(grades))


def average_of(grades):
    return sum(grades) / len(grades)

#%% md
---

**Վերջ։** Պահպանի՛ր և ուղարկի՛ր։
