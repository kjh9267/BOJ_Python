import sys
n, m = map(int,sys.stdin.readline().split())
inf = float('inf')
graph = [[inf for j in range(n)]for i in range(n)]
for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    if c is 0:
        graph[a-1][b-1] = 0
        graph[b-1][a-1] = 1
    else:
        graph[a-1][b-1] = 0
        graph[b-1][a-1] = 0
for v in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][v] + graph[v][j] < graph[i][j]:
                graph[i][j] = graph[i][v] + graph[v][j]
k = int(sys.stdin.readline())
for _ in range(k):
    a, b = map(int,sys.stdin.readline().split())
    if a is b:
        print 0
    else:
        print graph[a-1][b-1]