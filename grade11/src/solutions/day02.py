#%% md
# Թեմա 2 — Լուծումներ

#%% code
# Required 1 - a default for the rounding
def class_average(grades, digits=1):
    return round(sum(grades) / len(grades), digits)


print(class_average([9, 6, 10, 3, 8]))
print(class_average([9, 6, 10, 3, 8], 2))

#%% code
# Required 2 - a default for the school name
def report_header(class_name, school="School N 5"):
    print(school)
    print("Class:", class_name)


report_header("11A")
report_header("11B", "School N 12")

#%% code
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

#%% code
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

#%% code
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
