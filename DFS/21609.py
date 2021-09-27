# https://www.acmicpc.net/problem/21609


def is_in_bound(x, y):
    return 0 <= x < N and 0 <= y < N


def find_block_groups(x, y, color, size, rainbow_count):
    if not is_in_bound(x, y):
        return size, rainbow_count
    if visited[y][x][color]:
        return size, rainbow_count
    if grid[y][x] == black or grid[y][x] == empty:
        return size, rainbow_count
    if grid[y][x] != color and grid[y][x] != rainbow:
        return size, rainbow_count

    visited[y][x][color] = True

    for diff_x, diff_y in zip(dx, dy):
        next_x = x + diff_x
        next_y = y + diff_y
        size, rainbow_count = find_block_groups(next_x, next_y, color, size, rainbow_count)

    return size + 1, rainbow_count + 1 if grid[y][x] == rainbow else rainbow_count


def delete_block_group(x, y, color, new_grid):
    if not is_in_bound(x, y):
        return size
    if not visited[y][x][color]:
        return
    visited[y][x][color] = False

    new_grid[y][x] = empty

    for diff_x, diff_y in zip(dx, dy):
        next_x = x + diff_x
        next_y = y + diff_y
        delete_block_group(next_x, next_y, color, new_grid)

    return new_grid


def do_gravity():
    for row in range(N - 2, -1, -1):
        for col in range(N):
            down(col, row)


def down(col, row):
    if grid[row][col] == black:
        return

    diff = 1

    while is_in_bound(col, row + diff) and grid[row + diff][col] == empty:
        grid[row + diff][col] = grid[row + diff - 1][col]
        grid[row + diff - 1][col] = empty
        diff += 1


def rotate():
    new_grid = [row[:] for row in grid]

    for row in range(N):
        for col in range(N):
            new_grid[N - col - 1][row] = grid[row][col]

    return new_grid


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (0, -1, 0, 1)
    dy = (1, 0, -1, 0)
    minimum_size = 2
    empty = -2
    black = -1
    rainbow = 0
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    score = 0

    while True:
        visited = [[[False for _ in range(M + 1)] for _ in range(N)] for _ in range(N)]
        block_groups = list()

        for row in range(N):
            for col in range(N):
                for color in range(1, M + 1):
                    if grid[row][col] == empty or grid[row][col] == rainbow or grid[row][col] == black:
                        continue
                    if visited[row][col][color]:
                        continue
                    size, rainbow_count = find_block_groups(col, row, color, 0, 0)
                    if size < minimum_size:
                        continue
                    block_groups.append((size, rainbow_count, row, col, color))

        if not block_groups:
            break

        block_groups.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))

        size, rainbow_count, start_row, start_col, color = block_groups[0]

        score += size ** 2

        new_grid = [row[:] for row in grid]

        grid = delete_block_group(start_col, start_row, color, new_grid)

        do_gravity()

        grid = rotate()

        do_gravity()

    print(score)

