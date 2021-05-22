# https://www.acmicpc.net/problem/1865


def bellman_ford(start):
    dist = [inf for _ in range(N)]
    dist[start] = 0

    for count in range(N):
        for cur in range(N):
            for nxt, cost in graph[cur]:
                if dist[nxt] < dist[cur] + cost:
                    continue
                dist[nxt] = dist[cur] + cost

    for cur in range(N):
        for nxt, cost in graph[cur]:
            if dist[nxt] > dist[cur] + cost:
                return True

    return False


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    inf = 100_000_001
    TC = int(input())

    for _ in range(TC):
        N, M, W = map(int, input().split())
        graph = [list() for _ in range(N)]

        for _ in range(M):
            S, E, T = map(int, input().split())
            graph[S - 1].append((E - 1, T))
            graph[E - 1].append((S - 1, T))

        for _ in range(W):
            S, E, T = map(int, input().split())
            graph[S - 1].append((E - 1, -T))

        if bellman_ford(0):
            print('YES')
        else:
            print('NO')