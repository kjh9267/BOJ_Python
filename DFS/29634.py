# https://www.acmicpc.net/problem/29634


def dfs(x, y, size, visited):
    if not (0 <= x < M and 0 <= y < N):
        return
    if visited[y][x]:
        return
    if grid[y][x] == _wall:
        return
    visited[y][x] = True
    size[0] += 1

    for diff_x, diff_y in zip(dx, dy):
        next_x = x + diff_x
        next_y = y + diff_y
        dfs(next_x, next_y, size, visited)


def dfs_all():
    visited = [[False for _ in range(M)] for _ in range(N)]
    max_size = 0

    for row in range(N):
        for col in range(M):
            if visited[row][col]:
                continue
            size = [0]
            dfs(col, row, size, visited)
            max_size = max(max_size, size[0])

    return -1 if max_size == 0 else max_size


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _wall = '*'
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    N, M = map(int, input().split())
    grid = [input().rstrip() for _ in range(N)]

    result = dfs_all()
    print(result)
