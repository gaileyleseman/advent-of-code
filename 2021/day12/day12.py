import collections


def parse_text(input_txt):
    lines = open(input_txt, "r").read().split('\n')
    data = [line.split("-") for line in lines]
    return data


def create_cave_map(data):
    cave_map = collections.defaultdict(list)
    for path in data:
        start_cave, end_cave = path
        cave_map[start_cave].append(end_cave)
        cave_map[end_cave].append(start_cave)
    return cave_map


def find_paths_to_end(cave, cave_map, previous_caves):
    count = 0
    paths = cave_map[cave]
    for new_cave in paths:
        previous = previous_caves.copy()
        if new_cave.islower():
            if new_cave == "end":
                count += 1
                continue
            if new_cave in previous:
                continue
        previous.append(new_cave)
        count += find_paths_to_end(new_cave, cave_map, previous)
    return count



def part1(input_txt):
    data = parse_text(input_txt)
    cave_map = create_cave_map(data)
    previous_caves = ["start"]
    num_paths = find_paths_to_end("start", cave_map, previous_caves)
    return num_paths


def part2(input_txt):
    data = parse_text(input_txt)
    cave_map = create_cave_map(data)
    return 0


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
