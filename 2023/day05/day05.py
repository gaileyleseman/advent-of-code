import math

import numpy as np


def parse_text(input_txt):
    with open(input_txt, "r") as f:
        txt = f.read().split("\n\n")

    seeds = txt[0].split(":")[1].strip().split(" ")
    seeds = [int(seed) for seed in seeds]
    maps = {
        "SEED_TO_SOIL": LookUpTable(get_input_lines(txt, 1)),
        "SOIL_TO_FERTILIZER": LookUpTable(get_input_lines(txt, 2)),
        "FERTILIZER_TO_WATER": LookUpTable(get_input_lines(txt, 3)),
        "WATER_TO_LIGHT": LookUpTable(get_input_lines(txt, 4)),
        "LIGHT_TO_TEMPERATURE": LookUpTable(get_input_lines(txt, 5)),
        "TEMPERATURE_TO_HUMIDITY": LookUpTable(get_input_lines(txt, 6)),
        "HUMIDITY_TO_LOCATION": LookUpTable(get_input_lines(txt, 7)),
    }

    return (seeds, maps)


def get_input_lines(txt, index):
    return txt[index].split(":")[1].strip().split("\n")


class LookUpTable:
    def __init__(self, lines):
        self.map = []
        for line in lines:
            destination, source, range_length = line.strip().split(" ")
            rule_range = range(int(source), int(source) + int(range_length))
            self.map.append((rule_range, int(source), int(destination)))
        self.lookup = {}

    def get(self, value):
        if value in self.lookup:
            return self.lookup[value]

        self.lookup[value] = value
        for rule_range, source, destination in self.map:
            if value in rule_range:
                self.lookup[value] = value - source + destination
                return value - source + destination
        return value


def get_location_for_seed(seed, maps):
    soil = maps["SEED_TO_SOIL"].get(seed)
    fertilizer = maps["SOIL_TO_FERTILIZER"].get(soil)
    water = maps["FERTILIZER_TO_WATER"].get(fertilizer)
    light = maps["WATER_TO_LIGHT"].get(water)
    temperature = maps["LIGHT_TO_TEMPERATURE"].get(light)
    humidity = maps["TEMPERATURE_TO_HUMIDITY"].get(temperature)
    location = maps["HUMIDITY_TO_LOCATION"].get(humidity)
    return location


def part1(data):
    seeds, maps = data
    closest_location = math.inf
    for seed in seeds:
        location = get_location_for_seed(seed, maps)
        if location < closest_location:
            closest_location = location

    return closest_location


def part2(data):
    seeds, maps = data
    closest_location = math.inf
    soil_to_location = {}
    for i in range(0, len(seeds), 2):
        for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
            if seed not in soil_to_location:
                soil_to_location[seed] = get_location_for_seed(seed, maps)
            location = soil_to_location[seed]
            if location < closest_location:
                closest_location = location
    return closest_location


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
