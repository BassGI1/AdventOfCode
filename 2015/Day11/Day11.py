raw_input = open("./input.txt", "r").read()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

word = list(raw_input)
encoded_word = []

for letter in word:
    encoded_word.append(alphabet.index(letter))


def is_valid_password(password):
    rule1, rule2 = False, True

    for i in range(2, len(password)):
        if password[i] == password[i - 1] + 1 and password[i - 1] == password[i - 2] + 1:
            rule1 = True
            break

    for letter in password:
        if letter == 8 or letter == 11 or letter == 14:
            rule2 = False
            break

    repeat = None
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            if repeat is None:
                repeat = password[i]
            elif password[i] != repeat:
                repeat = True

    return rule1 and rule2 and repeat is True


def increment_word(word):
    i = len(word) - 1
    incremented = word.copy()

    while incremented[i] == 25:
        incremented[i] = 0
        i -= 1

    incremented[i] += 1

    return incremented


while not is_valid_password(encoded_word):
    encoded_word = increment_word(encoded_word)

print(f"Part 1 Answer: {"".join([alphabet[i] for i in encoded_word])}")

encoded_word = increment_word(encoded_word)
while not is_valid_password(encoded_word):
    encoded_word = increment_word(encoded_word)

print(f"Part 2 Answer: {"".join([alphabet[i] for i in encoded_word])}")