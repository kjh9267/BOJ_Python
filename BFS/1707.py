# https://www.acmicpc.net/problem/1707
import sys
from collections import deque

sys.setrecursionlimit(999999999)


def bfs(start, visited):
    queue = deque()
    queue.append(start)

    visited[start] = 1

    while queue:
        cur = queue.popleft()

        for nxt in graph[cur]:
            if visited[nxt] != _not_visited:
                if visited[nxt] == visited[cur]:
                    return True
                continue
            visited[nxt] = -visited[cur]
            queue.append(nxt)

    return False


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _yes = 'YES'
    _no = 'NO'
    _new_line = '\n'
    _not_visited = 0
    result = list()
    K = int(input())

    for _ in range(K):
        V, E = map(int, input().split())
        graph = [list() for _ in range(V + 1)]
        visited = [_not_visited for _ in range(V + 1)]

        for _ in range(E):
            start, end = map(int, input().split())
            graph[start].append(end)
            graph[end].append(start)

        impossible = False
        for start in range(1, V + 1):
            if visited[start] != _not_visited:
                continue
            impossible |= bfs(start, visited)

        if impossible:
            result.append(_no)
        else:
            result.append(_yes)

    print(_new_line.join(result))