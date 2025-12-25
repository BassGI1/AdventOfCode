from re import findall

raw_input = open("./input.txt", "r+").read()

width = 101
height = 103
num_seconds = 10000

grid = [[0]*width for _ in range(height)]

def format_grid():
	return "\n".join(["".join(["." if x == 0 else str(x) for x in a.copy()]) for a in grid])

robots = []
for line in raw_input.split("\n"):
	postion, velocity = findall(r"-?[0-9]+,-?[0-9]+", line)
	p_x, p_y = [int(n) for n in postion.split(",")]
	v_x, v_y = [int(n) for n in velocity.split(",")]
	robots.append([(p_x, p_y), (v_x, v_y)])
	grid[p_y][p_x] += 1

for s in range(num_seconds):
	for i in range(len(robots)):
		[p_x, p_y], [v_x, v_y] = robots[i]
		grid[p_y][p_x] -= 1
		new_position = ((p_x + v_x) % width, (p_y + v_y) % height)
		grid[new_position[1]][new_position[0]] += 1
		robots[i][0] = new_position
	
	# Part 2, this is a terrible question
# 	g = format_grid()
# 	if not len(findall(r"[2-9]+", g)): print(f"""Second: {s + 1}
# {g}""")

# Part 1
# middle_width_index = width // 2
# middle_height_index = height // 2

# quadrants = [0, 0, 0, 0]
# for y in range(height):
# 	for x in range(width):
# 		if y < middle_height_index:
# 			if x < middle_width_index: quadrants[1] += grid[y][x]
# 			elif x > middle_width_index: quadrants[0] += grid[y][x]
# 		elif y > middle_height_index:
# 			if x < middle_width_index: quadrants[2] += grid[y][x]
# 			elif x > middle_width_index: quadrants[3] += grid[y][x]

# total = quadrants[0]
# for i in range(1, len(quadrants)): total *= quadrants[i]

# print(total)