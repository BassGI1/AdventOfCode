# Terrible code, runs in 90 mins

raw_input = open("./input.txt", "r").read()


NUM_ELVES = int(raw_input)


def get_left_elf(e, c):
    return (c + 1) % len(e)


def get_opposite_elf(e, c):
    return int(c + (len(e) // 2)) % len(e)


curr_elf_index = 0
elves = [[i, 1] for i in range(NUM_ELVES)]

while len(elves) > 1:
    num, num_presents = elves[curr_elf_index]
    if num_presents == 0:
        elves.pop(curr_elf_index)

    else:
        next_elf = get_left_elf(elves, curr_elf_index)
        elves[curr_elf_index][1] += elves[next_elf][1]
        elves[next_elf][1] = 0
        curr_elf_index += 1

    curr_elf_index = curr_elf_index % len(elves)

print(f"Part 1 Answer: {elves[0][0] + 1}")

curr_elf_index = 0
elves = [[i, 1] for i in range(NUM_ELVES)]

while len(elves) > 1:
    num, num_presents = elves[curr_elf_index]
    opposite_elf = get_opposite_elf(elves, curr_elf_index)
    elves.pop(opposite_elf)

    if opposite_elf > curr_elf_index:
        curr_elf_index += 1

    curr_elf_index = curr_elf_index % len(elves)


print(f"Part 2 Answer: {elves[0][0] + 1}")
