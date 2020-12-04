data = open('input/day1_input.txt', "r").read().split('\n')

for i in range(0, len(data)-1):
    data[i] = int(data[i])

# Part 1
for i in range(0, len(data)-1):
    for j in range(i, len(data)-1):
        if data[i]+data[j] == 2020:
            print(data[i]*data[j])
# Part 2
for i in range(0, len(data)-1):
    for j in range(i, len(data)-1):
        for k in range(j, len(data)-1):
            if data[i]+data[j]+data[k] == 2020:
                print(data[i]*data[j]*data[k])

