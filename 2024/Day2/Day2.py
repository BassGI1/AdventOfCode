lines = open("./input.txt", "r+").read().split("\n")

# Part 1
# num_safe = 0

# for line in lines:
# 	report = [int(num) for num in line.split(" ")]
# 	safe = True

# 	for i in range(1, len(report)):
# 		curr = report[i]
# 		prev = report[i - 1]
# 		difference = abs(curr - prev)
# 		if ((curr > prev) != (report[1] > report[0])) or (difference > 3) or (difference < 1):
# 			safe = False
# 			break

# 	if safe: num_safe += 1


# Part 2
# num_safe = 0

# for line in lines:
# 	report = [int(num) for num in line.split(" ")]
# 	safe = True

# 	for i in range(len(report)):
# 		modified_report = report.copy()
# 		modified_report.pop(i)
# 		safe = True

# 		print(modified_report)

# 		for j in range(1, len(modified_report)):
# 			curr = modified_report[j]
# 			prev = modified_report[j - 1]
# 			difference = abs(curr - prev)
# 			if ((curr > prev) != (modified_report[1] > modified_report[0])) or (difference > 3) or (difference < 1):
# 				safe = False
# 				break
		
# 		if safe:
# 			num_safe += 1
# 			break

# print(num_safe)
