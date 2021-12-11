import numpy as np


def parse_text(input_txt):
    lines = open(input_txt, "r").read().split('\n')
    data = np.array([list(line) for line in lines], dtype=int)
    return data


def find_adjacent(loc, matrix):
    r0, c0 = loc
    adjacent = []
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            new_loc = (r0 + r, c0 + c)
            if -1 in new_loc or loc == new_loc:
                continue
            try:
                index_check = matrix[new_loc]
                adjacent.append(new_loc)
            except IndexError:
                pass
    return adjacent


def flash_octopus(octopuses, flashes):
    flash_locs = np.argwhere(octopuses > 9)
    for i, j in flash_locs:
        if flashes[i][j]:
            continue
        else:
            flashes[i][j] = True
            adjacent = find_adjacent((i, j), octopuses)
            for loc in adjacent:
                octopuses[loc] += 1
    if np.count_nonzero(octopuses > 9) != np.count_nonzero(flashes):
        octopuses, flashes = flash_octopus(octopuses, flashes)
    return octopuses, flashes




def part1(input_txt):
    octopuses = parse_text(input_txt)
    steps = 100
    flash_count = 0
    flashes = np.zeros(octopuses.shape, dtype=bool)
    for step in range(steps + 1):
        flash_count += np.count_nonzero(flashes)            # count flashes
        flashes = np.zeros(octopuses.shape, dtype=bool)     # reset flashes
        octopuses[octopuses > 9] = 0                        # reset octopuses
        octopuses += 1                                      # increment energy level for each octopus
        octopuses, flashes = flash_octopus(octopuses, flashes)  # check recursively for flashes
    return flash_count


def part2(input_txt):
    octopuses = parse_text(input_txt)
    steps = 0
    synchronized = False
    flashes = np.zeros(octopuses.shape, dtype=bool)
    while not synchronized:
        flashes_step = np.count_nonzero(flashes)            # count flashes
        if flashes_step == octopuses.size:
            return steps
        flashes = np.zeros(octopuses.shape, dtype=bool)     # reset flashes
        octopuses[octopuses > 9] = 0                        # reset octopuses
        octopuses += 1                                      # increment energy level for each octopus
        octopuses, flashes = flash_octopus(octopuses, flashes)  # check recursively for flashes
        steps += 1
    return 0


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
