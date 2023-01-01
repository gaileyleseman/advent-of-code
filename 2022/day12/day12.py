import numpy as np


def parse_text(input_txt):
    with open(input_txt, "r") as f:
        data = np.matrix([list(line) for line in f.read().split("\n")])
    return data


def get_possible_moves(pos, mat):
    moves = []
    current_height = ord(mat[pos])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for d in directions:
        move = (pos[0] + d[0], pos[1] + d[1])
        if (
            move[0] < 0
            or move[1] < 0
            or move[0] >= mat.shape[0]
            or move[1] >= mat.shape[1]
        ):
            continue
        h = ord(mat[move])
        if h <= current_height + 1:
            moves.append(move)
    return moves


def get_possible_moves_inverse(pos, mat):
    moves = []
    current_height = ord(mat[pos])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for d in directions:
        move = (pos[0] + d[0], pos[1] + d[1])
        if (
            move[0] < 0
            or move[1] < 0
            or move[0] >= mat.shape[0]
            or move[1] >= mat.shape[1]
        ):
            continue
        h = ord(mat[move])
        if h >= current_height - 1:
            moves.append(move)
    return moves


def get_start_end_position(mat):
    hill = mat.copy()
    s = np.where(hill == "S")
    e = np.where(hill == "E")
    hill[s] = "a"
    hill[e] = "z"
    return (s[0][0], s[1][0]), (e[0][0], e[1][0]), hill


def Dijkstra(graph, source, targets):
    positions = graph.keys()
    Q = set(positions)
    dist = {v: float("inf") for v in positions}
    prev = {v: None for v in positions}
    dist[source] = 0

    while Q:
        u = min(Q, key=lambda x: dist[x])
        if u in targets:
            return dist, prev
        Q.remove(u)
        for v in graph[u]:
            if v not in Q:
                continue
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist, prev


def part1(data):
    start, end, hill = get_start_end_position(data)
    positions = [(r, c) for r in range(hill.shape[0]) for c in range(hill.shape[1])]
    graph_up = {v: get_possible_moves(v, hill) for v in positions}

    len_paths, paths = Dijkstra(graph_up, start, [end])
    return len_paths[end]


def part2(data):
    start, end, hill = get_start_end_position(data)
    positions = [(r, c) for r in range(hill.shape[0]) for c in range(hill.shape[1])]
    graph_down = {v: get_possible_moves_inverse(v, hill) for v in positions}

    starts = [p for p in positions if hill[p] == "a"]
    len_paths, paths = Dijkstra(graph_down, end, starts)
    return min([len_paths[start] for start in starts])


if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
