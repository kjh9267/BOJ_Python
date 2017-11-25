t = input()
dp = [1, 2, 4, 7, 0, 0, 0, 0, 0, 0]
for i in range(4,10):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for i in range(t):
    n = input()
    print dp[n-1]