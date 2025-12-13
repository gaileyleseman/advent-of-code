# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "numpy",
# ]
# ///
import numpy as np


def parse_text(input_txt):
    with open(input_txt, "r") as f:
        raw_data = f.read().split("\n\n")
    presents = []
    for line in raw_data[:-1]:
        raw_shape = np.array([list(row) for row in line.split(":")[-1].strip().split("\n")])
        presents.append((raw_shape == '#').astype(int))
    regions = []
    for line in raw_data[-1].split("\n"):
        area = tuple(map(int, line.split(":")[0].split("x")))
        shape_counts = np.array(list(map(int, line.split(":")[1].strip().split())))
        regions.append((area, shape_counts))
    return presents, regions


def solve_pt1(data):
    PRESENT_SHAPE = (3,3) # specific for input!

    presents, regions = data
    presents_occupancy = np.array([np.sum(p) for p in presents])
    regions_filtered = []
    answer = 0
    
    for shape, counts in regions:
        rows, cols = shape
        total_occupancy = np.dot(counts, presents_occupancy)
        if total_occupancy > rows*cols: # never fits
            continue
        max_shapes_no_overlap = rows//PRESENT_SHAPE[0] * cols//PRESENT_SHAPE[1]
        if np.sum(counts) <= max_shapes_no_overlap: # always fits
            answer += 1
            continue
        regions_filtered.append((shape, counts))
    
    for shape, counts in regions_filtered:
        # prank, do not exist
        pass

    print(f"{answer=}")


if __name__ == "__main__":
    print("TEST")
    # solve_pt1(parse_text("test.txt"))

    print("INPUT")
    solve_pt1(parse_text("input.txt"))
