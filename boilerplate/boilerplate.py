def parse_text(input_txt):
    with open(input_txt, "r") as f:
        data = f.read().split('\n')
    return data


def part1(data):
    return 0


def part2(data):
    return 0


if __name__ == '__main__':
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
