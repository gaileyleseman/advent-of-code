START = 50 

OPERATORS = {
    "L": -1,
    "R": 1
}

def parse_text(input_txt):
    data = []
    with open(input_txt, "r") as f:
        for line in f.read().split('\n'):
            data.append((line[0], int(line[1:])))
    return data

def solve(data):
    dial = START
    part1 = 0
    part2 = 0
    for direction, distance in data:
        starts_on_zero = dial == 0
        turns, dial = divmod(dial + OPERATORS[direction]*distance, 100)
        ends_on_zero = dial == 0
        turns_left = turns < 0
        turns_right = turns > 0

        times_through_zero = abs(turns)
        if (starts_on_zero and turns_left) or (ends_on_zero and turns_right):
            times_through_zero -= 1
        
        part1 += ends_on_zero
        part2 += ends_on_zero + times_through_zero

    print(f"{part1=}")
    print(f"{part2=}")

if __name__ == "__main__":
    print("TEST")
    solve(parse_text("test.txt"))

    print("INPUT")
    solve(parse_text("input.txt"))
