from re import findall

raw_input = open("./input.txt", "r+").read()

machines = raw_input.split("\n\n")

# Part 1
# def optimize(x, y, target_x, target_y, da_x, da_y, db_x, db_y, cost, num_a, num_b, combination_set):
# 	if (num_a, num_b) in combination_set: return None
# 	combination_set.add((num_a, num_b))
# 	if x == target_x and y == target_y: return cost
# 	elif x >= target_x or y >= target_y or num_b > 100 or num_a > 100: return None
# 	a = optimize(x + da_x, y + da_y, target_x, target_y, da_x, da_y, db_x, db_y, cost + 3, num_a + 1, num_b, combination_set)
# 	b = optimize(x + db_x, y + db_y, target_x, target_y, da_x, da_y, db_x, db_y, cost + 1, num_a, num_b + 1, combination_set)
# 	if a != None and b != None: return min(a, b)
# 	elif a: return a
# 	elif b: return b

# total = 0

# for machine in machines:
# 	button_a_line, button_b_line, prize_line = machine.split("\n")
# 	a_x, a_y = [int(a) for a in findall(r"[0-9]+", button_a_line)]
# 	b_x, b_y = [int(a) for a in findall(r"[0-9]+", button_b_line)]
# 	p_x, p_y = [int(a) for a in findall(r"[0-9]+", prize_line)]
# 	cost = optimize(0, 0, p_x, p_y, a_x, a_y, b_x, b_y, 0, 0, 0, set())
# 	if cost != None: total += cost

# print(total)

# Part 2 Why didnt i just do this from the beginning? am i stupid?
# total = 0

# for machine in machines:
# 	button_a_line, button_b_line, prize_line = machine.split("\n")
# 	a_x, a_y = [int(a) for a in findall(r"[0-9]+", button_a_line)]
# 	b_x, b_y = [int(a) for a in findall(r"[0-9]+", button_b_line)]
# 	p_x, p_y = [int(a) for a in findall(r"[0-9]+", prize_line)]

# 	p_x += 10000000000000
# 	p_y += 10000000000000

# 	a = (p_y*b_x - p_x*b_y) / (a_y*b_x - a_x*b_y)
# 	b = (p_x - a_x*a) / b_x

# 	a = None if (a // 1) < a else int(a)
# 	b = None if (b // 1) < b else int(b)

# 	if a and b: total += a*3 + b

# print(total)