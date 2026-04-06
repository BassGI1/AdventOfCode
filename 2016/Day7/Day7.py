raw_input = open("./input.txt", "r").read()

supported_ips = 0
ips = raw_input.split("\n")

for ip in ips:
    i = 3
    is_within_bracket = False

    while i < len(ip):
        if ip[i] == "[":
            is_within_bracket = True
        elif ip[i] == "]":
            is_within_bracket = False

        if f"{ip[i - 3]}{ip[i - 2]}" == f"{ip[i]}{ip[i - 1]}" and ip[i] != ip[i - 1]:
            if is_within_bracket:
                break

            supported_ips += 1
            break

        i += 1


print(f"Part 1 Answer: {supported_ips}")
