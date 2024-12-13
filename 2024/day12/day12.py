import numpy as np
from dataclasses import dataclass, field
import itertools


def parse_text(input_txt):
    with open(input_txt, "r") as file:
        data = np.array([list(line) for line in file.read().splitlines()], dtype=str)
    return data


class Directions:
    DOWN = np.array([-1, 0])
    LEFT = np.array([0, -1])
    UP = np.array([1, 0])
    RIGHT = np.array([0, 1])


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
        self.get_sides(data)

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
    
    def get_sides(self, data):
        fences = np.pad(np.zeros(data.shape),1)
        for p in self.perimeter:
            fences[p] = 1
        fences = np.roll(fences, 1, axis=(0,1))
        self.sides = find_corners(fences)

    def get_plots(self):
        return self.plots

    def get_score(self):
        return len(self.plots) * len(self.perimeter)

    def get_score_pt2(self):
        return len(self.plots) * self.sides
    

def turn_right(direction):
    return np.array([direction[1], -direction[0]])
    

def find_corners(fences):
    first_fence = np.argwhere(fences == 1)[0]
    visited_fences = []
    current = first_fence
    step = Directions.RIGHT
    n_sides = 0
    while True:
        visited_fences.append(tuple(current))
        current = current + step
        if np.all(current == first_fence):
            break
        if fences[tuple(current)] == 1:
            continue
        if not within_bounds(fences, current):
            step = turn_right(step)
        n_sides += 1
        step = turn_right(step)
        possible_next = current + step
        while fences[tuple(possible_next)] == 0:
            n_sides += 1
            step = turn_right(step)
            possible_next = current + step

    for fence in visited_fences:
        fences[fence] = 0
    
    if np.sum(fences) > 0:
        n_sides += find_corners(fences)
    return n_sides



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
    scores_pt2 = [garden.get_score_pt2() for garden in gardens]
    return sum(scores), sum(scores_pt2)


if __name__ == "__main__":
    test1_data = parse_text("test1.txt")
    test2_data = parse_text("test2.txt")
    test_data = parse_text("test.txt")

    input_data = parse_text("input.txt")

    print("TEST1: ", find_garden(test1_data))
    print("TEST2: ", find_garden(test2_data))
    print("TEST: ", find_garden(test_data))
    # print("INPUT: ", find_garden(input_data))
