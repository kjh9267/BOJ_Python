# https://www.acmicpc.net/problem/2611
from collections import deque
import sys
sys.setrecursionlimit(999999999)


def dfs(cur):
    if cur == _end:
        return 0
    if dp[cur] != -1:
        return dp[cur]

    dp[cur] = 0
    for nxt, cost in graph[cur]:
        dp[cur] = max(dp[cur], dfs(nxt) + cost)

    return dp[cur]


def find_way(cur, total):
    if cur == _start:
        return total == dp[_start]
    if visited[cur]:
        return False
    visited[cur] = True

    for nxt, cost in reversed_graph[cur]:
        if dp[nxt] != total + cost:
            continue
        if find_way(nxt, total + cost):
            result.append(cur)
            return True

    return False


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _start = 0
    _end = 1
    _space = " "
    N = int(input())
    M = int(input())
    graph = [list() for _ in range(N + 1)]
    reversed_graph = [list() for _ in range(N + 1)]
    dp = [-1 for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    result = deque()

    for _ in range(M):
        start, end, cost = map(int, input().split())
        if start == _end:
            graph[_start].append((end, cost))
            reversed_graph[end].append((_start, cost))
        else:
            graph[start].append((end, cost))
            reversed_graph[end].append((start, cost))

    dfs(_start)
    find_way(_end, 0)

    result.appendleft(_end)

    print(dp[_start])
    print(_space.join(map(str, result)))
