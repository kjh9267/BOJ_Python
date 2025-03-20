# https://www.acmicpc.net/problem/2178

from collections import deque


def bfs():
    queue = deque()
    queue.append((_start_x, _start_y))

    visited = [[_not_visited for _ in range(M)] for _ in range(N)]
    visited[_start_y][_start_x] = 0

    while queue:
        x, y = queue.popleft()

        for diff_x, diff_y in zip(dx, dy):
            next_x = x + diff_x
            next_y = y + diff_y

            if not (0 <= next_x < M and 0 <= next_y < N):
                continue
            if grid[next_y][next_x] == _wall:
                continue
            if visited[next_y][next_x] != _not_visited:
                continue
            visited[next_y][next_x] = visited[y][x] + 1
            queue.append((next_x, next_y))

    return visited[N - 1][M - 1] + 1


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _not_visited = -1
    _wall = '0'
    _start_x = 0
    _start_y = 0
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    N, M = map(int, input().split())
    grid = [input().rstrip() for _ in range(N)]

    print(bfs())
