import itertools
import math

def parse_text(input_txt):
    with open(input_txt, "r") as f:
        return [tuple(map(int,line.split(","))) for line in f.read().split("\n")]

def solve(data, n_connections):
    pairs = itertools.combinations(data, 2)
    distances = {pair: get_distance(pair) for pair in pairs}
    distances_sorted = sorted(distances.items(), key=lambda x: x[1])
    circuits = []
    for i in range(len(distances_sorted)):
        p1, p2 = distances_sorted[i][0]
        connection = set([p1, p2])
        old_circuits = circuits
        circuits = []
        for c in old_circuits:
            if not connection.intersection(c):
                circuits.append(c) # TODO: bug in this logic for example pt.1
                continue
            connection = connection.union(c)
        circuits.append(connection)
        circuit_sizes = sorted([len(c) for c in circuits], reverse=True)
        if i == n_connections:
            print(f"part1 = {math.prod(circuit_sizes[:3])}")
        if circuit_sizes[0] >= len(data):
            print(f"part2 = {p1[0] * p2[0]}")
            return
        
def get_distance(pair):
    x1, y1, z1 = pair[0]
    x2, y2, z2 = pair[1]
    return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5

if __name__ == "__main__":
    print("TEST")
    solve(parse_text("test.txt"), 10)

    print("INPUT")
    solve(parse_text("input.txt"), 1000)
