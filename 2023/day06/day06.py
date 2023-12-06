def parse_text(input_txt):
    with open(input_txt, "r") as f:
        data = f.read().split("\n")
    times = data[0].split(": ")[1]
    distances = data[1].split(": ")[1]
    return times, distances


def get_distance(button_pressed_time, race_time):
    speed = button_pressed_time  # m/s
    time_left = race_time - button_pressed_time
    return speed * time_left


def part1(data):
    times, distances = data
    times = [int(x) for x in times.split(" ") if x.strip() != ""]
    distances = [int(x) for x in distances.split(" ") if x.strip() != ""]
    races = list(zip(times, distances))

    total = 1

    for race in races:
        count = 0
        time, record = race
        for i in range(time):
            if get_distance(i, time) > record:
                count += 1
        total *= count
    return total


def part2(data):
    times, distances = data
    time = int(times.replace(" ", ""))
    record = int(distances.replace(" ", ""))

    count = 0

    for i in range(time):
        if get_distance(i, time) > record:
            count += 1

    return count


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
