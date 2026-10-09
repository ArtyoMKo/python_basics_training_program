#%% md
# Օր 12 — Լուծումներ

#%% code
import numpy as np
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

grades = np.array([int(row[3]) for row in rows])
SUBJECTS = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]

# Required 1 - one class, four numbers
eleven_a = np.array([int(r[3]) for r in rows if r[0] == "11A"])
print(f"average {eleven_a.mean():.2f} · highest {eleven_a.max()} · "
      f"lowest {eleven_a.min()} · spread {eleven_a.std():.3f}")

#%% code
# Required 2 and 3 - a True/False array counts, and selects
below = grades < 4

print("failing grades:", below.sum())
print("their average: ", round(grades[below].mean(), 2))
print("passing average:", round(grades[grades >= 4].mean(), 2))

#%% code
# Required 4 - the same four numbers, per subject
def subject_numbers(subject):
    marks = np.array([int(r[3]) for r in rows if r[2] == subject])
    return marks.mean(), marks.max(), marks.min(), marks.std()


print(f"{'subject':<14} {'avg':>6} {'high':>5} {'low':>4} {'spread':>7}")
for subject in SUBJECTS:
    average, highest, lowest, spread = subject_numbers(subject)
    print(f"{subject:<14} {average:>6.2f} {highest:>5} {lowest:>4} {spread:>7.3f}")

#%% code
# Extra 5 and 7 - the median, and where the highest mark sits
print("mean:  ", round(grades.mean(), 2))
print("median:", np.median(grades))
# They differ because the distribution is not symmetric: a few very low marks
# pull the mean down further than they move the middle value.

position = grades.argmax()
print("highest mark:", grades[position], "-", rows[position][1],
      "in", rows[position][2])
