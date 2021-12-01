forest = open('input/day3_input.txt', "r").read().split('\n')

# Part 1 ----------------------------------------------------------#
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

# Part 2 ----------------------------------------------------------#

down = [1, 1, 1, 1, 2]
right = [1, 3, 5, 7, 1]

def countTrees(forest, down, right):
    height = len(forest) - 1
    width = len(forest[1])
    trees = 0
    i = 0
    j = 0
    while i + down <= height:
        i += down
        j += right
        if j >= width:
            j = j-width
        if forest[i][j] == '#':
            trees += 1
    return trees

total = 1
for i in range(0, len(down)):
    trees = countTrees(forest, down[i], right[i])
    total = total*trees
print(total)

