data = open('input/day2_input.txt', "r").read().split('\n')

# Part 1 ----------------------------------------------------------#
valid = 0
for i in range(0, len(data)-1):
    [policy, letter, password] = data[i].split(' ')
    [min, max] = policy.split('-')
    letter = letter[0]
    if int(min) <= password.count(letter) <= int(max):
        valid += 1
print("Part 1: ", valid)

# Part 2 ----------------------------------------------------------#
valid = 0
for i in range(0, len(data)-1):
    policy = data[i].split(' ')
    [pos1, pos2] = policy[0].split('-')
    letter = policy[1][0]
    letters = policy[2][int(pos1)-1] + policy[2][int(pos2)-1]
    if letters.count(letter) == 1:
        valid += 1
print("Part 2:", valid)
