def parse_text(input_txt):
    with open(input_txt, "r") as f:
        data = [line.split(" ") for line in f.read().split('\n')]
    return data

def get_signal_strength(data, goal_cycle):
    n_cycles = 0
    strength = 1
    for command in data:
        if command[0] == "addx":
            n_cycles += 2
            if n_cycles >= goal_cycle:
                break
            strength += int(command[1])
        if command[0] == "noop":
            n_cycles += 1
    return strength

def part1(data):
    signal_strenghts = [i*get_signal_strength(data, i) for i in range(20,260,40)]
    return sum(signal_strenghts)

# emoji unicode
black = u"\u2B1B"
white = u"\u2B1C"


def part2(data):
    CRT = []
    w = 40
    h = 6
    lines = [(i, i+w) for i in range(0,w*h, w)]
    for start, stop in lines:
        sprite = ""
        for i in range(start, stop):
            x = get_signal_strength(data, i+1)
            pixel = white if x-1 <= i%w <= x+1 else black
            sprite += pixel
        CRT.append(sprite)
    for line in CRT:
        print(line)
    return 0


if __name__ == '__main__':
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ")
    part2(test_data)
    print("Part 2: ")
    part2(input_data)
