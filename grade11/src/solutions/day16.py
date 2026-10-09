#%% md
# Թեմա 16 — Լուծումներ

#%% code
import pandas as pd

data = pd.read_csv("school.csv")

# Required 1 - the first questions you ask any new file
print("rows and columns:", data.shape)
print("columns:", data.columns.tolist())
print("average:", round(data["grade"].mean(), 2))
print()
print(data.head(3).to_string())

#%% code
# Required 2 and 3 - class averages, and who is failing
for class_name in ["11A", "11B", "11C"]:
    rows = data[data["class"] == class_name]
    print(class_name, round(rows["grade"].mean(), 2))

print()
failing = data[data["grade"] < 4]
print(len(failing), "failing grades")
print(failing["student"].nunique(), "students behind them")

#%% code
# Required 4 - one student's five rows
one = data[data["student"] == "Ani Hakobyan"]
print(one.to_string())
print("average:", round(one["grade"].mean(), 2))

#%% code
# Extra 5 to 8 - a new column, sorting, unique values, and the non-empty notes
data["passed"] = data["grade"] >= 4
print("passing marks:", int(data["passed"].sum()))

print()
print(data.sort_values("grade").head(10)[["student", "subject", "grade"]].to_string())

print()
for subject in data["subject"].unique():
    rows = data[data["subject"] == subject]
    print(f"{subject:<14} {rows['grade'].mean():.2f}")

print()
print(data[data["note"].notna()][["student", "note"]].to_string())
