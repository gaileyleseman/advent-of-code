import numpy as np


def parse_text(input_txt):
    with open(input_txt, "r") as file:
        data = np.array([list(line) for line in file.read().splitlines()], dtype=int)
    return data


class Directions:
    LEFT = np.array([-1, 0])
    UP = np.array([0, -1])
    RIGHT = np.array([1, 0])
    DOWN = np.array([0, 1])


DIRECTIONS = [Directions.LEFT, Directions.UP, Directions.RIGHT, Directions.DOWN]
TRAIL_END = 9


def within_bounds(data, position):
    return np.all(position >= 0) and np.all(position < data.shape)


def find_next_steps(data, current_position):
    next_height = data[tuple(current_position)] + 1
    next_steps = []
    for direction in DIRECTIONS:
        next_position = current_position + direction
        if not within_bounds(data, next_position):
            continue
        if data[tuple(next_position)] == next_height:
            next_steps.append(next_position)
    return next_height, next_steps


def find_paths_to_end(data, current_position):
    next_height, next_steps = find_next_steps(data, current_position)
    if next_height == TRAIL_END:
        return next_steps
    paths = []
    for next_step in next_steps:
        new_paths = find_paths_to_end(data, next_step)
        paths.extend(new_paths)
    return paths


def solve(data):
    possible_trailheads = np.argwhere(data == 0)
    score_pt1 = 0
    score_pt2 = 0
    for trail in possible_trailheads:
        paths = find_paths_to_end(data, trail)
        score_pt1 += len(set([tuple(path) for path in paths]))
        score_pt2 += len(paths)

    return score_pt1, score_pt2

if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    test1, test2 = solve(test_data)
    input1, input2 = solve(input_data)

    print("TEST: Part 1: ", test1)
    print("Part 1: ", input1)

    print("TEST: Part 2: ", test2)
    print("Part 2: ", input2)
