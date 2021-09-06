# https://www.acmicpc.net/problem/2780
from collections import deque
import sys
sys.setrecursionlimit(999999999)


def dfs(x, y, depth):
    if not grid[y][x]:
        return 0
    if depth == 1:
        return 1
    if dp[y][x][depth] != -1:
        return dp[y][x][depth]

    dp[y][x][depth] = 0
    for diff_x, diff_y in zip(dx, dy):
        next_x = x + diff_x
        next_y = y + diff_y
        if not (0 <= next_x < col_bound and 0 <= next_y < row_bound):
            continue
        dp[y][x][depth] += dfs(next_x, next_y, depth - 1)

    return dp[y][x][depth] % mod


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    col_bound = 3
    row_bound = 4
    mod = 1_234_567
    new_line = '\n'
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    limit = 1_000

    T = int(input())

    grid = [[True for col in range(col_bound)] for row in range(row_bound)]
    grid[3][1] = False
    grid[3][2] = False
    dp = [[[-1 for _ in range(limit + 1)] for _ in range(col_bound)] for _ in range(row_bound)]

    password_counts = [0 for _ in range(limit + 1)]

    result = deque()

    for _ in range(T):
        N = int(input())
        value = 0
        for row in range(row_bound):
            for col in range(col_bound):
                value += dfs(col, row, N)
        result.append(value % mod)

    print((new_line).join(map(str, result)))