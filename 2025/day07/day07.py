# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "numpy",
# ]
# ///
import numpy as np

def parse_text(input_txt):
    with open(input_txt, "r") as f:
        return np.array([list(line) for line in f.read().split("\n")])
    
def out_of_bounds(position, data):
    n_rows, n_cols = data.shape
    r, c = position
    if r < 0 or r >= n_rows or c < 0 or c >= n_cols:
        return True
    return False

def solve(data):
    S = np.where(data == "S")
    start_points = [tuple(map(int, (S[0][0], S[1][0])))]
    starts = {}
    splits = set()
    for start in start_points:
        if start in starts:
            continue
        start_points.extend(split_beam(start, starts, splits, data))
    print(f"part1 = {len(splits)}")
    timelines_data = {}
    print(f"part2 = {get_timelines(start_points[0], starts, timelines_data)}")


def get_timelines(position, starts, timelines_data):
    if position in timelines_data:
        return timelines_data[position]
    timelines = 0
    possible_directions = starts.get(position, [])
    if not possible_directions:
        return 1
    for p in possible_directions:
        timelines += get_timelines(p, starts, timelines_data)
    timelines_data[position] = timelines
    return timelines


def split_beam(start_position, starts, splits, data):
    pos = start_position
    while True:
        pos = (pos[0] + 1, pos[1])
        if out_of_bounds(pos, data):
            return []
        if data[pos] == "^":
            splits.add(pos)
            new_positions = [(pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
            starts[start_position] = new_positions
            return new_positions


if __name__ == "__main__":
    print("TEST")
    solve(parse_text("test.txt"))

    print("INPUT")
    solve(parse_text("input.txt"))
