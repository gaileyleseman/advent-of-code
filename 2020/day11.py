import numpy as np

input = open('./input/day11_input.txt', 'r').read().splitlines()
# input = open('./input/day11_test.txt', 'r').read().splitlines()

n_rows = len(input)
n_cols = len(input[0])
seats = np.empty([n_rows, n_cols])

for i in range(0, n_rows):
    for j in range(0, n_cols):
        if input[i][j] == ".":
            seats[i, j] = 0  # floor
        elif input[i][j] == "L":
            seats[i, j] = 1  # empty seat
        else:
            continue


# Part 1 ----------------------------------------------------------#
def getAdjacent(seats, i, j):
    sub = seats[max(i - 1, 0):min(i + 2, n_rows), max(j - 1, 0):min(j + 2, n_cols)]
    adjacent = sub.copy()
    occupied = np.sum(adjacent == 2) - int(seats[i, j] == 2)
    return occupied


getAdjacent(seats, 8, 0)


def updateSeats(seats):
    new_seats = np.empty([n_rows, n_cols])
    for i in range(0, n_rows):
        for j in range(0, n_cols):
            chair = seats[i, j]
            occupied = getAdjacent(seats, i, j)
            if chair == 1 and occupied == 0:  # seat is empty, no occupied adjacent
                new_seats[i, j] = 2  # becomes occupied
            elif chair == 2 and occupied >= 4:  # seat is occupied, four occupied adjacent
                new_seats[i, j] = 1  # becomes empty
            else:
                new_seats[i, j] = chair  # nothing changes
    return new_seats


def part1(seats):
    while True:
        new_seats = updateSeats(seats)
        if (new_seats == seats).all():
            ans_pt1 = np.sum(new_seats == 2)  # count occupied seats
            break
        else:
            seats = new_seats.copy()
    return ans_pt1


print("Part 1:", part1(seats))


# Part 2 ----------------------------------------------------------#
def getFirstVisible(seats, i, j):
    checked = []
    adjacent = []
    for north in range(i - 1, -1, -1):
        west = j - (i - north)
        east = j + (i - north)
        if "N" not in checked:
            if seats[north, j] != 0:
                adjacent.append(seats[north, j])
                checked.append("N")
        if "NW" not in checked:
            if west >= 0 and seats[north, west] != 0:
                adjacent.append(seats[north, west])
                checked.append("NW")
        if "NE" not in checked:
            if east < n_cols and seats[north, east] != 0:
                adjacent.append(seats[north, east])
                checked.append("NE")

    for south in range(i + 1, n_rows):
        west = j - (south - i)
        east = j + (south - i)
        if "S" not in checked:
            if seats[south, j] != 0:
                adjacent.append(seats[south, j])
                checked.append("S")
        if "SW" not in checked:
            if west >= 0 and seats[south, west] != 0:
                adjacent.append(seats[south, west])
                checked.append("SW")
        if "SE" not in checked:
            if east < n_cols and seats[south, east] != 0:
                adjacent.append(seats[south, east])
                checked.append("SE")

    for west in range(j - 1, -1, -1):
        if "W" not in checked:
            if seats[i, west] != 0:
                adjacent.append(seats[i, west])
                checked.append("W")
    for east in range(j + 1, n_cols):
        if "E" not in checked:
            if seats[i, east] != 0:
                adjacent.append(seats[i, east])
                checked.append("E")

    occupied = adjacent.count(2)
    return occupied


def updateSeats2(seats):
    new_seats = np.empty([n_rows, n_cols])
    for i in range(0, n_rows):
        for j in range(0, n_cols):
            chair = seats[i, j]
            occupied = getFirstVisible(seats, i, j)
            if chair == 1 and occupied == 0:  # seat is empty, no occupied adjacent
                new_seats[i, j] = 2  # becomes occupied
            elif chair == 2 and occupied >= 5:  # seat is occupied, five occupied adjacent
                new_seats[i, j] = 1  # becomes empty
            else:
                new_seats[i, j] = chair  # nothing changes
    return new_seats


def part2(seats):
    while True:
        new_seats = updateSeats2(seats)
        if (new_seats == seats).all():
            ans_pt2 = np.sum(new_seats == 2)  # count occupied seats
            break
        else:
            seats = new_seats.copy()
    return ans_pt2

print("Part 2:", part2(seats))
