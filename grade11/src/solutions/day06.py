#%% md
# Թեմա 6 — Լուծումներ

#%% code
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

#%% code
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

#%% code
# Required 4 - the names of the failed subjects, not their positions
def failed_subjects(student, pass_mark=4):
    return [SUBJECT_NAMES[i] for i in range(len(student.grades))
            if student.grades[i] < pass_mark]


aram = Student("Aram Harutyunyan", "11B", [3, 2, 4, 3, 5], 65)
print(failed_subjects(aram))

#%% code
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
