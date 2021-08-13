# https://www.acmicpc.net/problem/5719
from queue import PriorityQueue


def dijkstra():
    pq = PriorityQueue()
    pq.put((0, S))
    dist[S] = 0

    while not pq.empty():
        _, cur = pq.get()

        for nxt, cost in graph[cur]:
            if graph[cur][nxt] == 0:
                continue
            if dist[nxt] <= dist[cur] + cost:
                continue
            dist[nxt] = dist[cur] + cost
            pq.put((dist[nxt], nxt))

    return dist


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    inf = float('inf')
    result = list()

    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break

        S, D = map(int, input().split())
        graph = [[0 for _ in range(N)] for _ in range(N)]
        dist = [inf for _ in range(N)]

        for _ in range(M):
            U, V, P = map(int, input().split())
            graph[U][V] = P

        dijkstra()

        print(dist)

