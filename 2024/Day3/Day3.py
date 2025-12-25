from re import findall

string = open("./input.txt", "r+").read()

# Part 1
# valid_instructions = [s for s in findall(r"mul\(\d{1,3},\d{1,3}\)", string)]

# total = 0

# for i in valid_instructions:
# 	numbers = [int(n) for n in findall(r"\d{1,3}", i)]
# 	total += numbers[0] * numbers[1]

# print(total)

# Part 2
# valid_instructions = [s for s in findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", string)]

# total = 0
# add = True
# for instruction in valid_instructions:
# 	if instruction == "do()": add = True
# 	elif instruction == "don't()": add = False
# 	elif add:
# 		numbers = [int(n) for n in findall(r"\d{1,3}", instruction)]
# 		total += numbers[0] * numbers[1]

# print(total)