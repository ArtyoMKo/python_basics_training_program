#%% md
# Օր 15 — Լուծումներ

#%% code
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

rows = [line.split(",") for line in
        Path("school.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
        if line != ""]

SUBJECTS = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]
CLASSES = ["11A", "11B", "11C"]

# Required 1 - one histogram per class
for class_name in CLASSES:
    marks = np.array([int(r[3]) for r in rows if r[0] == class_name])
    plt.figure(figsize=(7, 4))
    plt.hist(marks, bins=range(1, 12), edgecolor="white", color="#47a")
    plt.xlabel("Grade")
    plt.ylabel("How many")
    plt.title(f"{class_name} — average {marks.mean():.2f}")
    plt.tight_layout()
    plt.savefig(f"dist_{class_name}.png", dpi=150)
    plt.close()

print("three histograms saved")

#%% code
# Required 2 - bars, not a line: the subjects have no natural order
failing = [len([r for r in rows if r[2] == s and int(r[3]) < 4]) for s in SUBJECTS]

plt.figure(figsize=(8, 4))
plt.bar(SUBJECTS, failing, color="#c74")
plt.ylabel("Failing grades")
plt.title("Failing grades by subject")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("failing.png", dpi=150)
plt.close()

print("failing per subject:", failing, "total", sum(failing))

#%% code
# Required 4 - the four charts in one picture
grades = np.array([int(r[3]) for r in rows])
averages = [np.array([int(r[3]) for r in rows if r[2] == s]).mean()
            for s in SUBJECTS]
class_averages = [np.array([int(r[3]) for r in rows if r[0] == c]).mean()
                  for c in CLASSES]
levels = list(range(1, 11))
counts = [int((grades == level).sum()) for level in levels]

plt.figure(figsize=(11, 7))

plt.subplot(2, 2, 1)
plt.bar(SUBJECTS, averages, color="#4a7")
plt.ylim(0, 10)
plt.xticks(rotation=25, fontsize=7)
plt.title("Subjects")

plt.subplot(2, 2, 2)
plt.bar(CLASSES, class_averages, color="#47a")
plt.ylim(0, 10)
plt.title("Classes")

plt.subplot(2, 2, 3)
plt.hist(grades, bins=range(1, 12), edgecolor="white", color="#a74")
plt.title("Distribution")

plt.subplot(2, 2, 4)
plt.plot(levels, counts, marker="o")
plt.grid(True, alpha=0.3)
plt.title("How many of each grade")

plt.tight_layout()
plt.savefig("term_report.png", dpi=150)
plt.close()

print("saved term_report.png")
