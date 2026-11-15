raw_input = open("./input.txt", "r").read()

STRING_P1 = "abcdefgh"
STRING_P2 = "fbgdceah"

string = STRING_P1
instructions = raw_input.split("\n")


def rotate_right(s):
    return f"{s[-1]}{s[:-1]}"


def rotate_left(s):
    return f"{s[1:]}{s[0]}"


def test_rotation(s, letter):
    index = s.index(letter)

    for _ in range(index + 1):
        s = rotate_right(s)

    if index >= 4:
        s = rotate_right(s)

    return s


for instruction in instructions:
    if "swap position" in instruction:
        instruction = instruction.replace(
            "swap position ", "").replace("with position ", "")
        pos_1, pos_2 = sorted([int(x) for x in instruction.split(" ")])
        string = f"{string[: pos_1]}{string[pos_2]}{string[pos_1 + 1: pos_2]}{string[pos_1]}{string[pos_2 + 1:]}"

    elif "swap letter" in instruction:
        instruction = instruction.replace(
            "swap letter ", "").replace("with letter ", "")
        pos_1, pos_2 = sorted([string.index(x)
                              for x in instruction.split(" ")])
        string = f"{string[: pos_1]}{string[pos_2]}{string[pos_1 + 1: pos_2]}{string[pos_1]}{string[pos_2 + 1:]}"

    elif "rotate based" in instruction:
        letter = instruction.replace("rotate based on position of letter ", "")
        index = string.index(letter)

        for _ in range(index + 1):
            string = rotate_right(string)

        if index >= 4:
            string = rotate_right(string)

    elif "reverse positions" in instruction:
        instruction = instruction.replace(
            "reverse positions ", "").replace("through ", "")
        pos_1, pos_2 = sorted([int(x) for x in instruction.split(" ")])
        string = f"{string[: pos_1]}{string[pos_1: pos_2 + 1][::-1]}{string[pos_2 + 1:]}"

    elif "move position" in instruction:
        instruction = instruction.replace(
            "move position ", "").replace("to position ", "")
        pos_1, pos_2 = [int(x) for x in instruction.split(" ")]

        if pos_1 > pos_2:
            string = f"{string[:pos_2]}{string[pos_1]}{string[pos_2: pos_1]}{string[pos_1 + 1:]}"
        else:
            string = f"{string[:pos_1]}{string[pos_1 + 1: pos_2 + 1]}{string[pos_1]}{string[pos_2 + 1:]}"

    elif "rotate" in instruction:
        if "left" in instruction:
            num_steps = int(instruction.replace(
                "rotate left ", "").replace(" step", "").replace("s", ""))
            for _ in range(num_steps):
                string = rotate_left(string)
        else:
            num_steps = int(instruction.replace(
                "rotate right ", "").replace(" step", "").replace("s", ""))
            for _ in range(num_steps):
                string = rotate_right(string)

print(f"Part 1 Answer: {string}")

string = STRING_P2
instructions.reverse()

for instruction in instructions:
    if "swap position" in instruction:
        instruction = instruction.replace(
            "swap position ", "").replace("with position ", "")
        pos_1, pos_2 = sorted([int(x) for x in instruction.split(" ")])
        string = f"{string[: pos_1]}{string[pos_2]}{string[pos_1 + 1: pos_2]}{string[pos_1]}{string[pos_2 + 1:]}"

    elif "swap letter" in instruction:
        instruction = instruction.replace(
            "swap letter ", "").replace("with letter ", "")
        pos_1, pos_2 = sorted([string.index(x)
                              for x in instruction.split(" ")])
        string = f"{string[: pos_1]}{string[pos_2]}{string[pos_1 + 1: pos_2]}{string[pos_1]}{string[pos_2 + 1:]}"

    elif "rotate based" in instruction:
        letter = instruction.replace("rotate based on position of letter ", "")
        temp = string

        while 1:
            temp = rotate_left(temp)
            test = test_rotation(temp, letter)
            if test == string:
                string = temp
                break

    elif "reverse positions" in instruction:
        instruction = instruction.replace(
            "reverse positions ", "").replace("through ", "")
        pos_1, pos_2 = sorted([int(x) for x in instruction.split(" ")])
        string = f"{string[: pos_1]}{string[pos_1: pos_2 + 1][::-1]}{string[pos_2 + 1:]}"

    elif "move position" in instruction:
        instruction = instruction.replace(
            "move position ", "").replace("to position ", "")
        pos_2, pos_1 = [int(x) for x in instruction.split(" ")]

        if pos_1 > pos_2:
            string = f"{string[:pos_2]}{string[pos_1]}{string[pos_2: pos_1]}{string[pos_1 + 1:]}"
        else:
            string = f"{string[:pos_1]}{string[pos_1 + 1: pos_2 + 1]}{string[pos_1]}{string[pos_2 + 1:]}"

    elif "rotate" in instruction:
        if "left" in instruction:
            num_steps = int(instruction.replace(
                "rotate left ", "").replace(" step", "").replace("s", ""))
            for _ in range(num_steps):
                string = rotate_right(string)
        else:
            num_steps = int(instruction.replace(
                "rotate right ", "").replace(" step", "").replace("s", ""))
            for _ in range(num_steps):
                string = rotate_left(string)

print(f"Part 2 Answer: {string}")
