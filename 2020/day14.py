import numpy as np
import itertools

input = open('./input/day14_input.txt', 'r').read().splitlines()
# input = open('./input/day14_test.txt', 'r').read().splitlines()
input = [line.split(" = ") for line in input]

# Part 1 ----------------------------------------------------------#
mem = {}

def masked(mask, value):
    value = "{0:b}".format(int(value)).zfill(36)
    new_value = []
    for i in range(0, len(mask)):
        if mask[i] == 'X':
            new_value.append(value[i])
        else:
            new_value.append(mask[i])
    new_value = int("".join(new_value), 2)
    return new_value

for line in input:
    cmd = line[0]
    value = line[1]
    if cmd == "mask":
        mask = list(value)
    else:
        cmd = cmd.replace("]", "[").split("[")
        address = int(cmd[1])
        masked_value = masked(mask, value)
        mem[address] = masked_value

ans_pt1 = sum(mem.values())
print("Part 1:", ans_pt1)

# Part 2 ----------------------------------------------------------#
mem = {}

def maskedAddress(mask, address):
    address = "{0:b}".format(int(address)).zfill(36)
    new_address = []
    for i in range(0, len(mask)):
        if mask[i] == 'X' or mask[i] == "1":
            new_address.append(mask[i])
        else:
            new_address.append(address[i])

    idxs = np.where(np.array(new_address) == 'X')[0]
    add_opts = []
    for idx in idxs:
        floating = list("0"*36)
        floating[idx] = "1"
        add_opt = int("".join(floating), 2)     # difference due to floating bit
        add_opts.append(add_opt)
    all_opts = []
    for r in range(len(add_opts) + 1):
        comb = list(itertools.combinations(add_opts, r))
        all_opts += comb
    possible = [int("".join(new_address).replace("X", "0"), 2)]
    for opt in all_opts:
        possible.append(possible[0] + sum(opt))
    return possible

for line in input:
    cmd = line[0]
    value = line[1]
    if cmd == "mask":
        mask = list(value)
    else:
        cmd = cmd.replace("]", "[").split("[")
        address = int(cmd[1])
        possible_address = maskedAddress(mask, address)
        for i in possible_address:
            mem[i] = int(value)

ans_pt2 = sum(mem.values())
print("Part 2:", ans_pt2)