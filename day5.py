
# Part 1 ----------------------------------------------------------------------#
boarding_passes = open('input/day5_input.txt', "r").read().split('\n')

def getSeatLocation(boarding_pass):
    row = int(boarding_pass[0:7].replace("F", "0").replace("B", "1"), 2)
    col = int(boarding_pass[7:].replace("L", "0").replace("R", "1"), 2)
    return (row, col)

def getSeatID(loc):
    return loc[0] * 8 + loc[1]

locs = []
ids = []

for boarding_pass in boarding_passes:
    loc = getSeatLocation(boarding_pass)
    locs.append(loc)
    ids.append(getSeatID(loc))

print("Highest Seat ID:", max(ids))

# Part 2 ----------------------------------------------------------------------#
ids.sort()
for k in range(0, len(ids)-1):
    if ids[k+1] - ids[k] != 1:
        print("My Seat ID:", ids[k] + 1)

