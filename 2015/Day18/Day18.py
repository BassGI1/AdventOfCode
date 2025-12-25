raw_input = open("./input.txt", "r").read()

num_iters = 100
grid = raw_input.split("\n")
grid = [["." for _ in range(len(grid) + 2)], *[[".", *list(x), "."]
                                               for x in grid], ["." for _ in range(len(grid) + 2)]]


def print_grid(g):
    print("\n".join(["".join(x) for x in g]))
    print()


for _ in range(num_iters):
    new_grid = [["." for _ in range(len(grid))] for x in range(len(grid))]

    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            new_grid[y][x] = grid[y][x]
            num_neighbours_on = 0

            if grid[y - 1][x - 1] == "#":
                num_neighbours_on += 1
            if grid[y - 1][x] == "#":
                num_neighbours_on += 1
            if grid[y - 1][x + 1] == "#":
                num_neighbours_on += 1

            if grid[y][x - 1] == "#":
                num_neighbours_on += 1
            if grid[y][x + 1] == "#":
                num_neighbours_on += 1

            if grid[y + 1][x - 1] == "#":
                num_neighbours_on += 1
            if grid[y + 1][x] == "#":
                num_neighbours_on += 1
            if grid[y + 1][x + 1] == "#":
                num_neighbours_on += 1

            if grid[y][x] == "." and num_neighbours_on == 3:
                new_grid[y][x] = "#"
            elif grid[y][x] == "#" and num_neighbours_on not in {2, 3}:
                new_grid[y][x] = "."

    grid = new_grid

num_lights_on = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "#":
            num_lights_on += 1

print(f"Part 1 Answer: {num_lights_on}")

num_lights_on = 0
grid = raw_input.split("\n")
grid = [["." for _ in range(len(grid) + 2)], *[[".", *list(x), "."]
                                               for x in grid], ["." for _ in range(len(grid) + 2)]]
always_on = {(1, 1), (1, len(grid) - 2), (len(grid) - 2, 1),
             (len(grid) - 2, len(grid) - 2)}

for y, x in always_on:
    grid[y][x] = "#"

for _ in range(num_iters):
    new_grid = [["." for _ in range(len(grid))] for x in range(len(grid))]

    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            if (x, y) in always_on:
                new_grid[y][x] = "#"
                continue

            new_grid[y][x] = grid[y][x]
            num_neighbours_on = 0

            if grid[y - 1][x - 1] == "#":
                num_neighbours_on += 1
            if grid[y - 1][x] == "#":
                num_neighbours_on += 1
            if grid[y - 1][x + 1] == "#":
                num_neighbours_on += 1

            if grid[y][x - 1] == "#":
                num_neighbours_on += 1
            if grid[y][x + 1] == "#":
                num_neighbours_on += 1

            if grid[y + 1][x - 1] == "#":
                num_neighbours_on += 1
            if grid[y + 1][x] == "#":
                num_neighbours_on += 1
            if grid[y + 1][x + 1] == "#":
                num_neighbours_on += 1

            if grid[y][x] == "." and num_neighbours_on == 3:
                new_grid[y][x] = "#"
            elif grid[y][x] == "#" and num_neighbours_on not in {2, 3}:
                new_grid[y][x] = "."

    grid = new_grid
    
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "#":
            num_lights_on += 1

print(f"Part 2 Answer: {num_lights_on}")