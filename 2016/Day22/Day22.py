from re import findall

MAX_NODE_DIM = 30
NUMBER_PATTERN = r"[0-9]+"

raw_input = open("./input.txt", "r").read()


def parse_line(line):
    vals = [int(x) for x in findall(NUMBER_PATTERN, line)]
    return {
        "x": vals[0],
        "y": vals[1],
        "size": vals[2],
        "used": vals[3],
        "avail": vals[4],
        "use_percent": vals[5],
        "goal": False
    }


def is_viable(a, b):
    return 1 if b and (a["x"] != b["x"] or a["y"] != b["y"]) and a["used"] != 0 and a["used"] <= b["avail"] else 0


def print_grid(n):
    node_grid = []

    for y in range(MAX_NODE_DIM + 1):
        row = []

        for x in range(MAX_NODE_DIM + 1):
            if n[x][y]["size"] >= 500:
                row.append("#")
            elif n[x][y]["avail"] >= 90:
                row.append("_")
            elif n[x][y]["goal"] is True:
                row.append("G")
            else:
                row.append(".")

        node_grid.append(row)

    node_grid[0][0] = "S"

    print("\n".join([" ".join(a) for a in node_grid]))


nodes = {}
free_node_coords = (0, 0)
node_vals = [parse_line(x) for x in raw_input.split("\n")[2:]]

num_viable = 0
for node_1 in node_vals:
    for node_2 in node_vals:
        num_viable += is_viable(node_1, node_2)

for node in node_vals:
    if node["x"] not in nodes:
        nodes[node["x"]] = {node["y"]: node}

    else:
        nodes[node["x"]][node["y"]] = node

    if node["avail"] > 90:
        free_node_coords = (node["x"], node["y"])


print(f"Part 1 Answer: {num_viable}")

num_steps = 0
nodes[30][0]["goal"] = True
while free_node_coords != (MAX_NODE_DIM - 1, 0):
    x, y = free_node_coords

    if y == 0:
        free_node_coords = (x + 1, y)
    elif nodes[x][y - 1]["size"] < 500:
        free_node_coords = (x, y - 1)
    else:
        free_node_coords = (x - 1, y)

    num_steps += 1

print(f"Part 2 Answer: {num_steps + 1 + 29*5}")
