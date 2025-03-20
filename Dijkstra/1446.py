# https://www.acmicpc.net/problem/1446
from queue import PriorityQueue


def dijkstra():
    pq = PriorityQueue()
    pq.put((0, 0))

    dist = [_inf for _ in range(D + 1)]
    dist[0] = 0

    while not pq.empty():
        cost, cur = pq.get()

        if cost > dist[cur]:
            continue

        for nxt, next_cost in graph[cur]:
            if dist[nxt] <= dist[cur] + next_cost:
                continue
            dist[nxt] = dist[cur] + next_cost
            pq.put((dist[nxt], nxt))

    return dist[D]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _inf = float('inf')
    N, D = map(int, input().split())
    graph = [list() for _ in range(D + 1)]

    for start in range(D):
        graph[start].append((start + 1, 1))

    for _ in range(N):
        start, end, cost = map(int, input().split())

        if end > D:
            continue

        graph[start].append((end, cost))

    print(dijkstra())