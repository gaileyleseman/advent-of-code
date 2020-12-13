#[timestamp, busses] = open('./input/day13_input.txt', 'r').read().splitlines()
[timestamp, busses] = open('./input/day13_test.txt', 'r').read().splitlines()
timestamp = int(timestamp)
busses = busses.split(",")

# Part 1 ----------------------------------------------------------#
available_busses = []
for bus in busses:
    if bus != 'x':
        available_busses.append(int(bus))   # ignore 'x'

next_bus = {}
for bus in available_busses:
    next_bus[((timestamp//bus)+1)*bus] = bus

first_time = min(next_bus)
first_bus = next_bus[first_time]
ans_pt1 = (first_time - timestamp)*first_bus
print("Part 1:", ans_pt1)

# Part 2 ----------------------------------------------------------#
