# Part 1
# grid = open("./input.txt", "r+").read().split("\n")
# for i in range(len(grid)): grid[i] = f"...{grid[i]}..."
# grid = ["."*len(grid[0]), "."*len(grid[0]), "."*len(grid[0]), *grid, "."*len(grid[0]), "."*len(grid[0]), "."*len(grid[0])]

# total = 0

# for y in range(3, len(grid) - 3):
#     for x in range(3, len(grid) - 3):
#         if grid[y][x] == "X":
#             if grid[y - 1][x] == "M" and grid[y - 2][x] == "A" and grid[y - 3][x] == "S":
#                 total += 1
#             if grid[y + 1][x] == "M" and grid[y + 2][x] == "A" and grid[y + 3][x] == "S":
#                 total += 1
#             if grid[y][x - 1] == "M" and grid[y][x - 2] == "A" and grid[y][x - 3] == "S":
#                 total += 1
#             if grid[y][x + 1] == "M" and grid[y][x + 2] == "A" and grid[y][x + 3] == "S":
#                 total += 1
#             if grid[y - 1][x - 1] == "M" and grid[y - 2][x - 2] == "A" and grid[y - 3][x - 3] == "S":
#                 total += 1
#             if grid[y + 1][x - 1] == "M" and grid[y + 2][x - 2] == "A" and grid[y + 3][x - 3] == "S":
#                 total += 1
#             if grid[y + 1][x + 1] == "M" and grid[y + 2][x + 2] == "A" and grid[y + 3][x + 3] == "S":
#                 total += 1
#             if grid[y - 1][x + 1] == "M" and grid[y - 2][x + 2] == "A" and grid[y - 3][x + 3] == "S":
#                 total += 1
                
# print(total)

# Part 2
# grid = open("./input.txt", "r+").read().split("\n")
# for i in range(len(grid)): grid[i] = f".{grid[i]}."
# grid = ["."*len(grid[0]), *grid, "."*len(grid[0])]

# total = 0

# for y in range(1, len(grid) - 1):
#     for x in range(1, len(grid) - 1):
#         if grid[y][x] == "A":
#             left_to_right = grid[y - 1][x - 1] + "A" + grid[y + 1][x + 1]
#             right_to_left = grid[y + 1][x - 1] + "A" + grid[y - 1][x + 1]
#             if (left_to_right == "MAS" or left_to_right[::-1] == "MAS") and (left_to_right == right_to_left or left_to_right[::-1] == right_to_left):
#             	total += 1

# print(total)