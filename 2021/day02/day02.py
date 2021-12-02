import numpy as np


def parse_text(input_txt):
    data = open(input_txt, "r").read().split('\n')
    data = [line.split() for line in data]
    return data


map_directions = {"up": np.array([0, -1]),
                  "down": np.array([0, 1]),
                  "forward": np.array([1, 0])}


def move_submarine(pos, command):
    direction, units = command
    new_pos = pos + map_directions.get(direction) * int(units)
    return new_pos


def part1(input_txt):
    data = parse_text(input_txt)
    pos = np.array([0, 0])
    for command in data:
        pos = move_submarine(pos, command)
    return pos[0]*pos[1]


def part2(input_txt):
    data = parse_text(input_txt)
    pos_with_aim = np.array([0, 0, 0])
    for command in data:
        direction, units = command
        if direction == "forward":
            change = np.array([1, 0, 0]) * int(units) + np.array([0, 1, 0]) * pos_with_aim[2] * int(units)
            pos_with_aim = pos_with_aim + change
        elif direction == "up":
            pos_with_aim = pos_with_aim + np.array([0, 0, -1]) * int(units)
        elif direction == "down":
            pos_with_aim = pos_with_aim + np.array([0, 0, 1]) * int(units)
        else:
            print("unknown command.")
            break
    return pos_with_aim[0]*pos_with_aim[1]


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
