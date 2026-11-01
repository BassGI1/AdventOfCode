from hashlib import md5

salt = open("./input.txt", "r").read()


def get_hash(s):
    return md5(s.encode("utf-8")).hexdigest()


def extract_fives(s):
    found = set()
    chars = [*[_ for _ in range(10)], "a", "b", "c", "d", "e", "f"]

    for char in chars:
        needle = f"{char}{char}{char}{char}{char}"
        if s.count(needle):
            found.add(needle)
            s.replace(needle, "")

    return found


def extract_threes(s):
    found = set()
    chars = [*[_ for _ in range(10)], "a", "b", "c", "d", "e", "f"]

    for char in chars:
        needle = f"{char}{char}{char}"
        if s.count(needle):
            found.add((needle, s.index(needle)))

    return sorted([x for x in found], key=lambda x: x[1])[0][0][0] if len(found) else None


hash_str_cash = {}
curr_index = 0
num_keys = 0

while 1:
    hash_str = f"{salt}{curr_index}"
    hashed_str = get_hash(hash_str)

    if hash_str not in hash_str_cash:
        hash_str_cash[hash_str] = {
            "three": extract_threes(hashed_str),
            "five": extract_fives(hashed_str)
        }

    if hash_str_cash[hash_str]["three"]:
        for i in range(1, 1001):
            new_hash_str = f"{salt}{curr_index + i}"
            new_hashed_str = get_hash(new_hash_str)

            char = hash_str_cash[hash_str]["three"]

            if new_hash_str not in hash_str_cash:
                hash_str_cash[new_hash_str] = {
                    "three": extract_threes(new_hashed_str),
                    "five": extract_fives(new_hashed_str)
                }

            if f"{char}{char}{char}{char}{char}" in hash_str_cash[new_hash_str]["five"]:
                num_keys += 1
                break

    if num_keys == 64:
        print(f"Part 1 Answer: {curr_index}")
        break

    curr_index += 1


hash_str_cash = {}
hash_cash = {}
curr_index = 0
num_keys = 0


def get_hash_p2(s):
    key = s

    if key in hash_cash:
        return hash_cash[key]

    s = md5(s.encode("utf-8")).hexdigest()
    for _ in range(2016):
        s = md5(s.encode("utf-8")).hexdigest()

    hash_cash[key] = s
    return s


while 1:
    hash_str = f"{salt}{curr_index}"
    hashed_str = get_hash_p2(hash_str)

    if hash_str not in hash_str_cash:
        hash_str_cash[hash_str] = {
            "three": extract_threes(hashed_str),
            "five": extract_fives(hashed_str)
        }

    if hash_str_cash[hash_str]["three"]:
        for i in range(1, 1001):
            new_hash_str = f"{salt}{curr_index + i}"
            new_hashed_str = get_hash_p2(new_hash_str)

            char = hash_str_cash[hash_str]["three"]

            if new_hash_str not in hash_str_cash:
                hash_str_cash[new_hash_str] = {
                    "three": extract_threes(new_hashed_str),
                    "five": extract_fives(new_hashed_str)
                }

            if f"{char}{char}{char}{char}{char}" in hash_str_cash[new_hash_str]["five"]:
                num_keys += 1
                break

    if num_keys == 64:
        print(f"Part 2 Answer: {curr_index}")
        break

    curr_index += 1
