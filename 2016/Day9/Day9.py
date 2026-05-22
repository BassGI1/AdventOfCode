from re import findall
from pprint import pprint

NUMBER_PATTERN = r"[0-9]+"
MARKER_PATTERN = r"\([0-9]+x[0-9]+\)"

raw_input = open("./input.txt", "r").read()
file = raw_input

fp = 0
while fp < len(file):
    if file[fp] == "(":
        closing_bracket_index = file.index(")", fp)
        brackets_string = file[fp: closing_bracket_index + 1]
        num_chars, num_repeat = [int(x) for x in findall(
            NUMBER_PATTERN, brackets_string)]

        file = file.replace(
            brackets_string, file[closing_bracket_index + 1: closing_bracket_index + num_chars + 1]*(num_repeat - 1), 1)
        fp += num_chars*num_repeat
        continue

    fp += 1


print(f"Part 1 Answer: {len(file)}")

cache = {}
file_length = 0
blocks = [(raw_input, 1)]

while len(blocks):
    block, num_iters = blocks.pop(0)

    if block in cache:
        file_length += cache[block]*num_iters
        continue

    if len([x for x in findall(MARKER_PATTERN, block)]) == 0:
        file_length += len(block)*num_iters
        cache[block] = len(block)
        continue

    fp = 0
    while fp < len(block):
        if block[fp] == "(":
            closing_bracket_index = block.index(")", fp)
            num_chars, num_repeat = [int(x) for x in findall(
                NUMBER_PATTERN, block[fp: closing_bracket_index + 1])]

            new_block = block[closing_bracket_index +
                              1: closing_bracket_index + num_chars + 1]
            block = block.replace(
                block[fp: closing_bracket_index + 1] + new_block, "", 1)
            blocks.append((new_block, num_iters*num_repeat))
            continue

        fp += 1

    file_length += num_iters*len(block)

print(f"Part 2 Answer: {file_length}")
