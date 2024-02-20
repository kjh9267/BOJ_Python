# https://www.acmicpc.net/problem/11410
from collections import deque


def compute_mcmf():
    total_cost = 0

    while True:
        way = spfa()

        if way[_sink] == _not_visited:
            break

        total_cost += do_flow(way)

    return total_cost


def spfa():
    queue = deque()
    queue.append(_source)

    dist = [_inf for _ in range(_size)]
    dist[_source] = 0

    way = [_not_visited for _ in range(_size)]

    in_queue = [False for _ in range(_size)]
    in_queue[_source] = True

    while queue:
        cur = queue.popleft()
        in_queue[cur] = False

        for nxt in graph[cur]:
            if capacities[cur][nxt] - flows[cur][nxt] <= 0:
                continue
            if dist[nxt] <= dist[cur] + costs[cur][nxt]:
                continue
            dist[nxt] = dist[cur] + costs[cur][nxt]
            way[nxt] = cur
            if not in_queue[nxt]:
                queue.append(nxt)
                in_queue[nxt] = True

    return way


def do_flow(way):
    node = _sink
    flow_value = _inf
    cost = 0

    while node != _source:
        prev = way[node]
        flow_value = min(flow_value, capacities[prev][node] - flows[prev][node])
        node = prev

    node = _sink
    while node != _source:
        prev = way[node]
        flows[prev][node] += flow_value
        flows[node][prev] -= flow_value
        cost += flow_value * costs[prev][node]
        node = prev

    return cost


def connect(start, end, capacity, cost):
    graph[start].append(end)
    graph[end].append(start)
    capacities[start][end] = capacity
    costs[start][end] = cost
    costs[end][start] = -cost


def init():
    connect(_source, 2, P, 0)

    for node in range(1, N):
        connect(node * 2 + 1, (node + 1) * 2, P, 0)

    for node in range(1, N + 1):
        connect(node * 2, node * 2 + 1, P, 0)

    for start, data in enumerate(zip(people, money)):
        people_data, money_data = data

        for end, value in enumerate(zip(people_data, money_data)):
            capacity, cost = value
            connect((start + 1) * 2 + 1, (N - end) * 2 + 1, capacity, -cost)

    connect((N * 2) + 1, _sink, P, 0)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, P = map(int, input().split())
    _inf = float('inf')
    _not_visited = -1
    _source = 0
    _sink = (N * 2) + 2
    _size = (N * 2) + 3
    graph = [list() for _ in range(_size)]
    capacities = [[0 for _ in range(_size)] for _ in range(_size)]
    flows = [[0 for _ in range(_size)] for _ in range(_size)]
    costs = [[0 for _ in range(_size)] for _ in range(_size)]
    people = [reversed(list((map(int, input().split())))) for _ in range(N - 1)]
    money = [reversed(list(map(int, input().split()))) for _ in range(N - 1)]

    init()
    result = compute_mcmf()

    print(-result)
