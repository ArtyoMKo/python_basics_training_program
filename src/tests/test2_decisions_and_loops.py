#%% md
# Ստուգողական 2 — Որոշումներ և ցիկլեր

### Օրեր 7–12 · Տնային · Մոտ 30 րոպե

Նույն կանոնները, ինչ առաջին անգամ. հուշաթերթը կարելի է, ինտերնետը՝ ոչ, անավարտը՝
նորմալ է։

#%% code
# Run this cell first - the other questions use it.

PASS_MARK = 4

student_names = ["Ani", "Davit", "Nare", "Aram", "Mariam", "Tigran", "Lilit", "Gor"]
class_grades = [9, 6, 10, 3, 8, 5, 8, 2]

print(len(student_names), "students")

#%% md
### Հարց 1 — ցուցակի հետ աշխատել

Ավելացրո՛ւ նոր աշակերտ երկու ցուցակին էլ (անուն և միավոր), հետո տպի՛ր,
թե քանիսն են դարձել։

#%% code
# Question 1

# your code here

#%% md
### Հարց 2 — պայման

Ստորև մեկ միավոր է։ Տպի՛ր `passed` կամ `failed`՝ `PASS_MARK`-ի հիման վրա։

#%% code
# Question 2

grade = 5

# your code here

#%% md
### Հարց 3 — elif շղթա

Գրի՛ր պայմանների շղթա, որը միավորը դասակարգում է չորս մակարդակի՝

- 9 կամ ավելի → `excellent`
- 7–8 → `good`
- 4–6 → `satisfactory`
- 4-ից ցածր → `unsatisfactory`

Ստուգի՛ր այն **չորս տարբեր միավորով**՝ մեկը ամեն մակարդակից։

#%% code
# Question 3

grade = 8

# your code here

#%% md
### Հարց 4 — ցիկլ

Տպի՛ր **բոլոր** աշակերտների անունները՝ ցիկլով։ Մեկ անուն՝ մեկ տողում։

#%% code
# Question 4

# your code here

#%% md
### Հարց 5 — ցիկլ և պայման

Տպի՛ր ամբողջ մատյանը՝ ամեն աշակերտի անունը և `passed`/`failed`։

Հուշում՝ երկու ցուցակը միասին օգտագործելու համար պետք է `range(len(...))`։

#%% code
# Question 5

# your code here

#%% md
### Հարց 6 — գումար և միջին

Հաշվի՛ր բոլոր միավորների գումարը ցիկլով, հետո տպի՛ր դասարանի միջինը՝
**մեկ նիշով կլորացրած**։

#%% code
# Question 6

# your code here

#%% md
### Հարց 7 — հաշվել պայմանով

Հաշվի՛ր, թե **քանի աշակերտ չի անցել**, և տպի՛ր այդ թիվը։

#%% code
# Question 7

# your code here

#%% md
### Հարց 8 — հավաքել նոր ցուցակ

Հավաքի՛ր **չանցած աշակերտների անունները** նոր ցուցակում և տպի՛ր այն։

#%% code
# Question 8

# your code here

#%% md
### Հարց 9 — սխալը գտնել

Ներքևի կոդը սխալ չի տալիս, բայց **սխալ պատասխան է տպում** 10 միավորի համար։

Գործարկի՛ր, նայի՛ր արդյունքին, և մեկնաբանության մեջ գրի՛ր՝ ինչու՞։
Հետո **ուղղի՛ր այն**։

#%% code
# Question 9 - this prints the wrong answer for 10. Why? Then fix it.
#
# It is wrong because:

grade = 10

if grade >= 4:
    print("satisfactory")
elif grade >= 7:
    print("good")
elif grade >= 9:
    print("excellent")

#%% md
---

**Վերջ։** Պահպանի՛ր և ուղարկի՛ր։
