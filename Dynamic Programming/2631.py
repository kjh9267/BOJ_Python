import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for i in range(n)]
dp = [0]*n
dp[0] = 1
for i in range(1,n):
    b = [dp[j] for j in range(i) if a[i] > a[j]]
    if a[i] > a[i-1]:
        if len(b) is 0:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = max(b) + 1
    else:
        if len(b) is 0:
            dp[i] = 1
        else:
            dp[i] = max(b) + 1
print n - max(dp)