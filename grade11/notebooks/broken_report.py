import pandas as pd

PASS_MARK = 4


def failing_count(data, class_name):
    """How many failing grades does this class have?"""
    rows = data[data["class"] == class_name]
    count = 0
    for grade in rows["grade"]:
        if grade < PASS_MARK:
            count = count + 1
        return count


def main():
    data = pd.read_csv("school.csv")
    for class_name in ["11A", "11B", "11C"]:
        print(class_name, failing_count(data, class_name))
    print("total should be 18")


if __name__ == "__main__":
    main()
