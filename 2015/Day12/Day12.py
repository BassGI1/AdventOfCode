from re import findall
from json import loads

raw_input = open("./input.txt", "r").read()

print(
    f"Part 1 Answer: {sum([int(x) for x in findall(r"-?[0-9]+", raw_input)])}")

total = [0]
base = loads(raw_input)


def recurse(obj, total_val):
    if type(obj) == int:
        total_val[0] += obj
        return

    elif type(obj) == dict:
        for val in obj.values():
            if val == "red":
                return

        for val in obj.values():
            recurse(val, total_val)

    elif type(obj) == list:
        for val in obj:
            recurse(val, total_val)


recurse(base, total)

print(f"Part 2 Answer: {total[0]}")
