# https://www.acmicpc.net/problem/14261
from collections import deque


def dinic():
    total = 0

    while True:
        level = [-1 for _ in range(size)]
        if not bfs(level):
            break
        work = [0 for _ in range(size)]
        while True:
            flow_value = dfs(source, work, level, _inf)
            if flow_value == 0:
                break
            total += flow_value

    return total


def bfs(level):
    queue = deque()
    queue.append(source)

    level[source] = 0

    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if level[nxt] != -1:
                continue
            if capacity[cur][nxt] - flow[cur][nxt] <= 0:
                continue
            level[nxt] = level[cur] + 1
            queue.append(nxt)

    return level[sink] != -1


def dfs(cur, work, level, flow_value):
    if cur == sink:
        return flow_value

    for index in range(work[cur], len(graph[cur])):
        work[cur] = index
        nxt = graph[cur][index]
        if level[nxt] != level[cur] + 1:
            continue
        if capacity[cur][nxt] - flow[cur][nxt] <= 0:
            continue
        min_flow_value = min(flow_value, capacity[cur][nxt] - flow[cur][nxt])
        min_flow_value = dfs(nxt, work, level, min_flow_value)

        if min_flow_value <= 0:
            continue

        flow[cur][nxt] += min_flow_value
        flow[nxt][cur] -= min_flow_value

        return min_flow_value

    return 0


def is_terminal_node(x):
    return x == source or x == N


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _inf = float('inf')
    _max_capacity = 100_000
    _yes = "YES"
    _no = "NO"
    N, M, K = map(int, input().split())
    nums = list(map(int, input().split()))
    source = 1
    sink = (N - 1) * 2
    size = (N - 1) * 2 + 1
    flow = [[0 for _ in range(size)] for _ in range(size)]
    capacity = [[0 for _ in range(size)] for _ in range(size)]
    graph = [list() for _ in range(size)]

    for _ in range(M):
        start, end = map(int, input().split())
        if end < start:
            start, end = end, start
        if is_terminal_node(start) and is_terminal_node(end):
            end = sink
            graph[start].append(sink)
            capacity[start][sink] = _max_capacity

            # graph[end].append(start)
        elif is_terminal_node(start):
            graph[start].append((end - 1) * 2)
            capacity[start][(end - 1) * 2] = _max_capacity
        elif is_terminal_node(end):
            end = sink
            graph[(start - 1) * 2 + 1].append(sink)
            capacity[(start - 1) * 2 + 1][sink] = _max_capacity
        else:
            graph[(start - 1) * 2 + 1].append((end - 1) * 2)
            capacity[(start - 1) * 2 + 1][(end - 1) * 2] = _max_capacity
            graph[(end - 1) * 2 + 1].append((start - 1) * 2)
            capacity[(end - 1) * 2 + 1][(start - 1) * 2] = _max_capacity

    for node in range(2, N):
        start = (node - 1) * 2
        end = (node - 1) * 2 + 1
        graph[start].append(end)
        capacity[start][end] = nums[node - 1]

    total = dinic()

    if total <= K:
        print(_yes)
    else:
        print(_no)
