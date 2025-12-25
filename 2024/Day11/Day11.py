raw_input = open("./input.txt", "r+").read()

num_blinks = 75

# Part 1
# stones = [s for s in raw_input.split(" ")]

# for i in range(num_blinks):
#     next_iteration = []
#     for stone in stones:
#         if stone == "0": next_iteration.append("1")
#         elif not (len(stone) % 2):
#             mid = int(len(stone) / 2)
#             left = stone[: mid]
#             right = str(int(stone[mid:]))
#             next_iteration.append(left)
#             next_iteration.append(right)
#         else: next_iteration.append(str(int(stone) * 2024))
#     stones = next_iteration
#     print(f"{len(stones)} {len(set(stones))}") # number of unique stone numbers converges to ~55 for some reason?

# print(len(stones))

# Part 2
# num_map = {}
# stones = { s: 1 for s in raw_input.split(" ") }

# for i in range(num_blinks):
# 	num_frequency = {}
# 	next_iteration = {}
# 	for stone, _ in stones.items():
# 		if stone not in num_frequency and stone not in num_map:
# 			num_frequency[stone] = 1
# 			num_map[stone] = []
# 			if stone == "0": num_map[stone].append("1")
# 			elif not (len(stone) % 2):
# 				mid = int(len(stone) / 2)
# 				left = stone[: mid]
# 				right = str(int(stone[mid:]))
# 				num_map[stone].append(left)
# 				num_map[stone].append(right)
# 			else: num_map[stone].append(str(int(stone) * 2024))

# 		elif stone not in num_frequency: num_frequency[stone] = 1
# 		else: num_frequency[stone] += 1

# 	for stone, freq in stones.items():
# 		for s in num_map[stone]:
# 			if s not in next_iteration: next_iteration[s] = freq*num_frequency[stone]
# 			else: next_iteration[s] += freq*num_frequency[stone]

# 	stones = next_iteration

# total = 0
# for _, v in stones.items(): total += v

# print(total)