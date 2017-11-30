def bfs(graph):
    queue = [1]
    while len(queue) is not 0:
        x = queue.pop(0)
        if x not in visit:
            visit.append(x)
            for i in range(n):
                if graph[x-1][i] == 1 and i + 1 not in visit:
                    queue.append(i+1)
    return visit
n = input()
m = input()
graph = [[0 for j in range(n)] for i in range(n)]
visit = []
for i in range(m):
    a, b = map(int,raw_input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
print len(bfs(graph)) - 1