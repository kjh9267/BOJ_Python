n = input()
s = map(int,raw_input().split())
dp = [0for j in range(n)]
dp[0] = s[0]
for i in range(1,n):
    dp[i] = max(dp[i-1] + s[i], s[i])
print max(dp)