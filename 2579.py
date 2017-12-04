n = input()
a = [input() for i in range(n)]
dp = [0]*n
dp[0] = a[0]
dp[1] = a[1] + dp[0]
dp[2] = max(a[2] + dp[0], a[2] + a[1])
for i in range(3,n):
    dp[i] = max(a[i] + a[i-1] + dp[i-3], a[i] + dp[i-2])
print dp[-1]