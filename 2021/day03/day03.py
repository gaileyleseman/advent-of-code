import numpy as np


def parse_text(input_txt):
    raw_data = open(input_txt, "r").read().split('\n')
    return raw_data


def parse_to_data(input_txt):
    raw_data = parse_text(input_txt)
    data = [list(line) for line in raw_data]
    data = [[int(i) for i in j] for j in data]
    data = np.array(data, dtype=object)
    return data


def find_most_and_least_common_bit(data):
    data = data.T
    most_common = ""
    least_common = ""
    for row in data:
        ones = sum(row)
        zeroes = len(row) - ones
        if ones >= zeroes:  # most common bit is 1
            most_common += "1"
            least_common += "0"
        else:  # most common bit is 0
            most_common += "0"
            least_common += "1"
    return most_common, least_common


def part1(input_txt):
    data = parse_to_data(input_txt)
    gamma_rate, epsilon_rate = find_most_and_least_common_bit(data)
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    return gamma_rate * epsilon_rate


def check_data_for_pos(data, i, option):
    most_common, least_common = find_most_and_least_common_bit(data)
    if option == "most":
        x_common = most_common
    elif option == "least":
        x_common = least_common

    rows_to_keep = []
    for row in range(len(data)):
        bit = data[row][i]
        if str(bit) == x_common[i]:
            rows_to_keep.append(row)
    data = data[rows_to_keep]
    return data


def find_final_number(data, option):
    for i in range(len(data[0])):
        data = check_data_for_pos(data, i, option)
        if len(data) == 1:
            break

    final_number = "".join([str(i) for i in data[0]])
    final_number = int(final_number, 2)
    return final_number


def part2(input_txt):
    data = parse_to_data(input_txt)
    oxygen_generator_rating = find_final_number(data, "most")
    co2_scrubber_rating = find_final_number(data, "least")
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    return life_support_rating


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
