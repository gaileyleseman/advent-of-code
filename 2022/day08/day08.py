import numpy as np

def parse_text(input_txt):
    with open(input_txt, "r") as f:
        lines = [list(line) for line in f.read().split('\n')]
        data = np.matrix(lines, dtype=int)
    return data


def check_visible(tree, forest):
    t = forest[tree]
    r, c = tree

    up = (forest[:r,c] < t).all()
    down = (forest[r+1:,c] < t).all()
    left = (forest[r,:c] < t).all()
    right = (forest[r,c+1:] < t).all()

    return np.array([up, down, left, right]).any()


def get_scenery_score(tree, forest):
    t = forest[tree]
    r, c = tree
    
    up = np.flip(forest[:r,c].getA1())
    down = forest[r+1:,c].getA1()
    left = np.flip(forest[r,:c].getA1())
    right = forest[r,c+1:].getA1()
    
    total_score = 1
    for direction in [up, left, down, right]:
        score = 0
        for next_tree in direction:
            score += 1
            if next_tree >= t:
                break
        total_score *= score
    return total_score

def part1(data):
    rows, cols = data.shape
    visible = 2*rows + 2*(cols-2) # outer edges
    
    for r in range(1,rows-1):
        for c in range(1, cols-1):
            if check_visible((r,c), data): 
                visible += 1
    return visible


def part2(data):
    rows, cols = data.shape
    score = 0
    for r in range(rows):
        for c in range(cols):
            score = max(score, get_scenery_score((r,c), data))
    return score


if __name__ == '__main__':
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
