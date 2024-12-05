from collections import defaultdict


def parse_text(input_txt):
    with open(input_txt, "r") as file:
        rules, updates = file.read().split("\n\n")

    rules = [list(map(int, rule.split("|"))) for rule in rules.split("\n")]
    updates = [list(map(int, update.split(","))) for update in updates.split("\n")]
    rules_lookup = create_rules_lookup(rules)
    return rules_lookup, updates


def create_rules_lookup(rules):
    rules_before = defaultdict(set)
    rules_after = defaultdict(set)
    for a, b in rules:
        rules_before[b].add(a)
        rules_after[a].add(b)
    rules_lookup = {"before": rules_before, "after": rules_after}
    return rules_lookup


def check_order_update(update, rules_lookup):
    for i, n in enumerate(update):
        before = set(update[:i]).issubset(rules_lookup["before"][n])
        after = set(update[i + 1 :]).issubset(rules_lookup["after"][n])
        if not before or not after:
            return False
    return True


def order_update(update, rules_lookup):
    order = {}
    for n in update:
        n_before = sum([1 for x in update if x in rules_lookup["before"][n]])
        order[n_before] = n
    ordered_update = [order[i] for i in range(len(update))]
    return ordered_update


def part1(data):
    rules_lookup, updates = data
    total = 0
    for update in updates:
        if check_order_update(update, rules_lookup):
            total += update[len(update) // 2]
    return total


def part2(data):
    rules_lookup, updates = data
    total = 0
    for update in updates:
        if not check_order_update(update, rules_lookup):
            ordered_update = order_update(update, rules_lookup)
            total += ordered_update[len(ordered_update) // 2]
    return total


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
