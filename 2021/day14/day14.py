import time

def parse_text(input_txt):
    template, raw_data = open(input_txt, "r").read().split('\n\n')
    data = [line.split(" -> ") for line in raw_data.split("\n")]
    rules = {i[0]:i[1] for i in data}
    return template, rules


def update_polymer(polymer, rules):
    new_polymer = ""
    for i in range(len(polymer) - 1):
        check = polymer[i:i + 2]
        next_check = polymer[i+1:i + 3]

        new_polymer += polymer[i]
        if check not in rules:
            continue
        new_polymer += rules[check]
        if next_check not in rules:
            new_polymer += polymer[i+1]
    return new_polymer
    

def part1(input_txt):
    polymer, rules = parse_text(input_txt)
    steps = 10
    for k in range(steps):
        polymer = update_polymer(polymer, rules)
    count = [polymer.count(L) for L in set(polymer)]
    return max(count) - min(count)


def part2(input_txt):
    polymer, rules = parse_text(input_txt)
    steps = 40
    for k in range(steps):
        polymer = update_polymer(polymer, rules)
    count = [polymer.count(L) for L in set(polymer)]
    return max(count) - min(count)


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
