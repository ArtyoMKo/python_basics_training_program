#%% md
# Թեմա 17 — Լուծումներ

#%% code
import pandas as pd

data = pd.read_csv("school.csv")

# Required 1 - three groupings, no loop and no list of names
print(data.groupby("class")["grade"].mean().round(2))
print()
print(data.groupby("subject")["grade"].mean().round(2).sort_values())
print()
print(data.groupby("student")["grade"].mean().round(2).head(10))

#%% code
# Required 2 - filter first, then group
failing = data[data["grade"] < 4]
counts = failing.groupby("class")["grade"].size()

print(counts)
print("total:", counts.sum())

#%% code
# Required 3 and 4 - several numbers at once, and the two-way table
per_student = data.groupby("student")["grade"].agg(["mean", "min", "max"]).round(2)
print(per_student.sort_values("mean", ascending=False).head().to_string())

print()
table = data.pivot_table(index="student", columns="subject", values="grade")
print("shape:", table.shape)

#%% code
# Extra 6 and 7 - the pass rate per subject, and the most uneven subject
data["passed"] = data["grade"] >= 4
print((data.groupby("subject")["passed"].mean() * 100).round(1))

print()
spread = data.groupby("subject")["grade"].std().round(3)
print(spread.sort_values(ascending=False))
print("most uneven:", spread.idxmax())
