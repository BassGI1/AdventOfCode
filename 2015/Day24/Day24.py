from math import prod

raw_input = open("./input.txt", "r").read()

weights = sorted([int(x) for x in raw_input.split("\n")], reverse=True)
target_val_p1 = int(sum(weights) / 3)
target_val_p2 = int(sum(weights) / 4)
cache = set()


def get_partition(remaining_vals: list[int], t: int, partition: list[int], min_len: list[int], partitions: set[tuple[int]]):
    s = sum(partition)
    part = tuple(sorted(partition))
    global cache

    if len(partition) >= min_len[0] or s > t or part in cache:
        return

    cache.add(part)

    if sum(partition) == t:
        partitions.add(part)
        min_len[0] = min(min_len[0], len(partition))
        return

    for i in range(len(remaining_vals)):
        c = remaining_vals.copy()
        new_num = c.pop(i)
        p_c = partition.copy()
        p_c.append(new_num)
        get_partition(c, t, p_c, min_len, partitions)


all_partitions = set()
minimum_size = [float("inf")]
get_partition(weights, target_val_p1, [], minimum_size, all_partitions)

min_QE = float("inf")
for partition in all_partitions:
    min_QE = min(min_QE, prod(partition))

print(f"Part 1 Answer: {min_QE}")


cache = set()
all_partitions = set()
minimum_size = [float("inf")]
get_partition(weights, target_val_p2, [], minimum_size, all_partitions)

min_QE = float("inf")
for partition in all_partitions:
    min_QE = min(min_QE, prod(partition))

print(f"Part 2 Answer: {min_QE}")
