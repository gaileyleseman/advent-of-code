data = open('day2_input.txt', "r").read().split('\n')
valid = 0
for i in range(0, len(data)-1):
    [policy, letter, password] = data[i].split(' ')
    [min, max] = policy.split('-')
    letter = letter[0]
    if int(min) <= password.count(letter) <= int(max):
        valid += 1
print(valid)