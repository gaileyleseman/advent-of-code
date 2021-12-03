import re

rules = {}

def parse_text(input_txt):
    data = open(input_txt, "r").read().split('\n')
    return data

# function to find bags that may contain your bag
def findPossibleBags(my_color, my_number, rules):
    possible_bags = []
    for outer_bag, inner_bags in rules.items():
        for color in inner_bags:
            if color == my_color and inner_bags[color] >= my_number:
                possible_bags.append(outer_bag)
    return possible_bags

# find all bags
def findNumBags(my_color, my_number, rules):
    checked_colors = []
    possible_bags = findPossibleBags(my_color, my_number, rules)
    for bag in possible_bags:
        if bag in checked_colors:
            continue
        else:
            outer_bag_options = findPossibleBags(bag, 1, rules)
            if len(outer_bag_options) >= 1:
                possible_bags.extend(outer_bag_options)
            checked_colors.append(bag)
    return len(set(possible_bags))

def part1(input_txt):
    rules_input = parse_text(input_txt)
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
    my_color = 'shiny gold'
    my_number = 1
    ans = findNumBags(my_color, my_number, rules)
    return ans


def findInnerBags(my_color, rules):
    total = 1
    for color, number in rules[my_color].items():
        if number == 0:
            continue
        total += number * findInnerBags(color, rules)
    return total


def part2(input_txt):
    data = parse_text(input_txt)
    my_color = 'shiny gold'
    ans = findInnerBags(my_color, rules) - 1
    return ans


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
