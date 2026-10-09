#%% md
# Օր 4 — Լուծումներ

#%% code
register = {
    "Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3, "Mariam": 8, "Tigran": 7,
    "Lilit": 5, "Gor": 4, "Anahit": 9, "Hayk": 2, "Sona": 8, "Vahe": 6,
}
PASS_MARK = 4

# Required 1 - three comprehensions
above_seven = [name for name in register if register[name] > 7]
plus_one = [register[name] + 1 for name in register]
starts_with_a = [name for name in register if name.startswith("A")]

print(above_seven)
print(plus_one)
print(starts_with_a)

#%% code
# Required 2 - a loop turned into one line
short_names = [name for name in register if len(name) <= 4]
print(short_names)

#%% code
# Required 3 - one line turned back into a loop
result_again = []
for name in register:
    if register[name] >= 8:
        result_again.append(name + ": " + str(register[name]))

print(result_again)

#%% code
# Required 4 - from the school file
from pathlib import Path

lines = Path("school.csv").read_text(encoding="utf-8").strip().splitlines()
rows = [line.split(",") for line in lines[1:] if line != ""]

maths = [int(row[3]) for row in rows if row[2] == "Mathematics"]
print(len(maths), "maths grades, average", round(sum(maths) / len(maths), 2))

#%% code
# Extra 8 - one class's names, then without repeats
names_11b = [row[1] for row in rows if row[0] == "11B"]
print(len(names_11b))

unique = sorted(set(names_11b))
print(len(unique))
