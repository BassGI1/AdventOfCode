raw_input = open("./input.txt", "r").read()

instructions = raw_input.split("\n")


def run_program(reg_a, reg_b, instruction_pointer):
    while instruction_pointer < len(instructions):
        instruction = instructions[instruction_pointer]
        inst, rem = instruction.split(" ", 1)

        if inst == "hlf":
            if rem == "a":
                reg_a = int(reg_a // 2)
            else:
                reg_b = int(reg_b // 2)
            instruction_pointer += 1

        elif inst == "tpl":
            if rem == "a":
                reg_a = reg_a * 3
            else:
                reg_b = reg_b * 3
            instruction_pointer += 1

        elif inst == "inc":
            if rem == "a":
                reg_a = reg_a + 1
            else:
                reg_b = reg_b + 1
            instruction_pointer += 1

        elif inst == "jmp":
            instruction_pointer = instruction_pointer + int(rem)

        elif inst == "jie":
            r, off = rem.split(", ")
            if r == "a":
                if reg_a % 2 == 0:
                    instruction_pointer = instruction_pointer + int(off)
                else:
                    instruction_pointer += 1
            elif r == "b":
                if reg_b % 2 == 0:
                    instruction_pointer = instruction_pointer + int(off)
                else:
                    instruction_pointer += 1

        elif inst == "jio":
            r, off = rem.split(", ")
            if r == "a":
                if reg_a == 1:
                    instruction_pointer = instruction_pointer + int(off)
                else:
                    instruction_pointer += 1
            elif r == "b":
                if reg_b == 1:
                    instruction_pointer = instruction_pointer + int(off)
                else:
                    instruction_pointer += 1

    return reg_b


print(f"Part 1 Answer: {run_program(0, 0, 0)}")
print(f"Part 2 Answer: {run_program(1, 0, 0)}")
