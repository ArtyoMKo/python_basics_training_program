#%% md
# Օր 18 — Լուծումներ

#%% code
import pandas as pd
import matplotlib.pyplot as plt

PASS_MARK = 4
data = pd.read_csv("school.csv")


# Required 1 - the six questions, as a function
def inspect(data):
    print("rows and columns:", data.shape)
    print("columns:", data.columns.tolist())
    print("classes:", sorted(data["class"].unique()))
    print("subjects:", sorted(data["subject"].unique()))
    print("students:", data["student"].nunique())
    print("missing values:")
    print(data.isna().sum().to_string())


inspect(data)

#%% code
# Required 2 - one class, as a dictionary
def class_summary(data, class_name):
    rows = data[data["class"] == class_name]
    return {
        "students": rows["student"].nunique(),
        "average": round(rows["grade"].mean(), 2),
        "spread": round(rows["grade"].std(), 3),
        "failing": int((rows["grade"] < PASS_MARK).sum()),
    }


for class_name in ["11A", "11B", "11C"]:
    print(class_name, class_summary(data, class_name))

#%% code
# Required 3 and 4 - the whole report behind one call
def save_distribution_chart(data, filename, title):
    plt.figure(figsize=(7, 4))
    plt.hist(data["grade"], bins=range(1, 12), edgecolor="white", color="#47a")
    plt.xlabel("Grade")
    plt.ylabel("How many")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()


def build_report(path):
    data = pd.read_csv(path)

    for class_name in sorted(data["class"].unique()):
        rows = data[data["class"] == class_name]
        save_distribution_chart(rows, f"dist_{class_name}.png",
                                f"{class_name} — average {rows['grade'].mean():.2f}")

    lines = ["TERM REPORT", "=" * 40]
    lines.append(f"Students:         {data['student'].nunique()}")
    lines.append(f"School average:   {data['grade'].mean():.2f}")
    lines.append(f"Failing grades:   {int((data['grade'] < PASS_MARK).sum())}")
    lines.append("")
    lines.append("Subject averages")
    averages = data.groupby("subject")["grade"].mean().sort_values()
    for subject in averages.index:
        lines.append(f"  {subject:<16} {averages[subject]:.2f}")

    text = "\n".join(lines)
    print(text)
    return text


build_report("school.csv")
