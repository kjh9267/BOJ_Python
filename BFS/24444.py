# https://www.acmicpc.net/problem/24444

from sys import stdin
from queue import PriorityQueue
from collections import deque


def bfs(start):
    queue = deque()
    queue.append(start)

    visited = [False for _ in range(N)]
    visited[start] = True

    result = [0 for _ in range(N)]
    result[start] = 1

    count = 1

    while queue:
        cur = queue.popleft()

        while not graph[cur].empty():
            nxt = graph[cur].get()

            if visited[nxt]:
                continue

            count += 1
            result[nxt] = count

            queue.append(nxt)
            visited[nxt] = True

    return result


if __name__ == '__main__':
    input = stdin.readline
    new_line = '\n'
    N, M, R = map(int, input().split())
    graph = [PriorityQueue() for _ in range(N)]

    for _ in range(M):
        start, end = map(lambda x: int(x) - 1, input().split())
        graph[start].put(end)
        graph[end].put(start)

    print(new_line.join(map(str, bfs(R - 1))))
