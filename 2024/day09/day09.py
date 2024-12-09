import math


def parse_text(input_txt):
    with open(input_txt, "r") as file:
        raw_data = file.read()
    file_id = lambda x: x // 2 if x % 2 == 0 else None
    data = [(file_id(i), int(k)) for i, k in enumerate(list(raw_data))]
    return data


def part1(files):
    i = 0
    score = 0
    file_index = 0

    while file_index < len(files):
        file_id, file_size = files[file_index]
        file_reservation = file_size

        if file_id is None:
            file_id, back_file_size = files[-1]
            if back_file_size > file_size:
                files[-1] = (file_id, back_file_size - file_size)
            else:
                files = files[:-2]
                file_reservation = back_file_size
                files[file_index] = (None, file_size - back_file_size)
                file_index -= 1

        score += file_id * sum(range(i, i + file_reservation))
        i += file_reservation
        file_index += 1

    return score


def part2(files):
    i = 0
    score = 0
    file_index = 0

    while file_index < len(files):
        file_id, file_reservation = files[file_index]

        if file_id == "MOVED" or file_reservation == 0:
            i += file_reservation
            file_index += 1
            continue

        if file_id is None:
            for j in range(-1, -len(files) + file_index, -2):  # skip files we've already covered, skip every other file
                back_file_id, back_file_size = files[j]
                if back_file_size <= file_reservation and back_file_id not in [None, "MOVED"]:
                    file_id = back_file_id
                    break
            else:
                i += file_reservation
                file_index += 1
                continue

            files[j] = ("MOVED", back_file_size)
            if back_file_size != file_reservation:
                files[file_index] = (None, file_reservation - back_file_size)
                file_reservation = back_file_size
                file_index -= 1  # repeat this file again

        score += file_id * sum(range(i, i + file_reservation))
        i += file_reservation
        file_index += 1

    return score


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
