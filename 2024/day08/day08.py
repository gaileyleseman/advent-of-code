import numpy as np
import itertools


def parse_text(input_txt):
    with open(input_txt, "r") as file:
        data = np.array([list(line) for line in file.read().splitlines()])
    return data


def find_antinodes(antenna_map, part: str = "1"):
    antennas_types = set(list(antenna_map.flatten()))
    antennas_types.remove(".")
    antinodes_map = np.zeros(antenna_map.shape, dtype=int)
    min = np.array([0,0])
    max = np.array(antenna_map.shape) - np.array([1,1])

    for antenna_type in antennas_types:
        xs, ys = np.nonzero(antenna_map == antenna_type)
        coordinates = [np.array([x,y]) for x,y in zip(xs, ys)]
        combos = itertools.permutations(coordinates, 2)
        for a, b in combos:
            if np.all(a == b):
                return None

            # part 
            if part == "1":
                antinode = b + (b-a)
                if np.all(antinode >= min) and np.all(antinode <= max):
                    x, y = antinode
                    antinodes_map[x,y] += 1

            # part 2
            if part == "2":
                antinode = np.copy(a)
                while np.all(antinode >= min) and np.all(antinode <= max):
                    x, y = antinode
                    antinodes_map[x, y] += 1
                    antinode += (b-a)

    return np.count_nonzero(antinodes_map)

if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", find_antinodes(test_data))
    print("Part 1: ", find_antinodes(input_data))

    print("TEST: Part 2: ", find_antinodes(test_data, part="2"))
    print("Part 2: ", find_antinodes(input_data, part="2"))
