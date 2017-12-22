import sys
n, m = map(int,sys.stdin.readline().split())
inf = float('inf')
graph = [[inf for j in range(n)]for i in range(n)]
for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 2
for v in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][v] is 1 and graph[v][j] is 1:
                graph[i][j] = 1
            if graph[i][v] is 2 and graph[v][j] is 2:
                graph[i][j] = 2
cnt = 0
for i in range(n):
    if graph[i].count(inf) is 1:
        cnt +=1
print cnt