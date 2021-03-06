#  https://www.acmicpc.net/problem/9576


def dfs(cur):
    if visit[cur]:
        return False
    visit[cur] = True
    a = graph[cur][0]
    b = graph[cur][1]
    for nxt in range(a,b):
        if B[nxt] is -1 or dfs(B[nxt]):
            A[cur] = nxt
            B[nxt] = cur
            return True
    return False


if __name__ == '__main__':
    input = __import__('sys').stdin.readline

    T = int(input())

    for _ in range(T):
        N, M = map(int,input().split())
        A = [-1 for _ in range(M)]
        B = [-1 for _ in range(N)]
        graph = [[] for _ in range(M)]
        res = 0

        for index in range(M):
            a, b = map(int,input().split())
            graph[index].extend([a-1,b])

        for index in range(M):
            if A[index] is -1:
                visit = [False for _ in range(M)]
                if dfs(index):
                    res += 1

        print(res)