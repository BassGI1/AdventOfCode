from pprint import pprint

raw_input = open("./input.txt", "r").read()

NUM_ROWS_PART_1 = 40
NUM_ROWS_PART_2 = 400000

rows = [[a == "^" for a in list(raw_input)]]


def is_safe(left, middle, right):
    return (left and middle and not right) or (not left and middle and right) or (left and not middle and not right) or (not left and not middle and right)


def print_rows(r):
    rs = []
    for row in r:
        rs.append("".join(["^" if t is True else "." for t in row]))

    print("\n".join(rs))


for _ in range(NUM_ROWS_PART_1 - 1):
    rows.append([is_safe(False, rows[-1][0], rows[-1][1])])

    for i in range(1, len(rows[0]) - 1):
        rows[-1].append(is_safe(rows[-2][i - 1], rows[-2]
                        [i - 1], rows[-2][i + 1]))

    rows[-1].append(is_safe(rows[-2][-2], rows[-2][-1], False))

num_safe = 0
for row in rows:
    for tile in row:
        if tile is False:
            num_safe += 1

print(f"Part 1 Answer: {num_safe}")

rows = [[a == "^" for a in list(raw_input)]]

for _ in range(NUM_ROWS_PART_2 - 1):
    rows.append([is_safe(False, rows[-1][0], rows[-1][1])])

    for i in range(1, len(rows[0]) - 1):
        rows[-1].append(is_safe(rows[-2][i - 1], rows[-2]
                        [i - 1], rows[-2][i + 1]))

    rows[-1].append(is_safe(rows[-2][-2], rows[-2][-1], False))

num_safe = 0
for row in rows:
    for tile in row:
        if tile is False:
            num_safe += 1

print(f"Part 2 Answer: {num_safe}")