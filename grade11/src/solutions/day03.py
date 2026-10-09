#%% md
# Օր 3 — Լուծումներ

#%% code
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

#%% code
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

#%% code
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

#%% code
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

#%% code
# Extra 6 - swapping without a third variable
first = "Ani"
second = "Davit"

first, second = second, first

print(first, second)
