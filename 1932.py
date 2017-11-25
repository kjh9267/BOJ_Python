n = input()
x = [map(int,raw_input().split()) for i in range(n)]
dp = [[0 for j in range(n)] for i in range(n)]
dp[0][0] = x[0][0]
for i in range(1,n):
    for j in range(len(x[i])):
        if j-1 < 0:
            dp[i][j] = dp[i - 1][ j] + x[i][j]
        elif j == len(x):
            dp[i][ j] = dp[i - 1][ j - 1] + x[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1]+x[i][j],dp[i-1][j]+x[i][j])
print max(dp[n-1])