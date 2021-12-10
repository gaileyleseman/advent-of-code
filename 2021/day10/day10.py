def parse_text(input_txt):
    lines = open(input_txt, "r").read().split('\n')
    data = [list(line) for line in lines]
    return data


pairs = {"{": "}", "[": "]", "(": ")", "<": ">"}
score = {")": 3, "]": 57, "}": 1197, ">": 25137}
score_pt2 = {")": 1, "]": 2, "}": 3, ">": 4}


def check_corrupted(line, pairs):
    open_brackets = pairs.keys()
    close_brackets = pairs.values()
    last_open = []
    for c in line:
        if c in open_brackets:
            last_open.append(c)
        elif c in close_brackets:
            if c != pairs[last_open[-1]]:
                return True, c
            else:
                last_open.pop(-1)
    return False, None


def close_line(line, pairs):
    open_brackets = pairs.keys()
    close_brackets = pairs.values()
    last_open = []
    for c in line:
        if c in open_brackets:
            last_open.append(c)
        elif c in close_brackets:
            if c != pairs[last_open[-1]]:
                pass
            else:
                last_open.pop(-1)
    to_close = [pairs[i] for i in last_open[::-1]]
    return to_close


def part1(input_txt):
    data = parse_text(input_txt)
    syntax_error = 0
    for line in data:
        corrupt, c = check_corrupted(line, pairs)
        if corrupt:
            syntax_error += score[c]
    return syntax_error


def part2(input_txt):
    data = parse_text(input_txt)
    data = [line for line in data if not check_corrupted(line, pairs)[0]]
    completion_scores = []
    for line in data:
        score = 0
        closing_brackets = close_line(line, pairs)
        for i in closing_brackets:
            score *= 5
            score += score_pt2[i]
        completion_scores.append(score)
    middle_index = int(len(completion_scores) / 2)
    final_score = sorted(completion_scores)[middle_index]
    return final_score


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
