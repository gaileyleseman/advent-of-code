import numpy as np


def parse_text(input_txt):
    lines = open(input_txt, "r").read().split(',')
    data = [int(number) for number in lines]
    return data


def simulate_fish(fish, days):
    new_fish_timer = 8
    old_fish_timer = 6
    fish_days, counts = np.unique(fish, return_counts=True)
    init_fish = dict(zip(fish_days, counts))
    fish_tracker = [init_fish[i] if i in init_fish else 0 for i in range(new_fish_timer + 1)]
    for day in range(days):
        fish_tracker[old_fish_timer + 1] += fish_tracker[0]  # reset fish timer
        fish_tracker = np.roll(fish_tracker, -1)  # shift one day
    return sum(fish_tracker)


def part1(input_txt):
    fish = parse_text(input_txt)
    return simulate_fish(fish, 80)


def part2(input_txt):
    fish = parse_text(input_txt)
    return simulate_fish(fish, 256)


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
