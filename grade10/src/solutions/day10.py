#%% md
# Թեմա 11 — Լուծումներ

#%% code
# Exercises 1 and 2 - four bands, tested on four grades

for grade in [10, 8, 5, 2]:
    if grade >= 9:
        print(grade, "- excellent")
    elif grade >= 7:
        print(grade, "- good")
    elif grade >= 4:
        print(grade, "- satisfactory")
    else:
        print(grade, "- unsatisfactory")

#%% code
# Exercise 3 - a rule with and

grade = 8
attendance = 90

if grade >= 4 and attendance >= 80:
    print("certificate granted")
else:
    print("certificate not granted")

#%% code
# Extra 5 - not (grade >= 4) and grade < 4 are the same thing

grade = 3

print(not (grade >= 4))
print(grade < 4)

#%% code
# Challenge 10 - the real certificate rule, three conditions

grade = 8
attendance = 90
behaviour_ok = True

if grade >= 4 and attendance >= 80 and behaviour_ok:
    print("certificate granted")
else:
    print("certificate not granted")
