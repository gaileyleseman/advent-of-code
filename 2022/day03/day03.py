def parse_text(input_txt):
    with open(input_txt) as f:
        data = f.read().split('\n')
    return data

def get_priority(item):
    if item.islower():
        return ord(item)- ord("a") + 1
    if item.isupper():
        return ord(item) - ord("A") + 27
    print("unknown character")


def part1(data):
    priorities = []
    for rucksack in data:
        half_items = int(len(rucksack)/2)
        c1, c2 = (rucksack[:half_items], rucksack[half_items:])
        rucksack_priorities = [get_priority(item) for item in set(c1) if item in c2]
        priorities.append(sum(rucksack_priorities))
    return sum(priorities)


def part2(data):
    priorities = []
    for i in range(int(len(data)/3)):
        e1, e2, e3 = data[i*3:(i+1)*3]
        badge = [get_priority(item) for item in set(e1) if (item in e2 and item in e3)]
        priorities.append(sum(badge))
    return sum(priorities)


if __name__ == '__main__':
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))


    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
