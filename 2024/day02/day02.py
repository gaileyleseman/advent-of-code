import numpy as np


def parse_text(input_txt):
    data = []
    with open(input_txt, "r") as f:
        for line in f.read().split('\n'):
            data.append(np.array(line.split(), dtype=int))
    return data

def is_safe_report(report):
    changes = np.diff(report)
    return np.all(np.abs(changes) <= 3) * np.any([(changes > 0).all(), (changes < 0).all()])
    

def part1(data):
    safe_reports = [1 for report in data if is_safe_report(report)]
    return sum(safe_reports)


def part2(data):
    safe_reports = 0
    for report in data:
        if is_safe_report(report):
            safe_reports += 1
            continue
        for i in range(len(report)):
            mutated_report = np.delete(report, i)
            if is_safe_report(mutated_report):
                safe_reports += 1
                break
    return safe_reports

if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
