from re import findall

raw_input = open("./input.txt", "r").read()

sectors_sum = 0
code_lines = raw_input.split("\n")
for line in code_lines:
    checksum_index = line.index("[")
    line_checksum = line[checksum_index + 1: -1]
    room = line[:checksum_index]

    num = [int(x) for x in findall(r"[0-9]+", room)][0]
    room = room[:room.index(str(num))].replace("-", "")

    counter = {}
    for char in room:
        if char not in counter:
            counter[char] = 1
        else:
            counter[char] += 1

    checksum = ""
    sorted_counter = sorted(list(counter.items()),
                            key=lambda x: (x[1], -ord(x[0])), reverse=True)
    for i in range(5):
        checksum = f"{checksum}{sorted_counter[i][0]}"

    if checksum == line_checksum:
        sectors_sum += num

print(f"Part 1 Answer: {sectors_sum}")

cipher_text = "abcdefghijklmnopqrstuvwxyz"

for line in code_lines:
    checksum_index = line.index("[")
    line_checksum = line[checksum_index + 1: -1]
    room = line[:checksum_index]

    num = [int(x) for x in findall(r"[0-9]+", room)][0]
    encrypted_text = room[:room.index(str(num))].replace("-", "")

    unencrypted_text = ""
    for char in encrypted_text:
        unencrypted_text = f"{unencrypted_text}{cipher_text[(cipher_text.index(char) + num) % len(cipher_text)]}"
        
    if unencrypted_text == "northpoleobjectstorage":
        print(f"Part 2 Answer: {num}")
        break