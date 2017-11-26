n = input()
x = [map(int,raw_input().split()) for i in range(n)]
dp = [[0 for j in range(3)] for i in range(n)]
for i in range(3):
    dp[0][i] = x[0][i]
for i in range(1,n):
    dp[i][0] = min(dp[i - 1][1] + x[i][0], dp[i - 1][2] + x[i][0])
    dp[i][1] = min(dp[i - 1][0] + x[i][1], dp[i - 1][2] + x[i][1])
    dp[i][2] = min(dp[i - 1][0] + x[i][2], dp[i - 1][1] + x[i][2])
print min(dp[n-1])