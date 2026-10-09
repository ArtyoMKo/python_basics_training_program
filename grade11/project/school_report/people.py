"""The people in a school, and what each of them can tell you about themselves.

Person is the common part. Student and Teacher add what only they have.
SchoolClass and School hold the ones below them -- a class is not a person, so it
does not inherit from Person; it HAS people.
"""

import settings


class Person:
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name

    def surname(self):
        parts = self.name.split(" ")
        if len(parts) < 2:
            return self.name
        return parts[1]

    def label(self):
        return f"{self.name} ({self.class_name})"

    def __str__(self):
        return self.label()


class Student(Person):
    def __init__(self, name, class_name, grades):
        super().__init__(name, class_name)
        # grades maps a subject name to one mark
        self.grades = grades

    def marks(self):
        return [self.grades[subject] for subject in settings.SUBJECTS
                if subject in self.grades]

    def average(self):
        marks = self.marks()
        if not marks:
            return 0.0
        return sum(marks) / len(marks)

    def failed_subjects(self):
        return [subject for subject in settings.SUBJECTS
                if self.grades.get(subject, settings.HIGHEST_GRADE) < settings.PASS_MARK]

    def at_risk(self):
        return len(self.failed_subjects()) > 0

    def label(self):
        return f"{self.name:<22} {self.class_name}  {self.average():>5.2f}"


class Teacher(Person):
    def __init__(self, name, class_name, subject):
        super().__init__(name, class_name)
        self.subject = subject

    def label(self):
        return f"{self.name:<22} {self.class_name}  {self.subject}"


class SchoolClass:
    def __init__(self, name, students=None):
        self.name = name
        if students is None:
            students = []
        self.students = students

    def add(self, student):
        self.students.append(student)

    def size(self):
        return len(self.students)

    def average(self):
        if not self.students:
            return 0.0
        return sum(s.average() for s in self.students) / self.size()

    def at_risk(self):
        return [s for s in self.students if s.at_risk()]

    def best(self):
        return sorted(self.students, key=lambda s: s.average(), reverse=True)[0]


class School:
    def __init__(self, name, classes=None):
        self.name = name
        if classes is None:
            classes = []
        self.classes = classes

    def add(self, school_class):
        self.classes.append(school_class)

    def students(self):
        everyone = []
        for school_class in self.classes:
            everyone = everyone + school_class.students
        return everyone

    def size(self):
        return len(self.students())

    def average(self):
        people = self.students()
        if not people:
            return 0.0
        return sum(s.average() for s in people) / len(people)

    def at_risk(self):
        return [s for s in self.students() if s.at_risk()]

    def subject_averages(self):
        """Subject name -> the school's average in it."""
        averages = {}
        for subject in settings.SUBJECTS:
            marks = [s.grades[subject] for s in self.students() if subject in s.grades]
            if marks:
                averages[subject] = sum(marks) / len(marks)
        return averages
