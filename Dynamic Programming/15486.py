import sys
sys.setrecursionlimit(999999999)


def dfs(date):
    if date > N:
        return 0

    if dp[date] != -1:
        return dp[date]

    next_date = date + data[date][0]
    dp[date] = 0

    if next_date <= N + 1:
        dp[date] = max(dp[date], dfs(next_date) + data[date][1])
    dp[date] = max(dp[date], dfs(date + 1))

    return dp[date]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    data = [[1, 0]] + [list(map(int, input().split())) for _ in range(N)]
    dp = [-1 for _ in range(N + 1)]

    dfs(0)

    print(dp[0])