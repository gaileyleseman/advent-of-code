def parse_text(input_txt):
    data = open(input_txt, "r").read().split('\n')
    return data


def part1(input_txt):
    data = parse_text(input_txt)
    valid = 0
    for i in range(len(data)):
        [policy, letter, password] = data[i].split(' ')
        [min, max] = policy.split('-')
        letter = letter[0]
        if int(min) <= password.count(letter) <= int(max):
            valid += 1
    return valid


def part2(input_txt):
    data = parse_text(input_txt)
    valid = 0
    for i in range(len(data)):
        policy = data[i].split(' ')
        [pos1, pos2] = policy[0].split('-')
        letter = policy[1][0]
        letters = policy[2][int(pos1) - 1] + policy[2][int(pos2) - 1]
        if letters.count(letter) == 1:
            valid += 1
    return valid


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
