import re
import math

def parse_text(input_txt):
    with open(input_txt, "r") as f:
        data = f.read().split("\n")
    return data

MUL_REGEX = r"mul\(\d+,\d+\)"
DO_REGEX = r"do\(\)"
DONT_REGEX = r"don't\(\)"

def part1(data):
    total = 0
    for line in data:
        mul_strings = re.findall(MUL_REGEX, line)
        for m in mul_strings:
            a, b = re.findall(r"\d+", m)
            total += int(a) * int(b)
    return total


def get_position_of_regex(regex, line):
    first_match = re.search(regex, line)
    if first_match is None:
        return (math.inf, math.inf)
    return first_match.span()

def part2(data):
    total = 0
    enabled = True
    for line in data:
        start_of_string = 0
        while len(line) > start_of_string:
            line = line[start_of_string:]
            first_mul = get_position_of_regex(MUL_REGEX, line)
            first_do = get_position_of_regex(DO_REGEX, line)
            first_dont = get_position_of_regex(DONT_REGEX, line)

            if first_dont < first_mul:
                enabled = False
                start_of_string = first_dont[1]
                continue
        
            if first_do < first_mul:
                enabled = True
                start_of_string = first_do[1]
                continue

            if enabled and first_mul != (math.inf, math.inf):
                a,b = re.findall(r"\d+", line[first_mul[0]:first_mul[1]])
                total += int(a) * int(b)
        
            start_of_string = first_mul[1]

    return total


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
