import math


def parse_text(input_txt):
    with open(input_txt, "r") as f:
        data = f.read().split("\n")
    data = [row.strip() for row in data if row != ""]
    return data


def part1(data):
    sum = 0
    for row in data:
        digits = [c for c in row if c.isdigit()]
        number = digits[0] + digits[-1]
        sum += int(number)
    return sum


VALID_DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part2(data):
    sum = 0
    for row in data:
        first_digit_index = math.inf
        last_digit_index = -math.inf
        first_digit = ""
        last_digit = ""

        for digit_word, digit in VALID_DIGITS.items():
            first_index_word = row.find(digit_word)
            first_index_digit = row.find(str(digit))
            last_index_word = row.rfind(digit_word)
            last_index_digit = row.rfind(str(digit))

            if first_index_word >= 0 and first_index_word < first_digit_index:
                first_digit_index = first_index_word
                first_digit = digit

            if first_index_digit >= 0 and first_index_digit < first_digit_index:
                first_digit_index = first_index_digit
                first_digit = digit

            if last_index_word >= 0 and last_index_word > last_digit_index:
                last_digit_index = last_index_word
                last_digit = digit

            if last_index_digit >= 0 and last_index_digit > last_digit_index:
                last_digit_index = last_index_digit
                last_digit = digit

        number = first_digit + last_digit
        sum += int(number)

    return sum


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    # print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
