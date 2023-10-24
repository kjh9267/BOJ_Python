# https://www.acmicpc.net/problem/16978
from math import log
from math import ceil


def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]

    mid = (start + end) >> 1
    left_node = init(node * 2, start, mid)
    right_node = init(node * 2 + 1, mid + 1, end)
    tree[node] = left_node + right_node

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
    tree[node] = left_node + right_node

    return tree[node]


def compute_sum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) >> 1
    left_node = compute_sum(node * 2, start, mid, left, right)
    right_node = compute_sum(node * 2 + 1, mid + 1, end, left, right)

    return left_node + right_node


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _update = 1
    _new_line = '\n'
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    M = int(input())
    read_queries = list()
    update_queries = list()
    height = ceil(log(N, 2)) + 1
    size = 2 ** height
    tree = [0 for _ in range(size)]

    init(1, 1, N)

    read_query_size = 0
    for _ in range(M):
        commands = list(map(int, input().split()))
        command = commands[0]

        if command == _update:
            index, value = commands[1:]
            update_queries.append((index, value))
        else:
            k, left, right = commands[1:]
            read_queries.append((k, read_query_size, left, right))
            read_query_size += 1

    read_queries.sort(key=lambda x: x[0])
    result = [0 for _ in range(read_query_size)]
    update_query_index = 0

    for k, read_query_index, left, right in read_queries:
        while update_query_index < k:
            index, value = update_queries[update_query_index]
            update(1, 1, N, index, value)
            update_query_index += 1

        value = compute_sum(1, 1, N, left, right)
        result[read_query_index] = value

    print(_new_line.join(map(str, result)))
