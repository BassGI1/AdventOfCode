from re import findall

raw_input = open("./input.txt", "r").read()
lines = raw_input.split("\n")

GRID_WIDTH = 50
GRID_HEIGHT = 6
NUMBER_PATTERN = r"[0-9]+"

grid = [list("."*(GRID_WIDTH)) for _ in range(GRID_HEIGHT)]


def print_grid(g):
    a = ["".join(x) for x in g]
    print("\n".join(a))
    print("")


for line in lines:
    if "rect" in line:
        x_end, y_end = [int(a) for a in findall(NUMBER_PATTERN, line)]
        for y in range(y_end):
            for x in range(x_end):
                grid[y][x] = "#"

    elif "x=" in line:
        col = []
        col_num, val = [int(a) for a in findall(NUMBER_PATTERN, line)]

        for i in range(GRID_HEIGHT):
            col.append((grid[i][col_num], (i + val) % GRID_HEIGHT))

        for led, i in col:
            grid[i][col_num] = led

    elif "y=" in line:
        row = []
        row_num, val = [int(a) for a in findall(NUMBER_PATTERN, line)]

        for i in range(GRID_WIDTH):
            row.append((grid[row_num][i], (i + val) % GRID_WIDTH))

        for led, i in row:
            grid[row_num][i] = led


num_pixels_lit = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "#":
            num_pixels_lit += 1
        else:
            grid[y][x] = " "

print(f"Part 1 Answer: {num_pixels_lit}")
print(f"Part 2 Answer: ")
print_grid(grid)