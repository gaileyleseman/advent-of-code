import numpy as np

def parse_text(input_txt):
    with open(input_txt, "r") as f:
        raw_data = f.read().split("\n")
    data = []
    for line in raw_data:
        coordinates = [c.split(",") for c in line.split(" -> ")]
        data.append([tuple([int(c) for c in coord]) for coord in coordinates])
    return data


def create_cave(data):
    all_x = [coord[0] for line in data for coord in line]
    all_y = [coord[1] for line in data for coord in line]
    # size of cave (with a lot of padding)
    min_x = min(all_x)-500
    max_x = max(all_x)+500
    abyss = max(all_y)+1
    floor = max(all_y)+2
    cave = np.zeros((floor+1, max_x - min_x + 1), dtype=int)

    for line in data:
        for i, start in enumerate(line[:-1]):
            end = line[i + 1]
            start = (start[0] - min_x, start[1])
            end = (end[0] - min_x, end[1])
            if start[0] == end[0]: # vertical line
                cave[min(start[1], end[1]):max(start[1], end[1])+1, start[0]] = 1
            elif start[1] == end[1]: # horizontal line
                cave[start[1], min(start[0], end[0]):max(start[0], end[0])+1] = 1
            else:
                raise ValueError("Invalid line")

    cave[floor, :] = 1
    return cave, min_x, abyss

def simulate_sand(sand, cave):
    (r, c) = sand
    down = (r + 1, c)
    left = (r + 1, c - 1)
    right = (r + 1, c + 1)

    for dir in [down, left, right]:
        if cave[dir] == 0:
            return simulate_sand(dir, cave)
    
    cave[((r, c))] = 1
    return cave



def part1(data):
    cave, start_col, abyss = create_cave(data)
    n_simulations = 0
    start = (0, 500 - start_col)
    while np.sum(cave[abyss, :]) < 1:
        cave = simulate_sand(start, cave)
        n_simulations += 1
    return n_simulations - 1


def part2(data):
    cave, start_col, _ = create_cave(data)
    n_simulations = 0
    start = (0, 500 - start_col)
    while cave[start] == 0:
        cave = simulate_sand(start, cave)
        n_simulations += 1
    return n_simulations


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
