# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "shapely",
# ]
# ///
import shapely
import itertools

def parse_text(input_txt):
    with open(input_txt, "r") as f:
        return [tuple(map(int, line.split(","))) for line in f.read().split("\n")]


def solve(data):
    pairs = itertools.combinations(data, 2)
    areas = {pair: get_area(pair) for pair in pairs}
    areas_sorted = sorted(areas.items(), key=lambda x: x[1], reverse=True)

    print(f"part1 = {areas_sorted[0][1]}")
    data.append(data[0])
    tiles = shapely.Polygon(data)
    for pair, area in areas_sorted:
        x0, y0, = pair[0]
        x1, y1  = pair[1]    
        rectangle = shapely.Polygon([(x0, y0),(x1, y0), (x1, y1), (x0, y1), (x0, y0)])
        if tiles.contains(rectangle):
            print(f"part2 = {area}") 
            return

def get_area(pair):
    x1, y1 = pair[0]
    x2, y2 = pair[1]
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


if __name__ == "__main__":
    print("TEST")
    test_data = parse_text("test.txt")
    solve(test_data)

    print("INPUT")
    data = parse_text("input.txt")
    solve(data)