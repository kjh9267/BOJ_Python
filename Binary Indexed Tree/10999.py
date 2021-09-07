# https://www.acmicpc.net/problem/10999
from collections import deque


def do_update(index, a_diff, b_diff):
    while index <= N:
        a_tree[index] += a_diff
        b_tree[index] += b_diff
        index += (index & -index)


def do_range_update(left, right, diff):
    do_update(left, diff, -diff * (left - 1))
    do_update(right + 1, -diff, diff * right)


def get_sum(index):
    a_value = 0
    b_value = 0
    end_index = index

    while index > 0:
        a_value += a_tree[index]
        b_value += b_tree[index]
        index -= (index & -index)

    return a_value * end_index + b_value


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    update = 1
    sum = 2
    new_line = '\n'
    N, M, K = map(int, input().split())
    data = [0] + [int(input()) for _ in range(N)]
    a_tree = [0 for _ in range(N + 1)]
    b_tree = [0 for _ in range(N + 1)]
    result = deque()

    for index in range(1, N + 1):
        num = data[index]
        do_range_update(index, index, num)

    for _ in range(M + K):
        inputs = list(map(int, input().split()))
        command = inputs[0]
        left = inputs[1]
        right = inputs[2]

        if command == update:
            diff = inputs[3]
            do_range_update(left, right, diff)
        else:
            value = get_sum(right) - get_sum(left - 1)
            result.append(value)

    print(new_line.join(map(str, result)))