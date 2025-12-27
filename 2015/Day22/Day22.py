from re import findall

raw_input = open("./input.txt", "r").read()

boss_hit_points, boss_damage = [int(x) for x in findall(r"[0-9]+", raw_input)]

durations = [0, 0, 6, 6, 5]
costs = [53, 73, 113, 173, 229]


def play_turn_p1(bhp, bd, php, pm, effects, turn, curr_cost, mwc):
    global durations, costs

    if bhp <= 0:
        mwc[0] = min(mwc[0], curr_cost)
        return

    if turn is False:
        php = php - max(1, bd - (0 if effects[2] == 0 else 7))
        pm = pm if effects[4] == 0 else pm + 101
        bhp = bhp if effects[3] == 0 else bhp - 3

        eff_copy = effects.copy()
        for i in range(2, 5):
            eff_copy[i] = max(0, eff_copy[i] - 1)

        play_turn_p1(bhp, bd, php, pm, eff_copy, True, curr_cost, mwc)

    else:
        if php <= 0 or curr_cost >= mwc[0]:
            return

        pm = pm if effects[4] == 0 else pm + 101
        bhp = bhp if effects[3] == 0 else bhp - 3

        if bhp <= 0:
            mwc[0] = min(mwc[0], curr_cost)
            return

        eff_copy = effects.copy()
        for i in range(2, 5):
            eff_copy[i] = max(0, eff_copy[i] - 1)

        playable_effects = {i for i in range(5) if eff_copy[i] == 0}
        if 0 in playable_effects and pm >= costs[0]:
            play_turn_p1(bhp - 4, bd, php, pm -
                         costs[0], eff_copy.copy(), False, curr_cost + costs[0], mwc)
        if 1 in playable_effects and pm >= costs[1]:
            play_turn_p1(bhp - 2, bd, php + 2, pm -
                         costs[1], eff_copy.copy(), False, curr_cost + costs[1], mwc)
        if 2 in playable_effects and pm >= costs[2]:
            c = eff_copy.copy()
            c[2] = durations[2]
            play_turn_p1(bhp, bd, php, pm -
                         costs[2], c, False, curr_cost + costs[2], mwc)
        if 3 in playable_effects and pm >= costs[3]:
            c = eff_copy.copy()
            c[3] = durations[3]
            play_turn_p1(bhp, bd, php, pm -
                         costs[3], c, False, curr_cost + costs[3], mwc)
        if 4 in playable_effects and pm >= costs[4]:
            c = eff_copy.copy()
            c[4] = durations[4]
            play_turn_p1(bhp, bd, php, pm -
                         costs[4], c, False, curr_cost + costs[4], mwc)


min_cost_win = [float("inf")]
play_turn_p1(boss_hit_points, boss_damage, 50, 500,
             [0, 0, 0, 0, 0], True, 0, min_cost_win)

print(f"Part 1 Answer: {min_cost_win[0]}")


def play_turn_p2(bhp, bd, php, pm, effects, turn, curr_cost, mwc):
    global durations, costs

    if bhp <= 0:
        mwc[0] = min(mwc[0], curr_cost)
        return

    if turn is False:
        php = php - max(1, bd - (0 if effects[2] == 0 else 7))
        pm = pm if effects[4] == 0 else pm + 101
        bhp = bhp if effects[3] == 0 else bhp - 3

        eff_copy = effects.copy()
        for i in range(2, 5):
            eff_copy[i] = max(0, eff_copy[i] - 1)

        play_turn_p2(bhp, bd, php, pm, eff_copy, True, curr_cost, mwc)

    else:
        php -= 1
        if php <= 0 or curr_cost >= mwc[0]:
            return

        pm = pm if effects[4] == 0 else pm + 101
        bhp = bhp if effects[3] == 0 else bhp - 3

        if bhp <= 0:
            mwc[0] = min(mwc[0], curr_cost)
            return

        eff_copy = effects.copy()
        for i in range(2, 5):
            eff_copy[i] = max(0, eff_copy[i] - 1)

        playable_effects = {i for i in range(5) if eff_copy[i] == 0}
        if 0 in playable_effects and pm >= costs[0]:
            play_turn_p2(bhp - 4, bd, php, pm -
                         costs[0], eff_copy.copy(), False, curr_cost + costs[0], mwc)
        if 1 in playable_effects and pm >= costs[1]:
            play_turn_p2(bhp - 2, bd, php + 2, pm -
                         costs[1], eff_copy.copy(), False, curr_cost + costs[1], mwc)
        if 2 in playable_effects and pm >= costs[2]:
            c = eff_copy.copy()
            c[2] = durations[2]
            play_turn_p2(bhp, bd, php, pm -
                         costs[2], c, False, curr_cost + costs[2], mwc)
        if 3 in playable_effects and pm >= costs[3]:
            c = eff_copy.copy()
            c[3] = durations[3]
            play_turn_p2(bhp, bd, php, pm -
                         costs[3], c, False, curr_cost + costs[3], mwc)
        if 4 in playable_effects and pm >= costs[4]:
            c = eff_copy.copy()
            c[4] = durations[4]
            play_turn_p2(bhp, bd, php, pm -
                         costs[4], c, False, curr_cost + costs[4], mwc)


min_cost_win = [float("inf")]
play_turn_p2(boss_hit_points, boss_damage, 50, 500,
             [0, 0, 0, 0, 0], True, 0, min_cost_win)

print(f"Part 2 Answer: {min_cost_win[0]}")
