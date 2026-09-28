#%% md
# Օր 8 — Լուծումներ

#%% code
# Առաջադրանք 1 և 2 — չորս մակարդակ, ստուգված չորս գնահատականով

for grade in [10, 8, 5, 2]:
    if grade >= 9:
        print(grade, "— գերազանց")
    elif grade >= 7:
        print(grade, "— լավ")
    elif grade >= 4:
        print(grade, "— բավարար")
    else:
        print(grade, "— անբավարար")

#%% code
# Առաջադրանք 3 — կանոն and-ով

grade = 8
attendance = 90

if grade >= 4 and attendance >= 80:
    print("վկայականը տրվում է")
else:
    print("վկայականը չի տրվում")

#%% code
# Առաջադրանք 5 — not (grade >= 4) և grade < 4 նույն բանն են

grade = 3

print(not (grade >= 4))
print(grade < 4)
