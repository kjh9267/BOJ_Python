# https://www.acmicpc.net/problem/14226
from collections import deque


def bfs():
    # num, copy_count
    queue = deque()
    queue.append((1, 0))

    visited = [[False for _ in range(limit + 1)] for _ in range(limit + 1)]
    count = -1

    while queue:
        size = len(queue)
        count += 1

        for _ in range(size):
            cur_count, copy_count = queue.popleft()

            if cur_count == S:
                return count

            if not visited[cur_count - 1][copy_count] and cur_count > 1:
                visited[cur_count - 1][copy_count] = True
                queue.append((cur_count - 1, copy_count))

            if not visited[cur_count][cur_count] and cur_count <= limit:
                visited[cur_count][cur_count] = True
                queue.append((cur_count, cur_count))

            if (cur_count + copy_count) <= limit and copy_count <= limit and not visited[cur_count + copy_count][copy_count]:
                visited[cur_count + copy_count][copy_count] = True
                queue.append((cur_count + copy_count, copy_count))


if __name__ == '__main__':
    limit = 2_000
    input = __import__('sys').stdin.readline
    S = int(input())
    print(bfs())