import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = float('inf')
graph = [[inf for j in xrange(n)]for i in xrange(n)]
for _ in xrange(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
visit = []
team = []
for i in xrange(n):
    y = []
    if i not in visit:
        queue = [i]
    while len(queue) is not 0:
        x = queue.pop(0)
        visit.append(x)
        y.append(x)
        for j in xrange(n):
            if graph[x][j] is 1 and j not in visit and j not in queue:
                queue.append(j)
    if len(y) is not 0:
        team.append(y)
for v in xrange(n):
    for i in xrange(n):
        for j in xrange(n):
            if i is not j:
                if graph[i][v] + graph[v][j] < graph[i][j]:
                    graph[i][j] = graph[i][v] + graph[v][j]
z = [[graph[i][j] for j in xrange(n) if graph[i][j] is not inf] for i in xrange(n)]
for i in range(n):
    if len(z[i]) is 0:
        z[i] = [0]
res = [[max(z[team[i][j]]) for j in xrange(len(team[i]))]for i in xrange(len(team))]
print len(res)
end = sorted([team[i][(res[i].index(min(res[i])))] + 1 for i in xrange(len(res))])
for i in range(len(end)):
    print end[i]