def count_literals(s):
    return len(s)


def count_characters(s):
    s = s[1:-1]
    length = i = 0
    while i < len(s):
        length += 1
        if s[i] == "\\":
            if s[i + 1] == "x":
                i += 4
            else:
                i += 2
        else:
            i += 1
    return length


def count_encoded(s):
    length = 2
    for char in s:
        if char in ('"', "\\"):
            length += 2
        else:
            length += 1
    return length


def part_one():
    total_literals = total_chars = 0
    with open("Day08_InputS.txt") as fin:
        for line in [s.strip() for s in fin.readlines()]:
            total_literals += count_literals(line)
            total_chars += count_characters(line)
    print("Difference between literals and chars: {}"
          .format(total_literals - total_chars))


def part_two():
    total_literals = total_encoded = 0
    with open("Day08_InputS.txt") as fin:
        for line in [s.strip() for s in fin.readlines()]:
            total_literals += count_literals(line)
            total_encoded += count_encoded(line)
    print("Difference between encoded and literals: {}"
          .format(total_encoded - total_literals))


if __name__ == "__main__":
    part_one()
    part_two()