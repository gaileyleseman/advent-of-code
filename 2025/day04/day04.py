# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "numpy",
# ]
# ///
import numpy as np


# TODO: maybe make utility function for convolution-like approaches
def conv2d(data, kernel):
    rows, cols = data.shape
    output = np.zeros((rows, cols))
    kernel_rows, kernel_cols = kernel.shape
    data = np.pad(data, ((kernel_rows - 1) // 2))  # assuming square kernel

    for i in range(rows):
        for j in range(cols):
            region = data[i : i + kernel_rows, j : j + kernel_cols]
            output[i, j] = np.sum(region * kernel)
    return output


def parse_text(input_txt):
    c = {".": 0, "@": 1}
    with open(input_txt, "r") as f:
        return np.array(
            [list(map(lambda x: c[x], line)) for line in f.read().splitlines()]
        )


def solve(rolls):
    neighbour_kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    accessible = np.zeros(rolls.shape)
    removed_rolls = []

    while True:
        rolls = rolls - accessible
        neighbours = conv2d(rolls, neighbour_kernel)
        accessible = np.where((rolls > 0) & (neighbours < 4), 1, 0)
        if np.sum(accessible) == 0:
            break
        removed_rolls.append(np.sum(accessible))

    print(f"part1 = {removed_rolls[0]}")
    print(f"part2 = {sum(removed_rolls)}")


if __name__ == "__main__":
    print("TEST")
    solve(parse_text("test.txt"))

    print("INPUT")
    solve(parse_text("input.txt"))
