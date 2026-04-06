raw_input = open("./input.txt", "r").read()

word_most_common = ""
word_least_common = ""
rows = raw_input.split("\n")

for x in range(len(rows[0])):
    counter = {}
    for y in range(len(rows)):
        if rows[y][x] in counter:
            counter[rows[y][x]] += 1
        else:
            counter[rows[y][x]] = 1

    word_most_common = f"{word_most_common}{sorted(list(counter.items()), key=lambda x: x[1], reverse=True)[0][0]}"
    word_least_common = f"{word_least_common}{sorted(list(counter.items()), key=lambda x: x[1])[0][0]}"

print(f"Part 1 Answer: {word_most_common}")
print(f"Part 2 Answer: {word_least_common}")
