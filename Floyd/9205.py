import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    inf = float('inf')
    graph = [[inf for j in range(n+2)]for i in range(n+2)]
    vertex = [map(int,sys.stdin.readline().split()) for i in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            if i is not j:
                if abs(vertex[i][0] - vertex[j][0]) + abs(vertex[i][1] - vertex[j][1]) <= 1000:
                    graph[i][j] = 1
    for v in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                if graph[i][v] + graph[v][j] is 2:
                    graph[i][j] = 1
    if graph[0][-1] is 1:
        print 'happy'
    else:
        print 'sad'