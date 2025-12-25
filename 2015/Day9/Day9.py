raw_input = open("./input.txt", "r").read()

steps = {}
lines = raw_input.split("\n")

for line in lines:
    places, distance = line.split(" = ")
    distance = int(distance)
    p1, p2 = places.split(" to ")
    
    if p1 not in steps:
        steps[p1] = [(p2, distance)]
    else:
        steps[p1].append((p2, distance))
        
    if p2 not in steps:
        steps[p2] = [(p1, distance)]
    else:
        steps[p2].append((p1, distance))
        
longest_path = [0]
shortest_path = [float("inf")]
num_stops = len(steps.keys())

def check_paths(current_loc, distance_covered, current_path, shortest, longest):
    if len(current_path) == num_stops:
        shortest[0] = min(shortest[0], distance_covered)
        longest[0] = max(longest[0], distance_covered)
        return
    
    for stop, distance in steps[current_loc]:
        if stop not in current_path:
            p = current_path.copy()
            p.add(stop)
            check_paths(stop, distance_covered + distance, p, shortest, longest)


for stop in steps.keys():
    check_paths(stop, 0, {stop}, shortest_path, longest_path)
    
print(f"Part 1 Answer: {shortest_path[0]}")
print(f"Part 2 Answer: {longest_path[0]}")