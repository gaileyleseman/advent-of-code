def parse_text(input_txt):
    data = open(input_txt, "r").read().split('\n')
    data = [int(i) for i in data]
    return data


def part1(input_txt):
    data = parse_text(input_txt)
    for i in range(0, len(data) - 1):
        for j in range(i, len(data) - 1):
            if data[i] + data[j] == 2020:
                return data[i] * data[j]


def part2(input_txt):
    data = parse_text(input_txt)
    for i in range(0, len(data) - 1):
        for j in range(i, len(data) - 1):
            for k in range(j, len(data) - 1):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i] * data[j] * data[k]


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
