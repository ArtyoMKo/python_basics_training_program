#%% md
# Օր 9 — Լուծումներ

#%% code
# Exercises 3, 4 and 5 - the class as a dictionary

class_grades = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3, "Mariam": 8}

print(class_grades["Ani"])
print(class_grades["Nare"])

class_grades["Tigran"] = 5          # add
class_grades["Aram"] = 4            # correct
del class_grades["Davit"]           # remove

print(class_grades)

#%% code
# Exercise 6 and Extra 7 - a safe lookup

looking_for = "Davit"

if looking_for in class_grades:
    print(f"{looking_for}: {class_grades[looking_for]}")
else:
    print("no such student in this class")

#%% code
# Extra 10 - a repeated key keeps only the LAST value

print({"Ani": 9, "Ani": 10})

#%% code
# Challenge 12 - build a dictionary from two lists.
# This is exactly what day 22 does when reading a file.

student_names = ["Ani", "Davit", "Nare"]
grade_values = [9, 6, 10]

class_grades = {}

for position in range(len(student_names)):
    class_grades[student_names[position]] = grade_values[position]

print(class_grades)
