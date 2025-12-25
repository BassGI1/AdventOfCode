raw_input = open("./input.txt", "r+").read()

top_map = []
for y in raw_input.split("\n"): top_map.append([int(height) if height != "." else -1 for height in y])

max_y = len(top_map) - 1
max_x = len(top_map[0]) - 1

starting_points = set()
for y in range(len(top_map)):
    for x in range(len(top_map[y])):
        if top_map[y][x] == 0: starting_points.add((0, y, x))

# Part 1      
# def recurse(point, seen, ending_points):
#     seen.add(point)
#     height, y, x = point
#     if height == 9: ending_points.add(point)
#     if y > 0 and top_map[y - 1][x] == height + 1:
#         recurse((height + 1, y - 1, x), seen, ending_points)
#     if y < max_y and top_map[y + 1][x] == height + 1:
#         recurse((height + 1, y + 1, x), seen, ending_points)
#     if x > 0 and top_map[y][x - 1] == height + 1:
#         recurse((height + 1, y, x - 1), seen, ending_points)
#     if x < max_x and top_map[y][x + 1] == height + 1:
#         recurse((height + 1, y, x + 1), seen, ending_points)
    
        
# def main():
#     total = 0
#     for point in starting_points:
#         seen = set()
#         ending_points = set()
#         recurse(point, seen, ending_points)
#         total += len(ending_points)
#     print(total)

# Part 2
# def recurse(point, total):
#     height, y, x = point
#     if height == 9: total[0] += 1
#     if y > 0 and top_map[y - 1][x] == height + 1:
#         recurse((height + 1, y - 1, x), total)
#     if y < max_y and top_map[y + 1][x] == height + 1:
#         recurse((height + 1, y + 1, x), total)
#     if x > 0 and top_map[y][x - 1] == height + 1:
#         recurse((height + 1, y, x - 1), total)
#     if x < max_x and top_map[y][x + 1] == height + 1:
#         recurse((height + 1, y, x + 1), total)
        

# def main():
#     total = [0]
#     for point in starting_points:
#         recurse(point, total)
#     print(total[0])
    
    
# if __name__ == "__main__": main()