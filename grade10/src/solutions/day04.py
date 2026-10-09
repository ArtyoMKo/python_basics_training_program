#%% md
# Թեմա 4 — Լուծումներ

`input()`-ի փոխարեն արժեքները ուղիղ գրված են, որպեսզի կարողանաս գործարկել առանց
պատասխանելու։ Քո տետրում `input()`-ը պետք է մնա։

#%% code
# Exercise 2 - the grade plus one

answer = "9"                  # what input() would have given
grade = int(answer)

print(grade + 1)

#%% code
# Exercise 3 - the average of two grades

first_grade = int("9")
second_grade = int("6")

print(round((first_grade + second_grade) / 2, 1))

#%% code
# Extra 5 - int("9.5") fails because "9.5" is not a whole number.
# Use float() instead.

print(float("9.5"))

#%% code
# Extra 8 - str() makes text, so + joins instead of adding

print(str(9) + str(1))
print(9 + 1)
