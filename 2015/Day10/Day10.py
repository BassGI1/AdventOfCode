raw_input = open("./input.txt", "r").read()


def encode_num(num):
    i = 1
    encoded = ""
    curr_start_index = 0

    while i < len(num):
        if num[i] != num[curr_start_index]:
            encoded = f"{encoded}{i - curr_start_index}{num[curr_start_index]}"
            curr_start_index = i
        i += 1

    encoded = f"{encoded}{i - curr_start_index}{num[curr_start_index]}"

    return encoded


digits = raw_input
for _ in range(40):
    digits = encode_num(digits)
    
print(f"Part 1 Answer: {len(digits)}")

# This trash code takes like 45 mins for finish
for _ in range(10):
    digits = encode_num(digits)
    
print(f"Part 2 Answer: {len(digits)}")