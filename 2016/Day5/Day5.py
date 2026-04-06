from hashlib import md5

raw_input = open("./input.txt", "r").read()

index = 0
password = ""

while 1:
    hash_str = md5(f"{raw_input}{index}".encode("utf-8")).hexdigest()
    if hash_str[:5] == "00000":
        password = f"{password}{hash_str[5]}"
        if len(password) == 8:
            break
    index += 1

print(f"Part 1 Answer: {password}")

index = 0
password = [None]*8

while 1:
    hash_str = md5(f"{raw_input}{index}".encode("utf-8")).hexdigest()
    if hash_str[:5] == "00000":
        pass_index = int(hash_str[5], 16)
        if pass_index < len(password) and password[pass_index] is None:
            password[pass_index] = hash_str[6]
        if None not in password:
            break

    index += 1

print(f"Part 2 Answer: {"".join(password)}")
