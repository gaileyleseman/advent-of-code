import re
rules_input = open('input/day7_input.txt', "r").read().split('\n')

# Part 1 -----------------------------------------------------------------------#

# create nested dictionary from rules
rules = {}
for rule_input in rules_input:
    rule = re.sub(' bag[s]{0,1}[\.]{0,1}', '', rule_input).split(' contain ')
    outer_bag = rule[0]
    inner_bags = {}
    for option in rule[1].split(', '):
        if option == "no other":
            [number, color] = 0, None
        else:
            [number, color] = option.split(" ", 1)
        inner_bags[color] = int(number)
    rules[outer_bag] = inner_bags

# function to find bags that may contain your bag
def findPossibleBags(my_color, my_number):
    possible_bags = []
    for outer_bag, inner_bags in rules.items():
        for color in inner_bags:
            if color == my_color and inner_bags[color] >= my_number:
                possible_bags.append(outer_bag)
    return possible_bags

# find all bags
def findNumBags(my_color, my_number):
    checked_colors = []
    possible_bags = findPossibleBags(my_color, my_number)
    for bag in possible_bags:
        if bag in checked_colors:
            continue
        else:
            outer_bag_options = findPossibleBags(bag, 1)
            if len(outer_bag_options) >= 1:
                possible_bags.extend(outer_bag_options)
            checked_colors.append(bag)
    return len(set(possible_bags))

my_color = 'shiny gold'
my_number = 1
ans = findNumBags(my_color, my_number)
print("Bags that can contain at least {0} {1} bag: {2}".format(my_number, my_color, ans))


# Part 2 -----------------------------------------------------------------------#

def findInnerBags(my_color):
    total = 1
    for color, number in rules[my_color].items():
        if number == 0:
            continue
        total += number * findInnerBags(color)
    return total

ans_pt2 = findInnerBags(my_color) - 1
print("{0} {1} bag must contain at least: {2} bags".format(my_number, my_color, ans_pt2))