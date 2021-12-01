

def parse_text(input_txt):
    data = open(input_txt, "r").read().split('\n')
    return data

def part1(input_txt):
    data = parse_text(input_txt)
    pass

def part2(input_txt):
    data = parse_text(input_txt)
    pass


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))