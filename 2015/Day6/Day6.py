from re import findall

raw_input = open("./input.txt", "r").read()

lines = raw_input.split("\n")
grid = [[False]*1000 for _ in range(1000)]

for line in lines:
    start_range, end_range = [list(map(int, r.split(",")))
                              for r in findall(r"[0-9]+,[0-9]+", line)]
    if "turn on" in line:
        for x in range(start_range[0], end_range[0] + 1):
            for y in range(start_range[1], end_range[1] + 1):
                grid[y][x] = True

    elif "turn off" in line:
        for x in range(start_range[0], end_range[0] + 1):
            for y in range(start_range[1], end_range[1] + 1):
                grid[y][x] = False

    else:
        for x in range(start_range[0], end_range[0] + 1):
            for y in range(start_range[1], end_range[1] + 1):
                grid[y][x] = not grid[y][x]


num_lit = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == True:
            num_lit += 1

print(f"Part 1 Answer: {num_lit}")


grid = [[0]*1000 for _ in range(1000)]

for line in lines:
    start_range, end_range = [list(map(int, r.split(",")))
                              for r in findall(r"[0-9]+,[0-9]+", line)]
    if "turn on" in line:
        for x in range(start_range[0], end_range[0] + 1):
            for y in range(start_range[1], end_range[1] + 1):
                grid[y][x] += 1

    elif "turn off" in line:
        for x in range(start_range[0], end_range[0] + 1):
            for y in range(start_range[1], end_range[1] + 1):
                grid[y][x] = max(0, grid[y][x] - 1)

    else:
        for x in range(start_range[0], end_range[0] + 1):
            for y in range(start_range[1], end_range[1] + 1):
                grid[y][x] += 2


total_brightness = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        total_brightness += grid[y][x]

print(f"Part 2 Answer: {total_brightness}")