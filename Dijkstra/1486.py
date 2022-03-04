from sys import stdin
from queue import PriorityQueue


def char_to_num(char):
    if 65 <= ord(char) < 91:
        return ord(char) - 65
    elif 97 <= ord(char) < 123:
        return ord(char) - 71


def dijkstra(direction):
    pq = PriorityQueue()
    # dist, (x, y)
    pq.put((0, (0, 0)))

    dist = [[inf for _ in range(M)] for _ in range(N)]
    dist[0][0] = 0

    while not pq.empty():
        cur_dist, cur_node = pq.get()
        cur_x, cur_y = cur_node

        for x_diff, y_diff in zip(dx, dy):
            next_x = cur_x + x_diff
            next_y = cur_y + y_diff

            if not (0 <= next_x < M and 0 <= next_y < N):
                continue

            height_diff = (grid[next_y][next_x] - grid[cur_y][cur_x]) * direction

            if 0 <= height_diff <= T and dist[next_y][next_x] > cur_dist + 1:
                dist[next_y][next_x] = cur_dist + 1
                pq.put((dist[next_y][next_x], (next_x, next_y)))
            elif -T <= height_diff < 0 and dist[next_y][next_x] > cur_dist + height_diff ** 2:
                dist[next_y][next_x] = cur_dist + height_diff ** 2
                pq.put((dist[next_y][next_x], (next_x, next_y)))

    return dist


def find_max_height(front_dist, back_dist):
    max_height = 0

    for row in range(N):
        for col in range(M):
            if front_dist[row][col] + back_dist[row][col] > D:
                continue
            if max_height < grid[row][col]:
                max_height = grid[row][col]

    return max_height


if __name__ == '__main__':
    input = stdin.readline
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    front = 1
    back = -1
    inf = float('inf')
    N, M, T, D = map(int, input().split())
    grid = [list(map(char_to_num, input().rstrip())) for _ in range(N)]

    front_dist = dijkstra(front)
    back_dist = dijkstra(back)
    max_height = find_max_height(front_dist, back_dist)

    print(max_height)
