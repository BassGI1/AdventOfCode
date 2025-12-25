from math import prod
from re import findall
from itertools import combinations

raw_input = open("./input.txt", "r").read()

ingredients = []
ingredient_vals = []
lines = raw_input.split("\n")

for line in lines:
    name, line = line.split(": ")
    ingredients.append(name)
    ingredient_vals.append(tuple([int(x) for x in findall(r"-?[0-9]+", line)]))

positions = list(range(100 + len(ingredients) - 1))
possible_bar_positions = list(combinations(positions, len(ingredients) - 1))

max_score = 0
max_score_with_calories = 0

for bar_positions in possible_bar_positions:
    counts = []
    bar_positions = [-1, *bar_positions, len(positions)]
    for i in range(len(bar_positions) - 1):
        counts.append(bar_positions[i + 1] - bar_positions[i] - 1)

    totals = [0 for _ in range(len(ingredient_vals[0]) - 1)]
    for ing_index in range(len(counts)):
        count = counts[ing_index]
        for i in range(len(totals)):
            totals[i] += count*ingredient_vals[ing_index][i]

    totals = [max(0, t) for t in totals]
    max_score = max(max_score, prod(totals))

    totals = [0 for _ in range(len(ingredient_vals[0]))]
    for ing_index in range(len(counts)):
        count = counts[ing_index]
        for i in range(len(totals)):
            totals[i] += count*ingredient_vals[ing_index][i]

    totals = [max(0, t) for t in totals]
    max_score_with_calories = max(max_score_with_calories, prod(
        totals[:-1])) if totals[-1] == 500 else max_score_with_calories

print(f"Part 1 Answer: {max_score}")
print(f"Part 2 Answer: {max_score_with_calories}")
