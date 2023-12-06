import numpy as np


def parse_text(input_txt):
    with open(input_txt, "r") as f:
        data = f.read().split("\n")
    return data


def part1(data):
    points = 0
    for row in data:
        _, card = row.split(":")
        winning, you = card.split("|")
        n_winning_numbers = 0
        for number in winning.strip().split(" "):
            if number == " ":
                continue
            if number in you.strip().split(" "):
                n_winning_numbers += 1
        if n_winning_numbers > 0:
            points += 2 ** (n_winning_numbers - 1)

    return points


def part2(data):
    n_cards = len(data)
    n_copies = np.ones(n_cards)
    for i, row in enumerate(data):
        _, card = row.split(":")
        winning, you = card.split("|")
        n_winning_numbers = 0
        for number in winning.strip().split(" "):
            if number == " " or number == "":
                continue
            if number in you.strip().split(" "):
                n_winning_numbers += 1
        if n_winning_numbers > 0:
            n_copies[i + 1 : i + 1 + n_winning_numbers] += n_copies[i]
    return np.sum(n_copies)


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
