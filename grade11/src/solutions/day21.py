#%% md
# Թեմա 21 — Լուծումներ

#%% code
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

#%% code
# Required 3 and 4 - a fraction is not a percentage
def pass_rate(data):
    assert len(data) > 0, "no rows"
    passed = data[data["grade"] >= 4]
    rate = len(passed) / len(data) * 100
    assert 0 <= rate <= 100, f"impossible pass rate: {rate}"
    return rate


print(pass_rate(data))

#%% code
# Extra 6 - three bugs: `=` instead of `==`, a result thrown away, the wrong divisor
def fixed_average(data, class_name):
    rows = data[data["class"] == class_name]
    total = 0
    for grade in rows["grade"]:
        total = total + grade
    return total / len(rows)


print(round(fixed_average(data, "11A"), 2))

#%% code
# Extra 8 - the hard-coded list is the bug waiting to happen
def report(data):
    found = sorted(data["class"].unique())
    assert len(found) > 0, "no classes in the file"
    for class_name in found:
        rows = data[data["class"] == class_name]
        print(class_name, round(rows["grade"].mean(), 2))


report(data)

#%% code
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
