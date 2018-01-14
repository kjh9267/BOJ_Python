import sys
from queue import PriorityQueue  # 최단 거리를 구하기 위해 우선순위큐 사용

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = float('inf')
graph = [[] for _ in range(n)]  # 출발점과 도착점이 같고 비용이 다른 경우를 위해 n*n 행렬 사용 하지 않음
cost = [[] for _ in range(n)]  # 간선의 비용을 입력하기 위한 list
res = [inf for j in range(n)]
res[x-1] = 0

for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a-1].append(b-1)  # 간선의 도착점
    cost[a-1].append(c)     # 간선의 비용
x, y = map(int,sys.stdin.readline().split())

pq = PriorityQueue()  # 우선순위 큐 사용
for i in range(n):
    if i is x - 1:
        pq.put((0, i))      # 출발점일 경우 0으로 하여 우선순위 큐에서 제일 먼저 나오게 한다
    else:
        pq.put((inf, i))    # 다른 노드들은 모두 무한대 값

while pq.qsize():               # 우선순위 큐가 빌 때 까지 반복
    dist, node = pq.get()       # 현재노드 까지의 최소값과 현재 노드
    for i, j in zip(graph[node], cost[node]):   # 간선의 도착점과 그에 대한 비용
        if res[i] > j + res[node]:      # 도착점의 비용과 현재 노드 까지의 비용 + 도착점 까지의 비용을 비교
            res[i] = j + res[node]      # 도착점의 비용이 더 클 경우 현재 노드 까지의 비용 + 도착점 까지의 비용으로 변경
            pq.put((res[i], i))         # 갱신된 값을 우선순위 큐에도 넣어준다

print(res[y-1])