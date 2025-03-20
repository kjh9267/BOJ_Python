# https://www.acmicpc.net/problem/1197
from queue import PriorityQueue


def find(x):
    if parents[x] < 0:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def merge(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    if parents[x] < parents[y]:
        parents[x] += parents[y]
        parents[y] = x
    else:
        parents[y] += parents[x]
        parents[x] = y

    return True


def mst():
    count = 0
    total = 0

    while not pq.empty():
        cost, start, end = pq.get()

        if merge(start, end):
            count += 1
            total += cost
            if count == V - 1:
                return total

    return total


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    V, E = map(int, input().split())
    parents = [-1 for _ in range(V + 1)]
    pq = PriorityQueue()

    for _ in range(E):
        start, end, cost = map(int, input().split())
        pq.put((cost, start, end))

    if V == 1:
        print(pq.get()[0])
    else:
        print(mst())