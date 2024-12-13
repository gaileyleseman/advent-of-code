import numpy as np
import re


def parse_text(input_txt):
    with open(input_txt, "r") as file:
        raw_data = file.read().split("\n\n")

    data = []
    for set in raw_data:
        A, B, prize = set.split("\n")
        equations = np.array([re.findall(r"(\d+)", eq) for eq in [A, B, prize]], dtype=int)
        data.append((equations.T))
    return data


TOKEN_COST = np.array([3, 1])


def part1(data):
    tokens = 0
    for equations in data:
        solved = np.linalg.solve(equations[:, :-1], equations[:, -1])
        if not np.all([i % 1 == 0 for i in solved]):
            continue
        solved = np.array([int(i) for i in solved])
        tokens += int(sum(TOKEN_COST * solved))
    return tokens


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    # print("TEST: Part 2: ", part2(test_data))
    # print("Part 2: ", part2(input_data))
