from hashlib import md5
from heapq import heappop, heappush

raw_input = open("./input.txt", "r").read()

PASSCODE = raw_input
OPEN_DOOR_CHARACTERS = {"b", "c", "d", "e", "f"}


def get_hash(s):
    return md5(s.encode("utf-8")).hexdigest()


def get_open_doors(string):
    open_doors = set()
    direction_string = get_hash(string)[:4]

    if direction_string[0] in OPEN_DOOR_CHARACTERS:
        open_doors.add("up")
    if direction_string[1] in OPEN_DOOR_CHARACTERS:
        open_doors.add("down")
    if direction_string[2] in OPEN_DOOR_CHARACTERS:
        open_doors.add("left")
    if direction_string[3] in OPEN_DOOR_CHARACTERS:
        open_doors.add("right")

    return open_doors


queue = []
# len(path), coords, path
heappush(queue, (0, (0, 0), ""))
longest_path_length = 0

while len(queue):
    path_len, coords, path = heappop(queue)
    open_doors = get_open_doors(f"{PASSCODE}{path}")

    if coords == (3, 3):
        if longest_path_length == 0:
            print(f"Part 1 Answer: {path}")
        longest_path_length = max(longest_path_length, path_len)
        continue

    if "up" in open_doors and coords[1] > 0:
        heappush(queue, (path_len + 1, (coords[0], coords[1] - 1), f"{path}U"))
    if "down" in open_doors and coords[1] < 3:
        heappush(queue, (path_len + 1, (coords[0], coords[1] + 1), f"{path}D"))
    if "left" in open_doors and coords[0] > 0:
        heappush(queue, (path_len + 1, (coords[0] - 1, coords[1]), f"{path}L"))
    if "right" in open_doors and coords[0] < 3:
        heappush(queue, (path_len + 1, (coords[0] + 1, coords[1]), f"{path}R"))

print(f"Part 2 Answer: {longest_path_length}")
