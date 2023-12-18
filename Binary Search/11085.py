# https://www.acmicpc.net/problem/11085


def binary_search():
    lo = 1
    hi = _limit

    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        visited = [False for _ in range(P)]
        dfs(C, mid, visited)

        if visited[V]:
            lo = mid
        else:
            hi = mid

    return lo


def dfs(cur, target, visited):
    if visited[cur]:
        return
    visited[cur] = True

    for nxt, width in graph[cur]:
        if width < target:
            continue
        dfs(nxt, target, visited)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _limit = 1_001
    P, W = map(int, input().split())
    C, V = map(int, input().split())
    graph = [list() for _ in range(P)]

    for _ in range(W):
        start, end, width = map(int, input().split())
        graph[start].append((end, width))
        graph[end].append((start, width))

    result = binary_search()

    print(result)
