from re import findall
from itertools import combinations

raw_input = open("./input.txt", "r").read()

boss_hit_points, boss_damage, boss_armor = [
    int(x) for x in findall(r"[0-9]+", raw_input)]


def play_game(bhp, bd, ba, pd, pa):
    php = 100
    turn_p = True
    while bhp > 0 and php > 0:
        if turn_p is True:
            bhp = bhp - max(1, pd - ba)
        else:
            php = php - max(1, bd - pa)
        turn_p = not turn_p

    return bhp < php


WEAPONS = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)
]
ARMOR = [
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5)
]
RINGS = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3)
]

weapon_combinations = [*list(combinations(WEAPONS, 1))]
armor_combinations = [*list(combinations(ARMOR, 1)),
                      *list(combinations(ARMOR, 0))]
ring_combinations = [*list(combinations(RINGS, 2)), *
                     list(combinations(RINGS, 1)), *list(combinations(RINGS, 0))]

min_win_cost = float("inf")

for w in weapon_combinations:
    for a in armor_combinations:
        for r in ring_combinations:
            total_cost = sum([x[0] for x in w]) + sum([x[0]
                                                       for x in a]) + sum([x[0] for x in r])
            total_damage = sum([x[1] for x in w]) + sum([x[1]
                                                         for x in a]) + sum([x[1] for x in r])
            total_armor = sum([x[2] for x in w]) + sum([x[2]
                                                       for x in a]) + sum([x[2] for x in r])

            if play_game(boss_hit_points, boss_damage, boss_armor, total_damage, total_armor) == 1:
                min_win_cost = min(min_win_cost, total_cost)


print(f"Part 1 Answer: {min_win_cost}")

max_lose_cost = 0

for w in weapon_combinations:
    for a in armor_combinations:
        for r in ring_combinations:
            total_cost = sum([x[0] for x in w]) + sum([x[0]
                                                       for x in a]) + sum([x[0] for x in r])
            total_damage = sum([x[1] for x in w]) + sum([x[1]
                                                         for x in a]) + sum([x[1] for x in r])
            total_armor = sum([x[2] for x in w]) + sum([x[2]
                                                       for x in a]) + sum([x[2] for x in r])

            if play_game(boss_hit_points, boss_damage, boss_armor, total_damage, total_armor) == 0:
                max_lose_cost = max(max_lose_cost, total_cost)

print(f"Part 2 Answer: {max_lose_cost}")