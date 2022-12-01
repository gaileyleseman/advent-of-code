def parse_text(input_txt):
    raw_data = open(input_txt, "r").read().split('\n\n')
    data = [i.split('\n') for i in raw_data]
    return data


def get_total_calories(data):
    total_calories = []
    for elf in data:
        calories = sum([int(snack) for snack in elf])
        total_calories.append(calories)
    return total_calories

def part1(input_txt):
    data = parse_text(input_txt)
    total_calories = get_total_calories(data)
    return max(total_calories)


def part2(input_txt):
    data = parse_text(input_txt)
    total_calories = get_total_calories(data)
    total_calories.sort()
    return(sum(total_calories[-3:]))


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))