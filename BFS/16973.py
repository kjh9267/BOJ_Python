# https://www.acmicpc.net/problem/16973

from sys import stdin
from collections import deque


def bfs():
    queue = deque()
    queue.append((start_col, start_row))

    visited = [[not_visited for _ in range(M + 1)] for _ in range(N + 1)]
    visited[start_row][start_col] = 0

    while queue:
        x, y = queue.popleft()

        for diff_x, diff_y in zip(dx, dy):
            next_x = x + diff_x
            next_y = y + diff_y

            if not is_in_grid(next_x, next_y):
                continue
            if has_wall(next_x, next_y):
                continue
            if visited[next_y][next_x] != not_visited:
                continue
            visited[next_y][next_x] = visited[y][x] + 1
            queue.append((next_x, next_y))

    return visited[end_row][end_col]


def is_in_grid(x, y):
    return x > 0 and x + W - 1 <= M and y > 0 and y + H - 1 <= N


def has_wall(x, y):
    return wall_info[y + H - 1][x + W - 1] - wall_info[y - 1][x + W - 1] - wall_info[y + H - 1][x - 1] + wall_info[y - 1][x - 1]


def init_wall_info():
    wall_info = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for row in range(1, N + 1):
        wall_info[row][1] = grid[row - 1][0]

    for col in range(1, M + 1):
        wall_info[1][col] = grid[0][col - 1]

    for row in range(2, N + 1):
        for col in range(2, M + 1):
            wall_info[row][col] = wall_info[row - 1][col] + wall_info[row][col - 1] + grid[row - 1][col - 1] - wall_info[row - 1][col - 1]

    return wall_info


if __name__ == '__main__':
    input = stdin.readline
    wall = '1'
    not_visited = -1
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    H, W, start_row, start_col, end_row, end_col = map(int, input().split())

    wall_info = init_wall_info()
    result = bfs()

    print(result)
