raw_input = open("./input.txt", "r").read()

floor = 0
basement_index = -1
for i in range(len(raw_input)):
    c = raw_input[i]
    
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1
    
    if floor < 0 and basement_index == -1:
        basement_index = i + 1
        
print(f"Part 1 Answer: {floor}")
print(f"Part 2 Answer: {basement_index}")