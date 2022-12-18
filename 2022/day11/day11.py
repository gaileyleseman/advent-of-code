from copy import deepcopy

def parse_text(input_txt):
    with open(input_txt, "r") as f:
        monkeys_data= f.read().split('\n\n')
    monkeys = []
    for i, monkey in enumerate(monkeys_data):
        attributes = monkey.split('\n')
        starting_items = [int(x) for x in attributes[1].split(':')[-1].strip().split(', ')]
        operation = eval("lambda item:" + attributes[2].split(':')[-1].strip().split(' = ')[-1].replace("old", "item"))
        modulus = int(attributes[3].split(' ')[-1])
        monkey_true = int(attributes[4].split(' ')[-1].strip())
        monkey_false = int(attributes[5].split(' ')[-1].strip())
        monkeys.append(Monkey(i, starting_items, operation, modulus, monkey_true, monkey_false))
    return monkeys

class Monkey:
    def __init__(self, i, starting_items, operation, modulus, monkey_true, monkey_false):
        self.name = i
        self.items = starting_items
        self.operation = operation
        self.modulus = modulus
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false
        self.inspections = 0

    def inspect_items(self, monkeys, less_worried=False, total_modulus=None):
        for item in self.items:
            self.inspections += 1
            new_worry_level = self.operation(item) 
            new_worry_level = new_worry_level % total_modulus if not less_worried else new_worry_level // 3

            if new_worry_level%self.modulus == 0: 
                monkeys[self.monkey_true].get_item(new_worry_level)
            else:
                monkeys[self.monkey_false].get_item(new_worry_level)
        self.items.clear()

    def get_item(self, item):
        self.items.append(item)
    
    def __repr__(self):
        return f"Monkey {self.name} with {self.items} items"

def get_monkey_business(monkeys):
    inspections = sorted([monkey.inspections for monkey in monkeys])
    monkey_business = inspections[-1] * inspections[-2]
    return monkey_business

def part1(data):
    monkeys = deepcopy(data)
    n_rounds = 20
    for _ in range(n_rounds):
        for monkey in monkeys:
            monkey.inspect_items(monkeys, less_worried=True)
    return get_monkey_business(monkeys)


def part2(data):
    monkeys = deepcopy(data)
    n_rounds = 10000
    total_modulus = 1
    for monkey in monkeys:
        total_modulus *= monkey.modulus
    for _ in range(n_rounds):
        for monkey in monkeys:
            monkey.inspect_items(monkeys, less_worried = False, total_modulus=total_modulus)
    return get_monkey_business(monkeys)


if __name__ == '__main__':
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
