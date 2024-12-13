import numpy as np
from dataclasses import dataclass, field
import itertools


def parse_text(input_txt):
    with open(input_txt, "r") as file:
        data = np.array([list(line) for line in file.read().splitlines()], dtype=str)
    return data


class Directions:
    LEFT = np.array([-1, 0])
    UP = np.array([0, -1])
    RIGHT = np.array([1, 0])
    DOWN = np.array([0, 1])


DIRECTIONS = [Directions.LEFT, Directions.UP, Directions.RIGHT, Directions.DOWN]


def within_bounds(data, position):
    return np.all(position >= 0) and np.all(position < data.shape)


@dataclass
class Garden:
    start_position: tuple
    plant: str
    plots: list = field(default_factory=list)
    perimeter: list = field(default_factory=list)

    def __post_init__(self):
        self.plots.append(self.start_position)

    def find_garden(self, data):
        adjacent, perimeter = self.find_adjacent_plants(data)
        self.plots.extend(adjacent)
        self.perimeter.extend(perimeter)

    def find_adjacent_plants(self, data):
        adjacent = []
        perimeter = []
        for direction in DIRECTIONS:
            new_position = tuple(self.start_position + direction)
            if new_position in self.plots:
                continue
            if not within_bounds(data, self.start_position + direction):
                perimeter.append(new_position)
                continue
            adjacent_plant = data[new_position]
            if adjacent_plant != self.plant:
                perimeter.append(new_position)
                continue
            new_adjacent, new_perimeter = Garden(new_position, adjacent_plant, plots=self.plots).find_adjacent_plants(
                data
            )
            adjacent.extend(new_adjacent)
            perimeter.extend(new_perimeter)

        return adjacent, perimeter
    
    def get_plots(self):
        return self.plots

    def get_score(self):
        return len(self.plots) * len(self.perimeter)

def find_garden(data):
    visited_plots = []
    gardens = []
    for idx, plant in np.ndenumerate(data):
        if idx in visited_plots:
            continue
        garden = Garden(start_position=idx, plant=plant)
        garden.find_garden(data)
        visited_plots.extend(garden.get_plots())
        gardens.append(garden)

    scores = [garden.get_score() for garden in gardens]
    return sum(scores)


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: ", find_garden(test_data))
    print("INPUT: ", find_garden(input_data))
