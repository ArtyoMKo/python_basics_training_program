#%% md
# Օր 13 — Լուծումներ

#%% code
import numpy as np
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

grades = np.array([int(row[3]) for row in rows])

# Required 1 and 2 - a whole array at once, and counting with a mask
percent = grades * 10
print(percent[:10], "average", percent.mean())

print("excellent:", (grades >= 9).sum())

#%% code
# Required 3 and 4 - selecting with one condition, then two
passing = grades[grades >= 4]
print(len(passing), "passing, average", round(passing.mean(), 2))
print("whole school average:", round(grades.mean(), 2))

maths = np.array([int(r[3]) for r in rows if r[2] == "Mathematics"])
middle = maths[(maths > 4) & (maths < 8)]
print(len(middle), "maths grades between 5 and 7")

#%% code
# Extra 5 to 7 - the school as a 36 x 5 table
SUBJECTS = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]

collected = {}
for row in rows:
    if row[1] not in collected:
        collected[row[1]] = {}
    collected[row[1]][row[2]] = int(row[3])

names = sorted(collected)
table = np.array([[collected[name][s] for s in SUBJECTS] for name in names])

print("shape:", table.shape)
print("per student:", np.round(table.mean(axis=1), 2)[:5])
print("per subject:", np.round(table.mean(axis=0), 2))
