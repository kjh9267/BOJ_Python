# https://www.acmicpc.net/problem/3187
import sys
sys.setrecursionlimit(999999999)


def dfs(x, y, animals):
    if x < 0 or x == C or y < 0 or y == R:
        return
    if visited[y][x]:
        return
    if grid[y][x] == _wall:
        return

    visited[y][x] = True

    if grid[y][x] == _wolf:
        animals[0] += 1
    elif grid[y][x] == _sheep:
        animals[1] += 1

    for diff_x, diff_y in zip(dx, dy):
        next_x = x + diff_x
        next_y = y + diff_y
        dfs(next_x, next_y, animals)


def count_animals():
    sheep_count = 0
    wolf_count = 0

    for row in range(R):
        for col in range(C):
            if grid[row][col] == _sheep:
                sheep_count += 1
            elif grid[row][col] == _wolf:
                wolf_count += 1

    return wolf_count, sheep_count


def count_all_animals(total_animals):
    for row in range(R):
        for col in range(C):
            if visited[row][col]:
                continue
            # wolf, sheep
            animals = [0, 0]
            dfs(col, row, animals)
            wolf_count = animals[0]
            sheep_count = animals[1]

            if wolf_count < sheep_count:
                total_animals[0] -= wolf_count
            else:
                total_animals[1] -= sheep_count

    return total_animals


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    _sheep = 'k'
    _wolf = 'v'
    _wall = '#'
    R, C = map(int, input().split())
    grid = [input().rstrip() for _ in range(R)]
    visited = [[False for _ in range(C)] for _ in range(R)]
    total_wolf_count, total_sheep_count = count_animals()
    total_animals = count_all_animals([total_wolf_count, total_sheep_count])

    print(total_animals[1], total_animals[0])