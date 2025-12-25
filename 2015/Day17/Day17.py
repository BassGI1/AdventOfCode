from itertools import combinations

raw_input = open("./input.txt", "r").read()

target_liters = 150
bucket_sizes = [int(x) for x in raw_input.split("\n")]

num_valid_combs = 0

for i in range(2, len(bucket_sizes)):
    combs = list(combinations(bucket_sizes, i))
    for c in combs:
        if sum(c) == target_liters:
            num_valid_combs += 1

print(f"Part 1 Answer: {num_valid_combs}")


for i in range(2, len(bucket_sizes)):
    num_valid_combs = 0
    combs = list(combinations(bucket_sizes, i))
    for c in combs:
        if sum(c) == target_liters:
            num_valid_combs += 1
    
    if num_valid_combs != 0:
        print(f"Part 2 Answer: {num_valid_combs}")
        break