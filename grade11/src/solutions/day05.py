#%% md
# Օր 5 — Լուծումներ

#%% code
register = {
    "Ani": 9, "Davit": 6, "Nare": 10, "Aram": 3, "Mariam": 8, "Tigran": 7,
    "Lilit": 5, "Gor": 4, "Anahit": 9, "Hayk": 2, "Sona": 8, "Vahe": 6,
}
PASS_MARK = 4

# Required 1 and 2 - choosing, not filtering
marks = ["+" if register[name] >= PASS_MARK else "-" for name in register]
adjusted = [register[name] if register[name] >= 5 else 0 for name in register]

print(marks)
print(adjusted)

#%% code
# Required 3 - a helper function keeps the comprehension readable
def word_for(grade):
    if grade >= 9:
        return "excellent"
    if grade >= 7:
        return "good"
    return "ok"


words = {name: word_for(register[name]) for name in register}
print(words)

#%% code
# Required 4 - sorting by a rule of your own
by_length = sorted(register, key=lambda name: len(name))
print(by_length)

#%% code
# Extra 5 and 6 - the top five, and the dictionary turned inside out
top_five = sorted(register, key=lambda name: register[name], reverse=True)[:5]
for name in top_five:
    print(f"{name}: {register[name]}")

print()

by_grade = {}
for name in register:
    grade = register[name]
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(name)

for grade in sorted(by_grade):
    print(grade, by_grade[grade])
