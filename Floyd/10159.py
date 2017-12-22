n = input()
m = input()
graph = [[0 for j in range(n)] for i in range(n)]
for i in range(m):
    a, b = map(int,raw_input().split())
    graph[a-1][b-1] = 1
for v in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][v] == 1 and graph[v][j] == 1:
                graph[i][j] = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[j][i] = 1
for i in range(n):
    print graph[i].count(0) - 1