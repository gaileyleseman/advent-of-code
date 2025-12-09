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
        return [tuple(map(int, line.split(","))) for line in f.read().split("\n")]


def solve(data):
    pairs = itertools.combinations(data, 2)
    areas = {pair: get_area(pair) for pair in pairs}
    areas_sorted = sorted(areas.items(), key=lambda x: x[1], reverse=True)

    print(f"part1 = {areas_sorted[0][1]}")

    grid, corner_pairs = get_grid_and_corner_pairs(data)
    for i, (pair, area) in enumerate(areas_sorted):
        if pair not in corner_pairs:
            continue
        rr = (pair[0][1], pair[1][1])
        cc = (pair[0][0], pair[1][0])
        all_true = grid[min(rr):max(rr)+1, min(cc):max(cc)+1].all()
        if all_true:
            print(f"part2 = {area}")
            return



def get_grid_and_corner_pairs(data):
    x, y = zip(*data)
    grid = np.zeros((max(y) + 1, max(x) + 1), dtype=bool)

    n_coordinates = len(data)
    corner_pairs = []
    for i in range(n_coordinates):
        j  = (i + 1) % n_coordinates # for a line
        k = (i + 2) % n_coordinates # for a rectangle

        r0, r1, r2 = y[i], y[j], y[k]
        c0, c1, c2 = x[i], x[j], x[k]

        grid[min(r0, r1):max(r0, r1)+1, min(c0, c1):max(c0, c1)+1] = True

        p0 = np.array([r0, c0])
        p1 = np.array([r1, c1])
        p2 = np.array([r2, c2])
        vector_ji = p0 - p1
        vector_jk = p2 - p1
        cross = vector_ji[0] * vector_jk[1] - vector_ji[1] * vector_jk[0]

        if cross > 0:
            corner_pairs.append((data[i], data[k]))
    
    # Source - https://stackoverflow.com/questions/60049171/fill-values-in-numpy-array-that-are-between-a-certain-value
    # Posted by Andy L., modified by community. See post 'Timeline' for change history
    # Retrieved 2025-12-09, License - CC BY-SA 4.0
    grid_filled = np.bitwise_xor.accumulate(grid) | grid


    return grid_filled, corner_pairs


def get_area(pair):
    x1, y1 = pair[0]
    x2, y2 = pair[1]
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


if __name__ == "__main__":
    print("TEST")
    test_data = parse_text("test.txt")
    solve(test_data)

    print("INPUT")
    data = parse_text("input.txt")
    # solve(data)
    print("done")
