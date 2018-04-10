import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append([0,0,[0]])
    while queue:
        a = queue.popleft()
        for i in range(n):
            if graph[a[0]][i] > 0 and i not in a[2]:
                a[2].append(i)
                queue.append([i,a[1]+graph[a[0]][i],a[2][:]])
                a[2].remove(i)
            elif len(a[2]) == n and i is 0:
                res.append(a[1] + graph[a[0]][0])


n = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
res = []

bfs()
print(min(res))