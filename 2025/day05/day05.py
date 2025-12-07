def parse_text(input_txt):
    with open(input_txt, "r") as f:
        raw_data = [line.split("\n") for line in f.read().split("\n\n")]
    ranges, ids = raw_data
    parsed_ranges = [tuple(map(int, r.split("-"))) for r in ranges]
    parsed_ids = list(map(int, ids))
    return (parsed_ranges, parsed_ids)


def part1(data):
    ranges, ids = data
    fresh_counter = 0
    for id in ids:
        for r_start, r_end in ranges:
            if r_start <= id <= r_end:
                fresh_counter += 1
                break
    print(f"part1 = {fresh_counter}")


def part2(data):
    ranges, _ = data
    ranges.sort()
    ranges_merged = []
    for r_start, r_end in ranges:
        updated = False
        for i, (x_start, x_end) in enumerate(ranges_merged):
            if x_start <= r_start <= x_end:
                ranges_merged[i] = [x_start, max(r_end, x_end)]
                updated = True
                break
            if x_start <= r_end <= x_end:
                ranges_merged[i] = [min(r_start, x_start), r_end]
                updated = True
                break
        if not updated:
            ranges_merged.append([r_start, r_end])
    fresh_ids_total = sum([(end - start + 1) for start, end in ranges_merged])
    print(f"part2 = {fresh_ids_total}")


if __name__ == "__main__":
    print("TEST")
    test_data = parse_text("test.txt")
    part1(test_data)
    part2(test_data)

    print("INPUT")
    data = parse_text("input.txt")
    part1(data)
    part2(data)
