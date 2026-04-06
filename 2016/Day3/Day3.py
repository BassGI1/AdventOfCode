from re import findall

raw_input = open("./input.txt", "r").read()

num_valid = 0
potential_triangle_strings = raw_input.split("\n")

for pts in potential_triangle_strings:
    side_lengths = sorted([int(x) for x in findall(r"[0-9]+", pts)])
    if side_lengths[0] + side_lengths[1] > side_lengths[2]:
        num_valid += 1
        
print(f"Part 1 Answer: {num_valid}")

num_valid = 0
all_side_lengths = [int(x) for x in findall(r"[0-9]+", raw_input)]
while len(all_side_lengths):
    buffer = []
    for _ in range(9):
        buffer.append(all_side_lengths.pop(0))
    
    group1 = sorted([buffer[0], buffer[3], buffer[6]])
    group2 = sorted([buffer[1], buffer[4], buffer[7]])
    group3 = sorted([buffer[2], buffer[5], buffer[8]])
    
    if group1[0] + group1[1] > group1[2]:
        num_valid += 1
    if group2[0] + group2[1] > group2[2]:
        num_valid += 1
    if group3[0] + group3[1] > group3[2]:
        num_valid += 1
        
print(f"Part 2 Answer: {num_valid}")