#%% md
# Օր 13 — Լուծումներ

#%% code
# Առաջադրանք 1, 2 — գումարը և միջինը

class_grades = [9, 6, 10, 3, 8, 5, 8, 4, 9, 2, 8, 6]

total = 0
for grade in class_grades:
    total = total + grade

print(f"Գումարը՝ {total}")
print(f"Միջինը՝ {total / len(class_grades):.1f}")

#%% code
# Առաջադրանք 4 — քանի՞սն ունեն 10

how_many = 0

for grade in class_grades:
    if grade == 10:
        how_many = how_many + 1

print(how_many)

#%% code
# Առաջադրանք 5 — բաշխումը

for mark in range(1, 11):
    how_many = 0
    for grade in class_grades:
        if grade == mark:
            how_many = how_many + 1
    print(f"{mark} միավոր՝ {how_many} աշակերտ")
