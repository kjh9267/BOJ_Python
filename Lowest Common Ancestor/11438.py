# https://www.acmicpc.net/problem/11438
from collections import deque
from math import log


def bfs():
    queue = deque()
    queue.append(_root)

    visited = [-1 for _ in range(N + 1)]
    visited[_root] = 0

    while queue:
        cur = queue.popleft()

        for nxt in tree[cur]:
            if visited[nxt] != _not_visited:
                continue
            visited[nxt] = visited[cur] + 1
            parents[nxt][0] = cur
            queue.append(nxt)

    return visited


def init_parents():
    for exp in range(1, log_n + 1):
        for node in range(1, N + 1):
            prev_node = parents[node][exp - 1]
            parents[node][exp] = parents[prev_node][exp - 1]


def find_lowest_common_ancestor(x, y):
    if depth[x] < depth[y]:
        x, y = y, x

    for exp in range(log_n, -1, -1):
        if depth[y] > depth[parents[x][exp]]:
            continue
        x = parents[x][exp]

    if x == y:
        return x

    for exp in range(log_n, -1, -1):
        if parents[x][exp] == parents[y][exp]:
            continue
        x = parents[x][exp]
        y = parents[y][exp]

    return parents[x][0]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _root = 1
    _not_visited = -1
    _new_line = '\n'
    N = int(input())
    tree = [list() for _ in range(N + 1)]
    log_n = int(log(N, 2))
    parents = [[0 for _ in range(log_n + 1)] for _ in range(N + 1)]

    for _ in range(N - 1):
        start, end = map(int, input().split())
        tree[start].append(end)
        tree[end].append(start)

    depth = bfs()
    init_parents()

    M = int(input())
    result = deque()

    for _ in range(M):
        x, y = map(int, input().split())
        lowest_common_ancestor = find_lowest_common_ancestor(x, y)
        result.append(lowest_common_ancestor)

    print(_new_line.join(map(str, result)))