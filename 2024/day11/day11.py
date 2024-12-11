
from collections import defaultdict

def parse_text(input_txt):
    with open(input_txt, "r") as file:
        data = list(map(int, file.read().split()))
    return data


class BlinkLookup(defaultdict):
    def __missing__(self, key):
        self[key] = {0: key, 1: _change_stone(key)}
        return self[key]
BLINK_LOOKUP = BlinkLookup()

def _change_stone(stone: int):
    if stone == 0:
        return [1]
    if len(str(stone))%2 == 0:
        i = len(str(stone))//2
        return list(map(int,[str(stone)[:i], str(stone)[i:]]))
    return [stone * 2024]

def change_stone(stone: int):
    maybe_stone = BLINK_LOOKUP[stone].get(1)
    if maybe_stone:
        return maybe_stone
    return _change_stone(stone)

def change_stone_n(stone: int, n: int):
    maybe_stone = BLINK_LOOKUP[stone].get(n)
    if maybe_stone:
        return maybe_stone

    new_stones = BLINK_LOOKUP[stone].get(1)
    all_new_stones = []
    for s in new_stones:
        new_stone = change_stone_n(s, n-1)
        all_new_stones.extend(new_stone)
    BLINK_LOOKUP[stone][n] = all_new_stones
    return all_new_stones


def blinks(stones: list, n: int):
    all_stones = []
    for stone in stones:
        new_stones = change_stone_n(stone, n)
        all_stones.extend(new_stones)
    return len(all_stones)


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", blinks(test_data, 25))
    print("Part 1: ", blinks(input_data, 25))

    print("Part 2: ", blinks(input_data, 40))
