
def parse_text(input_txt):
    data = open(input_txt, "r").read().split('\n')
    data = [int(i) for i in data]
    return data

def check_increases(data):
    num_increases = 0
    for i in range(len(data)-1):
        if data[i+1] > data[i]:
            num_increases += 1
    return num_increases

def part1(input_txt):
    data = parse_text(input_txt)
    return check_increases(data)

def part2(input_txt):
    data = parse_text(input_txt)
    sliding_window_data = []

    for i in range(len(data)):
        if len(data)-i > 2:
            sliding_window_data.append(sum(data[i:i+3]))
    return check_increases(sliding_window_data)


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))

