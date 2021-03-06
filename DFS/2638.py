# https://www.acmicpc.net/problem/2638
import sys
sys.setrecursionlimit(999999999)


def dfs(x, y):
    if not (0 <= x < M and 0 <= y < N):
        return
    if grid[y][x] == cheese:
        adj_air_count[y][x] += 1
        if adj_air_count[y][x] == 2:
            remove_target.add((x, y))
        return
    if visited[y][x]:
        return
    visited[y][x] = True

    for diff_x, diff_y in zip(dx, dy):
        next_x = x + diff_x
        next_y = y + diff_y
        dfs(next_x, next_y)


def is_end():
    for row in grid:
        if cheese in row:
            return False
    return True


def remove():
    for x, y in remove_target:
        grid[y][x] = air


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    cheese = '1'
    air = '0'
    N, M = map(int, input().split())
    grid = [input().split() for _ in range(N)]
    time = 0

    while not is_end():
        visited = [[False for _ in range(M)] for _ in range(N)]
        adj_air_count = [[0 for _ in range(M)] for _ in range(N)]
        remove_target = set()
        dfs(0, 0)
        time += 1
        remove()

    print(time)
