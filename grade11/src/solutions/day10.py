#%% md
# Թեմա 10 — Լուծումներ

#%% code
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

#%% code
# Required 3 - a directory with no `if` anywhere in it
def directory(people):
    for person in sorted(people, key=lambda p: p.name):
        print(person.label())


directory(everyone)

#%% code
# Extra 5 - counting each kind without isinstance
counts = {}
for person in everyone:
    kind = person.summary()
    if kind not in counts:
        counts[kind] = 0
    counts[kind] = counts[kind] + 1

print(counts)
print([p.can_vote() for p in everyone])
