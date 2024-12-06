import numpy as np

GUARD = "^"
OBSTACLE = "#"
VISITED = "X"


def parse_text(input_txt):
    with open(input_txt, "r") as file:
        data = [list(line) for line in file.read().splitlines()]
    data = np.array(data)
    return data


def find_symbol(slice: np.ndarray, symbol: str):
    try:
        r, c = np.nonzero(slice == symbol)
        return True, np.array([r[0], c[0]])
    except IndexError:
        return False, np.array(slice.shape) + np.array([1, 1])


def turn_right(direction: np.ndarray):
    return np.array([direction[1], -direction[0]])


def direction_to_letter(direction: np.ndarray):
    if np.all(direction == np.array([0, 1])):
        return "R"
    if np.all(direction == np.array([0, -1])):
        return "L"
    if np.all(direction == np.array([1, 0])):
        return "D"
    if np.all(direction == np.array([-1, 0])):
        return "U"


def get_slice_parameters(coordinate: int, direction: int, include_start: bool = False):
    start = coordinate + (0 if include_start else direction)
    if direction == 0:
        stop = coordinate + 1
        step = None
    else:
        stop = None
        step = np.sign(direction)
    return start, stop, step


def get_slice(coordinate: np.ndarray, direction: np.ndarray):
    """Get all symbols in a bee-line from a coordinate in a given direction"""
    slices = []
    for c, d in zip(coordinate, direction):
        start, stop, step = get_slice_parameters(c, d, include_start=False)
        slices.append(slice(start, stop, step))
    return tuple(slices)


def get_path(coordinate: np.ndarray, direction: np.ndarray, guard_map: np.ndarray):
    map_slice = guard_map[get_slice(coordinate, direction)]
    within_bounds, line = find_symbol(map_slice, OBSTACLE)
    path = line * direction
    return within_bounds, path


def get_slice_with_path(coordinate: np.ndarray, path: np.ndarray):
    """Get all symbols from a coordinate in a given path"""
    slices = []
    for c, p in zip(coordinate, path):
        start, stop, step = get_slice_parameters(c, p, include_start=True)
        end_of_path = c + p
        if start != end_of_path and end_of_path >= 0:
            stop = end_of_path
        slices.append(slice(start, stop, step))
    return tuple(slices)


def part1(data):
    guard_map = data.copy()
    within_bounds, guard = find_symbol(guard_map, GUARD)
    direction = np.array([-1, 0])
    while within_bounds:
        within_bounds, path = get_path(guard, direction, guard_map)
        guard_map[get_slice_with_path(guard, path)] = VISITED
        guard += path
        direction = turn_right(direction)
    return np.count_nonzero(guard_map == VISITED)

def find_infinite_loop(guard: np.ndarray, original_path: np.ndarray, direction: np.ndarray, guard_map: np.ndarray):
    options = 0
    possible_guard = guard.copy()
    possible_direction = turn_right(direction)
    next_turn = direction_to_letter(turn_right(possible_direction))
    while np.any(possible_guard != (guard + original_path)):
        possible_guard += direction
        possible_slice = guard_map[get_slice(possible_guard, possible_direction)]
        x = "".join(list(possible_slice.flatten()))
        if f"{next_turn}{OBSTACLE}" in x:
            options += 1
    return options

def part2(data):
    guard_map = data.copy()
    within_bounds, guard = find_symbol(guard_map, GUARD)
    direction = np.array([-1, 0])
    total = 0
    while within_bounds:
        within_bounds, path = get_path(guard, direction, guard_map)
        guard_map[get_slice_with_path(guard, path)] = VISITED
        guard_map[guard[0], guard[1]] = direction_to_letter(direction)

        total += find_infinite_loop(guard, path, direction, guard_map)

        guard += path
        direction = turn_right(direction)

    with open("guard_map.txt", "w") as file:
        for line in guard_map:
            file.write("".join(line) + "\n")
    return total


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
