raw_input = open("./input.txt", "r+").read()

grid = raw_input.split("\n")

antennae = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] != ".": antennae.append(( grid[y][x], y, x ))
        
antinodes = set()
        
# Part 1
# for symbol, y, x in antennae:
#     for other_symbol, other_y, other_x in antennae:
#         if y != other_y and x != other_x and other_symbol == symbol:
#             antinode_y = 2*y - other_y
#             antinode_x = 2*x - other_x
            
#             if antinode_y >= 0 and antinode_y < len(grid) and antinode_x >= 0 and antinode_x < len(grid[0]):
#                 antinodes.add((antinode_y, antinode_x))
        
# print(len(antinodes))

# Part 2
# for symbol, y, x in antennae:
#     for other_symbol, other_y, other_x in antennae:
#         if y != other_y and x != other_x and other_symbol == symbol:
#             dy = y - other_y
#             dx = x - other_x
            
#             curr_ant_y = y + dy
#             curr_ant_x = x + dx
            
#             while curr_ant_y >= 0 and curr_ant_y < len(grid) and curr_ant_x >= 0 and curr_ant_x < len(grid[0]):
#                 antinodes.add((curr_ant_y, curr_ant_x))
#                 curr_ant_y += dy
#                 curr_ant_x += dx
                
# for _, y, x in antennae:
#     antinodes.add((y, x))
                
# print(len(antinodes))