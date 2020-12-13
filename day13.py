import numpy as np
import time

[timestamp, busses] = open('./input/day13_input.txt', 'r').read().splitlines()
# [timestamp, busses] = open('./input/day13_test.txt', 'r').read().splitlines()
timestamp = int(timestamp)
busses = busses.split(",")

# Part 1 ----------------------------------------------------------#
available_busses = []
i = 0
for bus in busses:
    if bus != 'x':
        available_busses.append(int(bus))   # ignore 'x'
    i += 1

next_bus = {}
for bus in available_busses:
    next_bus[((timestamp//bus)+1)*bus] = bus

first_time = min(next_bus)
first_bus = next_bus[first_time]
ans_pt1 = (first_time - timestamp)*first_bus
print("Part 1:", ans_pt1)

# Part 2 ----------------------------------------------------------#
first_bus = available_busses[0]
available_busses = sorted(available_busses)

time_diff = [busses.index(str(bus)) for bus in available_busses]
time_diff = np.array(time_diff)
time_diff = time_diff - time_diff[-1]

t = time.time()
n_busses = len(available_busses)
step = available_busses[-1]
min_time = 100000000000000      # surely the actual earliest timestamp wil be larger than ...
i = min_time//step + 1
while True:
    timestamp = time_diff + i * step
    checked = 0
    for j in range(0, n_busses):
        if not timestamp[j] % available_busses[j] == 0:
            break
        else:
            checked += 1
    if checked == n_busses:
        idx = available_busses.index(first_bus)
        print("Part 2:", timestamp[idx])
        break
    i += 1

elapsed = time.time() - t
print(elapsed)




