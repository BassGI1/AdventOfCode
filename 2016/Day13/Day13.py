from heapq import heappop, heappush

raw_input = open("./input.txt", "r").read()

FAVOURITE_NUM = int(raw_input)
TARGET_COORDS = (31, 39)


def isWall(x, y):
    temp = x*x + 3*x + 2*x*y + y + y*y + FAVOURITE_NUM
    num_set_bits = 0
    while temp > 0:
        num_set_bits += temp & 1
        temp = temp >> 1

    return bool(num_set_bits % 2)


def distanceFromTarget(x, y):
    return ((x - TARGET_COORDS[0])**2 + (y - TARGET_COORDS[1])**2)**0.5


seen = {(1, 1)}

priority_queue = []
heappush(priority_queue, (-distanceFromTarget(1, 1), (1, 1, 0)))


def step(x, y, num_steps):
    if (x, y) not in seen:
        heappush(priority_queue, (-distanceFromTarget(x, y), (x, y, num_steps)))


while len(priority_queue):
    x, y, num_steps = heappop(priority_queue)[1]
    seen.add((x, y))

    if (x, y) == TARGET_COORDS:
        print(f"Part 1 Answer: {num_steps}")
        break

    if isWall(x, y):
        continue

    if x > 0:
        step(x - 1, y, num_steps + 1)
    step(x + 1, y, num_steps + 1)

    if y > 0:
        step(x, y - 1, num_steps + 1)
    step(x, y + 1, num_steps + 1)


TARGET_COORDS = (100_000, 100_000)

seen = {(1, 1)}
reached = {(1, 1)}

priority_queue = []
heappush(priority_queue, (-distanceFromTarget(1, 1), (1, 1, 0)))

while len(priority_queue):
    x, y, num_steps = heappop(priority_queue)[1]
    seen.add((x, y))

    if isWall(x, y):
        continue

    reached.add((x, y))

    if num_steps == 50:
        continue

    if x > 0:
        step(x - 1, y, num_steps + 1)
    step(x + 1, y, num_steps + 1)

    if y > 0:
        step(x, y - 1, num_steps + 1)
    step(x, y + 1, num_steps + 1)


print(f"Part 2 Answer: {len(reached)}")