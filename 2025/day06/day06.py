# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "numpy",
# ]
# ///
import numpy as np

OPERATOR_LOOKUP = {
    "*": np.prod,
    "+": np.sum,
}


def parse_text_pt1(input_txt):
    with open(input_txt, "r") as f:
        raw_data = np.array([line.split() for line in f.read().split("\n")])
    numbers = raw_data.T[:, :-1].astype(int)
    operators = list(raw_data[-1, :])
    return numbers, operators


def parse_text_pt2(input_txt):
    with open(input_txt, "r") as f:
        raw_data = np.array([list(line) for line in f.read().split("\n")])
    numbers = []
    sublist = []
    for r in raw_data.T[:, :-1]:
        joined = "".join(r).strip()
        if not joined:
            numbers.append(sublist)
            sublist = []
            continue
        sublist.append(int(joined))
    numbers.append(sublist)
    operators = "".join(raw_data[-1, :]).split()
    return numbers, operators


def solve(input_txt):
    data1 = parse_text_pt1(input_txt)
    data2 = parse_text_pt2(input_txt)
    for i, data in enumerate((data1, data2)):
        numbers, operators = data
        answer = 0
        for row, operator in zip(numbers, operators):
            answer += OPERATOR_LOOKUP[operator](row)
        print(f"part{i} = {answer}")


if __name__ == "__main__":
    print("TEST")
    solve("test.txt")

    print("INPUT")
    solve("input.txt")
