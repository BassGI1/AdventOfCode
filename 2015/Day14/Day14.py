from re import findall

raw_input = open("./input.txt", "r").read()

lines = raw_input.split("\n")
reindeer = []

for line in lines:
    name = line.split(" ")[0]
    speed, duration, rest = [int(x) for x in findall(r"[0-9]+", line)]
    reindeer.append({
        "name": name,
        "moving": True,
        "time_left": duration,
        "resting_time": rest,
        "moving_time": duration,
        "moving_speed": speed,
        "distance": 0,
        "points": 0
    })


num_seconds_remaining = 2503
while num_seconds_remaining > 0:
    num_seconds_remaining -= 1

    for deer in reindeer:
        deer["time_left"] -= 1

        if deer["moving"] is True:
            deer["distance"] += deer["moving_speed"]

            if deer["time_left"] == 0:
                deer["time_left"] = deer["resting_time"]
                deer["moving"] = False

        elif deer["time_left"] == 0:
            deer["moving"] = True
            deer["time_left"] = deer["moving_time"]
            
    lead_distance = 0
    for deer in reindeer:
        lead_distance = max(lead_distance, deer["distance"])
    
    for deer in reindeer:
        if deer["distance"] == lead_distance:
            deer["points"] += 1


print(f"Part 1 Answer: {max([deer["distance"] for deer in reindeer])}")
print(f"Part 2 Answer: {max([deer["points"] for deer in reindeer])}")
