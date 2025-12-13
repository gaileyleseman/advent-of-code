from collections import defaultdict

def parse_text(input_txt):
    data = {}
    with open(input_txt, "r") as f:
        for line in f.read().split("\n"):
            [start, end] = line.split(":")
            data[start.strip()] = set(end.strip().split())
    return data


def solve_pt1(data):
    cache = {"out": 1}
    print(f"part1 = {find_num_paths_to_node('you', 'out', data, cache)}")


def find_num_paths_to_node(start_node, end_node, graph, cache):
    if start_node in cache:
        return cache[start_node]
    ans = 0
    for next_node in graph[start_node]:
        ans += find_num_paths_to_node(next_node, end_node, graph, cache)
    cache[start_node] = ans
    return ans


def solve_pt2(data):
    print(len(data))
    cache = {"out": 1}
    data["out"] = []
    print(data["out"])
    print(f"ref = {find_num_paths_to_node('svr', 'dac', data, cache)}")
    paths = find_paths_to_node("svr", "dac", data)
    print(len(paths))


def find_paths_to_node(start, end, graph):
    paths = []
    stack = [(start, [start])]  # (node, path)
    while stack:
        u, p = stack.pop()
        if u == end:
            paths.append((p))
            continue
        for v in graph[u]:
            if v not in p:  # avoid cycles
                stack.append((v, p + [v]))
    return paths


if __name__ == "__main__":
    print("TEST")
    # solve_pt1(parse_text("test1.txt"))
    # solve_pt2(parse_text("test2.txt"))

    print("INPUT")
    # solve_pt1(parse_text("input.txt"))
    solve_pt2(parse_text("input.txt"))
