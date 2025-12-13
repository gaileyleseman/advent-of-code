def parse_text(input_txt):
    data = {}
    with open(input_txt, "r") as f:
        for line in f.read().split("\n"):
            [start, end] = line.split(":")
            data[start.strip()] = set(end.strip().split())
    return data


def solve_pt1(data):
    print(f"part1 = {find_num_paths_to_node('you', 'out', data)}")


def find_num_paths_to_node(start_node, end_node, graph, cache=None):
    if cache is None:
        cache = {end_node: 1}
    if start_node in cache:
        return cache[start_node]
    ans = 0
    for next_node in graph[start_node]:
        ans += find_num_paths_to_node(next_node, end_node, graph, cache)
    cache[start_node] = ans
    return ans


def solve_pt2(data):
    data["out"] = []
    print(f"ref = {find_num_paths_to_node('svr', 'out', data)}")
    combos = [
        [["svr", "dac"],["dac", "fft"],["fft", "out"]],
        [["svr", "fft"], ["fft", "dac"], ["dac", "out"]],
    ]
    answer = 0
    for combo_set in combos:
        set_answer = 1
        for combo in combo_set:
            set_answer *= find_num_paths_to_node(combo[0], combo[1], data)
        answer += set_answer
    print(f"part2 = {answer}")


if __name__ == "__main__":
    print("TEST")
    solve_pt1(parse_text("test1.txt"))
    solve_pt2(parse_text("test2.txt"))

    print("INPUT")
    solve_pt1(parse_text("input.txt"))
    solve_pt2(parse_text("input.txt"))
