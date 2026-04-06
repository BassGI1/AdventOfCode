from sys import exit

raw_input = open("./input.txt", "r").read()

coords = [0, 0]
orientation = "^"
movements = raw_input.split(", ")

for movement in movements:
    direction = movement[0]
    magnitude = int(movement[1:])

    if orientation == "^":
        if direction == "R":
            coords[0] += magnitude
            orientation = ">"
        elif direction == "L":
            coords[0] -= magnitude
            orientation = "<"

    elif orientation == ">":
        if direction == "R":
            coords[1] -= magnitude
            orientation = "V"
        elif direction == "L":
            coords[1] += magnitude
            orientation = "^"

    elif orientation == "V":
        if direction == "R":
            coords[0] -= magnitude
            orientation = "<"
        elif direction == "L":
            coords[0] += magnitude
            orientation = ">"

    elif orientation == "<":
        if direction == "R":
            coords[1] += magnitude
            orientation = "^"
        elif direction == "L":
            coords[1] -= magnitude
            orientation = "V"

print(f"Part 1 Answer: {sum([abs(a) for a in coords])}")


coords = [0, 0]
orientation = "^"
visited = set((0, 0))

for movement in movements:
    direction = movement[0]
    magnitude = int(movement[1:])

    if orientation == "^":
        if direction == "R":
            for _ in range(magnitude):
                coords[0] += 1
                t = tuple(coords)
                if t in visited:
                    print(f"Part 2 Answer: {sum([abs(a) for a in coords])}")
                    exit(0)
                visited.add(t)
            orientation = ">"
            
        elif direction == "L":
            for _ in range(magnitude):
                coords[0] -= 1
                t = tuple(coords)
                if t in visited:
                    print(f"Part 2 Answer: {sum([abs(a) for a in coords])}")
                    exit(0)
                visited.add(t)
            orientation = "<"

    elif orientation == ">":
        if direction == "R":
            for _ in range(magnitude):
                coords[1] -= 1
                t = tuple(coords)
                if t in visited:
                    print(f"Part 2 Answer: {sum([abs(a) for a in coords])}")
                    exit(0)
                visited.add(t)
            orientation = "V"
            
        elif direction == "L":
            for _ in range(magnitude):
                coords[1] += 1
                t = tuple(coords)
                if t in visited:
                    print(f"Part 2 Answer: {sum([abs(a) for a in coords])}")
                    exit(0)
                visited.add(t)
            orientation = "^"

    elif orientation == "V":
        if direction == "R":
            for _ in range(magnitude):
                coords[0] -= 1
                t = tuple(coords)
                if t in visited:
                    print(f"Part 2 Answer: {sum([abs(a) for a in coords])}")
                    exit(0)
                visited.add(t)
            orientation = "<"
            
        elif direction == "L":
            for _ in range(magnitude):
                coords[0] += 1
                t = tuple(coords)
                if t in visited:
                    print(f"Part 2 Answer: {sum([abs(a) for a in coords])}")
                    exit(0)
                visited.add(t)
            orientation = ">"

    elif orientation == "<":
        if direction == "R":
            for _ in range(magnitude):
                coords[1] += 1
                t = tuple(coords)
                if t in visited:
                    print(f"Part 2 Answer: {sum([abs(a) for a in coords])}")
                    exit(0)
                visited.add(t)
            orientation = "^"
            
        elif direction == "L":
            for _ in range(magnitude):
                coords[1] -= 1
                t = tuple(coords)
                if t in visited:
                    print(f"Part 2 Answer: {sum([abs(a) for a in coords])}")
                    exit(0)
                visited.add(t)
            orientation = "V"

print(f"Part 2 Answer: {sum([abs(a) for a in coords])}")
