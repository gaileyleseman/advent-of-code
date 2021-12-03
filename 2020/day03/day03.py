def parse_text(input_txt):
    data = open(input_txt, "r").read().split('\n')
    return data

def countTrees(forest, down, right):
    height = len(forest)-1
    width = len(forest[1])
    trees = 0
    i = 0
    j = 0
    while i + down <= height:
        i += down
        j += right
        if j >= width:
            j = j - width
        if forest[i][j] == '#':
            trees += 1
    return trees


def part1(input_txt):
    forest = parse_text(input_txt)
    down = 1
    right = 3
    return countTrees(forest, down, right)


def part2(input_txt):
    forest = parse_text(input_txt)
    down = [1, 1, 1, 1, 2]
    right = [1, 3, 5, 7, 1]

    total = 1
    for i in range(0, len(down)):
        trees = countTrees(forest, down[i], right[i])
        total = total * trees
    return total


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
