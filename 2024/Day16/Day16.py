raw_input = open("./input.txt", "r+").read()

grid = [[x for x in line] for line in raw_input.split("\n")]

moves = []
min_cost_moves = {}
ending_coords = None

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "S":
            moves.append((y, x, ">", 0, {(y, x)}))
        if grid[y][x] == "E":
            ending_coords = (y, x)

min_cost = 1e9
min_moves = 1e9

while len(moves):
    (y, x, direction, cost, past_moves) = moves[0]

    if f"{y} {x}" not in min_cost_moves or min_cost_moves[f"{y} {x}"] > cost:
        min_cost_moves[f"{y} {x}"] = cost

        if y == ending_coords[0] and x == ending_coords[1]:
            min_moves = min(min_moves, len(past_moves))
            min_cost = min(min_cost, cost)

        if grid[y + 1][x] != "#" and (y + 1, x) not in past_moves:
            temp = past_moves.copy()
            temp.add((y + 1, x))
            if direction == "V":
                moves.append((y + 1, x, "V", cost + 1, temp))
            else:
                moves.append((y + 1, x, "V", cost + 1001, temp))

        if grid[y - 1][x] != "#" and (y - 1, x) not in past_moves:
            temp = past_moves.copy()
            temp.add((y - 1, x))
            if direction == "^":
                moves.append((y - 1, x, "^", cost + 1, temp))
            else:
                moves.append((y - 1, x, "^", cost + 1001, temp))

        if grid[y][x + 1] != "#" and (y, x + 1) not in past_moves:
            temp = past_moves.copy()
            temp.add((y, x + 1))
            if direction == ">":
                moves.append((y, x + 1, ">", cost + 1, temp))
            else:
                moves.append((y, x + 1, ">", cost + 1001, temp))

        if grid[y][x - 1] != "#" and (y, x - 1) not in past_moves:
            temp = past_moves.copy()
            temp.add((y, x - 1))
            if direction == "<":
                moves.append((y, x - 1, "<", cost + 1, temp))
            else:
                moves.append((y, x - 1, "<", cost + 1001, temp))

    moves.pop(0)
    moves.sort(key=lambda x: x[3])


print(min_cost, min_moves)
