# https://www.acmicpc.net/problem/1766
from sys import stdin
from queue import PriorityQueue


def put_problems():
    for problem in range(1, N + 1):
        in_degree = in_degrees[problem]
        if visited[problem]:
            continue
        if in_degree != 0:
            continue
        pq.put(problem)


def topological_sort():
    while not pq.empty():
        cur_problem = pq.get()
        result.append(cur_problem)
        visited[cur_problem] = True

        for nxt_problem in graph[cur_problem]:
            in_degrees[nxt_problem] -= 1
            if in_degrees[nxt_problem] != 0 or visited[nxt_problem]:
                continue
            pq.put(nxt_problem)


if __name__ == '__main__':
    input = stdin.readline
    space = " "
    N, M = map(int, input().split())
    in_degrees = [0 for _ in range(N + 1)]
    graph = [list() for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    pq = PriorityQueue()
    result = list()

    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        in_degrees[B] += 1

    put_problems()

    topological_sort()

    print(space.join(map(str, result)))