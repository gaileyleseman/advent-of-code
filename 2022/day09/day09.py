import numpy as np

def parse_text(input_txt):
    data = []
    with open(input_txt, "r") as f:
        for line in f.read().split('\n'):
            l = line.split(" ")
            data.append((l[0], int(l[1])))
    return data

def move_head(H, dir):
    if dir == "U":
        H += np.array([1,0])
    elif dir == "D":
        H += np.array([-1,0])
    elif dir == "L":
        H += np.array([0,-1])
    elif dir == "R":
        H += np.array([0,1])
    else:
        raise ValueError("Invalid direction")
    return H

def move_tail(H, T):
    d = H - T
    if sum(abs(d)) <= 1 or abs(d[0]) == abs(d[1]) == 1:
        return T
    T += np.sign(d)
    return T


def part1(data):
    H = np.array([0,0])
    T = np.array([0,0])
    visited = []
    for commmand in data:
        direction, number = commmand
        for _ in range(number):
            H = move_head(H, direction)
            T = move_tail(H, T)
            visited.append(tuple(T))
    return len(set(visited))


def part2(data):
    snake = np.zeros((10,2), dtype=int)
    visited = []
    for commmand in data:
        direction, number = commmand
        for _ in range(number):
            snake[0] = move_head(snake[0], direction)
            for i in range(1,len(snake)):
                snake[i]= move_tail(snake[i-1], snake[i])
            visited.append(tuple(snake[-1]))
    return len(set(visited))


if __name__ == '__main__':
    test_data = parse_text("test.txt")
    test2_data = parse_text("test2.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("TEST: Part 2 (2): ", part2(test2_data))
    print("Part 2: ", part2(input_data))
