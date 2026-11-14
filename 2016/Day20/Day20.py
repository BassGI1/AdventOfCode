raw_input = open("./input.txt", "r").read()


def parse_range(string):
    n1, n2 = string.split("-")
    return [int(n1), int(n2)]


IP_MIN = 0
IP_MAX = 4294967295

allowed_ips = range(0, IP_MAX + 1)
ranges = sorted([parse_range(x)
                for x in raw_input.split("\n")], key=lambda x: x[0])

i = 1
min_allowed_ip = 0

while i < len(ranges):
    if ranges[i - 1][1] + 1 >= ranges[i][0]:
        ranges[i - 1][1] = max(ranges[i - 1][1], ranges[i][1])
        ranges.pop(i)
        i = 0

    else:
        min_allowed_ip = ranges[0][1] + 1

    i += 1

num_allowed_ips = 0
ranges.append([IP_MAX + 1, IP_MAX + 1])

for i in range(1, len(ranges)):
    min_1, max_1 = ranges[i]
    min_2, max_2 = ranges[i - 1]
    num_allowed_ips = num_allowed_ips + (min_1 - max_2 - 1)


print(f"Part 1 Answer: {min_allowed_ip}")
print(f"Part 2 Answer: {num_allowed_ips}")
