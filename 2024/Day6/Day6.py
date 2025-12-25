raw_input = open("./input.txt", "r+").read()

grid = [f"D{s}D" for s in raw_input.split("\n")]
grid = ["D"*len(grid[0]), *grid, "D"*len(grid[0])]

current_char = None
current_coords = (0, 0)

for y in range(len(grid)):
    done = False
    for x in range(len(grid[y])):
        if grid[y][x] in { ">", "<", "^", "V" }:
            current_char = grid[y][x]
            current_coords = (y, x)
            grid[y] = grid[y][:x] + "X" + grid[y][x + 1:]
            done = True
            break
    if done: break
    
while current_char != "D":
    y, x = current_coords
    if current_char == "^":
        next_move = grid[y - 1][x]
        if next_move == "D":
            current_char = "D"
            grid[y] = grid[y][:x] + "X" + grid[y][x + 1:]
        elif next_move == "#": current_char = ">"
        else:
            grid[y] = grid[y][:x] + "X" + grid[y][x + 1:]
            current_coords = (y - 1, x)

    if current_char == ">":
        next_move = grid[y][x + 1]
        if next_move == "D":
            current_char = "D"
            grid[y] = grid[y][:x] + "X" + grid[y][x + 1:]
            current_coords = (y, x + 1)
        elif next_move == "#": current_char = "V"
        else:
            grid[y] = grid[y][:x] + "X" + grid[y][x + 1:]
            current_coords = (y, x + 1)
            
    if current_char == "V":
        next_move = grid[y + 1][x]
        if next_move == "D":
            current_char = "D"
            grid[y] = grid[y][:x] + "X" + grid[y][x + 1:]
            current_coords = (y + 1, x)
        elif next_move == "#": current_char = "<"
        else:
            grid[y] = grid[y][:x] + "X" + grid[y][x + 1:]
            current_coords = (y + 1, x)
            
    if current_char == "<":
        next_move = grid[y][x - 1]
        if next_move == "D":
            current_char = "D"
            grid[y] = grid[y][:x] + "X" + grid[y][x + 1:]
            current_coords = (y, x - 1)
        elif next_move == "#": current_char = "^"
        else:
            grid[y] = grid[y][:x] + "X" + grid[y][x + 1:]
            current_coords = (y, x - 1)
            
total = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "X": total += 1
    
print(total)