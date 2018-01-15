import sys
from queue import PriorityQueue     # 우선순위 큐

n, m, x = map(int, sys.stdin.readline().split())
inf = float('inf')
graph = [[] for _ in range(m)]           # 정방향 그래프
cost = [[] for _ in range(m)]            # 정방향 그래프의 비용
reverse_graph = [[] for _ in range(m)]   # 역방향 그래프 (역방향 그래프를 이용하여 도착지 까지 모든 노드들의 최소값 구함)
reverse_cost = [[] for _ in range(m)]    # 역방향 그래프의 비용

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a - 1].append(b - 1)
    cost[a - 1].append(c)
    reverse_graph[b - 1].append(a - 1)
    reverse_cost[b - 1].append(c)

pq = PriorityQueue()

for i in range(n):
    if i is x - 1:
        pq.put((0, i))          # 출발 노드는 거리를 0으로 하여 우선순위 큐에서 제일 먼저 나오게 한다
    else:
        pq.put((inf, i))        # 출발 노드를 제외한 곳은 모두 무한대 값

res = [inf for i in range(n)]
res[x-1] = 0

while pq.qsize():                               # 정방향 그래프를 이용한 다익스트라 알고리즘
    dist, node = pq.get()
    for i, j in zip(graph[node], cost[node]):    # 간선의 도착점과 그에 대한 비용
        if res[i] > j + res[node]:               # 도착점의 비용과 도착점의 비용 + 전 노드까지의 값을 비교
            res[i] = j + res[node]               # 도착점의 비용이 더 클 경우 도착점의 비용 + 전 노드까지의 값으로 변경
            pq.put((res[i], i))                  # 갱신된 값을 우선순위 큐에도 넣어준다

reverse_pq = PriorityQueue()

for i in range(n):
    if i is x - 1:
        reverse_pq.put((0, i))
    else:
        reverse_pq.put((inf, i))

reverse_res = [inf for i in range(n)]
reverse_res[x-1] = 0

while reverse_pq.qsize():                                           # 역방향 그래프를 이용한 다익스트라 알고리즘
    dist, node = reverse_pq.get()
    for i, j in zip(reverse_graph[node], reverse_cost[node]):
        if reverse_res[i] > j + reverse_res[node]:
            reverse_res[i] = j + reverse_res[node]
            reverse_pq.put((reverse_res[i], i))

result = [res[i] + reverse_res[i] for i in range(n)]                # 결과값 두개를 각각 합하여 왕복값을 구한 list
print(max(result))