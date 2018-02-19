import sys

n = int(sys.stdin.readline())
dp = [0]*1000
dp[0] = 1
dp[1] = 3
dp[2] = 5

for i in range(3,n):
    dp[i] = (dp[i-1] + dp[i-2] * 2)%10007

print(dp[n-1])