# https://www.acmicpc.net/problem/2042
from collections import deque


def do_update(index, diff):
    while index < N + 1:
        tree[index] += diff
        index += (index & -index)


def get_sum(index):
    value = 0

    while index > 0:
        value += tree[index]
        index -= (index & -index)

    return value


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    update = 1
    sum = 2
    new_line = '\n'
    N, M, K = map(int, input().split())
    data = [0] + [int(input()) for _ in range(N)]
    tree = [0 for _ in range(N + 1)]
    result = deque()

    for index in range(1, N + 1):
        do_update(index, data[index])

    for _ in range(M + K):
        a, b, c = map(int, input().split())

        if a == update:
            diff = c - data[b]
            data[b] = c
            do_update(b, diff)
        else:
            value = get_sum(c) - get_sum(b - 1)
            result.append(value)

    print(new_line.join(map(str, result)))