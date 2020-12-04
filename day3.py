forest = open('day3_input.txt', "r").read().split('\n')

height = len(forest)-1
width = len(forest[1])
down = 1
right = 3

i = 0
j = 0
trees = 0

while i + down < height:
    i += down
    j += right
    if j >= width:
        j = j-width
    if forest[i][j] == '#':
        trees += 1

print(trees)



