raw_input = open("./input.txt", "r+").read()

grid, moves = raw_input.split("\n\n")

# Part 1
# grid = [[c for c in a] for a in grid.split("\n")]
# moves = [c for c in moves]

# postion = None
# for y in range(len(grid)):
# 	stop = False
# 	for x in range(len(grid[0])):
# 		if grid[y][x] == "@":
# 			postion = [y, x]
# 			stop = True
# 			break
# 	if stop: break

# for move in moves:
# 	if move == "<":
# 		y, x = postion
# 		if grid[y][x - 1] != "O" and grid[y][x - 1] == ".":
# 			grid[y][x - 1] = "@"
# 			grid[y][x] = "."
# 			postion[1] -= 1
# 		elif grid[y][x - 1] == "O":
# 			x -= 1
# 			while grid[y][x] == "O": x -= 1
# 			if grid[y][x] == ".":
# 				grid[y][x] = "O"
# 				grid[y][postion[1]] = "."
# 				grid[y][postion[1] - 1] = "@"
# 				postion[1] -= 1

# 	if move == ">":
# 		y, x = postion
# 		if grid[y][x + 1] != "O" and grid[y][x + 1] == ".":
# 			grid[y][x + 1] = "@"
# 			grid[y][x] = "."
# 			postion[1] += 1
# 		elif grid[y][x + 1] == "O":
# 			x += 1
# 			while grid[y][x] == "O": x += 1
# 			if grid[y][x] == ".":
# 				grid[y][x] = "O"
# 				grid[y][postion[1]] = "."
# 				grid[y][postion[1] + 1] = "@"
# 				postion[1] += 1
	
# 	if move == "^":
# 		y, x = postion
# 		if grid[y - 1][x] != "O" and grid[y - 1][x] == ".":
# 			grid[y - 1][x] = "@"
# 			grid[y][x] = "."
# 			postion[0] -= 1
# 		elif grid[y - 1][x] == "O":
# 			y -= 1
# 			while grid[y][x] == "O": y -= 1
# 			if grid[y][x] == ".":
# 				grid[y][x] = "O"
# 				grid[postion[0]][x] = "."
# 				grid[postion[0] - 1][x] = "@"
# 				postion[0] -= 1

# 	if move == "v":
# 		y, x = postion
# 		if grid[y + 1][x] != "O" and grid[y + 1][x] == ".":
# 			grid[y + 1][x] = "@"
# 			grid[y][x] = "."
# 			postion[0] += 1
# 		elif grid[y + 1][x] == "O":
# 			y += 1
# 			while grid[y][x] == "O": y += 1
# 			if grid[y][x] == ".":
# 				grid[y][x] = "O"
# 				grid[postion[0]][x] = "."
# 				grid[postion[0] + 1][x] = "@"
# 				postion[0] += 1

# total = 0
# for y in range(len(grid)):
# 	for x in range(len(grid[0])):
# 		if grid[y][x] == "O": total += 100*y + x

# print(total)

# Part 2
grid = [
	[
		x for x in a
		.replace("#", "##")
		.replace("O", "[]")
		.replace(".", "..")
		.replace("@", "@.")
	] 
	for a in grid.split("\n")
]
moves = [c for c in moves]

position = None
for y in range(len(grid)):
	stop = False
	for x in range(len(grid[0])):
		if grid[y][x] == "@":
			position = (y, x)
			stop = True
			break
	if stop: break

print(position)