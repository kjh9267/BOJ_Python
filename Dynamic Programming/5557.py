# https://www.acmicpc.net/problem/5557


def dfs(cur, total):
    if cur == N - 1:
        if total == nums[cur]:
            return 1
        return 0
    if dp[cur][total] != -1:
        return dp[cur][total]

    dp[cur][total] = 0
    if total - nums[cur] >= 0:
        dp[cur][total] += dfs(cur + 1, total - nums[cur])
    if total + nums[cur] <= _limit:
        dp[cur][total] += dfs(cur + 1, total + nums[cur])

    return dp[cur][total]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _limit = 20
    N = int(input())
    nums = list(map(int, input().split()))
    dp = [[-1 for _ in range(_limit + 1)] for _ in range(N)]
    print(dfs(1, nums[0]))