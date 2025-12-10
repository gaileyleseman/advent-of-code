# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "numpy",
# ]
# ///
import numpy as np

import itertools


def parse_text(input_txt):
    with open(input_txt, "r") as f:
        raw_data = [line.split(" ") for line in f.read().split("\n")]
    data = []
    lights_map = lambda c: (-1 if c == "#" else 1) #noqa
    for line in raw_data:
        indicators = np.array(list(map(lights_map, line.pop(0)[1:-1])), dtype=int)
        joltages = np.array(list(line.pop(-1)[1:-1].split(",")), dtype=int)
        buttons = [list(map(int, b[1:-1].split(","))) for b in line]
        data.append((indicators, buttons, joltages))
    return data


def solve_pt1(data):
    answer = 0
    for goal, buttons, _ in data:
        button_matrix = get_button_matrix(goal, buttons) * -1 | 1
        possible_presses = sorted(
            itertools.product([0, 1], repeat=len(buttons)), key=lambda x: (sum(x), x)
        )
        for presses in possible_presses:
            result = np.prod(button_matrix ** np.array(presses), axis=1)
            if (result == goal).all():
                answer += sum(presses)
                break
    print(f"part1 = {answer}")


def solve_pt2(data):
    answer = 0
    for _, buttons, goal in data:
        counter = np.inf
        button_matrix = get_button_matrix(goal, buttons) * 1
        for presses in itertools.product(range(max(goal + 1)), repeat=len(buttons)):
            result = np.dot(button_matrix, np.array(presses))
            if (result > goal).any():
                continue
            if (result == goal).all():
                counter = min(sum(presses), counter)
        answer += counter
        print(f"\t{counter=}")
    print(f"part2 = {answer}")


def get_button_matrix(goal, buttons):
    mat = np.zeros((len(goal), len(buttons)), dtype=bool)
    for c, button in enumerate(buttons):
        for r in button:
            mat[(r, c)] = True
    return mat


if __name__ == "__main__":
    print("TEST")
    test_data = parse_text("test.txt")
    solve_pt1(test_data)
    solve_pt2(test_data)

    print("INPUT")
    data = parse_text("input.txt")
    solve_pt1(data)
    solve_pt2(data)
