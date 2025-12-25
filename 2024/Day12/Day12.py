raw_input = open("./input.txt", "r+").read()

grid = [f".{r}." for r in raw_input.split("\n")]
grid = ["."*len(grid[0]), *grid, "."*len(grid[0])]

def recurse(symbol, y, x, seen, region):
	region.add((y, x))
	seen.add((y, x))
	if grid[y - 1][x] == symbol and (y - 1, x) not in seen: recurse(symbol, y - 1, x, seen, region)
	if grid[y + 1][x] == symbol and (y + 1, x) not in seen: recurse(symbol, y + 1, x, seen, region)
	if grid[y][x - 1] == symbol and (y, x - 1) not in seen: recurse(symbol, y, x - 1, seen, region)
	if grid[y][x + 1] == symbol and (y, x + 1) not in seen: recurse(symbol, y, x + 1, seen, region)

seen = set()
all_regions = []
for y in range(1, len(grid) - 1):
	for x in range(1, len(grid[0]) - 1):
		if (y, x) not in seen:
			region = set()
			recurse(grid[y][x], y, x, seen, region)
			all_regions.append((grid[y][x], region))

# Part 1
# total = 0

# for symbol, region in all_regions:
# 	area = len(region)
# 	perimeter = 0
# 	for y, x in region:
# 		if grid[y - 1][x] != symbol: perimeter += 1
# 		if grid[y + 1][x] != symbol: perimeter += 1
# 		if grid[y][x - 1] != symbol: perimeter += 1
# 		if grid[y][x + 1] != symbol: perimeter += 1
# 	total += area*perimeter

# print(total)

# Part 2
# total = 0
# for i in range(len(all_regions)):
# 	symbol, region = all_regions[i]
# 	outer_points = set()
# 	for y, x in region:
# 		if (y - 1, x) not in region or (y + 1, x) not in region or (y, x - 1) not in region or (y, x + 1) not in region: outer_points.add((y, x))
# 	all_regions[i] = (symbol, outer_points, region)

# for symbol, outer_points, region in all_regions:
# 	min_y = min(outer_points, key=lambda x: x[0])[0]
# 	min_x = min(outer_points, key=lambda x: x[1])[1]
# 	max_y = max(outer_points, key=lambda x: x[0])[0]
# 	max_x = max(outer_points, key=lambda x: x[1])[1]

# 	num_sides = 0
# 	y, x = min_y, min_x

# 	while y <= max_y:
# 		still_going = False
# 		sides = 0
# 		while x <= max_x:
# 			if grid[y - 1][x] != symbol and not still_going and (y, x) in region:
# 				still_going = True
# 				sides += 1
# 			elif grid[y - 1][x] == symbol or grid[y][x] != symbol:
# 				still_going = False
# 			x += 1
# 		x = min_x
# 		y += 1
# 		num_sides += sides

# 	y, x = min_y, min_x

# 	while y <= max_y:
# 		still_going = False
# 		sides = 0
# 		while x <= max_x:
# 			if grid[y + 1][x] != symbol and not still_going and (y, x) in region:
# 				still_going = True
# 				sides += 1
# 			elif grid[y + 1][x] == symbol or grid[y][x] != symbol:
# 				still_going = False
# 			x += 1
# 		x = min_x
# 		y += 1
# 		num_sides += sides

# 	y, x = min_y, min_x

# 	while x <= max_x:
# 		still_going = False
# 		sides = 0
# 		while y <= max_y:
# 			if grid[y][x - 1] != symbol and not still_going and (y, x) in region:
# 				still_going = True
# 				sides += 1
# 			elif grid[y][x - 1] == symbol or grid[y][x] != symbol:
# 				still_going = False
# 			y += 1
# 		y = min_y
# 		x += 1
# 		num_sides += sides

# 	y, x = min_y, min_x

# 	while x <= max_x:
# 		still_going = False
# 		sides = 0
# 		while y <= max_y:
# 			if grid[y][x + 1] != symbol and not still_going and (y, x) in region:
# 				still_going = True
# 				sides += 1
# 			elif grid[y][x + 1] == symbol or grid[y][x] != symbol:
# 				still_going = False
# 			y += 1
# 		y = min_y
# 		x += 1
# 		num_sides += sides

# 	total += num_sides*len(region)

# print(total)
