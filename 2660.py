import sys
n = int(sys.stdin.readline())
inf = float('inf')
graph = [[inf for j in range(n)]for i in range(n)]
while True:
    a, b = map(int,sys.stdin.readline().split())
    if a is -1 and b is -1:
        break
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
for v in range(n):
    for i in range(n):
        for j in range(n):
            if i is not j:
                if graph[i][v] + graph[v][j] < graph[i][j]:
                    graph[i][j] = graph[i][v] + graph[v][j]
res = [max([graph[i][j] for j in range(n) if i is not j])for i in range(n)]
res2 = [i+1 for i in range(len(res)) if res[i] is min(res)]
print '{} {}'.format(min(res),res.count(min(res)))
print ' '.join(map(str,res2))