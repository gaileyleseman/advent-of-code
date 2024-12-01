import numpy as np
from collections import Counter

def parse_text(input_txt):
    data_array = np.loadtxt(input_txt, dtype=int)
    return data_array

def part1(data):
    sorted_data = np.sort(data, axis=0)
    distances = np.abs(np.diff(sorted_data, axis=1))
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
