# https://www.acmicpc.net/problem/24481
import sys
sys.setrecursionlimit(999999999)


def dfs(cur):
    for nxt in graph[cur]:
        if visited[nxt] != _not_visited:
            continue
        visited[nxt] = visited[cur] + 1
        dfs(nxt)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _not_visited = -1
    _new_line = '\n'
    N, M, R = map(int, input().split())
    graph = [list() for _ in range(N)]
    visited = [_not_visited for _ in range(N)]
    visited[R - 1] = 0

    for _ in range(M):
        start, end = map(lambda x: int(x) - 1, input().split())
        graph[start].append(end)
        graph[end].append(start)

    graph = list(map(sorted, graph))
    dfs(R - 1)
    print(_new_line.join(map(str, visited)))
