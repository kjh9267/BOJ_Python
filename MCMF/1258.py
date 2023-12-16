# https://www.acmicpc.net/problem/1258

from sys import stdin
from collections import deque


def network_flow():
    total = 0

    while True:
        way = spfa()
        if way[sink] == not_visited:
            break
        total = do_flow(way, total)

    return total


def spfa():
    queue = deque()
    queue.append(source)

    in_queue = [False for _ in range(size)]
    in_queue[source] = True

    way = [not_visited for _ in range(size)]

    dist = [inf for _ in range(size)]
    dist[source] = 0

    while queue:
        cur = queue.popleft()
        in_queue[cur] = False

        for nxt, value in enumerate(zip(capacities[cur], flows[cur])):
            capacity, flow = value
            if capacity - flow <= 0:
                continue
            if dist[nxt] <= dist[cur] + costs[cur][nxt]:
                continue
            dist[nxt] = dist[cur] + costs[cur][nxt]
            way[nxt] = cur
            if in_queue[nxt]:
                continue
            in_queue[nxt] = True
            queue.append(nxt)

    return way


def do_flow(way, total):
    node = sink

    while node != source:
        prev = way[node]
        flows[prev][node] += 1
        flows[node][prev] -= 1
        total += costs[prev][node]
        node = prev

    return total


if __name__ == '__main__':
    input = stdin.readline
    inf = 1_000_000
    not_visited = -1
    N = int(input())
    source = 0
    sink = N * 2 + 1
    size = N * 2 + 2
    total = 0
    capacities = [[0 for _ in range(size)] for _ in range(size)]
    flows = [[0 for _ in range(size)] for _ in range(size)]
    costs = [[0 for _ in range(size)] for _ in range(size)]

    for student in range(1, N + 1):
        capacities[source][student] = 1

        for problem, time in enumerate(input().split()):
            time = int(time)
            capacities[student][problem + 1 + N] = 1
            costs[student][problem + 1 + N] = time
            costs[problem + 1 + N][student] = -time

    for problem in range(N + 1, N * 2 + 1):
        capacities[problem][sink] = 1

    total = network_flow()
    print(total)