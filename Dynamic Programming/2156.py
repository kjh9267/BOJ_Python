n = input()
a = [input() for i in range(n)]
if n == 1:
    print a[0]
elif n == 2:
    print a[0] + a[1]
elif n == 3:
    print max(a[0] + a[1], a[1] + a[2], a[0] + a[2])
else:
    dp = [0]*n
    dp[0] = a[0]
    dp[1] = a[0] + a[1]
    dp[2] = max(a[0] + a[1], a[1] + a[2], a[0] + a[2])
    for i in range(3,n):
        dp[i] = max(a[i] + dp[i-2], a[i] + a[i-1] + dp[i-3], dp[i-1])
    print max(dp)