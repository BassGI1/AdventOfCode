from re import fullmatch

raw_input = open("./input.txt", "r").read()

CONSTANT_REGEX = r"[0-9]+"
SIXTEEN_BIT_CLAMP = 0b1111111111111111

nodes = {}
cache = {}
lines = raw_input.split("\n")


class RenameExpr:
    def __init__(self, name, val):
        self.name = name
        self.val = val

    def output(self):
        return nodes[self.val].output()


class ConstantExpr:
    def __init__(self, name, val):
        self.name = name
        self.val = val

    def output(self):
        return self.val & SIXTEEN_BIT_CLAMP


class NotExpr:
    def __init__(self, name, child):
        self.name = name
        self.child = child

    def output(self):
        if self.name in cache:
            return cache[self.name]
        v = (~nodes[self.child].output()) & SIXTEEN_BIT_CLAMP
        cache[self.name] = v
        return v


class AndExpr:
    def __init__(self, name, c1, c2):
        self.name = name
        self.leftChild = c1
        self.rightChild = c2

    def output(self):
        if self.name in cache:
            return cache[self.name]
        v = (nodes[self.leftChild].output() &
             nodes[self.rightChild].output()) & SIXTEEN_BIT_CLAMP
        cache[self.name] = v
        return v


class OrExpr:
    def __init__(self, name, c1, c2):
        self.name = name
        self.leftChild = c1
        self.rightChild = c2

    def output(self):
        if self.name in cache:
            return cache[self.name]
        v = (nodes[self.leftChild].output() |
             nodes[self.rightChild].output()) & SIXTEEN_BIT_CLAMP
        cache[self.name] = v
        return v


class LeftShiftExpr:
    def __init__(self, name, c1, c2):
        self.name = name
        self.leftChild = c1
        self.rightChild = c2

    def output(self):
        if self.name in cache:
            return cache[self.name]
        v = (nodes[self.leftChild].output() <<
             nodes[self.rightChild].output()) & SIXTEEN_BIT_CLAMP
        cache[self.name] = v
        return v


class RightShiftExpr:
    def __init__(self, name, c1, c2):
        self.name = name
        self.leftChild = c1
        self.rightChild = c2

    def output(self):
        if self.name in cache:
            return cache[self.name]
        v = (nodes[self.leftChild].output() >>
             nodes[self.rightChild].output()) & SIXTEEN_BIT_CLAMP
        cache[self.name] = v
        return v


for line in lines:
    gate, output = line.split(" -> ")
    gate = gate.split(" ")

    if "LSHIFT" in gate:
        if fullmatch(CONSTANT_REGEX, gate[0]):
            nodes[gate[0]] = ConstantExpr(gate[0], int(gate[0]))
        if fullmatch(CONSTANT_REGEX, gate[2]):
            nodes[gate[2]] = ConstantExpr(gate[2], int(gate[2]))

        nodes[output] = LeftShiftExpr(output, gate[0], gate[2])

    elif "RSHIFT" in gate:
        if fullmatch(CONSTANT_REGEX, gate[0]):
            nodes[gate[0]] = ConstantExpr(gate[0], int(gate[0]))
        if fullmatch(CONSTANT_REGEX, gate[2]):
            nodes[gate[2]] = ConstantExpr(gate[2], int(gate[2]))

        nodes[output] = RightShiftExpr(output, gate[0], gate[2])

    elif "NOT" in gate:
        if fullmatch(CONSTANT_REGEX, gate[1]):
            nodes[gate[1]] = ConstantExpr(gate[1], int(gate[1]))

        nodes[output] = NotExpr(output, gate[1])

    elif "AND" in gate:
        if fullmatch(CONSTANT_REGEX, gate[0]):
            nodes[gate[0]] = ConstantExpr(gate[0], int(gate[0]))
        if fullmatch(CONSTANT_REGEX, gate[2]):
            nodes[gate[2]] = ConstantExpr(gate[2], int(gate[2]))

        nodes[output] = AndExpr(output, gate[0], gate[2])

    elif "OR" in gate:
        if fullmatch(CONSTANT_REGEX, gate[0]):
            nodes[gate[0]] = ConstantExpr(gate[0], int(gate[0]))
        if fullmatch(CONSTANT_REGEX, gate[2]):
            nodes[gate[2]] = ConstantExpr(gate[2], int(gate[2]))

        nodes[output] = OrExpr(output, gate[0], gate[2])

    else:
        if fullmatch(CONSTANT_REGEX, gate[0]):
            nodes[output] = ConstantExpr(output, int(gate[0]))
        else:
            nodes[output] = RenameExpr(output, gate[0])

print(f"Part 1 Answer: {nodes["a"].output()}")

nodes["b"] = ConstantExpr("b", nodes["a"].output())
cache = {}

print(f"Part 2 Answer: {nodes["a"].output()}")
