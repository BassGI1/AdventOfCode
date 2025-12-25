raw_input = open("./input.txt", "r").read()

replacements = []
replacements_string, initial_molecule = raw_input.split("\n\n")
replacements_string = replacements_string.split("\n")

for r in replacements_string:
    key, val = r.replace(" => ", ",").split(",")
    replacements.append((key, val))


def create_molecules(molecule):
    created_molecules = set()

    for s, r in replacements:
        i = 0
        while i < len(molecule):
            if molecule[i: i + len(s)] == s:
                prefix = molecule[:i]
                suffix = molecule[i:].replace(s, r, 1)
                created_molecules.add(f"{prefix}{suffix}")

            i += 1

    return created_molecules


print(f"Part 1 Answer: {len(create_molecules(initial_molecule))}")

num_steps = 0
molecule = initial_molecule
replacements.sort(key=lambda x: len(x[1]), reverse=True)

while molecule != 'e':
    for src, repl in replacements:
        if repl in molecule:
            molecule = molecule.replace(repl, src, 1)
            num_steps += 1

print(f"Part 2 Answer: {num_steps}")
