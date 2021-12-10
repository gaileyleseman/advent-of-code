import numpy as np


def parse_text(input_txt):
    lines = open(input_txt, "r").read().split('\n')
    data = np.array([list(line) for line in lines], dtype=int)
    return data


def find_adjacent(loc, matrix):
    r, c = loc
    r_max, c_max = matrix.shape
    adjacent = []
    adjacent_locs = []
    if not r == 0:
        adjacent.append(matrix[r-1][c])
        adjacent_locs.append((r-1, c))
    if not r == r_max-1:
        adjacent.append(matrix[r+1][c])
        adjacent_locs.append((r+1, c))
    if not c == 0:
        adjacent.append(matrix[r][c-1])
        adjacent_locs.append((r, c-1))
    if not c == c_max-1:
        adjacent.append(matrix[r][c+1])
        adjacent_locs.append((r, c+1))
    return adjacent, adjacent_locs


def check_for_low_point(i, adjacent):
    if sum(i < adjacent) == len(adjacent):
        return True


def find_lowest_points(data):
    rows, columns = data.shape
    lowest_points_points = []
    lowest_points_locs = []
    for i in range(rows):
        for j in range(columns):
            point = data[i][j]
            adjacent, locs = find_adjacent((i, j), data)
            if check_for_low_point(point, adjacent):
                lowest_points_points.append(point)
                lowest_points_locs.append((i, j))
    return lowest_points_points, lowest_points_locs


def find_basin_size(loc, matrix):
    locs = [loc]
    basin_size = 1
    for loc in locs:
        r, c = loc
        point = matrix[r][c]
        adjacent, adjacent_locs = find_adjacent(loc, matrix)
        for i in range(len(adjacent)):
            if point < adjacent[i] < 9:
                if adjacent_locs[i] not in locs:
                    locs.append(adjacent_locs[i])
                    basin_size += 1
    return basin_size


def part1(input_txt):
    data = parse_text(input_txt)
    points, locs = find_lowest_points(data)
    risk_level = len(points) + sum(points)
    return risk_level


def part2(input_txt):
    data = parse_text(input_txt)
    points, locs = find_lowest_points(data)
    basin_size = []
    for loc in locs:
        basin_size.append(find_basin_size(loc, matrix=data))
    big_three = np.sort(basin_size)[-3:]
    return np.prod(big_three)


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
