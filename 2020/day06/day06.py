def parse_text(input_txt):
    data = open(input_txt, "r").read().split('\n\n')
    return data


def part1(input_txt):
    input = parse_text(input_txt)
    n_total = 0
    for group in input:
        questions = set(group)
        if '\n' in questions:
            questions.remove('\n')
        n_total += len(questions)
    return n_total


def part2(input_txt):
    input = parse_text(input_txt)
    n_total = 0
    for group in input:
        n_persons = len(group.split('\n'))
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            n_answered = group.count(letter)
            if n_answered == n_persons:
                n_total += 1
    return n_total


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
