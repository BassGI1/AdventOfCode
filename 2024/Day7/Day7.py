raw_input = open("./input.txt", "r+").read()

def add(target, curr_result, numbers, index):
    curr_result += numbers[index]
    if index == len(numbers) - 1 and curr_result == target: return True
    elif index < len(numbers) - 1:
        return mul(target, curr_result, numbers, index + 1) or add(target, curr_result, numbers, index + 1) or concat(target, curr_result, numbers, index + 1)

def mul(target, curr_result, numbers, index):
    curr_result *= numbers[index]
    if index == len(numbers) - 1 and curr_result == target: return True
    elif index < len(numbers) - 1:
        return mul(target, curr_result, numbers, index + 1) or add(target, curr_result, numbers, index + 1) or concat(target, curr_result, numbers, index + 1)
    
def concat(target, curr_result, numbers, index):
    curr_result = int(f"{curr_result}{numbers[index]}")
    if index == len(numbers) - 1 and curr_result == target: return True
    elif index < len(numbers) - 1:
        return mul(target, curr_result, numbers, index + 1) or add(target, curr_result, numbers, index + 1) or concat(target, curr_result, numbers, index + 1)

total = 0    

calculations = raw_input.split("\n")
for calculation in calculations:
    result, numbers = calculation.split(": ")
    result = int(result)
    numbers = [int(n) for n in numbers.split(" ")]
    if add(result, 0, numbers, 0) or mul(result, 1, numbers, 0) or concat(result, "", numbers, 0): total += result
    
print(total)