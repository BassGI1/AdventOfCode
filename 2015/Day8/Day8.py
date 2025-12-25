raw_input = open("./input.txt", "r").read()

total_chars = 0
total_mem_chars = 0
lines = raw_input.split("\n")

for line in lines:
    i = 1
    total_mem_chars += len(line)
    while i < len(line) - 1:
        if line[i] == "\\":
            if line[i + 1] == "\\" or line[i + 1] == "\"":
                i += 1
            else:
                i += 3

        i += 1
        total_chars += 1

print(f"Part 1 Answer: {total_mem_chars - total_chars}")


def encode_line(line):
    return f'"{line.replace('\\', "\\\\").replace('"', '\\"')}"'


total_encoded_chars = 0

for line in lines:
    total_encoded_chars += len(encode_line(line))

print(f"Part 2 Answer: {total_encoded_chars - total_mem_chars}")
