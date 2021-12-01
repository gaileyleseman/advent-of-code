data = open('input/day9_input.txt', "r").read().split('\n')
data = [int(i) for i in data]

# Part 1 -----------------------------------------------------#

def checkValid(x, i, data):
    prev = data[i-x:i]
    for j in range(0, x):
        for k in range(j+1, x):
            if prev[j] + prev[k] == data[i]:
                return True
    return False

def findFirstNonValid(x, data):
    for i in range(x, len(data)-1):
        if not checkValid(x, i, data):
            return data[i]

ans1 = findFirstNonValid(25, data)
print("Part 1:", ans1)

# Part 2 -----------------------------------------------------#

def findSet(input, data):
    set_length = 2
    while True:
        for i in range(0, len(data)-1):
            subset = data[i:i+set_length]
            if sum(subset) == input:
                return min(subset) + max(subset)
                break
        set_length += 1



ans2 = findSet(ans1, data)
print("Part 2:", ans2)

