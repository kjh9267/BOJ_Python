# https://www.acmicpc.net/problem/5568


def dfs(depth, cards, result):
    if depth == K:
        num = ''.join(cards)
        if num in visited_num:
            return
        visited_num.add(num)
        result[0] += 1
        return

    for nxt in range(N):
        if visited[nxt]:
            continue
        visited[nxt] = True
        dfs(depth + 1, cards + [data[nxt]], result)
        visited[nxt] = False


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    K = int(input())
    data = [input().rstrip() for _ in range(N)]
    visited = [False for _ in range(N)]
    visited_num = set()
    result = [0]

    dfs(0, list(), result)
    print(result[0])