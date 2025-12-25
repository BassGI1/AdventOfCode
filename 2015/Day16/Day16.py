raw_input = open("./input.txt", "r").read()

known_values = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

sues = []
lines = raw_input.split("\n")

for i in range(len(lines)):
    line = lines[i][lines[i].index(": ") + 2:]
    thing_strings = line.split(", ")
    sue_entry = {"number": i + 1}

    for string in thing_strings:
        key, val = string.split(": ")
        sue_entry[key] = int(val)

    sues.append(sue_entry)

possible_sues = sues.copy()
for key, value in known_values.items():
    possible_sues = list(
        filter(lambda x: key not in x or x[key] == value, possible_sues))

print(f"Part 1 Answer: {possible_sues[0]["number"]}")

possible_sues = sues.copy()
for key, value in known_values.items():
    if key == "cats" or key == "trees":
        possible_sues = list(
            filter(lambda x: key not in x or x[key] > value, possible_sues))
        continue

    if key == "pomeranians" or key == "goldfish":
        possible_sues = list(
            filter(lambda x: key not in x or x[key] < value, possible_sues))
        continue

    possible_sues = list(
        filter(lambda x: key not in x or x[key] == value, possible_sues))

print(f"Part 2 Answer: {possible_sues[0]["number"]}")