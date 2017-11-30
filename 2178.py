def bfs(graph,visit):
    queue = [[1,1]]
    level = []
    cnt = 0
    while len(queue) is not 0:
        for i in range(len(queue)):
            visit.append(queue[i])
            if [n, m] in queue:
                break
            if queue[i][0] - 1 >= 1:
                if graph[queue[i][0]-2][queue[i][1]-1] == 1 and [queue[i][0] - 1, queue[i][1]] not in visit and [queue[i][0] - 1,queue[i][1]] not in level:
                    level.append([queue[i][0] - 1,queue[i][1]])
            if queue[i][1] - 1 >= 1:
                if graph[queue[i][0]-1][queue[i][1]-2] == 1 and [queue[i][0], queue[i][1]-1] not in visit and [queue[i][0],queue[i][1]-1] not in level:
                    level.append([queue[i][0],queue[i][1]-1])
            if queue[i][0] + 1 <= len(graph):
                if graph[queue[i][0]][queue[i][1]-1] == 1 and [queue[i][0] + 1, queue[i][1]] not in visit and [queue[i][0] + 1,queue[i][1]] not in level:
                    level.append([queue[i][0] + 1,queue[i][1]])
            if queue[i][1] + 1 <= len(graph[0]):
                if graph[queue[i][0]-1][queue[i][1]] == 1 and [queue[i][0], queue[i][1]+1] not in visit and [queue[i][0],queue[i][1]+1] not in level:
                    level.append([queue[i][0],queue[i][1]+1])
        queue = []
        if len(queue) is 0:
            queue = level
            level = []
        cnt += 1
    return cnt
n, m = map(int,raw_input().split())
graph = [map(int,list(raw_input())) for i in range(n)]
visit = []
print bfs(graph,visit)