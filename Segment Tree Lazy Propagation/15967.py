# https://www.acmicpc.net/problem/15967
from math import ceil
from math import log


def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]

    mid = (start + end) >> 1
    left_node = init(node * 2, start, mid)
    right_node = init(node * 2 + 1, mid + 1, end)
    tree[node] = left_node + right_node

    return tree[node]


def propagate(node, start, end):
    if lazy[node] == 0:
        return

    tree[node] += lazy[node] * (end - start + 1)
    if start != end:
        lazy[node * 2] += lazy[node]
        lazy[node * 2 + 1] += lazy[node]

    lazy[node] = 0


def range_update(node, start, end, left, right, value):
    propagate(node, start, end)
    if left > end or right < start:
        return tree[node]
    if left <= start and end <= right:
        tree[node] += value * (end - start + 1)

        if start == end:
            return tree[node]

        lazy[node * 2] += value
        lazy[node * 2 + 1] += value
        return tree[node]

    mid = (start + end) >> 1
    left_node = range_update(node * 2, start, mid, left, right, value)
    right_node = range_update(node * 2 + 1, mid + 1, end, left, right, value)
    tree[node] = left_node + right_node

    return tree[node]


def read(node, start, end, left, right):
    propagate(node, start, end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) >> 1
    left_node = read(node * 2, start, mid, left, right)
    right_node = read(node * 2 + 1, mid + 1, end, left, right)

    return left_node + right_node


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _read = 1
    _new_line = "\n"
    N, Q1, Q2 = map(int, input().split())
    Q = Q1 + Q2
    nums = [0] + list(map(int, input().split()))
    height = ceil(log(N, 2)) + 1
    size = 2 ** height
    tree = [0 for _ in range(size)]
    lazy = [0 for _ in range(size)]
    result = list()

    init(1, 1, N)

    for _ in range(Q):
        commands = list(map(int, input().split()))
        command = commands[0]

        if command == _read:
            left, right = commands[1:]
            value = read(1, 1, N, left, right)
            result.append(value)
        else:
            left, right, value = commands[1:]
            range_update(1, 1, N, left, right, value)

    print(_new_line.join(map(str, result)))
