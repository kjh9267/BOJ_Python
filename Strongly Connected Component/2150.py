# https://www.acmicpc.net/problem/2150
import sys
sys.setrecursionlimit(999999999)


def dfs_all():
    visited = [0 for _ in range(V + 1)]
    finished = [False for _ in range(V + 1)]
    stack = list()
    index = [0]

    for node in range(1, V + 1):
        if visited[node] == 0:
            dfs(node, index, count, visited, stack, finished)


def dfs(cur, index, count, visited, stack, finished):
    index[0] += 1
    visited[cur] = index[0]
    parent = visited[cur]
    stack.append(cur)

    for nxt in graph[cur]:
        if visited[nxt] == 0:
            parent = min(parent, dfs(nxt, index, count, visited, stack, finished))
        elif not finished[nxt]:
            parent = min(parent, visited[nxt])

    if parent == visited[cur]:
        extract(cur, count, stack, finished)

    return parent


def extract(cur, count, stack, finished):
    count[0] += 1
    value = 0
    temp = list()

    while value != cur:
        value = stack.pop()
        finished[value] = True
        temp.append(value)

    result.append(temp)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _end = -1
    _space = " "
    _new_line = "\n"
    V, E = map(int, input().split())
    graph = [list() for _ in range(V + 1)]
    index = [0]
    count = [0]
    result = list()

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    dfs_all()
    print(count[0])
    result = sorted(map(lambda x: x + [_end], map(sorted, result)))
    print(_new_line.join(map(lambda x: _space.join(map(str, x)), result)))