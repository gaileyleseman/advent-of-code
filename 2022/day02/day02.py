def parse_text(input_txt):
    data = []
    with open(input_txt, "r") as f:
        for line in f.read().split('\n'):
            if line == "":
                continue
            turn = line.split(" ")
            data.append((ord(turn[0])-start_number, ord(turn[1])-start_number-start_opponent))
    return data

start_number = ord("A")-1
start_opponent = 23  # 26 - 3

# A = rock      = X     = 1
# B = paper     = Y     = 2
# C = scissors  = Z     = 3
# rock, scissors = (1, 3) = 2 -> but loose
# scissors, rock = (3, 1) = -2 -> but win
hacky_win_map = {2: -1, -2: 1}

def part1(data):
    points = 0
    for turn in data: 
        win = turn[1] - turn[0]
        if win in hacky_win_map: 
            win = hacky_win_map[win]
        points += turn[1] + (win+1)*3
    return points

# X = loose = -1
# Y = draw = 0
# Z = win = 1
hacky_signal_map = {0: 3, 4: 1}

def part2(data):
    points = 0
    for turn in data:
        win = turn[1]-2
        hand_signal = (turn[0] + win)
        if hand_signal in hacky_signal_map:
            hand_signal = hacky_signal_map[hand_signal]
        points += hand_signal + (win+1)*3
    return points


if __name__ == '__main__':
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))