adapters = open('./input/day10_input.txt', 'r').read().splitlines()
# adapters = open('./input/day10_test.txt', 'r').read().splitlines()

adapters = [int(i) for i in adapters]

# Part 1 ----------------------------------------------------------#
output_joltage = 0
joltage_diff = []

while output_joltage < max(adapters):
    for i in [1, 2, 3]:
        if output_joltage + i in adapters:
            joltage_diff.append(i)
            output_joltage += i
            break

joltage_diff.append(3)  # last step to my device
ans1 = joltage_diff.count(1) * joltage_diff.count(3)
print("Part 1: ", ans1)

# Part 2 ----------------------------------------------------------#
p = {}
options = []
adapters = sorted(adapters, reverse=True)
adapters.append(0)
my_device = max(adapters) + 3

for adapter in adapters:
    num_options = 0
    for i in [1, 2, 3]:
        opt = adapter + i
        if opt == my_device:
            num_options += 1
        if opt in adapters:
            if opt in p:
                num_options += p[opt]
            else:
                num_options += 1
    p[adapter] = num_options
    options.append(num_options)

total = p[min(adapters)]

print("Part 2:", total)
