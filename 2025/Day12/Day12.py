# What a troll
raw_input = open("./input.txt", "r").read()

*raw_shapes, raw_grids = raw_input.split("\n\n")
raw_grids = raw_grids.split("\n")

shapes = {}
for shape in raw_shapes:
    index, shape_string = shape.split(":\n")
    shape_string = sum([1 for s in "".join(shape_string.split("\n")) if s == "#"])

    shapes[index] = shape_string

num_fittable = 0

for line in raw_grids:
    dims, shape_nums = line.split(": ")
    dims = [int(d) for d in dims.split("x")]
    shape_nums = [int(s) for s in shape_nums.split(" ")]
    
    num_spaces = dims[0]*dims[1]
    num_blocks = 0
    for i in range(len(shape_nums)):
        num_blocks += shape_nums[i]*shapes[str(i)]
        
    if num_blocks < num_spaces:
        num_fittable += 1
    
print(f"Answer: {num_fittable}")