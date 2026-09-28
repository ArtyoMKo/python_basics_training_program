#%% md
# Օր 15 — Լուծումներ

Այս տետրում input()-ի փոխարեն ցուցակ է օգտագործված, որպեսզի կարողանաս գործարկել։
Քո տետրում input()-ը պետք է մնա։

#%% code
# Առաջադրանք 1-4 — ամբողջական ցիկլ բոլոր ստուգումներով

answers = ["9", "ինը", "15", "6", "դուրս"]      # այն, ինչ օգտվողը կգրեր
class_grades = []

for answer in answers:
    if answer == "դուրս":
        break

    if not answer.isdigit():
        print(f"«{answer}» — դա թիվ չէ։")
        continue

    grade = int(answer)

    if grade < 1 or grade > 10:
        print(f"{grade} — պետք է լինի 1-ից 10։")
        continue

    class_grades.append(grade)

print(f"Հավաքվեց {len(class_grades)} գնահատական՝ {class_grades}")
print(f"Միջինը՝ {sum(class_grades) / len(class_grades):.1f}")
