import numpy as np


def parse_text(input_txt):
    with open(input_txt, "r") as f:
        raw_data = [line.split("=") for line in f.read().split("\n")]
    data = []
    for line in raw_data:
        sensor_x = int(line[1].split(",")[0])
        sensor_y = int(line[2].split(":")[0])
        beacon_x = int(line[3].split(",")[0])
        beacon_y = int(line[4])
        data.append([(sensor_y, sensor_x), (beacon_y, beacon_x)])
    return data


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def part1(data, question_row=10):
    detected_row = {}
    for sensor, beacon in data:
        sr = sensor[0]
        sc = sensor[1]
        if sr == question_row:
            detected_row[sensor[1]] = "S"
        elif beacon[0] == question_row:
            detected_row[beacon[1]] = "B"

        dist = manhattan_distance(sensor, beacon)
        for row in range(sr - dist, sr + dist + 1):
            if row != question_row:
                continue
            for col in range(sc - dist + abs(row - sr), sc + dist - abs(row - sr) + 1):
                if col not in detected_row:
                    detected_row[col] = "#"

    return(list(detected_row.values()).count("#"))

def part2(data, size):
    map = np.zeros((size, size), dtype=bool)
    for sensor, beacon in data:
        sr = sensor[0]
        sc = sensor[1]
        if 0 <= sr < size and 0 <= sc < size:
            map[sr, sc] = True
        if 0 <= beacon[0] < size - 1 and 0 <= beacon[1] < size - 1:
            map[beacon[0], beacon[1]] = True

        dist = manhattan_distance(sensor, beacon)
        min_row = max(0, sr - dist)
        max_row = min(size - 1, sr + dist)
        for row in range(min_row, max_row + 1):
            min_col = max(0, sc - dist + abs(row - sr))
            max_col = min(size - 1, sc + dist - abs(row - sr))
            map[row, min_col:max_col + 1] = True

    beacon_y, beacon_x = np.where(map == False)
    return 4000000*beacon_x + beacon_y


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data, 10))
    # print("Part 1: ", part1(input_data, 2000000))

    print("TEST: Part 2: ", part2(test_data, 20))
    print("Part 2: ", part2(input_data, 4000000))
