from queue import PriorityQueue
from math import ceil


def solution(x, y):
    N = len(x)
    pq = PriorityQueue()
    parents = [-1 for _ in range(N)]

    for node1 in range(N):
        for node2 in range(node1 + 1, N):
            distance = get_distance(x, y, node1, node2)
            pq.put((distance, node1, node2))

    return get_max_distance(pq, parents, N)


def get_distance(x, y, node1, node2):
    return ((x[node1] - x[node2]) ** 2 + (y[node1] - y[node2]) ** 2) ** (1 / 2)


def find(x, parents):
    if parents[x] < 0:
        return x
    parents[x] = find(parents[x], parents)
    return parents[x]


def merge(x, y, parents):
    x = find(x, parents)
    y = find(y, parents)

    if x == y:
        return False

    if parents[x] > parents[y]:
        parents[y] += parents[x]
        parents[x] = y
    else:
        parents[x] += parents[y]
        parents[y] = x

    return True


def get_max_distance(pq, parents, N):
    count = 0
    max_distance = 0

    while not pq.empty():
        distance, node1, node2 = pq.get()
        if merge(node1, node2, parents):
            max_distance = max(max_distance, distance)
            count += 1
            if count == N - 1:
                break

    return ceil(max_distance)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline

    print(solution([1, 2, 6, 8]	, [1, 2, 5, 7]	))
    print(solution([1, 2, 4, 2]	, [1, 1, 4, 2]	))
    print(solution([1, 2], [2, 1]))