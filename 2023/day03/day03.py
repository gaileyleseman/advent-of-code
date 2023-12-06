import numpy as np


def parse_text(input_txt):
    with open(input_txt, "r") as f:
        data = f.read().split("\n")
    data = [row for row in data if row != ""]
    data = np.array(data)
    return data


def is_adjacent_to_symbol(data, row, col):
    adjacent = False
    c_max = len(data)
    r_max = len(data[0])
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r < 0 or r >= r_max or c < 0 or c >= c_max:
                continue
            object = data[r][c]
            if not object.isdigit() and object != ".":
                adjacent = True
    return adjacent


def is_adjacent_to_gears(data, row, col):
    c_max = len(data)
    r_max = len(data[0])
    gears = []
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r < 0 or r >= r_max or c < 0 or c >= c_max:
                continue
            object = data[r][c]
            if object == "*":
                gears.append(str(f"{r},{c}"))
    return gears


def part1(data):
    part_numbers = []
    for i, row in enumerate(data):
        j = 0
        while j < len(row):
            digit = row[j]
            if digit == "." or not digit.isdigit():
                j += 1
                continue
            digit_start = j
            len_digit = 1
            while True:
                if digit_start + len_digit >= len(row):
                    break
                if data[i][digit_start + len_digit].isdigit():
                    digit += data[i][digit_start + len_digit]
                    len_digit += 1
                else:
                    break
            for k in range(digit_start, digit_start + len_digit):
                if is_adjacent_to_symbol(data, i, k):
                    part_numbers.append(int(digit))
                    break
            j = digit_start + len_digit
    return sum(part_numbers)


def part2(data):
    all_gears = {}
    for i, row in enumerate(data):
        j = 0
        while j < len(row):
            digit = row[j]
            if digit == "." or not digit.isdigit():
                j += 1
                continue
            digit_start = j
            len_digit = 1
            while True:
                if digit_start + len_digit >= len(row):
                    break
                if data[i][digit_start + len_digit].isdigit():
                    digit += data[i][digit_start + len_digit]
                    len_digit += 1
                else:
                    break
            for k in range(digit_start, digit_start + len_digit):
                gears = is_adjacent_to_gears(data, i, k)
                if len(gears) != 0:
                    for gear in gears:
                        if gear not in all_gears:
                            all_gears[gear] = []
                        all_gears[gear].append(int(digit))
                    break
            j = digit_start + len_digit

    gears_with_two_parts = [parts for parts in all_gears.values() if len(parts) == 2]
    gear_ratios = [parts[0] * parts[1] for parts in gears_with_two_parts]
    return sum(gear_ratios)


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
