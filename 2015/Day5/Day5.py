raw_input = open("./input.txt", "r").read()

vowels = {"a", "e", "i", "o", "u"}
naughty_substrings = {"ab", "cd", "pq", "xy"}

num_nice = 0
strings = raw_input.split("\n")

for string in strings:
    num_vowels = 0
    is_naughty = False
    two_in_a_row = False

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            two_in_a_row = True
        if string[i] in vowels:
            num_vowels += 1
        if string[i : i + 2] in naughty_substrings:
            is_naughty = True
            break
    
    if string[-1] in vowels:
        num_vowels += 1
        
    if num_vowels > 2 and not is_naughty and two_in_a_row:
        num_nice += 1
        
print(f"Part 1 Answer: {num_nice}")

num_nice = 0
for string in strings:
    has_oreo = False
    has_repeat = False
    
    for i in range(len(string) - 1):
        if len(string.replace(string[i : i + 2], "")) < (len(string) - 3):
            has_repeat = True
            break
    
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            has_oreo = True
            break
    
    if has_oreo and has_repeat:
        num_nice += 1
        
print(f"Part 2 Answer: {num_nice}")