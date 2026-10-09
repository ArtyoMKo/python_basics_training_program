#%% md
# Թեմա 8 — Լուծումներ

#%% code
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
