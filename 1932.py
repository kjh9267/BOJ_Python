n = input()
x = [map(int,raw_input().split()) for i in range(n)]
dp = [[0 for u in range(i*2)] for i in range(1,len(x))]
dp.insert(0,x[0])
for i in range(1,len(x)):
    dp[i][0] = x[i][0] + dp[i-1][0]
    dp[i][2*i-1] = x[i][i] + dp[i-1][2*(i-1)-1]
for i in range(2,len(x)):
    for u in range(1,i*2-1,2):
        '''dp[i][u] = dp[i-1][u-1] + x[i][]
        dp[i][u+1] = dp[i-1][u] + x[i][]'''
        print dp