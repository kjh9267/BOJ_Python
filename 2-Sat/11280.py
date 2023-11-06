# https://www.acmicpc.net/problem/11280
import sys
from collections import deque
sys.setrecursionlimit(999999999)


def dfs_all():
    count = [0]
    stack = deque()
    result = list()
    visited = [0 for _ in range(2 * N + 1)]
    finished = [False for _ in range(2 * N + 1)]

    for node in range(1, N * 2 + 1):
        if visited[node] != 0:
            continue
        dfs(node, visited, count, stack, result, finished)

    if is_possible(result):
        return True

    return False


def is_possible(result):
    for scc in result:
        for value in scc:
            if value + N in scc or value - N in scc:
                return False

    return True


def dfs(cur, visited, count, stack, result, finished):
    count[0] += 1
    visited[cur] = count[0]
    parent = visited[cur]
    stack.append(cur)

    for nxt in graph[cur]:
        if visited[nxt] == 0:
            parent = min(parent, dfs(nxt, visited, count, stack, result, finished))
        elif not finished[nxt]:
            parent = min(parent, visited[nxt])

    if parent == visited[cur]:
        extract(cur, stack, result, finished)

    return parent


def extract(cur, stack, result, finished):
    scc = set()

    while True:
        value = stack.pop()
        scc.add(value)
        finished[value] = True

        if value == cur:
            break

    result.append(scc)


def change_node(x):
    if x < 0:
        return -x + N
    return x


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _possible = 1
    _impossible = 0
    N, M = map(int, input().split())
    graph = [list() for _ in range(2 * N + 1)]

    for _ in range(M):
        i, j = map(int, input().split())
        x, y = change_node(-i), change_node(j)
        graph[x].append(y)

        x, y = change_node(i), change_node(-j)
        graph[y].append(x)

    if dfs_all():
        print(_possible)
    else:
        print(_impossible)
