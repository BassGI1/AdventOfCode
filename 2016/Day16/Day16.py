raw_input = open("./input.txt", "r").read()

DISK_LENGTH = 272


def reverse_int(num, num_bits):
    b = 0

    for _ in range(num_bits):
        lsb = num & 1
        b = (b << 1) + lsb
        num = num >> 1

    return b


def dragon_curve(a, num_bits):
    return (a << (num_bits + 1)) + (reverse_int(a, num_bits) ^ (2**(num_bits) - 1))


def checksum(a, num_bits):
    c = 0

    for _ in range(int(num_bits // 2)):
        comp = a & 0b11
        a = a >> 2
        if comp == 1 or comp == 2:
            c = (c << 1) + 0
        else:
            c = (c << 1) + 1

    return reverse_int(c, int(num_bits // 2))


disk = int(raw_input, 2)
curr_num_bits = len(raw_input)

while curr_num_bits < DISK_LENGTH:
    disk = dragon_curve(disk, curr_num_bits)
    curr_num_bits = curr_num_bits * 2 + 1
    
disk = disk >> (curr_num_bits - DISK_LENGTH)
curr_num_bits = DISK_LENGTH

while curr_num_bits % 2 == 0:
    disk = checksum(disk, curr_num_bits)
    curr_num_bits = int(curr_num_bits // 2)
    
print(f"Part 1 Answer: {disk:0{curr_num_bits}b}")

DISK_LENGTH = 35_651_584

disk = int(raw_input, 2)
curr_num_bits = len(raw_input)

while curr_num_bits < DISK_LENGTH:
    disk = dragon_curve(disk, curr_num_bits)
    curr_num_bits = curr_num_bits * 2 + 1
    print(curr_num_bits)

disk = disk >> (curr_num_bits - DISK_LENGTH)
curr_num_bits = DISK_LENGTH

while curr_num_bits % 2 == 0:
    disk = checksum(disk, curr_num_bits)
    curr_num_bits = int(curr_num_bits // 2)
    
print(f"Part 2 Answer: {disk:0{curr_num_bits}b}")
