from collections import defaultdict, Counter


def parse_text(input_txt):
    with open(input_txt, "r") as file:
        data = list(map(int, file.read().split()))
    return data


def _change_stone(stone: int) -> list:
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        i = len(str(stone)) // 2
        return list(map(int, [str(stone)[:i], str(stone)[i:]]))
    return [stone * 2024]


class ChangeLookup(defaultdict):
    def __missing__(self, key):
        self[key] = _change_stone(key)
        return self[key]


CHANGE_LOOKUP = ChangeLookup()


class BlinkLookup(defaultdict):
    def __missing__(self, key):
        self[key] = {0: 1, 1: len(CHANGE_LOOKUP[key])}
        return self[key]


BLINK_LOOKUP = BlinkLookup()


def change_stone_n(stone: int, n: int):
    maybe_stone = BLINK_LOOKUP[stone].get(n)
    if maybe_stone:
        return maybe_stone

    new_stones = CHANGE_LOOKUP.get(stone)
    total_new_stones = blinks(new_stones, n - 1)
    BLINK_LOOKUP[stone][n] = total_new_stones
    return total_new_stones


def blinks(stones: list, n: int):
    # Hint from reddit: 
    # - Problem is similar to 2021 - Day 6 (Lanternfish). The lists are too long to keep track of (memory-wise).
    #
    # So instead of storing the list of generated stones, we can store the number of stones generated in the lookup.
    # Additionally, we can avoid repeating calculations per round with the Counter. 
    # Final result is ~0.15 seconds for part 2.

    stones_counter = Counter(stones)
    all_stones = 0
    for stone, count in stones_counter.items():
        number_of_new_stones = change_stone_n(stone, n)
        all_stones += count * number_of_new_stones
    return all_stones


def part_1(data):
    return blinks(data, 25)


def part_2(data):
    return blinks(data, 75)


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part_1(test_data))
    print("Part 1: ", part_1(input_data))
    print("Part 2: ", part_2(input_data))