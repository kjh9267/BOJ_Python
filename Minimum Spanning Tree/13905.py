# https://www.acmicpc.net/problem/13905
from queue import PriorityQueue
from collections import deque


class Link:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

    def __lt__(self, other):
        return self.cost > other.cost


def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def merge(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y
    return True


def mst():
    count = 0

    while not pq.empty():
        link = pq.get()
        if not merge(link.x, link.y):
            continue
        tree[link.x].append((link.y, link.cost))
        tree[link.y].append((link.x, link.cost))
        count += 1
        if count == N - 1:
            break


def bfs():
    queue = deque()
    queue.append((start, inf))

    visited = [False for _ in range(N + 1)]
    visited[start] = True

    result = inf

    while queue:
        cur, cur_cost = queue.popleft()

        if cur == end:
            result = min(result, cur_cost)

        for nxt, nxt_cost in tree[cur]:
            if visited[nxt]:
                continue
            visited[nxt] = True
            queue.append((nxt, min(cur_cost, nxt_cost)))

    return 0 if result == inf else result


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    inf = float('inf')
    N, M = map(int, input().split())
    start, end = map(int, input().split())
    parent = [-1 for _ in range(N + 1)]
    tree = [list() for _ in range(N + 1)]
    pq = PriorityQueue()

    for _ in range(M):
        h1, h2, k = map(int, input().split())
        pq.put(Link(h1, h2, k))

    mst()

    print(bfs())
