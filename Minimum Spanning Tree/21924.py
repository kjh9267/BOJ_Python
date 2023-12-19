# https://www.acmicpc.net/problem/21924
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


def find_minimum_spanning_tree_cost():
    count = 0
    minimum_cost = 0

    while not pq.empty():
        cost, start, end = pq.get()

        if merge(start, end):
            count += 1
            minimum_cost += cost

            if count == N - 1:
                return minimum_cost

    return _impossible


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _impossible = -1
    N, M = map(int, input().split())
    pq = PriorityQueue()
    parents = [-1 for _ in range(N + 1)]
    total = 0

    for _ in range(M):
        start, end, cost = map(int, input().split())
        pq.put((cost, start, end))
        total += cost

    minimum_cost = find_minimum_spanning_tree_cost()

    if minimum_cost == _impossible:
        print(_impossible)
    else:
        print(total - minimum_cost)
