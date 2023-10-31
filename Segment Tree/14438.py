# https://www.acmicpc.net/problem/14438
from math import ceil
from math import log


def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]

    mid = (start + end) >> 1
    left_node = init(node * 2, start, mid)
    right_node = init(node * 2 + 1, mid + 1, end)
    tree[node] = min(left_node, right_node)

    return tree[node]


def update(node, start, end, index, value):
    if not (start <= index <= end):
        return tree[node]

    if start == end:
        tree[node] = value
        return tree[node]

    mid = (start + end) >> 1
    left_node = update(node * 2, start, mid, index, value)
    right_node = update(node * 2 + 1, mid + 1, end, index, value)
    tree[node] = min(left_node, right_node)

    return tree[node]


def read(node, start, end, left, right):
    if left > end or right < start:
        return _inf
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) >> 1
    left_node = read(node * 2, start, mid, left, right)
    right_node = read(node * 2 + 1, mid + 1, end, left, right)

    return min(left_node, right_node)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _update = 1
    _inf = float('inf')
    _new_line = "\n"
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    M = int(input())
    height = ceil(log(N, 2)) + 1
    size = 2 ** height
    tree = [0 for _ in range(size)]
    result = list()

    init(1, 1, N)

    for _ in range(M):
        commands = list(map(int, input().split()))
        command = commands[0]

        if command == _update:
            index, value = commands[1:]
            update(1, 1, N, index, value)
        else:
            left, right = commands[1:]
            value = read(1, 1, N, left, right)
            result.append(value)

    print(_new_line.join(map(str, result)))
