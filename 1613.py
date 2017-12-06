import sys
n, k = map(int,sys.stdin.readline().split())
inf = float('inf')
graph = [[inf for j in range(n)]for i in range(n)]
for _ in range(k):
    a, b = map(int,sys.stdin.readline().split())
    graph[a-1][b-1] = 1
for v in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][v] is 1 and graph[v][j] is 1:
                graph[i][j] = 1
s = int(sys.stdin.readline())
for _ in range(s):
    c, d = map(int,sys.stdin.readline().split())
    if graph[c-1][d-1] is 1:
        print -1
    elif graph[d-1][c-1] is 1:
        print 1
    else:
        print 0