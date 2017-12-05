v, e = map(int,raw_input().split())
inf = float('inf')
graph = [[inf for j in range(v)] for i in range(v)]
for i in range(e):
    a, b, c = map(int,raw_input().split())
    graph[a-1][b-1] = c
for u in range(v):
    for i in range(v):
        for j in range(v):
            graph[i][j] = min(graph[i][j], graph[i][u] + graph[u][j])
res = min([graph[i][i] for i in range(v)])
if type(res) == float:
    print -1
else:
    print res