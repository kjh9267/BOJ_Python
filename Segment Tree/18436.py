# https://www.acmicpc.net/problem/18436
from math import log
from math import ceil


def init(node, start, end, tree, mod):
    if start == end:
        tree[node] = 1 if nums[start] % 2 == mod else 0

        return tree[node]

    mid = (start + end) >> 1
    left_node = init(node * 2, start, mid, tree, mod)
    right_node = init(node * 2 + 1, mid + 1, end, tree, mod)
    tree[node] = left_node + right_node

    return tree[node]


def update(node, start, end, tree, index, value, mod):
    if not (start <= index <= end):
        return tree[node]

    if start == end:
        tree[node] = 1 if value % 2 == mod else 0
        return tree[node]

    mid = (start + end) >> 1
    left_node = update(node * 2, start, mid, tree, index, value, mod)
    right_node = update(node * 2 + 1, mid + 1, end, tree, index, value, mod)
    tree[node] = left_node + right_node

    return tree[node]


def read(node, start, end, left, right, tree):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) >> 1
    left_node = read(node * 2, start, mid, left, right, tree)
    right_node = read(node * 2 + 1, mid + 1, end, left, right, tree)

    return left_node + right_node


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _update = 1
    _read_even = 2
    _new_line = "\n"
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    M = int(input())
    height = ceil(log(N, 2)) + 1
    size = 2 ** height
    odd_tree = [0 for _ in range(size)]
    even_tree = [0 for _ in range(size)]
    result = list()

    init(1, 1, N, odd_tree, 1)
    init(1, 1, N, even_tree, 0)

    for _ in range(M):
        commands = list(map(int, input().split()))
        command = commands[0]

        if command == _update:
            index, value = commands[1:]
            update(1, 1, N, odd_tree, index, value, 1)
            update(1, 1, N, even_tree, index, value, 0)
        elif command == _read_even:
            left, right = commands[1:]
            value = read(1, 1, N, left, right, even_tree)
            result.append(value)
        else:
            left, right = commands[1:]
            value = read(1, 1, N, left, right, odd_tree)
            result.append(value)

    print(_new_line.join(map(str, result)))
