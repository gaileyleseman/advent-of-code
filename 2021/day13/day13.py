import numpy as np


def parse_text(input_txt):
    raw_data, raw_instructions = open(input_txt, "r").read().split('\n\n')
    data = np.array([line.split(",")for  line in raw_data.split("\n")], dtype=int)
    instructions = [line.split("=") for line in raw_instructions.split("\n")]
    instructions = [(i[0][-1], int(i[1])) for i in instructions]
    return data, instructions


def populate_matrix(data):
    cols, rows = np.max(data, axis=0) + [1, 1]

    matrix = np.zeros((rows, cols))
    for line in data:
        loc = tuple(np.flip(line))
        matrix[loc] = 1
    return matrix


def fold(matrix, ax, line):
    mat = matrix if ax == "y" else matrix.T
    top = mat[:][:line]
    bottom = mat[:][(line+1):]
    if top.shape[0] > bottom.shape[0]:
        folded = top
        folded[1:][:] += np.flip(bottom, axis=0)
    else:
        folded = top + np.flip(bottom, axis=0)
    return folded if ax == "y" else folded.T


def draw_matrix(matrix):
    print("")
    for row in matrix:
        line = "".join(["##" if i >= 1 else "  " for i in row])
        print(line)



def part1(input_txt):
    data, instructions = parse_text(input_txt)
    matrix = populate_matrix(data)
    i = instructions[0]
    folded = fold(matrix, i[0], i[1])
    dots = np.count_nonzero(folded >= 1)
    return dots


def part2(input_txt):
    data, instructions = parse_text(input_txt)
    matrix = populate_matrix(data)
    for i in instructions:
        folded = fold(matrix, i[0], i[1])
        matrix = folded
    print("Part 2:")
    draw_matrix(matrix)


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    part2(test_txt)
    part2(input_txt)
