#%% md
# Օր 19 — Լուծումներ

#%% code
school = {
    "name": "School N 5",
    "parts": [
        {
            "name": "Science stream",
            "parts": [
                {
                    "name": "11A",
                    "parts": [
                        {"name": "group 1", "students": ["Ani", "Davit"]},
                        {"name": "group 2", "students": ["Nare"]},
                    ],
                },
                {"name": "11B", "students": ["Aram", "Mariam"]},
            ],
        },
        {
            "name": "Humanities stream",
            "parts": [
                {"name": "11C", "students": ["Tigran", "Lilit", "Gor"]},
            ],
        },
    ],
}


# Required 1 and 2 - how deep, and how many parts
def depth(part):
    if "students" in part:
        return 1
    return 1 + max(depth(smaller) for smaller in part["parts"])


def count_parts(part):
    if "students" in part:
        return 1
    total = 1
    for smaller in part["parts"]:
        total = total + count_parts(smaller)
    return total


print("depth:", depth(school))
print("parts:", count_parts(school))

#%% code
# Required 3 and 4 - finding one student, and the biggest group
def find(part, name):
    if "students" in part:
        if name in part["students"]:
            return part["name"]
        return None
    for smaller in part["parts"]:
        found = find(smaller, name)
        if found is not None:
            return found
    return None


def biggest(part):
    if "students" in part:
        return part["name"], len(part["students"])
    best_name = None
    best_size = -1
    for smaller in part["parts"]:
        name, size = biggest(smaller)
        if size > best_size:
            best_name = name
            best_size = size
    return best_name, best_size


print(find(school, "Nare"), "|", find(school, "Someone"))
print(biggest(school))

#%% code
# Extra 5 and 6 - the whole path, and flattening a nested list
def path_to(part, name):
    if "students" in part:
        if name in part["students"]:
            return [part["name"]]
        return None
    for smaller in part["parts"]:
        found = path_to(smaller, name)
        if found is not None:
            return [part["name"]] + found
    return None


def flatten(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result = result + flatten(item)
        else:
            result.append(item)
    return result


print(path_to(school, "Davit"))
print(flatten([1, [2, 3, [4, [5, 6]], 7], [8], 9]))

#%% code
# Challenge 9 - the same answer with a queue instead of recursion
def count_with_queue(school):
    queue = [school]
    total = 0
    while queue:
        part = queue.pop()
        if "students" in part:
            total = total + len(part["students"])
        else:
            queue = queue + part["parts"]
    return total


print(count_with_queue(school))
