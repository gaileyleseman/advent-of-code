import math

def parse_text(input_txt):
    nodemap = {}
    with open(input_txt, "r") as f:
        instructions, nodemap_data = f.read().split("\n\n")
        for line in nodemap_data.split("\n"):
            k, v = line.split(" = ")
            nodemap[k] = v.strip().replace("(", "").replace(")", "").split(", ")
    return (instructions, nodemap)


INSTRUCTIONS_LOOKUP = {"L": 0, "R": 1}


def find_steps_from_node_to_end_nodes(instructions, nodemap, start_node, end_nodes):
    steps = 0
    node = start_node
    while steps == 0 or node not in end_nodes:
        for i in instructions:
            steps += 1
            node = nodemap[node][INSTRUCTIONS_LOOKUP[i]]
    return steps, node


def part1(data):
    instructions, nodemap = data
    steps, _ = find_steps_from_node_to_end_nodes(instructions, nodemap, "AAA", ["ZZZ"])
    return steps


def calc_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def part2(data):
    instructions, nodemap = data
    start_nodes = [node for node in nodemap.keys() if node.endswith("A")]
    end_nodes = [node for node in nodemap.keys() if node.endswith("Z")]
    steps_list = []
    for n in start_nodes:
        steps_to_first_end_node, first_end_node = find_steps_from_node_to_end_nodes(instructions, nodemap, n, end_nodes)
        # steps_to_same_end_node, _ = find_steps_from_node_to_end_nodes(
        #     instructions, nodemap, first_end_node, [first_end_node]
        # )
        # mods = [s%len(instructions) for s in range(steps_to_first_end_node)]

        ## From https://www.youtube.com/watch?v=_nnxLcrwO_U&ab_channel=HyperNeutrino
        ## Data is manipulated to be cyclic
        # - steps to the same end node is the same as steps to the first end node
        # - steps are all a multiple of the number of instructions?

        steps_list.append(steps_to_first_end_node)

    lcm = calc_lcm(steps_list[0], steps_list[1])
    for i in range(2, len(steps_list)):
        lcm = calc_lcm(lcm, steps_list[i])
    return lcm


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    # print("TEST: Part 1: ", part1(test_data))
    # print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
