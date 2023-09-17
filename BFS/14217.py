# https://www.acmicpc.net/problem/14217
from collections import deque


def bfs():
    queue = deque()
    queue.append(_start)

    visited = [_not_visited for _ in range(N)]
    visited[_start] = 0

    while queue:
        cur = queue.popleft()

        for nxt, is_connected in enumerate(graph[cur]):
            if not is_connected:
                continue
            if visited[nxt] != _not_visited:
                continue
            visited[nxt] = visited[cur] + 1
            queue.append(nxt)

    return visited


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _connect = 0
    _start = 0
    _not_visited = -1
    _space = " "
    _new_line = "\n"
    result = list()
    N, M = map(int, input().split())
    graph = [[False for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        start, end = map(lambda x: int(x) - 1, input().split())
        graph[start][end] = True
        graph[end][start] = True

    Q = int(input())

    for _ in range(Q):
        command, start, end = map(lambda x: int(x) - 1, input().split())
        if command == _connect:
            graph[start][end] = True
            graph[end][start] = True
        else:
            graph[start][end] = False
            graph[end][start] = False

        dist = bfs()
        result.append(_space.join(map(str, dist)))

    print(_new_line.join(result))