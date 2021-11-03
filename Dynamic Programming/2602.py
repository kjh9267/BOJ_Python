# https://www.acmicpc.net/problem/2602
from sys import stdin


def dfs(magic_string_index, x, y):
    if magic_string_index == m:
        return 0
    if magic_string_index == m - 1 and magic_string[magic_string_index] == data[y][x]:
        return 1
    if magic_string[magic_string_index] != data[y][x]:
        return 0
    if dp[y][x][magic_string_index] != 0:
        return dp[y][x][magic_string_index]

    for nxt in range(x + 1, n):
        if y == 0:
            dp[y][x][magic_string_index] += dfs(magic_string_index + 1, nxt, 1)
        else:
            dp[y][x][magic_string_index] += dfs(magic_string_index + 1, nxt, 0)

    return dp[y][x][magic_string_index]


if __name__ == '__main__':
    input = stdin.readline
    magic_string = list(input().rstrip())
    data = [input().rstrip() for _ in range(2)]
    n = len(data[0])
    m = len(magic_string)
    dp = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]
    result = 0

    for row in range(2):
        for col in range(n):
            if data[row][col] != magic_string[0]:
                continue
            result += dfs(0, col, row)

    print(result)