from re import findall

PATTERN = r"[a-z]+\[[a-z]+\]"

raw_input = open("./input.txt", "r").read()

lines = raw_input.split("\n")


def contains_palindrome(string):
    for i in range(len(string) - 3):
        if string[i: i + 4] == string[i: i + 4][::-1] and string[i] != string[i + 1]:
            return True

    return False


num_valid = 0

for line in lines:
    pairs = findall(PATTERN, line)
    p_non_bracket, p_bracket = False, False

    for pair in pairs:
        index = pair.index("[")

        part1 = pair[:index]
        part2 = pair[index + 1: -1]

        line = line.replace(pair, "")

        if contains_palindrome(part2):
            p_bracket = True
            break
        if contains_palindrome(part1):
            p_non_bracket = True

    if contains_palindrome(line):
        p_non_bracket = True

    if p_non_bracket and not p_bracket:
        num_valid += 1

print(f"Part 1 Answer: {num_valid}")

num_valid = 0

def inverse(a):
    return f"{a[1]}{a[0]}{a[1]}"

def extract_pals(string):
    pals = []
    
    for i in range(len(string) - 2):
        if string[i : i + 3] == string[i : i + 3][::-1] and string[i] != string[i + 1]:
            pals.append(string[i : i + 3])
            
    return pals

for line in lines:
    outside, inside = [], []
    pairs = findall(PATTERN, line)

    for pair in pairs:
        index = pair.index("[")

        outside.append(pair[:index])
        inside.append(pair[index + 1 : -1])

        line = line.replace(pair, "")
        
    outside.append(line)
    
    break_out = False
    outer_pals = set()
    
    for s in outside:
        pals = extract_pals(s)
        for pal in pals:
            outer_pals.add(pal)
            
    for s in inside:
        pals = extract_pals(s)
        
        for pal in pals:
            if inverse(pal) in outer_pals:
                num_valid += 1
                break_out = True
                break
        
        if break_out:
            break
        
print(f"Part 2 Answer: {num_valid}")