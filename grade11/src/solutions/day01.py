#%% md
# Օր 1 — Լուծումներ

Այս լուծումները **մեկ հնարավոր տարբերակն** են։ Եթե քոնը այլ է, բայց աշխատում է —
քոնը նույնպես ճիշտ է։

#%% code
from pathlib import Path

lines = Path("school.csv").read_text(encoding="utf-8").strip().splitlines()

# Required 1 - every distinct subject
subjects = []
for line in lines[1:]:
    if line == "":
        continue
    subject = line.split(",")[2]
    if subject not in subjects:
        subjects.append(subject)

print(subjects)

#%% code
# Required 2 - the students of one class, without repeats
names = []
for line in lines[1:]:
    if line == "":
        continue
    parts = line.split(",")
    if parts[0] == "11B" and parts[1] not in names:
        names.append(parts[1])

print(len(names), "students")
print(names)

#%% code
# Required 3 and 4 - failing grades, and one subject's average
PASS_MARK = 4
failing = 0
subject_total = 0
subject_count = 0

for line in lines[1:]:
    if line == "":
        continue
    parts = line.split(",")
    grade = int(parts[3])
    if grade < PASS_MARK:
        failing = failing + 1
    if parts[2] == "Mathematics":
        subject_total = subject_total + grade
        subject_count = subject_count + 1

print("failing grades:", failing)
print("Mathematics average:", subject_total / subject_count)

#%% code
# Extra 7 - the students with at least one failing grade
at_risk = []
for line in lines[1:]:
    if line == "":
        continue
    parts = line.split(",")
    if int(parts[3]) < PASS_MARK and parts[1] not in at_risk:
        at_risk.append(parts[1])

print(len(at_risk), "students at risk")
