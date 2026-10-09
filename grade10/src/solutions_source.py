#%% day02 md
# Թեմա 2 — Լուծումներ

Այս լուծումները **մեկ հնարավոր տարբերակն** են։ Եթե քոնը այլ է, բայց աշխատում է —
քոնը նույնպես ճիշտ է։

#%% day02 code
# Exercises 1 and 2 - the header and four students

print("7-B class - biology")
print()
print("Ani:", 9)
print("Davit:", 6)
print("Nare:", 10)
print("Aram:", 3)

#%% day02 code
# Extra 8 - a quote inside text. Use the other kind of quote outside.

print('He said "yes"')

#%% day02 code
# Challenge 9 - aligned columns by hand: pad the short names with spaces

print("Ani      9")
print("Davit    6")
print("Mariam   8")

#%% day03 md
# Թեմա 3 — Լուծումներ

#%% day03 code
# Exercises 1 and 2 - four types, checked

student_name = "Ani"
student_grade = 9
class_average = 6.5
student_passed = True

print(type(student_name))
print(type(student_grade))
print(type(class_average))
print(type(student_passed))

#%% day03 code
# Exercise 3 - sum and average of two grades

print(9 + 6)
print((9 + 6) / 2)

#%% day03 code
# Exercise 4 - the fix: make both of them text

print("Ani" + " " + "9")

#%% day03 code
# Extra 5 and 6 - * repeats text, but multiplies numbers

print("Ani" * 3)
print("9" * 3)
print(9 * 3)

#%% day03 code
# Challenge 10 - // is whole division, % is the remainder

print(10 // 3)      # how many whole 3s fit into 10
print(10 % 3)       # what is left over

#%% day04 md
# Թեմա 4 — Լուծումներ

`input()`-ի փոխարեն արժեքները ուղիղ գրված են, որպեսզի կարողանաս գործարկել առանց
պատասխանելու։ Քո տետրում `input()`-ը պետք է մնա։

#%% day04 code
# Exercise 2 - the grade plus one

answer = "9"                  # what input() would have given
grade = int(answer)

print(grade + 1)

#%% day04 code
# Exercise 3 - the average of two grades

first_grade = int("9")
second_grade = int("6")

print(round((first_grade + second_grade) / 2, 1))

#%% day04 code
# Extra 5 - int("9.5") fails because "9.5" is not a whole number.
# Use float() instead.

print(float("9.5"))

#%% day04 code
# Extra 8 - str() makes text, so + joins instead of adding

print(str(9) + str(1))
print(9 + 1)

#%% day05 md
# Թեմա 5 — Լուծումներ

#%% day05 code
# Exercises 1, 2 and 3

student_name = "Ani"
student_grade = 9
subject = "biology"

print(f"{student_name} - {subject} - {student_grade} points")

student_grade = student_grade + 1

print(f"{student_name} - {subject} - {student_grade} points")

#%% day05 code
# Extra 5 - the average in a variable, one decimal place

first_grade = 9
second_grade = 6
average = (first_grade + second_grade) / 2

print(f"Average: {average:.1f}")

#%% day05 code
# Challenge 9 - a five-student register with separate variables

student_1_name = "Ani"
student_1_grade = 9
student_2_name = "Davit"
student_2_grade = 6
student_3_name = "Nare"
student_3_grade = 10

print("7-B class")
print()
print(f"{student_1_name}: {student_1_grade}")
print(f"{student_2_name}: {student_2_grade}")
print(f"{student_3_name}: {student_3_grade}")

#%% day06 md
# Թեմա 6 — Լուծումներ

#%% day06 code
# Exercises 3 and 4 - the whole class in two lists

student_names = ["Ani", "Davit", "Nare", "Aram", "Mariam",
                 "Tigran", "Lilit", "Gor", "Anahit", "Hayk"]
class_grades = [9, 6, 10, 3, 8, 5, 8, 4, 9, 2]

print("students:", len(student_names))
print("first:   ", student_names[0])
print("last:    ", student_names[-1])

#%% day06 code
# Extra 6 and 7 - one row, and the sum of the first three

print(f"{student_names[2]}: {class_grades[2]}")
print(class_grades[0] + class_grades[1] + class_grades[2])

#%% day06 code
# Challenge 10 - the whole register, one index at a time.
# Ten students, ten lines. Day 11 turns this into four.

print(f"{student_names[0]}: {class_grades[0]}")
print(f"{student_names[1]}: {class_grades[1]}")
print(f"{student_names[2]}: {class_grades[2]}")

#%% day07 md
# Թեմա 7 — Լուծումներ

#%% day07 code
# Exercises 1, 2, 3 and 4

student_names = ["Ani", "Davit", "Nare", "Aram"]

student_names.append("Tigran")

if "Aram" in student_names:
    student_names.remove("Aram")

student_names.sort()

print(student_names)
print(student_names[0:3])

#%% day07 code
# Extra 5 - the three highest grades

class_grades = [9, 6, 10, 3, 8]
class_grades.sort(reverse=True)

print(class_grades[0:3])

#%% day07 code
# Extra 7 - .remove() on a name that is not there raises an error.
# Guard it with in.

if "Vahe" in student_names:
    student_names.remove("Vahe")
else:
    print("Vahe is not in this class - nothing removed")

#%% day07 code
# Challenge 10 - split the class into two groups

student_names = ["Ani", "Davit", "Nare", "Aram", "Mariam", "Tigran"]
half = len(student_names) // 2

print("group 1:", student_names[0:half])
print("group 2:", student_names[half:])

#%% day09 md
# Թեմա 10 — Լուծումներ

#%% day09 code
# Exercises 1, 2 and 3

PASS_MARK = 4

student_name = "Ani"
grade = 9

if grade == 10:
    print(f"{student_name}: excellent")
elif grade >= PASS_MARK:
    print(f"{student_name}: passed")
else:
    print(f"{student_name}: failed")

#%% day09 code
# Extra 7 - compare two grades

first_grade = 9
second_grade = 6

if first_grade > second_grade:
    print("the first one is higher")
else:
    print("the second one is higher or equal")

#%% day09 code
# Challenge 11 - a condition inside a condition

student_names = ["Ani", "Davit"]
student_name = "Ani"
grade = 10

if student_name in student_names:
    if grade == 10:
        print(f"{student_name} is in the class and has a perfect grade")

#%% day10 md
# Թեմա 11 — Լուծումներ

#%% day10 code
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

#%% day10 code
# Exercise 3 - a rule with and

grade = 8
attendance = 90

if grade >= 4 and attendance >= 80:
    print("certificate granted")
else:
    print("certificate not granted")

#%% day10 code
# Extra 5 - not (grade >= 4) and grade < 4 are the same thing

grade = 3

print(not (grade >= 4))
print(grade < 4)

#%% day10 code
# Challenge 10 - the real certificate rule, three conditions

grade = 8
attendance = 90
behaviour_ok = True

if grade >= 4 and attendance >= 80 and behaviour_ok:
    print("certificate granted")
else:
    print("certificate not granted")

#%% day11 md
# Թեմա 12 — Լուծումներ

#%% day11 code
# Exercises 3, 4 and 5 - everything with a loop

PASS_MARK = 4

student_names = ["Ani", "Davit", "Nare", "Aram", "Mariam"]
class_grades = [9, 6, 10, 3, 8]

for student_name in student_names:
    print(student_name)

print()

for grade in class_grades:
    if grade >= PASS_MARK:
        print(grade, "- passed")
    else:
        print(grade, "- failed")

#%% day11 code
# Exercise 6 - the whole register in four lines

for position in range(len(student_names)):
    if class_grades[position] >= PASS_MARK:
        print(f"{student_names[position]}: passed")
    else:
        print(f"{student_names[position]}: failed")

#%% day11 code
# Extra 11 - after the loop, the variable keeps the LAST value it had

for student_name in student_names:
    pass

print("after the loop:", student_name)

#%% day11 code
# Challenge 12 - a numbered register. position starts at 0, so add 1.

for position in range(len(student_names)):
    print(f"{position + 1}. {student_names[position]}: {class_grades[position]}")

#%% day12 md
# Թեմա 13 — Լուծումներ

#%% day12 code
# Exercises 1 and 2 - total and average

class_grades = [9, 6, 10, 3, 8, 5, 8, 4, 9, 2, 8, 6]

total = 0
for grade in class_grades:
    total = total + grade

print(f"Total:   {total}")
print(f"Average: {total / len(class_grades):.1f}")

#%% day12 code
# Exercise 4 - how many have 10

how_many = 0

for grade in class_grades:
    if grade == 10:
        how_many = how_many + 1

print(how_many)

#%% day12 code
# Extra 6 and 7 - percentage passed, and the average of those who passed

PASS_MARK = 4

passed_total = 0
passed_count = 0

for grade in class_grades:
    if grade >= PASS_MARK:
        passed_total = passed_total + grade
        passed_count = passed_count + 1

print(f"passed: {passed_count / len(class_grades) * 100:.0f}%")
print(f"their average: {passed_total / passed_count:.1f}")

#%% day12 code
# Challenge 10 - a text chart

for mark in range(10, 0, -1):
    how_many = 0
    for grade in class_grades:
        if grade == mark:
            how_many = how_many + 1
    print(f"{mark:>2}: {'*' * how_many}")

#%% day13 md
# Թեմա 16 — Լուծումներ

#%% day13 code
# Exercises 1, 2, 3 and 4 - all together

PASS_MARK = 4

student_names = ["Ani", "Davit", "Nare", "Aram", "Mariam", "Tigran",
                 "Lilit", "Gor", "Anahit", "Hayk", "Sona", "Vahe"]
class_grades = [9, 6, 10, 3, 8, 5, 8, 4, 9, 2, 8, 6]

how_many_passed = 0
failing_students = []

for position in range(len(class_grades)):
    if class_grades[position] >= PASS_MARK:
        how_many_passed = how_many_passed + 1
    else:
        failing_students.append(student_names[position])

print(f"passed: {how_many_passed}")
print(f"failed: {failing_students}")

best_position = 0
for position in range(len(class_grades)):
    if class_grades[position] > class_grades[best_position]:
        best_position = position

print(f"highest: {student_names[best_position]} ({class_grades[best_position]})")

#%% day13 code
# Extra 5 - the lowest. Same shape, < instead of >.

worst_position = 0
for position in range(len(class_grades)):
    if class_grades[position] < class_grades[worst_position]:
        worst_position = position

print(f"lowest: {student_names[worst_position]} ({class_grades[worst_position]})")

#%% day13 code
# Challenge 11 - the student closest to the average.
# abs() removes the minus sign, so a distance is never negative.

total = 0
for grade in class_grades:
    total = total + grade
average = total / len(class_grades)

closest_position = 0
for position in range(len(class_grades)):
    if abs(class_grades[position] - average) < abs(class_grades[closest_position] - average):
        closest_position = position

print(f"average {average:.1f}, closest: {student_names[closest_position]}")

#%% day16 md
# Թեմա 15 — Լուծումներ

`input()`-ի փոխարեն ցուցակ է օգտագործված, որպեսզի կարողանաս գործարկել։
Քո տետրում `input()`-ը պետք է մնա։

#%% day16 code
# Exercises 1-4 - the full loop with every check

answers = ["9", "nine", "15", "6", "quit"]      # what the teacher would type
class_grades = []

for answer in answers:
    if answer == "quit":
        break

    if not answer.isdigit():
        print(f"'{answer}' is not a number.")
        continue

    grade = int(answer)

    if grade < 1 or grade > 10:
        print(f"{grade} must be between 1 and 10.")
        continue

    class_grades.append(grade)

print(f"collected {len(class_grades)}: {class_grades}")

total = 0
for grade in class_grades:
    total = total + grade
print(f"average: {total / len(class_grades):.1f}")

#%% day08 md
# Թեմա 9 — Լուծումներ

#%% day08 code
# Exercises 3, 4 and 5 - the class as a dictionary

class_grades = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3, "Mariam": 8}

print(class_grades["Ani"])
print(class_grades["Nare"])

class_grades["Tigran"] = 5          # add
class_grades["Aram"] = 4            # correct
del class_grades["Davit"]           # remove

print(class_grades)

#%% day08 code
# Exercise 6 and Extra 7 - a safe lookup

looking_for = "Davit"

if looking_for in class_grades:
    print(f"{looking_for}: {class_grades[looking_for]}")
else:
    print("no such student in this class")

#%% day08 code
# Extra 10 - a repeated key keeps only the LAST value

print({"Ani": 9, "Ani": 10})

#%% day08 code
# Challenge 12 - build a dictionary from two lists.
# This is exactly what day 22 does when reading a file.

student_names = ["Ani", "Davit", "Nare"]
grade_values = [9, 6, 10]

class_grades = {}

for position in range(len(student_names)):
    class_grades[student_names[position]] = grade_values[position]

print(class_grades)

#%% day14 md
# Թեմա 8 — Լուծումներ

#%% day14 code
# Exercises 1-4 - the full register from a dictionary

PASS_MARK = 4

class_grades = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3,
                "Mariam": 8, "Tigran": 5, "Lilit": 8, "Gor": 4}

total = 0
failing = 0

print("=== REGISTER ===")

for student_name, grade in class_grades.items():
    if grade >= PASS_MARK:
        result = "passed"
    else:
        result = "failed"
        failing = failing + 1
    total = total + grade
    print(f"{student_name:<10} {grade:>3}   {result}")

print()
print(f"students: {len(class_grades)}")
print(f"average:  {total / len(class_grades):.1f}")
print(f"failing:  {failing}")

#%% day14 code
# Extra 8 - a numbered register needs a counter before the loop

number = 1

for student_name, grade in class_grades.items():
    print(f"{number}. {student_name:<10} {grade:>3}")
    number = number + 1

#%% day14 code
# Extra 10 - names starting with A. student_name[0] is the first letter.

for student_name, grade in class_grades.items():
    if student_name[0] == "A":
        print(student_name)

#%% day14 code
# Challenge 11 - sorted by grade, high to low

for mark in range(10, 0, -1):
    for student_name, grade in class_grades.items():
        if grade == mark:
            print(f"{student_name:<10} {grade:>3}")

#%% day15 md
# Թեմա 14 — Լուծումներ

#%% day15 code
# Exercises 1-5 - report cards with several grades each

PASS_MARK = 4

class_grades = {
    "Ani": [9, 10, 8],
    "Davit": [6, 5, 7],
    "Nare": [10, 10, 9],
    "Aram": [3, 4, 2],
}

class_grades["Ani"].append(7)

print("=== REPORT CARDS ===")

for student_name, grades in class_grades.items():
    total = 0
    for grade in grades:
        total = total + grade
    student_average = total / len(grades)

    if student_average >= PASS_MARK:
        result = "passed"
    else:
        result = "failed"

    print(f"{student_name:<10} {str(grades):<16} {student_average:.1f}   {result}")

#%% day15 code
# Extra 8 - each student's best grade

for student_name, grades in class_grades.items():
    highest = grades[0]
    for grade in grades:
        if grade > highest:
            highest = grade
    print(f"{student_name}: best {highest}")

#%% day15 code
# Extra 11 - an empty list makes the average divide by zero.
# Guard it before dividing.

grades = []

if not grades:
    print("no grades yet")
else:
    print(sum(grades) / len(grades))

#%% day15 code
# Challenge 12 - who improved the most. :+d shows the plus sign.

for student_name, grades in class_grades.items():
    improvement = grades[-1] - grades[0]
    print(f"{student_name}: {improvement:+d}")

#%% day17 md
# Թեմա 17 — Լուծումներ

#%% day17 code
# Exercises 2, 4 and 5 - the function, used everywhere

PASS_MARK = 4

class_grades = {
    "Ani": [9, 10, 8],
    "Davit": [6, 5, 7],
    "Nare": [10, 10, 9],
    "Aram": [3, 4, 2],
}


def average_of(grades):
    total = 0
    for grade in grades:
        total = total + grade
    return round(total / len(grades), 1)


for student_name, grades in class_grades.items():
    print(f"{student_name:<10} {average_of(grades)}")

#%% day17 code
# Extra 6, 7 and 8 - three more small functions

def highest_of(grades):
    highest = grades[0]
    for grade in grades:
        if grade > highest:
            highest = grade
    return highest


def lowest_of(grades):
    lowest = grades[0]
    for grade in grades:
        if grade < lowest:
            lowest = grade
    return lowest


def print_report_card(student_name, grades):
    print(f"{student_name:<10} {average_of(grades):>5}  "
          f"best {highest_of(grades)}  worst {lowest_of(grades)}")


for student_name, grades in class_grades.items():
    print_report_card(student_name, grades)

#%% day17 code
# Extra 10 - an empty list divides by zero. Guard it inside the function.

def average_of(grades):
    if not grades:
        return 0
    total = 0
    for grade in grades:
        total = total + grade
    return round(total / len(grades), 1)


print(average_of([]))

#%% day17 code
# Challenge 11 - the whole register as one function

def class_report(class_grades):
    print("=== REGISTER ===")
    for student_name, grades in class_grades.items():
        print(f"{student_name:<10} {average_of(grades)}")
    print(f"{len(class_grades)} students")


class_report(class_grades)

#%% day18 md
# Թեմա 18 — Լուծումներ

**Պահի՛ր այս տետրը։** 20-րդ թեմայում այս ֆունկցիաները տեղափոխվում են `grades.py` ֆայլ։

#%% day18 code
# Exercises 1-4 - the four-function toolkit

PASS_MARK = 4


def average_of(grades):
    """Return the average of a list of grades."""
    if not grades:
        return 0
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


my_class = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3,
            "Mariam": 8, "Tigran": 5, "Lilit": 8, "Gor": 4,
            "Anahit": 9, "Hayk": 2, "Sona": 8, "Vahe": 6}

print("average:", average_of(list(my_class.values())))
print("highest:", highest_of(my_class))
print("failing:", failing_students(my_class))

#%% day18 code
# Extra 5, 6 and 8

def lowest_of(class_grades):
    """Return the name of the student with the lowest grade."""
    worst_name = ""
    worst_grade = 11
    for student_name, grade in class_grades.items():
        if grade < worst_grade:
            worst_grade = grade
            worst_name = student_name
    return worst_name


def how_many_passed(class_grades, pass_mark=PASS_MARK):
    """Return how many students passed."""
    how_many = 0
    for student_name, grade in class_grades.items():
        if grade >= pass_mark:
            how_many = how_many + 1
    return how_many


def grade_band(grade):
    """Return the name of the band this grade falls into."""
    if grade >= 9:
        return "excellent"
    elif grade >= 7:
        return "good"
    elif grade >= 4:
        return "satisfactory"
    return "unsatisfactory"


print(lowest_of(my_class))
print(how_many_passed(my_class))
print(grade_band(9))

#%% day18 code
# Extra 9 - a function with no return gives back None

def print_average(grades):
    print(sum(grades) / len(grades))


print(print_average([9]))

#%% day18 code
# Challenge 11 - a function can return a dictionary

def class_summary(class_grades):
    """Return the headline numbers as a dictionary."""
    return {
        "average": average_of(list(class_grades.values())),
        "passed": how_many_passed(class_grades),
        "failed": len(failing_students(class_grades)),
    }


print(class_summary(my_class))

#%% day19 md
# Թեմա 19 — Լուծումներ

**Սա ամբողջական ծրագիրն է։** 20-րդ և 21-րդ թեմաներին այն բաժանվում է չորս ֆայլի։

#%% day19 code
# The whole assembled register program

PASS_MARK = 4
DECIMAL_PLACES = 1
NAME_WIDTH = 12

class_grades = {
    "Ani": [9, 10, 8],
    "Davit": [6, 5, 7],
    "Nare": [10, 10, 9],
    "Aram": [3, 4, 2],
    "Mariam": [8, 8, 9],
    "Tigran": [5, 6, 5],
}


def average_of(grades):
    """Return the average of a list of grades."""
    if not grades:
        return 0
    total = 0
    for grade in grades:
        total = total + grade
    return round(total / len(grades), DECIMAL_PLACES)


def has_passed(grades, pass_mark=PASS_MARK):
    """Return True if this student's average is a pass."""
    return average_of(grades) >= pass_mark


def failing_students(class_grades):
    """Return the names of the students who did not pass."""
    failing = []
    for student_name, grades in class_grades.items():
        if not has_passed(grades):
            failing.append(student_name)
    return failing


def class_average(class_grades):
    """Return the average of every student's average."""
    all_averages = []
    for student_name, grades in class_grades.items():
        all_averages.append(average_of(grades))
    return average_of(all_averages)


def print_register(class_grades):
    """Print the whole register, one line per student."""
    print()
    print("=== REGISTER ===")
    for student_name, grades in class_grades.items():
        if has_passed(grades):
            result = "passed"
        else:
            result = "failed"
        print(f"{student_name:<{NAME_WIDTH}} {str(grades):<14} "
              f"{average_of(grades):>5}   {result}")
    print()
    print(f"students:      {len(class_grades)}")
    print(f"class average: {class_average(class_grades)}")
    print(f"did not pass:  {len(failing_students(class_grades))}")


print_register(class_grades)

#%% day19 code
# Extra 8 - removing a student, guarded with in

def remove_student(class_grades, student_name):
    """Remove one student. Says so if there is no such student."""
    if student_name not in class_grades:
        print(f"{student_name} is not in this class - nothing removed")
        return
    del class_grades[student_name]
    print(f"{student_name} removed")


remove_student(class_grades, "Tigran")
remove_student(class_grades, "Vahe")
