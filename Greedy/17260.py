# https://www.acmicpc.net/problem/17260
from sys import stdin
from collections import deque


def has_path():
    visited = [0 for _ in range(N)]

    for node, height in heights_pair:
        if visited[node] > 0:
            continue
        if node == K:
            continue
        if is_connect(node, visited):
            return True

    return False


def is_connect(node, visited):
    queue = deque()
    queue.append((node, heights[node]))

    visited[node] = heights[node]

    while queue:
        cur_node, cur_height = queue.popleft()

        for nxt_node in graph[cur_node]:
            nxt_height = (cur_height - heights[nxt_node]) / 2 + heights[nxt_node]

            if cur_height < heights[nxt_node]:
                continue
            if visited[nxt_node] >= nxt_height:
                continue
            queue.append((nxt_node, nxt_height))
            visited[nxt_node] = nxt_height

    return visited[K] > 0


if __name__ == '__main__':
    input = stdin.readline
    N, K = map(int, input().split())
    K -= 1

    heights_pair = [(node, height) for node, height in enumerate(map(int, input().split()))]
    heights_pair.sort(key=lambda x: -x[1])

    heights = [0 for _ in range(N)]

    for node, height in heights_pair:
        heights[node] = height

    graph = [list() for _ in range(N)]

    for _ in range(N - 1):
        start, end = map(lambda x: int(x) - 1, input().split())
        graph[start].append(end)
        graph[end].append(start)

    if has_path():
        print(1)
    else:
        print(0)