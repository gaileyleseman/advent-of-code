def parse_text(input_txt):
    data = open(input_txt, "r").read().split('\n')
    return data


def getSeatLocation(boarding_pass):
    row = int(boarding_pass[0:7].replace("F", "0").replace("B", "1"), 2)
    col = int(boarding_pass[7:].replace("L", "0").replace("R", "1"), 2)
    return row, col


def getSeatID(loc):
    return loc[0] * 8 + loc[1]


def part1(input_txt):
    boarding_passes = parse_text(input_txt)
    locs = []
    ids = []
    for boarding_pass in boarding_passes:
        loc = getSeatLocation(boarding_pass)
        locs.append(loc)
        ids.append(getSeatID(loc))
    return max(ids)


def part2(input_txt):
    boarding_passes = parse_text(input_txt)
    locs = []
    ids = []
    for boarding_pass in boarding_passes:
        loc = getSeatLocation(boarding_pass)
        locs.append(loc)
        ids.append(getSeatID(loc))
    ids.sort()
    for k in range(0, len(ids) - 1):
        if ids[k + 1] - ids[k] != 1:
            return ids[k] + 1

if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
