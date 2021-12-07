import numpy as np


def parse_text(input_txt):
    lines = open(input_txt, "r").read().split(',')
    data = np.array([int(number) for number in lines])
    return data


def sum_n(n):
    return n * (n+1) / 2


def part1(input_txt):
    crabs = parse_text(input_txt)
    fuel_costs = np.zeros(max(crabs))
    for pos in range(max(crabs)):
        fuel_costs[pos] = np.sum(np.abs(crabs - pos))
    return int(min(fuel_costs))


def part2(input_txt):
    crabs = parse_text(input_txt)
    fuel_costs = np.zeros(max(crabs))
    for pos in range(max(crabs)):
        fuel_costs[pos] = np.sum(sum_n(np.abs(crabs - pos)))
    return int(min(fuel_costs))


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
