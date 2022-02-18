# https://www.acmicpc.net/problem/1595

from sys import stdin
from collections import deque


def bfs(start):
    queue = deque()
    queue.append(start)

    visited = [-1 for _ in range(limit)]
    visited[start] = 0

    while queue:
        cur = queue.popleft()

        for nxt, cost in graph[cur]:
            if visited[nxt] != -1:
                continue
            visited[nxt] = visited[cur] + cost
            queue.append(nxt)

    max_distance = max(visited)

    return visited.index(max_distance), max_distance


if __name__ == '__main__':
    input = stdin.readline
    limit = 10_001

    graph = [list() for _ in range(limit)]

    while True:
        line = input().rstrip()

        if line == '':
            break

        start, end, cost = map(int, line.split())
        graph[start].append((end, cost))
        graph[end].append((start, cost))

    next_start, _ = bfs(1)
    _, result = bfs(next_start)

    print(result)