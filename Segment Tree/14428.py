# https://www.acmicpc.net/problem/14428
from math import log


def init(node, start, end):
    if start == end:
        tree[node][0] = nums[start]
        tree[node][1] = start
        return tree[node]

    mid = (start + end) >> 1
    left_node = init(node * 2, start, mid)
    right_node = init(node * 2 + 1, mid + 1, end)
    tree[node] = compare(left_node, right_node)
    return tree[node]


def compare(x, y):
    if x[0] == y[0]:
        if x[1] < y[1]:
            return x
        return y
    if x[0] < y[0]:
        return x
    return y


def update(node, start, end, index, value):
    if not (start <= index <= end):
        return tree[node]

    if index == tree[node][1]:
        tree[node][0] = value
        tree[node][1] = index

    if start == end:
        return tree[node]

    mid = (start + end) >> 1
    left_node = update(node * 2, start, mid, index, value)
    right_node = update(node * 2 + 1, mid + 1, end, index, value)
    tree[node] = compare(left_node, right_node)

    return tree[node]


def find_minimum_value(node, start, end, left, right):
    if left > end or right < start:
        return _inf_pair
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) >> 1
    left_node = find_minimum_value(node * 2, start, mid, left, right)
    right_node = find_minimum_value(node * 2 + 1, mid + 1, end, left, right)

    return compare(left_node, right_node)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _update = 1
    _new_line = '\n'
    _inf = float('inf')
    _inf_pair = (_inf, _inf)
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    height = int(log(N, 2)) + 1
    size = 2 ** (height + 1)
    # value, index
    tree = [[0, 0] for _ in range(size)]
    M = int(input())
    result = list()
    init(1, 1, N)

    for _ in range(M):
        command, x, y = map(int, input().split())

        if command == _update:
            update(1, 1, N, x, y)
        else:
            minimum_value = find_minimum_value(1, 1, N, x, y)
            result.append(minimum_value)

    print(_new_line.join(map(lambda x: str(x[1]), result)))