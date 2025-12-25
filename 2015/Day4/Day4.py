from hashlib import md5

num = 0
secret_key = open("./input.txt", "r").read()

while 1:
    string = f"{secret_key}{num}".encode("utf-8")
    hex_code = md5(string).hexdigest()
    
    if hex_code[:5] == "00000":
        print(f"Part 1 Answer: {num}")
        break
    
    num += 1
    
    
num = 0
while 1:
    string = f"{secret_key}{num}".encode("utf-8")
    hex_code = md5(string).hexdigest()
    
    if hex_code[:6] == "000000":
        print(f"Part 2 Answer: {num}")
        break
    
    num += 1