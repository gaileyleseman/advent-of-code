import itertools


def parse_text(input_txt):
    with open(input_txt, "r") as f:
        return [tuple(map(int, line.split(","))) for line in f.read().split("\n")]


def solve_pt1(data):
    pairs = itertools.combinations(data, 2)
    areas = [get_area(pair) for pair in pairs]
    print(f"part1 = {max(areas)}")


def get_area(pair):
    x1, y1 = pair[0]
    x2, y2 = pair[1]
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


if __name__ == "__main__":
    print("TEST")
    test_data = parse_text("test.txt")
    solve_pt1(test_data)

    print("INPUT")
    data = parse_text("input.txt")
    solve_pt1(data)
