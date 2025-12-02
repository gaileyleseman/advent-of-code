def parse_text(input_txt):
    data = []
    with open(input_txt, "r") as f:
        for line in f.read().split(','):
            start, end = map(int, line.split("-"))
            data.append((start, end))
    return data

def solve(data):
    part1 = []
    part2 = []
    for start, end in data:
        for n in range(start, end+1):
            s = str(n)
            for i in range(1, len(s)//2 + 1):
                times = int(len(s) / i)
                if s == s[:i] * times:
                    if times == 2:
                        part1.append(n)
                    part2.append(n)
                    break
    print(f"part1 = {sum(part1)}")
    print(f"part2 = {sum(part2)}")


if __name__ == "__main__":
    print("TEST")
    solve(parse_text("test.txt"))

    print("INPUT")
    solve(parse_text("input.txt"))
