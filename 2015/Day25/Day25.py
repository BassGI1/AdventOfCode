end_row, end_col = 3075, 2981
starting_val = 20151125


def get_next_code(num: int) -> int:
    return (num * 252533) % 33554393


val = starting_val
num_iterations = sum([x for x in range(1, end_col)]) + \
    sum([y + end_col for y in range(1, end_row)])

for _ in range(num_iterations):
    val = get_next_code(val)

print(f"Answer: {val}")
