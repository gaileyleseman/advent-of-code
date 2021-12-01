import numpy as np
import math
actions = open('./input/day12_input.txt', 'r').read().splitlines()
# actions = open('./input/day12_test.txt', 'r').read().splitlines()

# Part 1 ----------------------------------------------------------#
navigation = {"N": np.array([1, 0, 0]),
              "S": np.array([-1, 0, 0]),
              "E": np.array([0, 1, 0]),
              "W": np.array([0, -1, 0]),
              "L": np.array([0, 0, 1]),
              "R": np.array([0, 0, -1])}

def forward(pos, value):
    n = math.sin(math.radians(pos[2]))*value
    e = math.cos(math.radians(pos[2]))*value
    new_pos = pos + np.array([n, e, 0])
    return new_pos

def move(action, pos):
    cmd = action[0]
    value = int(action[1:])
    if cmd == "F":
        new_pos = forward(pos, value)
    else:
        new_pos = pos + navigation[cmd] * value
    return new_pos

pos0 = np.array([0, 0, 0])
pos = pos0.copy()
for action in actions:
    pos = move(action, pos)

ans_pt1 = round(sum(abs(pos[0:2])))
print("Part 1:", ans_pt1)


# Part 2 ----------------------------------------------------------#
wp_nav = {"N": np.array([1, 0]),
          "S": np.array([-1, 0]),
          "E": np.array([0, 1]),
          "W": np.array([0, -1])}

def move_waypoint(pos_ship, pos_wp, action):
    cmd = action[0]
    value = int(action[1:])
    if cmd in wp_nav:
        new_pos = pos_wp + wp_nav[cmd] * value
    else:
        diff_n, diff_e = pos_wp - pos_ship
        l = math.sqrt(diff_n**2 + diff_e**2)
        current_angle = np.arctan2(diff_n, diff_e)
        if cmd == "L":
            angle = current_angle + math.radians(value)
        else:
            angle = current_angle - math.radians(value)
        new_diff = [math.sin(angle)*l, math.cos(angle)*l]
        new_pos = pos_ship + new_diff
    return new_pos

def move_ship(pos_ship, pos_wp, value):
    diff = pos_wp - pos_ship
    new_pos_ship = pos_ship + diff*value
    new_pos_wp = new_pos_ship + diff
    return new_pos_ship, new_pos_wp

pos_ship = np.array([0, 0])
pos_wp = np.array([1, 10])

for action in actions:
    if action[0] == "F":
        value = int(action[1:])
        pos_ship, pos_wp = move_ship(pos_ship, pos_wp, value)
    else:
        pos_wp = move_waypoint(pos_ship, pos_wp, action)

ans_pt2 = round(sum(abs(pos_ship[0:2])))
print("Part 2:", ans_pt2)