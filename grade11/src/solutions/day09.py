#%% md
# Օր 9 — Լուծումներ

#%% code
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

#%% code
# Required 3 - a third level, inheriting from Teacher rather than Person
class HeadTeacher(Teacher):
    def __init__(self, name, class_name, phone, subject, salary, since_year):
        super().__init__(name, class_name, phone, subject, salary)
        self.since_year = since_year


head = HeadTeacher("Sona Martirosyan", "11B", "091-00-00-00",
                   "Physics", 420000, 2019)

print(head.contact_line())
print(head.is_experienced(), head.since_year)

#%% code
# Required 4 - everyone is a Person, whatever else they are
ani = Student("Ani Hakobyan", "11A", "077-11-22-33", [7, 6, 8, 9, 8])
tigran = Teacher("Tigran Mkrtchyan", "11A", "091-44-55-66", "Mathematics", 350000)

for person in [ani, tigran, mother, head]:
    print(f"{person.name:<22} Person? {isinstance(person, Person)}")
