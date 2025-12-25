lines = open("input.txt", "r+").read()

left = []
right = []

for line in lines.split("\n"):
	splitted = line.split("   ")
	left.append(int(splitted[0]))
	right.append(int(splitted[1]))

# Part 1
# left.sort()
# right.sort()

# distance = 0
# for i in range(len(left)):
# 	distance += abs(left[i] - right[i])

# print(distance)

# Part 2
# leftMap = {}
# rightMap = {}

# for i in left:
# 	if i in leftMap: leftMap[i] += 1
# 	else: leftMap[i] = 1

# for i in right:
# 	if i in rightMap: rightMap[i] += 1
# 	else: rightMap[i] = 1

# similarity = 0

# for num in left:
# 	if num in rightMap:
# 		similarity += rightMap[num]*num

# print(similarity)