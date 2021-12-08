import numpy as np


def parse_text(input_txt):
    lines = [x.split(" | ") for x in open(input_txt, "r").read().split('\n')]
    data = lines
    return data


def find_easy_digits(line):
    letters = line.split(" ")
    count = 0
    for i in letters:
        if len(i) == 2 or len(i) == 3 or len(i) == 4 or len(i) == 7:
            count += 1
    return count


def find_digits_map(line):
    letters = line.split(" ")
    length_map = {len(x): x for x in letters}
    digits_map = {1: "".join(sorted(length_map[2])),
                  7: "".join(sorted(length_map[3])),
                  4: "".join(sorted(length_map[4])),
                  8: "".join(sorted(length_map[7]))}
    cf = digits_map[1]
    bd = "".join([letter for letter in digits_map[4] if letter not in cf])
    for i in letters:
        if len(i) == 5:
            if cf[0] in i and cf[1] in i:
                digits_map[3] = "".join(sorted(i))
            else:
                if bd[0] in i and bd[1] in i:
                    digits_map[5] = "".join(sorted(i))
                else:
                    digits_map[2] = "".join(sorted(i))
        elif len(i) == 6:
            if cf[0] in i and cf[1] in i:
                if bd[0] in i and bd[1] in i:
                    digits_map[9] = "".join(sorted(i))
                else:
                    digits_map[0] = "".join(sorted(i))
            else:
                digits_map[6] = "".join(sorted(i))
    return dict([(value, key) for key, value in digits_map.items()])

def map_digits(digits_map, line):
    letters = ["".join(sorted(l)) for l in line.split()]
    digits = int("".join([str(digits_map[l]) for l in letters]))
    return digits

def part1(input_txt):
    data = parse_text(input_txt)
    count = 0
    for line in data:
        count += find_easy_digits(line[1])
    return count


def part2(input_txt):
    data = parse_text(input_txt)
    count = 0
    for line in data:
        digits_map = find_digits_map(line[0])
        digits = map_digits(digits_map, line[1])
        count += digits
    return count


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
