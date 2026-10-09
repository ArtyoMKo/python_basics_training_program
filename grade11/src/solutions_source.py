#%% day01 md
# Օր 1 — Լուծումներ

Այս լուծումները **մեկ հնարավոր տարբերակն** են։ Եթե քոնը այլ է, բայց աշխատում է —
քոնը նույնպես ճիշտ է։

#%% day01 code
from pathlib import Path

lines = Path("school.csv").read_text(encoding="utf-8").strip().splitlines()

# Required 1 - every distinct subject
subjects = []
for line in lines[1:]:
    if line == "":
        continue
    subject = line.split(",")[2]
    if subject not in subjects:
        subjects.append(subject)

print(subjects)

#%% day01 code
# Required 2 - the students of one class, without repeats
names = []
for line in lines[1:]:
    if line == "":
        continue
    parts = line.split(",")
    if parts[0] == "11B" and parts[1] not in names:
        names.append(parts[1])

print(len(names), "students")
print(names)

#%% day01 code
# Required 3 and 4 - failing grades, and one subject's average
PASS_MARK = 4
failing = 0
subject_total = 0
subject_count = 0

for line in lines[1:]:
    if line == "":
        continue
    parts = line.split(",")
    grade = int(parts[3])
    if grade < PASS_MARK:
        failing = failing + 1
    if parts[2] == "Mathematics":
        subject_total = subject_total + grade
        subject_count = subject_count + 1

print("failing grades:", failing)
print("Mathematics average:", subject_total / subject_count)

#%% day01 code
# Extra 7 - the students with at least one failing grade
at_risk = []
for line in lines[1:]:
    if line == "":
        continue
    parts = line.split(",")
    if int(parts[3]) < PASS_MARK and parts[1] not in at_risk:
        at_risk.append(parts[1])

print(len(at_risk), "students at risk")

#%% day02 md
# Օր 2 — Լուծումներ

#%% day02 code
# Required 1 - a default for the rounding
def class_average(grades, digits=1):
    return round(sum(grades) / len(grades), digits)


print(class_average([9, 6, 10, 3, 8]))
print(class_average([9, 6, 10, 3, 8], 2))

#%% day02 code
# Required 2 - a default for the school name
def report_header(class_name, school="School N 5"):
    print(school)
    print("Class:", class_name)


report_header("11A")
report_header("11B", "School N 12")

#%% day02 code
# Required 3 - one change per call, each named
def attendance_line(name, present=True, late=False, note=""):
    status = "present"
    if not present:
        status = "absent"
    if late:
        status = status + ", late"
    if note != "":
        status = status + f" ({note})"
    return f"{name}: {status}"


print(attendance_line("Ani"))
print(attendance_line("Davit", present=False))
print(attendance_line("Nare", late=True))
print(attendance_line("Aram", note="left early"))

#%% day02 code
# Required 4 - two defaults working together
def failing_students(grades, pass_mark=4, sort_them=False):
    names = []
    for name in grades:
        if grades[name] < pass_mark:
            names.append(name)
    if sort_them:
        names = sorted(names)
    return names


register = {"Ani": 9, "Davit": 6, "Aram": 3, "Hayk": 2, "Nare": 10}
print(failing_students(register))
print(failing_students(register, sort_them=True))
print(failing_students(register, pass_mark=7, sort_them=True))

#%% day02 code
# Challenge 10 - the mutable default argument
#
# The list is created ONCE, when the function is defined -- not on each call.
# So every call that does not pass its own list shares the same one.
#
# The fix is always the same shape:
def add_student(name, register=None):
    if register is None:
        register = []
    register.append(name)
    return register


print(add_student("Ani"))
print(add_student("Davit"))

#%% day03 md
# Օր 3 — Լուծումներ

#%% day03 code
register = {"Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3, "Mariam": 8, "Hayk": 2}
PASS_MARK = 4


# Required 1 - two values, one pass
def highest_and_lowest(grades):
    highest = None
    lowest = None
    for name in grades:
        grade = grades[name]
        if highest is None or grade > highest:
            highest = grade
        if lowest is None or grade < lowest:
            lowest = grade
    return highest, lowest


highest, lowest = highest_and_lowest(register)
print("highest:", highest, "lowest:", lowest)

#%% day03 code
# Required 2 - the name as well as the number
def best_student(grades):
    best_name = None
    best_grade = None
    for name in grades:
        if best_grade is None or grades[name] > best_grade:
            best_name = name
            best_grade = grades[name]
    return best_name, best_grade


name, grade = best_student(register)
print(f"best: {name} with {grade}")

#%% day03 code
# Required 3 - two lists out of one loop
def split_by_result(grades, pass_mark=4):
    passed = []
    failed = []
    for name in grades:
        if grades[name] >= pass_mark:
            passed.append(name)
        else:
            failed.append(name)
    return passed, failed


passed, failed = split_by_result(register)
print("passed:", passed)
print("failed:", failed)

#%% day03 code
# Required 4 - four values, so a dictionary rather than a tuple
def register_report(grades, pass_mark=4):
    passed, failed = split_by_result(grades, pass_mark)
    return {
        "students": len(grades),
        "average": sum(grades.values()) / len(grades),
        "passed": len(passed),
        "failed": len(failed),
    }


report = register_report(register)
for key in report:
    print(f"{key:<10} {report[key]}")

#%% day03 code
# Extra 6 - swapping without a third variable
first = "Ani"
second = "Davit"

first, second = second, first

print(first, second)

#%% day04 md
# Օր 4 — Լուծումներ

#%% day04 code
register = {
    "Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3, "Mariam": 8, "Tigran": 7,
    "Lilit": 5, "Gor": 4, "Anahit": 9, "Hayk": 2, "Sona": 8, "Vahe": 6,
}
PASS_MARK = 4

# Required 1 - three comprehensions
above_seven = [name for name in register if register[name] > 7]
plus_one = [register[name] + 1 for name in register]
starts_with_a = [name for name in register if name.startswith("A")]

print(above_seven)
print(plus_one)
print(starts_with_a)

#%% day04 code
# Required 2 - a loop turned into one line
short_names = [name for name in register if len(name) <= 4]
print(short_names)

#%% day04 code
# Required 3 - one line turned back into a loop
result_again = []
for name in register:
    if register[name] >= 8:
        result_again.append(name + ": " + str(register[name]))

print(result_again)

#%% day04 code
# Required 4 - from the school file
from pathlib import Path

lines = Path("school.csv").read_text(encoding="utf-8").strip().splitlines()
rows = [line.split(",") for line in lines[1:] if line != ""]

maths = [int(row[3]) for row in rows if row[2] == "Mathematics"]
print(len(maths), "maths grades, average", round(sum(maths) / len(maths), 2))

#%% day04 code
# Extra 8 - one class's names, then without repeats
names_11b = [row[1] for row in rows if row[0] == "11B"]
print(len(names_11b))

unique = sorted(set(names_11b))
print(len(unique))

#%% day05 md
# Օր 5 — Լուծումներ

#%% day05 code
register = {
    "Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3, "Mariam": 8, "Tigran": 7,
    "Lilit": 5, "Gor": 4, "Anahit": 9, "Hayk": 2, "Sona": 8, "Vahe": 6,
}
PASS_MARK = 4

# Required 1 and 2 - choosing, not filtering
marks = ["+" if register[name] >= PASS_MARK else "-" for name in register]
adjusted = [register[name] if register[name] >= 5 else 0 for name in register]

print(marks)
print(adjusted)

#%% day05 code
# Required 3 - a helper function keeps the comprehension readable
def word_for(grade):
    if grade >= 9:
        return "excellent"
    if grade >= 7:
        return "good"
    return "ok"


words = {name: word_for(register[name]) for name in register}
print(words)

#%% day05 code
# Required 4 - sorting by a rule of your own
by_length = sorted(register, key=lambda name: len(name))
print(by_length)

#%% day05 code
# Extra 5 and 6 - the top five, and the dictionary turned inside out
top_five = sorted(register, key=lambda name: register[name], reverse=True)[:5]
for name in top_five:
    print(f"{name}: {register[name]}")

print()

by_grade = {}
for name in register:
    grade = register[name]
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(name)

for grade in sorted(by_grade):
    print(grade, by_grade[grade])

#%% day06 md
# Օր 6 — Լուծումներ

#%% day06 code
SUBJECT_NAMES = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]
PASS_MARK = 4


class Student:
    def __init__(self, name, class_name, grades, attendance, note=""):
        self.name = name
        self.class_name = class_name
        self.grades = grades
        self.attendance = attendance
        self.note = note


# Required 1 and 2 - a second class, with a default
class Teacher:
    def __init__(self, name, subject, years, school="School N 5"):
        self.name = name
        self.subject = subject
        self.years = years
        self.school = school


tigran = Teacher("Tigran Mkrtchyan", "Mathematics", 12)
lilit = Teacher("Lilit Khachatryan", "Physics", 4, "School N 12")

print(tigran.name, tigran.subject, tigran.years, tigran.school)
print(lilit.name, lilit.school)

#%% day06 code
# Required 3 - many objects from one loop
raw = [
    ["Lilit Khachatryan", "11C", [9, 8, 9, 10, 9], 96],
    ["Gor Vardanyan", "11C", [4, 5, 4, 6, 5], 81],
    ["Anahit Avetisyan", "11A", [7, 5, 8, 7, 8], 90],
]

group = []
for row in raw:
    group.append(Student(row[0], row[1], row[2], row[3]))

for student in group:
    print(student.name, student.class_name)

#%% day06 code
# Required 4 - the names of the failed subjects, not their positions
def failed_subjects(student, pass_mark=4):
    return [SUBJECT_NAMES[i] for i in range(len(student.grades))
            if student.grades[i] < pass_mark]


aram = Student("Aram Harutyunyan", "11B", [3, 2, 4, 3, 5], 65)
print(failed_subjects(aram))

#%% day06 code
# Extra 8 - thirty-six objects out of the file
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

collected = {}
for row in rows:
    if row[1] not in collected:
        collected[row[1]] = [row[0], []]
    collected[row[1]][1].append(int(row[3]))

school = [Student(name, collected[name][0], collected[name][1], 90)
          for name in collected]

print(len(school), "students")
print(school[0].name, school[0].grades)

#%% day07 md
# Օր 7 — Լուծումներ

#%% day07 code
SUBJECT_NAMES = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]
PASS_MARK = 4


# Required 1 to 4 - four methods and a __str__
class Student:
    def __init__(self, name, class_name, grades, attendance, note=""):
        self.name = name
        self.class_name = class_name
        self.grades = grades
        self.attendance = attendance
        self.note = note

    def average(self):
        return sum(self.grades) / len(self.grades)

    def attends_enough(self):
        return self.attendance > 85

    def best_subject(self):
        return SUBJECT_NAMES[self.grades.index(max(self.grades))]

    def worst_subject(self):
        return SUBJECT_NAMES[self.grades.index(min(self.grades))]

    def add_grade(self, subject_index, grade):
        self.grades[subject_index] = grade

    def __str__(self):
        return (f"{self.name} · {self.class_name} · "
                f"{self.average():.1f} · {self.attendance}%")


ani = Student("Ani Hakobyan", "11A", [7, 6, 8, 9, 8], 94)
davit = Student("Davit Grigoryan", "11A", [5, 3, 6, 5, 7], 78)

print(ani.attends_enough(), davit.attends_enough())
print(ani.best_subject(), ani.worst_subject())
print(ani)

print(round(ani.average(), 2))
ani.add_grade(1, 10)
print(round(ani.average(), 2))

#%% day07 code
# Extra 6 and 7 - comparing two students, and a sorted group report
class Student(Student):
    def better_than(self, other):
        return self.average() > other.average()


def print_group(students):
    for student in sorted(students, key=lambda s: s.average(), reverse=True):
        print(student)


ani = Student("Ani Hakobyan", "11A", [7, 6, 8, 9, 8], 94)
davit = Student("Davit Grigoryan", "11A", [5, 3, 6, 5, 7], 78)

print(ani.better_than(davit))
print_group([davit, ani])

#%% day08 md
# Օր 8 — Լուծումներ

#%% day08 code
PASS_MARK = 4


class Student:
    def __init__(self, name, class_name, grades, attendance=90):
        self.name = name
        self.class_name = class_name
        self.grades = grades
        self.attendance = attendance

    def average(self):
        return sum(self.grades) / len(self.grades)

    def has_passed(self):
        return min(self.grades) >= PASS_MARK

    def __str__(self):
        return f"{self.name} ({self.class_name}), average {self.average():.1f}"


# Required 1 to 4 - four more methods on the class
class SchoolClass:
    def __init__(self, name, students=None):
        self.name = name
        if students is None:
            students = []
        self.students = students

    def size(self):
        return len(self.students)

    def average(self):
        return sum(s.average() for s in self.students) / self.size()

    def attendance(self):
        return sum(s.attendance for s in self.students) / self.size()

    def best(self):
        return sorted(self.students, key=lambda s: s.average(), reverse=True)[0]

    def worst(self):
        return sorted(self.students, key=lambda s: s.average())[0]

    def find(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def report(self):
        print(f"--- {self.name} ---")
        for student in sorted(self.students, key=lambda s: s.average(),
                              reverse=True):
            print(" ", student)
        print(f"class average: {self.average():.2f}")


eleven_a = SchoolClass("11A", [
    Student("Ani Hakobyan", "11A", [7, 6, 8, 9, 8], 94),
    Student("Davit Grigoryan", "11A", [5, 3, 6, 5, 7], 78),
    Student("Nare Petrosyan", "11A", [10, 9, 10, 9, 10], 99),
])

print(round(eleven_a.attendance(), 1))
print(eleven_a.best().name, eleven_a.worst().name)
print(eleven_a.find("Nare Petrosyan"))
print(eleven_a.find("Someone Else"))
eleven_a.report()

#%% day09 md
# Օր 9 — Լուծումներ

#%% day09 code
class Person:
    def __init__(self, name, class_name, phone):
        self.name = name
        self.class_name = class_name
        self.phone = phone

    def surname(self):
        return self.name.split(" ")[1].upper()

    def short_name(self):
        return self.name.split(" ")[0]

    def contact_line(self):
        return f"{self.name} {self.class_name} — {self.phone}"


class Student(Person):
    def __init__(self, name, class_name, phone, grades):
        super().__init__(name, class_name, phone)
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


class Teacher(Person):
    def __init__(self, name, class_name, phone, subject, salary=250000):
        super().__init__(name, class_name, phone)
        self.subject = subject
        self.salary = salary

    def is_experienced(self):
        return self.salary > 300000

    def raise_salary(self, percent):
        self.salary = self.salary + self.salary * percent / 100


# Required 1 - the third class, inheriting rather than copying
class Parent(Person):
    def __init__(self, name, class_name, phone, child_name):
        super().__init__(name, class_name, phone)
        self.child_name = child_name


mother = Parent("Lilit Hakobyan", "11A", "055-77-88-99", "Ani Hakobyan")
print(mother.contact_line())
print(mother.surname(), mother.short_name())

#%% day09 code
# Required 3 - a third level, inheriting from Teacher rather than Person
class HeadTeacher(Teacher):
    def __init__(self, name, class_name, phone, subject, salary, since_year):
        super().__init__(name, class_name, phone, subject, salary)
        self.since_year = since_year


head = HeadTeacher("Sona Martirosyan", "11B", "091-00-00-00",
                   "Physics", 420000, 2019)

print(head.contact_line())
print(head.is_experienced(), head.since_year)

#%% day09 code
# Required 4 - everyone is a Person, whatever else they are
ani = Student("Ani Hakobyan", "11A", "077-11-22-33", [7, 6, 8, 9, 8])
tigran = Teacher("Tigran Mkrtchyan", "11A", "091-44-55-66", "Mathematics", 350000)

for person in [ani, tigran, mother, head]:
    print(f"{person.name:<22} Person? {isinstance(person, Person)}")

#%% day10 md
# Օր 10 — Լուծումներ

#%% day10 code
class Person:
    def __init__(self, name, class_name, phone):
        self.name = name
        self.class_name = class_name
        self.phone = phone

    def label(self):
        return f"{self.name} ({self.class_name})"

    def summary(self):
        return "person"

    def can_vote(self):
        return True

    # Required 1 - __str__ inherited by everyone, defined once
    def __str__(self):
        return self.label()


class Student(Person):
    def __init__(self, name, class_name, phone, grades):
        super().__init__(name, class_name, phone)
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def label(self):
        return super().label() + f" — average {self.average():.1f}"

    def summary(self):
        return "student"

    def can_vote(self):
        return False


class Teacher(Person):
    def __init__(self, name, class_name, phone, subject):
        super().__init__(name, class_name, phone)
        self.subject = subject

    def label(self):
        return super().label() + f" — {self.subject}"

    def summary(self):
        return "teacher"


# Required 2 - a third level that overrides its parent's override
class HeadTeacher(Teacher):
    def label(self):
        return Person.label(self) + " — head teacher"


everyone = [
    Student("Ani Hakobyan", "11A", "077-11-22-33", [7, 6, 8, 9, 8]),
    Teacher("Tigran Mkrtchyan", "11A", "091-44-55-66", "Mathematics"),
    HeadTeacher("Sona Martirosyan", "11B", "091-00-00-00", "Physics"),
]

for person in everyone:
    print(person)

#%% day10 code
# Required 3 - a directory with no `if` anywhere in it
def directory(people):
    for person in sorted(people, key=lambda p: p.name):
        print(person.label())


directory(everyone)

#%% day10 code
# Extra 5 - counting each kind without isinstance
counts = {}
for person in everyone:
    kind = person.summary()
    if kind not in counts:
        counts[kind] = 0
    counts[kind] = counts[kind] + 1

print(counts)
print([p.can_vote() for p in everyone])

#%% day11 md
# Օր 11 — Լուծումներ

#%% day11 code
PASS_MARK = 4
SUBJECT_NAMES = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]


class Person:
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name

    def label(self):
        return f"{self.name:<22} {self.class_name}"

    def __str__(self):
        return self.label()


class Student(Person):
    def __init__(self, name, class_name, grades):
        super().__init__(name, class_name)
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def has_passed(self):
        return min(self.grades) >= PASS_MARK

    def label(self):
        status = "passed" if self.has_passed() else "failed"
        return super().label() + f"  {self.average():>5.2f}  {status}"


# Required 1 - a teacher who is not counted in the class average
class Teacher(Person):
    def __init__(self, name, class_name, subject):
        super().__init__(name, class_name)
        self.subject = subject

    def label(self):
        return super().label() + f"  {self.subject}"


class SchoolClass:
    def __init__(self, name, students=None, teacher=None):
        self.name = name
        if students is None:
            students = []
        self.students = students
        self.teacher = teacher

    def average(self):
        return sum(s.average() for s in self.students) / len(self.students)

    def at_risk(self):
        return [s for s in self.students if not s.has_passed()]


# Required 2 and 3 - the school, and everyone at risk in it
class School:
    def __init__(self, name, classes=None):
        self.name = name
        if classes is None:
            classes = []
        self.classes = classes

    def students(self):
        everyone = []
        for school_class in self.classes:
            everyone = everyone + school_class.students
        return everyone

    def average(self):
        people = self.students()
        return sum(s.average() for s in people) / len(people)

    def at_risk(self):
        return [s for s in self.students() if not s.has_passed()]

    def report(self):
        print(f"=== {self.name} ===")
        for school_class in self.classes:
            print(f"{school_class.name}  {school_class.average():.2f}")
        print(f"school average: {self.average():.2f}")

#%% day11 code
# Required 4 - the whole school out of the file, with the three numbers checked
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

collected = {}
for row in rows:
    if row[1] not in collected:
        collected[row[1]] = [row[0], []]
    collected[row[1]][1].append(int(row[3]))

by_class = {}
for name in collected:
    class_name = collected[name][0]
    if class_name not in by_class:
        by_class[class_name] = SchoolClass(class_name)
    by_class[class_name].students.append(
        Student(name, class_name, collected[name][1]))

school = School("School N 5", [by_class[n] for n in sorted(by_class)])

school.report()
print()
print("students:", len(school.students()))
print("average: ", round(school.average(), 2))
print("at risk: ", len(school.at_risk()))

#%% day12 md
# Օր 12 — Լուծումներ

#%% day12 code
import numpy as np
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

grades = np.array([int(row[3]) for row in rows])
SUBJECTS = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]

# Required 1 - one class, four numbers
eleven_a = np.array([int(r[3]) for r in rows if r[0] == "11A"])
print(f"average {eleven_a.mean():.2f} · highest {eleven_a.max()} · "
      f"lowest {eleven_a.min()} · spread {eleven_a.std():.3f}")

#%% day12 code
# Required 2 and 3 - a True/False array counts, and selects
below = grades < 4

print("failing grades:", below.sum())
print("their average: ", round(grades[below].mean(), 2))
print("passing average:", round(grades[grades >= 4].mean(), 2))

#%% day12 code
# Required 4 - the same four numbers, per subject
def subject_numbers(subject):
    marks = np.array([int(r[3]) for r in rows if r[2] == subject])
    return marks.mean(), marks.max(), marks.min(), marks.std()


print(f"{'subject':<14} {'avg':>6} {'high':>5} {'low':>4} {'spread':>7}")
for subject in SUBJECTS:
    average, highest, lowest, spread = subject_numbers(subject)
    print(f"{subject:<14} {average:>6.2f} {highest:>5} {lowest:>4} {spread:>7.3f}")

#%% day12 code
# Extra 5 and 7 - the median, and where the highest mark sits
print("mean:  ", round(grades.mean(), 2))
print("median:", np.median(grades))
# They differ because the distribution is not symmetric: a few very low marks
# pull the mean down further than they move the middle value.

position = grades.argmax()
print("highest mark:", grades[position], "-", rows[position][1],
      "in", rows[position][2])

#%% day13 md
# Օր 13 — Լուծումներ

#%% day13 code
import numpy as np
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

grades = np.array([int(row[3]) for row in rows])

# Required 1 and 2 - a whole array at once, and counting with a mask
percent = grades * 10
print(percent[:10], "average", percent.mean())

print("excellent:", (grades >= 9).sum())

#%% day13 code
# Required 3 and 4 - selecting with one condition, then two
passing = grades[grades >= 4]
print(len(passing), "passing, average", round(passing.mean(), 2))
print("whole school average:", round(grades.mean(), 2))

maths = np.array([int(r[3]) for r in rows if r[2] == "Mathematics"])
middle = maths[(maths > 4) & (maths < 8)]
print(len(middle), "maths grades between 5 and 7")

#%% day13 code
# Extra 5 to 7 - the school as a 36 x 5 table
SUBJECTS = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]

collected = {}
for row in rows:
    if row[1] not in collected:
        collected[row[1]] = {}
    collected[row[1]][row[2]] = int(row[3])

names = sorted(collected)
table = np.array([[collected[name][s] for s in SUBJECTS] for name in names])

print("shape:", table.shape)
print("per student:", np.round(table.mean(axis=1), 2)[:5])
print("per subject:", np.round(table.mean(axis=0), 2))

#%% day14 md
# Օր 14 — Լուծումներ

#%% day14 code
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

SUBJECTS = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]
CLASSES = ["11A", "11B", "11C"]

averages = [np.array([int(r[3]) for r in rows if r[2] == s]).mean()
            for s in SUBJECTS]
class_averages = [np.array([int(r[3]) for r in rows if r[0] == c]).mean()
                  for c in CLASSES]

# Required 1 and 3 - a chart for the classes, saved
plt.figure(figsize=(7, 4))
plt.bar(CLASSES, class_averages, color="#47a")
plt.ylim(0, 10)
plt.ylabel("Average grade")
plt.title("Class averages, term 1")
plt.tight_layout()
plt.savefig("classes.png", dpi=150)
plt.close()

print("saved classes.png")

#%% day14 code
# Required 2 and 4 - horizontal bars, coloured by the result
colours = []
for value in averages:
    if value > 7:
        colours.append("#4a7")
    else:
        colours.append("#f71")

plt.figure(figsize=(8, 4))
plt.barh(SUBJECTS, averages, color=colours)
plt.xlim(0, 10)
plt.xlabel("Average grade")
plt.title("Subject averages, term 1")
plt.tight_layout()
plt.savefig("subjects.png", dpi=150)
plt.close()

print("saved subjects.png")

#%% day14 code
# Extra 5, 6 and 8 - a reference line, the numbers on the bars, and the failures
school_average = np.array([int(r[3]) for r in rows]).mean()
failing = [len([r for r in rows if r[2] == s and int(r[3]) < 4]) for s in SUBJECTS]

print("failing per subject:", failing, "total", sum(failing))

plt.figure(figsize=(8, 4))
plt.bar(SUBJECTS, averages, color="#4a7")
plt.axhline(y=school_average, color="red", linestyle="--", label="school average")
for position in range(len(SUBJECTS)):
    plt.text(position, averages[position] + 0.2, f"{averages[position]:.2f}",
             ha="center")
plt.ylim(0, 10)
plt.xticks(rotation=20)
plt.legend()
plt.tight_layout()
plt.savefig("subjects_labelled.png", dpi=150)
plt.close()

print("saved subjects_labelled.png")

#%% day15 md
# Օր 15 — Լուծումներ

#%% day15 code
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

SUBJECTS = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]
CLASSES = ["11A", "11B", "11C"]

# Required 1 - one histogram per class
for class_name in CLASSES:
    marks = np.array([int(r[3]) for r in rows if r[0] == class_name])
    plt.figure(figsize=(7, 4))
    plt.hist(marks, bins=range(1, 12), edgecolor="white", color="#47a")
    plt.xlabel("Grade")
    plt.ylabel("How many")
    plt.title(f"{class_name} — average {marks.mean():.2f}")
    plt.tight_layout()
    plt.savefig(f"dist_{class_name}.png", dpi=150)
    plt.close()

print("three histograms saved")

#%% day15 code
# Required 2 - bars, not a line: the subjects have no natural order
failing = [len([r for r in rows if r[2] == s and int(r[3]) < 4]) for s in SUBJECTS]

plt.figure(figsize=(8, 4))
plt.bar(SUBJECTS, failing, color="#c74")
plt.ylabel("Failing grades")
plt.title("Failing grades by subject")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("failing.png", dpi=150)
plt.close()

print("failing per subject:", failing, "total", sum(failing))

#%% day15 code
# Required 4 - the four charts in one picture
grades = np.array([int(r[3]) for r in rows])
averages = [np.array([int(r[3]) for r in rows if r[2] == s]).mean()
            for s in SUBJECTS]
class_averages = [np.array([int(r[3]) for r in rows if r[0] == c]).mean()
                  for c in CLASSES]
levels = list(range(1, 11))
counts = [int((grades == level).sum()) for level in levels]

plt.figure(figsize=(11, 7))

plt.subplot(2, 2, 1)
plt.bar(SUBJECTS, averages, color="#4a7")
plt.ylim(0, 10)
plt.xticks(rotation=25, fontsize=7)
plt.title("Subjects")

plt.subplot(2, 2, 2)
plt.bar(CLASSES, class_averages, color="#47a")
plt.ylim(0, 10)
plt.title("Classes")

plt.subplot(2, 2, 3)
plt.hist(grades, bins=range(1, 12), edgecolor="white", color="#a74")
plt.title("Distribution")

plt.subplot(2, 2, 4)
plt.plot(levels, counts, marker="o")
plt.grid(True, alpha=0.3)
plt.title("How many of each grade")

plt.tight_layout()
plt.savefig("term_report.png", dpi=150)
plt.close()

print("saved term_report.png")

#%% day16 md
# Օր 16 — Լուծումներ

#%% day16 code
import pandas as pd

data = pd.read_csv("school.csv")

# Required 1 - the first questions you ask any new file
print("rows and columns:", data.shape)
print("columns:", data.columns.tolist())
print("average:", round(data["grade"].mean(), 2))
print()
print(data.head(3).to_string())

#%% day16 code
# Required 2 and 3 - class averages, and who is failing
for class_name in ["11A", "11B", "11C"]:
    rows = data[data["class"] == class_name]
    print(class_name, round(rows["grade"].mean(), 2))

print()
failing = data[data["grade"] < 4]
print(len(failing), "failing grades")
print(failing["student"].nunique(), "students behind them")

#%% day16 code
# Required 4 - one student's five rows
one = data[data["student"] == "Ani Hakobyan"]
print(one.to_string())
print("average:", round(one["grade"].mean(), 2))

#%% day16 code
# Extra 5 to 8 - a new column, sorting, unique values, and the non-empty notes
data["passed"] = data["grade"] >= 4
print("passing marks:", int(data["passed"].sum()))

print()
print(data.sort_values("grade").head(10)[["student", "subject", "grade"]].to_string())

print()
for subject in data["subject"].unique():
    rows = data[data["subject"] == subject]
    print(f"{subject:<14} {rows['grade'].mean():.2f}")

print()
print(data[data["note"].notna()][["student", "note"]].to_string())

#%% day17 md
# Օր 17 — Լուծումներ

#%% day17 code
import pandas as pd

data = pd.read_csv("school.csv")

# Required 1 - three groupings, no loop and no list of names
print(data.groupby("class")["grade"].mean().round(2))
print()
print(data.groupby("subject")["grade"].mean().round(2).sort_values())
print()
print(data.groupby("student")["grade"].mean().round(2).head(10))

#%% day17 code
# Required 2 - filter first, then group
failing = data[data["grade"] < 4]
counts = failing.groupby("class")["grade"].size()

print(counts)
print("total:", counts.sum())

#%% day17 code
# Required 3 and 4 - several numbers at once, and the two-way table
per_student = data.groupby("student")["grade"].agg(["mean", "min", "max"]).round(2)
print(per_student.sort_values("mean", ascending=False).head().to_string())

print()
table = data.pivot_table(index="student", columns="subject", values="grade")
print("shape:", table.shape)

#%% day17 code
# Extra 6 and 7 - the pass rate per subject, and the most uneven subject
data["passed"] = data["grade"] >= 4
print((data.groupby("subject")["passed"].mean() * 100).round(1))

print()
spread = data.groupby("subject")["grade"].std().round(3)
print(spread.sort_values(ascending=False))
print("most uneven:", spread.idxmax())

#%% day18 md
# Օր 18 — Լուծումներ

#%% day18 code
import pandas as pd
import matplotlib.pyplot as plt

PASS_MARK = 4
data = pd.read_csv("school.csv")


# Required 1 - the six questions, as a function
def inspect(data):
    print("rows and columns:", data.shape)
    print("columns:", data.columns.tolist())
    print("classes:", sorted(data["class"].unique()))
    print("subjects:", sorted(data["subject"].unique()))
    print("students:", data["student"].nunique())
    print("missing values:")
    print(data.isna().sum().to_string())


inspect(data)

#%% day18 code
# Required 2 - one class, as a dictionary
def class_summary(data, class_name):
    rows = data[data["class"] == class_name]
    return {
        "students": rows["student"].nunique(),
        "average": round(rows["grade"].mean(), 2),
        "spread": round(rows["grade"].std(), 3),
        "failing": int((rows["grade"] < PASS_MARK).sum()),
    }


for class_name in ["11A", "11B", "11C"]:
    print(class_name, class_summary(data, class_name))

#%% day18 code
# Required 3 and 4 - the whole report behind one call
def save_distribution_chart(data, filename, title):
    plt.figure(figsize=(7, 4))
    plt.hist(data["grade"], bins=range(1, 12), edgecolor="white", color="#47a")
    plt.xlabel("Grade")
    plt.ylabel("How many")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()


def build_report(path):
    data = pd.read_csv(path)

    for class_name in sorted(data["class"].unique()):
        rows = data[data["class"] == class_name]
        save_distribution_chart(rows, f"dist_{class_name}.png",
                                f"{class_name} — average {rows['grade'].mean():.2f}")

    lines = ["TERM REPORT", "=" * 40]
    lines.append(f"Students:         {data['student'].nunique()}")
    lines.append(f"School average:   {data['grade'].mean():.2f}")
    lines.append(f"Failing grades:   {int((data['grade'] < PASS_MARK).sum())}")
    lines.append("")
    lines.append("Subject averages")
    averages = data.groupby("subject")["grade"].mean().sort_values()
    for subject in averages.index:
        lines.append(f"  {subject:<16} {averages[subject]:.2f}")

    text = "\n".join(lines)
    print(text)
    return text


build_report("school.csv")

#%% day19 md
# Օր 19 — Լուծումներ

#%% day19 code
school = {
    "name": "School N 5",
    "parts": [
        {
            "name": "Science stream",
            "parts": [
                {
                    "name": "11A",
                    "parts": [
                        {"name": "group 1", "students": ["Ani", "Davit"]},
                        {"name": "group 2", "students": ["Nare"]},
                    ],
                },
                {"name": "11B", "students": ["Aram", "Mariam"]},
            ],
        },
        {
            "name": "Humanities stream",
            "parts": [
                {"name": "11C", "students": ["Tigran", "Lilit", "Gor"]},
            ],
        },
    ],
}


# Required 1 and 2 - how deep, and how many parts
def depth(part):
    if "students" in part:
        return 1
    return 1 + max(depth(smaller) for smaller in part["parts"])


def count_parts(part):
    if "students" in part:
        return 1
    total = 1
    for smaller in part["parts"]:
        total = total + count_parts(smaller)
    return total


print("depth:", depth(school))
print("parts:", count_parts(school))

#%% day19 code
# Required 3 and 4 - finding one student, and the biggest group
def find(part, name):
    if "students" in part:
        if name in part["students"]:
            return part["name"]
        return None
    for smaller in part["parts"]:
        found = find(smaller, name)
        if found is not None:
            return found
    return None


def biggest(part):
    if "students" in part:
        return part["name"], len(part["students"])
    best_name = None
    best_size = -1
    for smaller in part["parts"]:
        name, size = biggest(smaller)
        if size > best_size:
            best_name = name
            best_size = size
    return best_name, best_size


print(find(school, "Nare"), "|", find(school, "Someone"))
print(biggest(school))

#%% day19 code
# Extra 5 and 6 - the whole path, and flattening a nested list
def path_to(part, name):
    if "students" in part:
        if name in part["students"]:
            return [part["name"]]
        return None
    for smaller in part["parts"]:
        found = path_to(smaller, name)
        if found is not None:
            return [part["name"]] + found
    return None


def flatten(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result = result + flatten(item)
        else:
            result.append(item)
    return result


print(path_to(school, "Davit"))
print(flatten([1, [2, 3, [4, [5, 6]], 7], [8], 9]))

#%% day19 code
# Challenge 9 - the same answer with a queue instead of recursion
def count_with_queue(school):
    queue = [school]
    total = 0
    while queue:
        part = queue.pop()
        if "students" in part:
            total = total + len(part["students"])
        else:
            queue = queue + part["parts"]
    return total


print(count_with_queue(school))

#%% day20 md
# Օր 20 — Լուծումներ

#%% day20 code
import importlib.metadata as metadata
from pathlib import Path

# Required 1 and 2 - what is installed, and where it lives
import numpy
import pandas
import matplotlib

for module in [numpy, pandas, matplotlib]:
    name = module.__name__
    print(f"{name:<12} {metadata.version(name):<10} {Path(module.__file__).parent}")

#%% day20 code
# Required 3 - the file a colleague needs
requirements = "\n".join(
    f"{name}=={metadata.version(name)}"
    for name in ["numpy", "pandas", "matplotlib"]
) + "\n"

Path("requirements.txt").write_text(requirements, encoding="utf-8")
print(requirements)

#%% day20 code
# Required 4 - four imports, one function
import numpy
print(numpy.mean([1, 2, 3]))

import numpy as np
print(np.mean([1, 2, 3]))

from numpy import mean
print(mean([1, 2, 3]))

from numpy import mean as average
print(average([1, 2, 3]))

#%% day20 code
# Extra 5 - standard library, or installed?
import sys

names = ["json", "numpy", "math", "pandas", "csv", "matplotlib", "datetime"]
for name in names:
    kind = "standard" if name in sys.stdlib_module_names else "installed"
    print(f"{name:<12} {kind}")

#%% day21 md
# Օր 21 — Լուծումներ

#%% day21 code
import pandas as pd

data = pd.read_csv("school.csv")


# Required 2 - the bug is the starting value, not the loop
def highest(grades):
    best = grades[0]
    for grade in grades:
        if grade > best:
            best = grade
    return best


print(highest([7, 6, 8]))
print(highest([-3, -6, -1]))

#%% day21 code
# Required 3 and 4 - a fraction is not a percentage
def pass_rate(data):
    assert len(data) > 0, "no rows"
    passed = data[data["grade"] >= 4]
    rate = len(passed) / len(data) * 100
    assert 0 <= rate <= 100, f"impossible pass rate: {rate}"
    return rate


print(pass_rate(data))

#%% day21 code
# Extra 6 - three bugs: `=` instead of `==`, a result thrown away, the wrong divisor
def fixed_average(data, class_name):
    rows = data[data["class"] == class_name]
    total = 0
    for grade in rows["grade"]:
        total = total + grade
    return total / len(rows)


print(round(fixed_average(data, "11A"), 2))

#%% day21 code
# Extra 8 - the hard-coded list is the bug waiting to happen
def report(data):
    found = sorted(data["class"].unique())
    assert len(found) > 0, "no classes in the file"
    for class_name in found:
        rows = data[data["class"] == class_name]
        print(class_name, round(rows["grade"].mean(), 2))


report(data)

#%% day21 code
# Challenge 10 - the checks a real program runs every time it reads data
def check_data(data, expected_rows=180, subjects=5, classes=3):
    problems = []
    if len(data) != expected_rows:
        problems.append(f"{len(data)} rows, expected {expected_rows}")
    outside = (data["grade"] < 1) | (data["grade"] > 10)
    if outside.sum() > 0:
        problems.append(f"{outside.sum()} grade(s) outside 1-10")
    per_student = data.groupby("student")["grade"].size()
    wrong = per_student[per_student != subjects]
    if len(wrong) > 0:
        problems.append(f"{len(wrong)} student(s) without {subjects} grades")
    if data["class"].nunique() != classes:
        problems.append(f"{data['class'].nunique()} classes, expected {classes}")
    return problems


print(check_data(data) or "all checks passed")

broken = data.copy()
broken.loc[0, "grade"] = 99
print(check_data(broken))
