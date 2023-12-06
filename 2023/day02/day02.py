def parse_text(input_txt):
    with open(input_txt, "r") as f:
        data = f.read().split("\n")
    return data


def part1(data, max_red: int = 12, max_green: int = 13, max_blue: int = 14):
    sum = 0
    for row in data:
        game_id, game_sets = row.split(":")
        game_id = int(game_id.strip().split(" ")[-1])
        game_sets = game_sets.split(";")
        possible = True
        for set in game_sets:
            sets_per_color = set.split(",")
            for cube_set in sets_per_color:
                number, color = cube_set.strip().split(" ")
                if color == "red":
                    if int(number) > max_red:
                        possible = False
                if color == "green":
                    if int(number) > max_green:
                        possible = False
                if color == "blue":
                    if int(number) > max_blue:
                        possible = False
        if possible:
            sum += game_id

    return sum


def part2(data):
    sum = 0
    for row in data:
        game_sets = row.split(":")[1].split(";")
        min_red, min_green, min_blue = 0, 0, 0
        for set in game_sets:
            sets_per_color = set.split(",")
            for cube_set in sets_per_color:
                number, color = cube_set.strip().split(" ")
                if color == "red":
                    min_red = max(min_red, int(number))
                if color == "green":
                    min_green = max(min_green, int(number))
                if color == "blue":
                    min_blue = max(min_blue, int(number))
        power = min_red * min_green * min_blue
        sum += power
    return sum


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
