#%% md
# Թեմա 7 — Լուծումներ

#%% code
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

#%% code
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
