raw_input = open("./input.txt", "r").read()

lines = raw_input.split("\n")

total_p1, total_p2 = 0, 0
for line in lines:
    lengths = sorted([int(x) for x in line.split("x")])
    l1, l2, l3 = lengths[0]*lengths[1], lengths[1] * \
        lengths[2], lengths[0]*lengths[2]

    total_p1 += 2*(l1 + l2 + l3) + l1
    total_p2 += 2*(lengths[0] + lengths[1]) + (lengths[0]*lengths[1]*lengths[2])

print(f"Part 1 Answer: {total_p1}")
print(f"Part 2 Answer: {total_p2}")
