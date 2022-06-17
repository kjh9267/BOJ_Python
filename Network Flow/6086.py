import sys
from collections import deque


def change(char):
    if ord(char) <= 90:
        return ord(char) - 65
    return ord(char) - 97 + 26


def network_flow():
    total = 0

    while True:
        way = bfs(start)
        if way[target] == not_visited:
            break
        flow_value = calculate_flow_value(way)
        do_flow(flow_value, way)
        total += flow_value

    return total


def bfs(start):
    queue = deque()
    queue.append(start)
    way = [not_visited for _ in range(size)]

    while queue:
        cur = queue.popleft()
        for nxt in range(size):
            if not can_flow_more(cur, nxt):
                continue
            if way[nxt] != not_visited:
                continue
            queue.append(nxt)
            way[nxt] = cur
            if nxt == target:
                return way

    return way


def can_flow_more(cur, nxt):
    return capacity[cur][nxt] - flow[cur][nxt] > 0


def calculate_flow_value(way):
    flow_value = inf
    node = target

    while node != start:
        if flow_value > capacity[way[node]][node] - flow[way[node]][node]:
            flow_value = capacity[way[node]][node] - flow[way[node]][node]
        node = way[node]

    return flow_value


def do_flow(flow_value, way):
    node = target

    while node != start:
        flow[way[node]][node] += flow_value
        flow[node][way[node]] -= flow_value
        node = way[node]


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    inf = float('inf')
    size = 52
    start = 0
    target = 25
    not_visited = -1
    capacity = [[0 for _ in range(size)] for _ in range(size)]
    flow = [[0 for _ in range(size)] for _ in range(size)]

    for _ in range(n):
        u, v, w = sys.stdin.readline().split()
        u = change(u)
        v = change(v)
        w = int(w)
        capacity[u][v] += w
        capacity[v][u] += w

    total = network_flow()
    print(total)