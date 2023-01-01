from ast import literal_eval
import json


def parse_text(input_txt):
    data = []
    with open(input_txt, "r") as f:
        pairs = [pair.split("\n") for pair in f.read().split("\n\n")]
    for pair in pairs:
        # data.append([eval(line) for line in pair])        # NOT SAFE
        data.append([literal_eval(line) for line in pair])
        # data.append([json.loads(line) for line in pair])  # ALSO WORKS
    return data


def compare(left, right):
    for i, l in enumerate(left):
        if i >= len(right):
            return False
        r = right[i]

        if type(l) == type(r) == int:
            if l == r:
                continue
            return l < r

        l = [l] if type(l) == int else l
        r = [r] if type(r) == int else r
        return compare(l, r)
    return True


def part1(data):
    correct_order = 0
    for pair_index, (left, right) in enumerate(data):
        if compare(left, right):
            correct_order += pair_index + 1
    return correct_order


def part2(data):
    data = [line for pair in data for line in pair]
    divider_packets = [[[2]], [[6]]]
    for packet in divider_packets:
        data.append(packet)

    decoder_key = 1
    sorted = []
    while len(data) > 0:
        smallest = data[0]
        for line in data:
            if compare(line, smallest):
                smallest = line
        sorted.append(smallest)
        data.remove(smallest)

    for i, line in enumerate(sorted):
        if line in divider_packets:
            decoder_key *= i + 1

    return decoder_key


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
