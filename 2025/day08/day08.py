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
    for i in range(n_connections):
        p1, p2 = distances_sorted[i][0]
        connection = set([p1, p2])
        prev = None
        for k, c in enumerate(circuits):
            if connection.intersection(c):
                if prev:
                    circuits[prev] = circuits[prev].union(circuits.pop(k))
                    continue
                circuits[k] = c.union(connection)
                prev = k
        if not prev:
            circuits.append(connection)
    frozen = set(map(frozenset, circuits))  # some bug where there are duplicate circuits that are not merged
    print((len(circuits), len(frozen)))
    circuit_sizes = sorted([len(c) for c in frozen], reverse=True)
    print(f"part1 = {math.prod(circuit_sizes[:3])}")
        
def get_distance(pair):
    x1, y1, z1 = pair[0]
    x2, y2, z2 = pair[1]
    return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5

if __name__ == "__main__":
    print("TEST")
    solve(parse_text("test.txt"), 10)

    print("INPUT")
    solve(parse_text("input.txt"), 1000)
