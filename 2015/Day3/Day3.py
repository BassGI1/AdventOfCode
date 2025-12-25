raw_input = open("./input.txt", "r").read()

visited = set()
current_coords = (0, 0)

for move in raw_input:
    x, y = current_coords
    if move == "^":
        y += 1
    elif move == "v":
        y -= 1
    elif move == ">":
        x += 1
    elif move == "<":
        x -= 1
    
    current_coords = (x, y)
    visited.add((x, y))
    
print(f"Part 1 Answer: {len(visited)}")

visited = set()
current_coords = (0, 0)
current_robo_coords = (0, 0)

for i in range(0, len(raw_input) - 1, 2):
    santa_move = raw_input[i]
    robo_move = raw_input[i + 1]
    
    x_santa, y_santa = current_coords
    x_robo, y_robo = current_robo_coords
    
    if santa_move == "^":
        y_santa += 1
    elif santa_move == "v":
        y_santa -= 1
    elif santa_move == ">":
        x_santa += 1
    elif santa_move == "<":
        x_santa -= 1
        
    if robo_move == "^":
        y_robo += 1
    elif robo_move == "v":
        y_robo -= 1
    elif robo_move == ">":
        x_robo += 1
    elif robo_move == "<":
        x_robo -= 1
    
    current_coords = (x_santa, y_santa)
    current_robo_coords = (x_robo, y_robo)
    
    visited.add((x_santa, y_santa))
    visited.add((x_robo, y_robo))
    
print(f"Part 2 Answer: {len(visited)}")