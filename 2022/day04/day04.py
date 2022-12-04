def parse_text(input_txt):
    with open(input_txt, "r") as f:
        raw_data = [line.split(",") for line in f.read().split('\n')]
        data = []
        for line in raw_data:
            sections = []
            for elf in line:
                sections.append([int(i) for i in elf.split("-")])
            data.append(sections)
    return data


def part1(data):
    count = 0
    for elf1, elf2 in data:
        if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
            count += 1
        elif elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:
            count += 1
    return count


def part2(data):
    count = 0
    for elf1, elf2 in data:
        to_check = range(elf2[0], elf2[1]+1)
        for i in range(elf1[0], elf1[1]+1):
            if i in to_check:
                count += 1
                break
    return count   


if __name__ == '__main__':
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
