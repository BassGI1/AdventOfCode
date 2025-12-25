from itertools import permutations

raw_input = open("./input.txt", "r").read()

happiness_hash = {}
lines = raw_input.split("\n")

for line in lines:
    line = line.replace("would ", "").replace(
        " happiness units by sitting next to", "")[:-1]
    splitted = line.split(" ")
    diff = int(splitted[2]) if splitted[1] == "gain" else int(splitted[2])*-1
    p1, p2 = splitted[0], splitted[3]

    if p1 not in happiness_hash:
        happiness_hash[p1] = {p2: diff}
    else:
        happiness_hash[p1][p2] = diff

possible_perms = set(permutations(happiness_hash.keys()))

max_happiness = 0
for perm in possible_perms:
    happiness = 0

    for i in range(len(perm)):
        behind = happiness_hash[perm[i]][perm[(i + len(perm) - 1) % len(perm)]]
        ahead = happiness_hash[perm[i]][perm[(i + 1) % len(perm)]]
        happiness = happiness + ahead + behind

    max_happiness = max(max_happiness, happiness)

print(f"Part 1 Answer: {max_happiness}")

people = happiness_hash.keys()
for key, val in happiness_hash.items():
    val["Me"] = 0
happiness_hash["Me"] = {p: 0 for p in people}

possible_perms = set(permutations(happiness_hash.keys()))

max_happiness = 0
for perm in possible_perms:
    happiness = 0

    for i in range(len(perm)):
        behind = happiness_hash[perm[i]][perm[(i + len(perm) - 1) % len(perm)]]
        ahead = happiness_hash[perm[i]][perm[(i + 1) % len(perm)]]
        happiness = happiness + ahead + behind

    max_happiness = max(max_happiness, happiness)

print(f"Part 2 Answer: {max_happiness}")
