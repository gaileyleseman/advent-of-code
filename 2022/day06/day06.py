def parse_text(input_txt):
    with open(input_txt, "r") as f:
        data = f.read()
    return data

def find_marker_string(string, n):
    for i in range(len(string)-n):
        if len(set(string[i:i+n])) == n:
            break
    return i + n 

def part1(data):
    return find_marker_string(data, 4)


def part2(data):
    return find_marker_string(data, 14)


if __name__ == '__main__':
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
