import numpy as np
from collections import Counter

def parse_text(input_txt):
    data = []
    with open(input_txt, "r") as f:
        for line in f.read().split('\n'):
            data.append([int(d) for d in line.split(" ") if d])
    
    data_array = np.array(data)
    return data_array


def part1(data):
    new_data = []
    for column in data.T:
        sorted_column = np.sort(column)
        new_data.append(sorted_column)
    sorted_data = np.array(new_data).T
    distances = np.abs(np.subtract(sorted_data[:,1], sorted_data[:,0]))
    total_distance = np.sum(distances)
    return total_distance


def part2(data):
    similarity_scores = Counter(data[:,1])
    total_score = 0
    for number in data[:,0]:
        total_score += number * similarity_scores.get(number, 0)
    return total_score


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
