#%% md
# Թեմա 11 — Լուծումներ

#%% code
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

#%% code
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
