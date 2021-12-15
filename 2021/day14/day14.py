import time

def parse_text(input_txt):
    template, raw_data = open(input_txt, "r").read().split('\n\n')
    data = [line.split(" -> ") for line in raw_data.split("\n")]
    return template, data


polymer_letters = ["B", "C", "N", "H"]

def insert(polymer, to_insert):
    k = 0
    for i, c in to_insert:
        polymer = polymer[:i+k] + c + polymer[i+k:]
        k += 1
    return polymer


def update_polymer(polymer, rules, steps):
    for k in range(steps):
        to_insert = []
        for i in range(len(polymer) - 1):
            check = polymer[i:i + 2]
            for pair, element in rules:
                if check == pair:
                    to_insert.append([i+1, element])
        polymer = insert(polymer, to_insert)
    return polymer


def part1(input_txt):
    polymer, rules = parse_text(input_txt)
    steps = 40
    t = time.time()
    polymer = update_polymer(polymer, rules, steps)
    print(time.time() - t)
    count = [polymer.count(L) for L in polymer_letters]
    return max(count) - min(count)


def part2(input_txt):
    data = parse_text(input_txt)
    return 0


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
