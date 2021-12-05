import re
import numpy as np

def parse_text(input_txt):
    data = open(input_txt, "r").read().split('\n')
    data = [list(map(int, re.split(',| -> ', line))) for line in data]
    data = np.array(data, dtype=object)
    return data

def get_start_and_end(line, shape):
    x_max, y_max = shape
    x1, y1, x2, y2 = line
    x_start = min(min(x1, x2), x_max -1)
    x_end = min(max(x1, x2), x_max-1) + 1
    y_start = min(min(y1, y2), y_max -1)
    y_end = min(max(y1, y2), y_max-1) + 1
    return x_start, x_end, y_start, y_end


def draw_straight_lines(diagram, data):
    shape = diagram.shape
    for line in data:
        x1, y1, x2, y2 = line
        if x1 == x2 or y1 == y2:    # horizontal lines
            x_start, x_end, y_start, y_end = get_start_and_end(line, shape)
            diagram[y_start:y_end, x_start:x_end] += 1
    return diagram

def draw_diagional_lines(diagram, data):
    for line in data:
        x1, y1, x2, y2 = line
        if abs(x1 - x2) == abs(y1 - y2):
            i = list(range(x1, x2+1) if x1 < x2 else reversed(range(x2, x1+1)))
            j = list(range(y1, y2+1) if y1 < y2 else reversed(range(y2, y1+1)))
            for k in range(abs(x1-x2)+1):
                diagram[j[k], i[k]] += 1
    return diagram




def part1(input_txt):
    data = parse_text(input_txt)
    x1_max, y1_max, x2_max, y2_max = data.max(axis=0)
    diagram = np.zeros((max(x1_max, x2_max)+1, max(y1_max, y2_max)+1))
    diagram = draw_straight_lines(diagram, data)
    overlap = np.count_nonzero(diagram > 1)
    return overlap


def part2(input_txt):
    data = parse_text(input_txt)
    x1_max, y1_max, x2_max, y2_max = data.max(axis=0)
    diagram = np.zeros((max(x1_max, x2_max)+1, max(y1_max, y2_max)+1))
    diagram = draw_straight_lines(diagram, data)
    diagram = draw_diagional_lines(diagram, data)
    overlap = np.count_nonzero(diagram > 1)
    return overlap


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
