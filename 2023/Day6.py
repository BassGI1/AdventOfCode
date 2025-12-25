puzz = """Time:        40     82     84     92
Distance:   233   1011   1110   1487""".split("\n")

time = int("".join([t for t in puzz[0][puzz[0].index(":") + 1:].split(" ") if len(t) > 0]))
distance = int("".join([d for d in puzz[1][puzz[1].index(":") + 1:].split(" ") if len(d) > 0]))

total = 1
holding = time // 2
while holding*(time - holding) > distance:
	holding -= 1000
	total += 2*1000

holding += 1000

while holding*(time - holding) > distance:
	holding -= 1
	total += 2

total -= 2002

print(total)

# total = 1

# for i in range(len(distances)):
# 	s = 1
# 	holding = times[i] // 2
# 	while holding*(times[i] - holding) > distances[i]:
# 		holding -= 1
# 		s += 2
# 	total *= s - 2

# print(total)