# https://www.acmicpc.net/problem/10025

if __name__ == '__main__':
    limit = 1_000_001
    input = __import__('sys').stdin.readline
    N, K = map(int, input().split())
    data = [0 for _ in range(limit + 1)]
    dp = [0 for _ in range(limit + 1)]

    for _ in range(N):
        amount, location = map(int, input().split())
        location += 1
        data[location] = amount

    for index in range(1, limit + 1):
        dp[index] = dp[index - 1] + data[index]

    result = 0

    for index in range(1, limit + 1):
        left = max(0, index - K - 1)
        right = min(limit, index + K)
        result = max(result, dp[right] - dp[left])

    print(result)