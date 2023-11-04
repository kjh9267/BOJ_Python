# https://www.acmicpc.net/problem/15480
import sys
from math import log
sys.setrecursionlimit(999999999)


def dfs(cur, depth, prev):
    depths[cur] = depth

    for nxt in tree[cur]:
        if nxt == prev:
            continue
        parents[nxt][0] = cur
        dfs(nxt, depth + 1, cur)


def find_lca(x, y):
    if depths[x] < depths[y]:
        x, y = y, x

    for exp in range(log_n, -1, -1):
        if depths[parents[x][exp]] < depths[y]:
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


def init():
    for exp in range(1, log_n + 1):
        for node in range(1, N + 1):
            prev_node = parents[node][exp - 1]
            parents[node][exp] = parents[prev_node][exp - 1]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _new_line = "\n"
    N = int(input())
    tree = [list() for _ in range(N + 1)]
    depths = [0 for _ in range(N + 1)]
    log_n = int(log(N, 2))
    parents = [[0 for _ in range(log_n + 1)] for _ in range(N + 1)]

    for _ in range(N - 1):
        start, end = map(int, input().split())
        tree[start].append(end)
        tree[end].append(start)

    M = int(input())
    result = list()

    dfs(1, 1, 0)
    init()

    for _ in range(M):
        root, x, y = map(int, input().split())
        x_y_lca = find_lca(x, y)
        x_root_lca = find_lca(x, root)
        y_root_lca = find_lca(y, root)

        if depths[x_y_lca] < depths[x_root_lca]:
            result.append(x_root_lca)
        elif depths[x_y_lca] < depths[y_root_lca]:
            result.append(y_root_lca)
        else:
            result.append(x_y_lca)

    print(_new_line.join(map(str, result)))
