def parse_text(input_txt):
    with open(input_txt, "r") as f:
        raw_stacks, raw_instructions = f.read().split('\n\n')
    
    instructions = []
    for line in raw_instructions.split("\n"):
        instructions.append([int(i) for i in line.split(" ") if i.isnumeric()])

    indicators = raw_stacks.split("\n")[-1]
    stack_values = raw_stacks.split("\n")[-2::-1]
    stacks = []
    for i in range(len(indicators)):
        if indicators[i].isnumeric():
            stack = ""
            for line in stack_values:
                stack += line[int(i)]
            stacks.append(list(stack.strip()))

    return [stacks, instructions]


def part1(data):
    original_stacks, instructions = data
    stacks = [stack.copy() for stack in original_stacks]
    for line in instructions:
        n = line[0]
        original = line[1]-1
        new = line[2]-1
        for _ in range(n):
            stacks[new].append(stacks[original].pop())
    answer = "".join([i[-1] for i in stacks])
    return answer


def part2(data):
    original_stacks, instructions = data
    stacks = [stack.copy() for stack in original_stacks]

    for line in instructions:
        n = line[0]
        original = line[1]-1
        new = line[2]-1

        stacks[new].extend(stacks[original][-n:])
        stacks[original] = stacks[original][:-n]

    answer = "".join([i[-1] for i in stacks])
    return answer


if __name__ == '__main__':
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
