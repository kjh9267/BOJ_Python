import sys

n, m = map(int,sys.stdin.readline().split())
graph = [map(int,sys.stdin.readline().split()) for _ in xrange(n)]
dp = [[0 for j in xrange(m)] for i in xrange(n)]
dp[0][0] = graph[0][0]
for i in xrange(1,m):
    dp[0][i] = dp[0][i-1] + graph[0][i]
for i in xrange(1,n):
    dp[i][0] = dp[i-1][0] + graph[i][0]
for i in xrange(1,n):
    for j in xrange(1,m):
        dp[i][j] = max(dp[i-1][j] + graph[i][j], dp[i][j-1] + graph[i][j], dp[i-1][j-1] + graph[i][j])
print dp[n-1][m-1]