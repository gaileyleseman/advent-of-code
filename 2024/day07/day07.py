import itertools

def parse_text(input_txt):
    data = []
    with open(input_txt, "r") as f:
        lines = f.read().split("\n")
        for  line in lines:
            result, parameters = line.split(": ")
            result = int(result.strip())
            parameters = list(map(int, parameters.split()))
            data.append((result, parameters))
    return data

def check_valid_expression(result, parameters, possible_combinations):
    for operators in possible_combinations:
        res = parameters[0]
        for operator, parameter in zip(operators, parameters[1:]):
            if operator == "*":
                res *= parameter
            elif operator == "+":
                res += parameter
            elif operator == "||":
                res = int(str(res) + str(parameter))
            if res > result:
                break
        if res == result:
            return True
    return False

def part1(data):
    total = 0
    for result, parameters in data:
        operators = ["*", "+"]
        possible_combinations = list(itertools.product(operators, repeat=len(parameters)-1))
        if check_valid_expression(result, parameters, possible_combinations):
            total += result
    return total


def part2(data):
    total = 0
    for result, parameters in data:
        operators = ["*", "+", "||"]
        possible_combinations = list(itertools.product(operators, repeat=len(parameters) - 1))
        print(possible_combinations)
        if check_valid_expression(result, parameters, possible_combinations):
            total += result
    return total

if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    import time
    print("TEST: Part 1: ", part1(test_data))
    t_start = time.time()
    print("Part 1: ", part1(input_data))
    print("Time: ", time.time() - t_start)

    print("TEST: Part 2: ", part2(test_data))
    t_start = time.time()
    # print("Part 2: ", part2(input_data))
    print("Time: ", time.time() - t_start)
