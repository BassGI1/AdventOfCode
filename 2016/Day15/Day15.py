from re import findall

raw_input = open("./input.txt", "r").read()

discs = []
lines = raw_input.split("\n")

for i in range(len(lines)):
    nums = [int(x) for x in findall(r"[0-9]+", lines[i])]
    num_positions = nums[1]
    position = (nums[0] + nums[3]) % num_positions

    discs.append([position, num_positions])
    
discs_p2 = [x.copy() for x in discs]

def inc_disc(disc):
    disc[0] = (disc[0] + 1) % disc[1]
    
    
def check_discs(discs_arr):
    for d in discs_arr:
        if d[0] != 0:
            return False
        
    return True
    
time = 0
while 1:
    if check_discs(discs):
        print(f"Part 1 Answer: {time}")
        break
    
    for d in discs:
        inc_disc(d)
        
    time += 1
    
discs_p2.append([len(lines) + 1, 11])

time = 0
while 1:
    if check_discs(discs_p2):
        print(f"Part 2 Answer: {time}")
        break
    
    for d in discs_p2:
        inc_disc(d)
        
    time += 1