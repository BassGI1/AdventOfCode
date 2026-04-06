raw_input = open("./input.txt", "r").read()

keypad = (1, 2, 3, 4, 5, 6, 7, 8, 9)

code_instructions = raw_input.split("\n")
code = ""
coords = [1, 1]

for instruction_line in code_instructions:
    instruction_line = list(instruction_line)
    for inst in instruction_line:
        if inst == "U":
            coords[1] = max(0, coords[1] - 1)
        elif inst == "R":
            coords[0] = min(2, coords[0] + 1)
        elif inst == "D":
            coords[1] = min(2, coords[1] + 1)
        elif inst == "L":
            coords[0] = max(0, coords[0] - 1)

    code = f"{code}{keypad[coords[1]*3 + coords[0]]}"

print(f"Part 1 Answer: {code}")

keypad = (
    ".", ".", "1", ".", ".",
    ".", "2", "3", "4", ".",
    "5", "6", "7", "8", "9",
    ".", "A", "B", "C", ".",
    ".", ".", "D", ".", ".",
)
coords = [0, 2]
code = ""


def get_keypad_val_p2(c):
    return keypad[c[1]*5 + c[0]]


for instruction_line in code_instructions:
    instruction_line = list(instruction_line)
    for inst in instruction_line:
        if inst == "U" and coords[1] > 0:
            new_coords = coords.copy()
            new_coords[1] -= 1
            if get_keypad_val_p2(new_coords) != ".":
                coords = new_coords

        elif inst == "R" and coords[0] < 4:
            new_coords = coords.copy()
            new_coords[0] += 1
            if get_keypad_val_p2(new_coords) != ".":
                coords = new_coords

        elif inst == "D" and coords[1] < 4:
            new_coords = coords.copy()
            new_coords[1] += 1
            if get_keypad_val_p2(new_coords) != ".":
                coords = new_coords

        elif inst == "L":
            new_coords = coords.copy()
            new_coords[0] -= 1
            if get_keypad_val_p2(new_coords) != ".":
                coords = new_coords

    code = f"{code}{get_keypad_val_p2(coords)}"
    
print(f"Part 2 Answer: {code}")