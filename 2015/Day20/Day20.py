from math import sqrt

raw_input = open("./input.txt", "r").read()


def find_factors(n):
    factors = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            if i != n // i:
                factors.add(n // i)

    return factors


house_num = 1
target_val = int(raw_input)

while 1:
    factors = find_factors(house_num)
    house_val = sum([x*10 for x in factors])

    if house_val > target_val:
        print(f"Part 1 Answer: {house_num}")
        break

    house_num += 1


house_num = 1

while 1:
    factors = find_factors(house_num)
    house_val = sum([x*11 for x in factors if int(house_num // x) <= 50])

    if house_val > target_val:
        print(f"Part 2 Answer: {house_num}")
        break

    house_num += 1
