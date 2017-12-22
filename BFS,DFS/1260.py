n, m, v = map(int,raw_input().split())
graph = [[0 for j in range(n)] for i in range(n)]
for i in range(m):
    a, b = map(int,raw_input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
    
def dfs(graph, start):
    stack = [start]
    visit = []
    while len(stack) != 0:
        x = stack.pop(-1)
        if x not in visit:
            visit.append(x)
            for i in range(n-1,-1,-1):
                if graph[x-1][i] == 1 and i+1 not in visit:
                    stack.append(i+1)
    return visit

def bfs(graph, start):
    queue = [start]
    visit = []
    while len(queue) != 0 :
        x = queue.pop(0)
        if x not in visit:
            visit.append(x)
            for i in range(n):
                if graph[x-1][i] == 1 and i+1 not in visit:
                    queue.append(i+1)
    return visit
print " ".join(map(str,dfs(graph,v)))
print " ".join(map(str,bfs(graph,v)))