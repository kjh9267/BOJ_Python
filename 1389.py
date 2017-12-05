n, m = map(int,raw_input().split())
graph = [[float('inf') for j in range(n)] for i in range(n)]
for i in range(m):
    a, b = map(int,raw_input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
for v in range(n):
    for i in range(n):
        for j in range(n):
            if i is not j:
                graph[i][j] = min(graph[i][j], graph[i][v] + graph[v][j])
res = [sum([graph[i][j] for j in range(n) if i is not j]) for i in range(n)]
print res.index(min(res)) + 1