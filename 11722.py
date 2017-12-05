n = input()
a = map(int,raw_input().split())
dp = [0]*n
dp[-1] = 1
for i in range(n-2,-1,-1):
    b = [dp[j] for j in range(n-1,i,-1) if a[i] > a[j]]
    if a[i] > a[i+1]:
        if len(b) == 0:
            dp[i] = dp[i+1]+1
        else:
            dp[i] = max(b) + 1
    else:
        if len(b) == 0:
            dp[i] = 1
        else:
            dp[i] = max(b) + 1
print max(dp)