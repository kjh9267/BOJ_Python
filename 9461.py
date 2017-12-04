for i in range(input()):
    dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21]
    n = input()
    if n <= 13:
        print dp[n-1]
    else:
        for j in range(14,n+1):
            dp.append(dp[-1] + dp[-5])
        print dp[-1]