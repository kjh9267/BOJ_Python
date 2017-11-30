def bfs(graph, visit, start):
    cnt = 0
    queue = start
    level = []
    while len(queue) is not 0:
        for i in range(len(queue)):
            if queue[i][0]-1 >= 0 and graph[queue[i][0]-1][queue[i][1]] == 0:
                visit[queue[i][0] - 1][queue[i][1]] = 1
                level.append([queue[i][0]-1, queue[i][1]])
            if queue[i][1]-1 >= 0 and graph[queue[i][0]][queue[i][1]-1] == 0:
                visit[queue[i][0]][queue[i][1] - 1] = 1
                level.append([queue[i][0], queue[i][1] -1])
            if queue[i][0]+1 < n and graph[queue[i][0]+1][queue[i][1]] == 0:
                visit[queue[i][0] + 1][queue[i][1]] = 1
                level.append([queue[i][0]+1, queue[i][1]])
            if queue[i][1]+1 < m and graph[queue[i][0]][queue[i][1]+1] == 0:
                visit[queue[i][0]][queue[i][1] + 1] = 1
                level.append([queue[i][0], queue[i][1]+1])
        queue = []
        graph = visit
        if len(queue) is 0:
            queue = level
            level = []
            cnt += 1
    return cnt - 1
m, n = map(int,raw_input().split())
graph = [map(int,raw_input().split()) for i in range(n)]
visit = [[graph[i][j] for j in range(m)]for i in range(n)]
res = [[graph[i][j] for j in range(m)]for i in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            res[i][j] = 1
start = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            start.append([i,j])
a = bfs(graph,visit,start)
if visit != res:
    print -1
else:
    print a