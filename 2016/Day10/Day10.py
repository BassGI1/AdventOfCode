from re import findall

# horrible code but it works ig

BOT_PATTERN = r"bot [0-9]+"
OUTPUT_PATTERN = r"output [0-9]+"
NUMBER_PATTERN = r"[0-9]+"

TARGET_LOW = 17
TARGET_HIGH = 61

raw_input = open("./input.txt", "r").read()

lines = raw_input.split("\n")
num_bots = max([int(x[4:]) for x in findall(BOT_PATTERN, raw_input)]) + 1
num_outputs = max([int(x[7:]) for x in findall(OUTPUT_PATTERN, raw_input)]) + 1

ready_bots = set()
bot_states = [[-1, -1] for _ in range(num_bots)]
output_states = [-1 for _ in range(num_outputs)]

instructions = ["" for _ in range(num_bots)]
for line in lines:
    if "value" in line:
        val, bot_num = [int(x) for x in findall(NUMBER_PATTERN, line)]
        bot_states[bot_num][0] = val
        bot_states[bot_num].sort()

        if bot_states[bot_num][0] != -1 and bot_states[bot_num][1] != -1:
            ready_bots.add(bot_num)

    else:
        bot_num = [int(x) for x in findall(NUMBER_PATTERN, line)][0]
        instructions[bot_num] = line


while len(ready_bots):
    curr_bot = ready_bots.pop()
    if bot_states[curr_bot][0] == TARGET_LOW and bot_states[curr_bot][1] == TARGET_HIGH:
        print(f"Part 1 Answer: {curr_bot}")

    inst = instructions[curr_bot]
    inst = inst.replace(f"bot {curr_bot} gives low to ",
                        "").replace(" and high to ", ",")
    low, high = inst.split(",")

    if "bot" in low:
        low_bot = int(low[4:])
        low = bot_states[low_bot]
        low[0] = bot_states[curr_bot][0]
        low.sort()

        if low[0] != -1 and low[1] != -1:
            ready_bots.add(low_bot)

    elif "output" in low:
        output_states[int(low[7:])] = bot_states[curr_bot][0]

    if "bot" in high:
        high_bot = int(high[4:])
        high = bot_states[high_bot]
        high[0] = bot_states[curr_bot][1]
        high.sort()

        if high[0] != -1 and high[1] != -1:
            ready_bots.add(high_bot)

    elif "output" in high:
        output_states[int(high[7:])] = bot_states[curr_bot][1]


print(f"Part 2 Answer: {output_states[0]*output_states[1]*output_states[2]}")
