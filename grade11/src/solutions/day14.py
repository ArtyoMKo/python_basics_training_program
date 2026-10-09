#%% md
# Թեմա 14 — Լուծումներ

#%% code
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

SUBJECTS = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]
CLASSES = ["11A", "11B", "11C"]

averages = [np.array([int(r[3]) for r in rows if r[2] == s]).mean()
            for s in SUBJECTS]
class_averages = [np.array([int(r[3]) for r in rows if r[0] == c]).mean()
                  for c in CLASSES]

# Required 1 and 3 - a chart for the classes, saved
plt.figure(figsize=(7, 4))
plt.bar(CLASSES, class_averages, color="#47a")
plt.ylim(0, 10)
plt.ylabel("Average grade")
plt.title("Class averages, term 1")
plt.tight_layout()
plt.savefig("classes.png", dpi=150)
plt.close()

print("saved classes.png")

#%% code
# Required 2 and 4 - horizontal bars, coloured by the result
colours = []
for value in averages:
    if value > 7:
        colours.append("#4a7")
    else:
        colours.append("#f71")

plt.figure(figsize=(8, 4))
plt.barh(SUBJECTS, averages, color=colours)
plt.xlim(0, 10)
plt.xlabel("Average grade")
plt.title("Subject averages, term 1")
plt.tight_layout()
plt.savefig("subjects.png", dpi=150)
plt.close()

print("saved subjects.png")

#%% code
# Extra 5, 6 and 8 - a reference line, the numbers on the bars, and the failures
school_average = np.array([int(r[3]) for r in rows]).mean()
failing = [len([r for r in rows if r[2] == s and int(r[3]) < 4]) for s in SUBJECTS]

print("failing per subject:", failing, "total", sum(failing))

plt.figure(figsize=(8, 4))
plt.bar(SUBJECTS, averages, color="#4a7")
plt.axhline(y=school_average, color="red", linestyle="--", label="school average")
for position in range(len(SUBJECTS)):
    plt.text(position, averages[position] + 0.2, f"{averages[position]:.2f}",
             ha="center")
plt.ylim(0, 10)
plt.xticks(rotation=20)
plt.legend()
plt.tight_layout()
plt.savefig("subjects_labelled.png", dpi=150)
plt.close()

print("saved subjects_labelled.png")
