raw_input = open("./input.txt", "r").read()
instructions = raw_input.split("\n")

registers = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0
}


def parseIntOrReg(val):
    try:
        return int(val)
    except:
        return val


instruction_pointer = 0
while instruction_pointer < len(instructions):
    tokens = instructions[instruction_pointer].split(" ")

    if len(tokens) == 3:
        if tokens[0] == "cpy":
            val1 = parseIntOrReg(tokens[1])
            val1 = val1 if type(val1) == int else registers[str(val1)]
            registers[tokens[2]] = val1

        elif tokens[0] == "jnz":
            val1 = parseIntOrReg(tokens[1])
            val1 = val1 if type(val1) == int else registers[str(val1)]
            if val1 != 0:
                instruction_pointer += int(parseIntOrReg(tokens[2]))
                continue

    elif len(tokens) == 2:
        if tokens[0] == "inc":
            registers[tokens[1]] += 1
        elif tokens[0] == "dec":
            registers[tokens[1]] -= 1

    instruction_pointer += 1

print(f"Part 1 Answer: {registers["a"]}")


registers = {
    "a": 0,
    "b": 0,
    "c": 1,
    "d": 0
}


instruction_pointer = 0
while instruction_pointer < len(instructions):
    tokens = instructions[instruction_pointer].split(" ")

    if len(tokens) == 3:
        if tokens[0] == "cpy":
            val1 = parseIntOrReg(tokens[1])
            val1 = val1 if type(val1) == int else registers[str(val1)]
            registers[tokens[2]] = val1

        elif tokens[0] == "jnz":
            val1 = parseIntOrReg(tokens[1])
            val1 = val1 if type(val1) == int else registers[str(val1)]
            if val1 != 0:
                instruction_pointer += int(parseIntOrReg(tokens[2]))
                continue

    elif len(tokens) == 2:
        if tokens[0] == "inc":
            registers[tokens[1]] += 1
        elif tokens[0] == "dec":
            registers[tokens[1]] -= 1

    instruction_pointer += 1
    
    
print(f"Part 2 Answer: {registers["a"]}")