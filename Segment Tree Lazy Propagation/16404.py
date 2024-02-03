# https://www.acmicpc.net/problem/16404
from math import ceil
from math import log
import sys
sys.setrecursionlimit(999999999)


def dfs(cur):
    global index
    index += 1
    indices[cur] = index
    left = index
    right = index

    for nxt in tree[cur]:
        right = max(right, dfs(nxt))

    ranges[cur] = [left, right]

    return index


def range_update(node, start, end, left, right, value):
    propagate(node, start, end)

    if left > end or right < start:
        return segment_tree[node]

    if left <= start and end <= right:
        segment_tree[node] += (end - start + 1) * value

        if start == end:
            return segment_tree[node]

        lazy[node * 2] += value
        lazy[node * 2 + 1] += value

        return segment_tree[node]

    mid = (start + end) >> 1
    left_node = range_update(node * 2, start, mid, left, right, value)
    right_node = range_update(node * 2 + 1, mid + 1, end, left, right, value)
    segment_tree[node] = left_node + right_node

    return segment_tree[node]


def propagate(node, start, end):
    if lazy[node] == 0:
        return

    segment_tree[node] += (end - start + 1) * lazy[node]

    if start != end:
        lazy[node * 2] += lazy[node]
        lazy[node * 2 + 1] += lazy[node]

    lazy[node] = 0


def read(node, start, end, left, right):
    propagate(node, start, end)

    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return segment_tree[node]

    mid = (start + end) >> 1
    left_node = read(node * 2, start, mid, left, right)
    right_node = read(node * 2 + 1, mid + 1, end, left, right)

    return left_node + right_node


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _update = 1
    _new_line = "\n"
    N, M = map(int, input().split())
    tree = [list() for _ in range(N + 1)]
    data = list(map(int, input().split()))
    height = ceil(log(N, 2)) + 1
    size = 2 ** height
    segment_tree = [0 for _ in range(size)]
    lazy = [0 for _ in range(size)]
    index = 0
    indices = [0 for _ in range(N + 1)]
    ranges = [[0, 0] for _ in range(N + 1)]
    result = list()

    for node, parent in enumerate(data[1:]):
        node += 2
        tree[parent].append(node)

    dfs(1)

    for _ in range(M):
        commands = list(map(int, input().split()))
        command = commands[0]

        if command == _update:
            node, value = commands[1:]
            left, right = ranges[node]
            range_update(1, 1, N, left, right, value)
        else:
            node = commands[1]
            node = indices[node]
            value = read(1, 1, N, node, node)
            result.append(value)

    print(_new_line.join(map(str, result)))
