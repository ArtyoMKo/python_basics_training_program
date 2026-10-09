#%% md
# Օր 7 — Լուծումներ

#%% code
# Exercises 1, 2, 3 and 4

student_names = ["Ani", "Davit", "Nare", "Aram"]

student_names.append("Tigran")

if "Aram" in student_names:
    student_names.remove("Aram")

student_names.sort()

print(student_names)
print(student_names[0:3])

#%% code
# Extra 5 - the three highest grades

class_grades = [9, 6, 10, 3, 8]
class_grades.sort(reverse=True)

print(class_grades[0:3])

#%% code
# Extra 7 - .remove() on a name that is not there raises an error.
# Guard it with in.

if "Vahe" in student_names:
    student_names.remove("Vahe")
else:
    print("Vahe is not in this class - nothing removed")

#%% code
# Challenge 10 - split the class into two groups

student_names = ["Ani", "Davit", "Nare", "Aram", "Mariam", "Tigran"]
half = len(student_names) // 2

print("group 1:", student_names[0:half])
print("group 2:", student_names[half:])
