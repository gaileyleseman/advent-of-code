import numpy as np
from itertools import product


def parse_text(input_txt):
    with open(input_txt, "r") as file:
        data = np.array([list(line) for line in file.read().splitlines()])
    return data

def out_of_bounds(data, rows, cols):
    return any([x < 0 or y < 0 or x >= data.shape[1] or y >= data.shape[0] for x, y in zip(rows, cols)])

def get_word(data, rows, cols):
    return "".join([data[y, x] for x, y in zip(rows, cols)])

def part1(data):
    WORD = "XMAS"
    found_coordinates = []
    directions = [np.array(x) for x in product(range(-1, 2), repeat=2)]
    for row, col in product(range(data.shape[0]), range(data.shape[1])):
        for d in directions:
            rows = [row + i * d[0] for i in range(4)]
            cols = [col + i * d[1] for i in range(4)]
            if out_of_bounds(data, rows, cols):
                continue
            words = [get_word(data, rows, cols), get_word(data, rows[::-1], cols[::-1])]
            if WORD in words:
                coordinates = sorted(list(zip(rows, cols)))
                if coordinates not in found_coordinates:
                    found_coordinates.append(coordinates)
    return len(found_coordinates)


def part2(data):
    WORDS = ["MAS", "SAM"]
    found_coordinates = []
    for row, col in product(range(data.shape[0]), range(data.shape[1])):
        rows = [row + i for i in range(3)]
        cols = [col + i for i in range(3)]
        if out_of_bounds(data, rows, cols):
            continue
        words = [get_word(data, rows, cols), get_word(data, rows[::-1], cols)]
        if all([w in WORDS for w in words]):
            coordinates = sorted(list(zip(rows, cols)))
            if coordinates not in found_coordinates:
                found_coordinates.append(coordinates)
    return len(found_coordinates)


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
