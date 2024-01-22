# https://www.acmicpc.net/problem/13038
from math import ceil
from math import log
import sys
sys.setrecursionlimit(999999999)


def dfs(cur, prev):
    for nxt in tree[cur]:
        if prev != nxt:
            tree_sizes[cur] += dfs(nxt, cur)

    return tree_sizes[cur]


def decompose(cur, depth):
    global index
    global group

    index += 1
    indices[cur] = index
    depths[index] = depth
    groups[index] = group

    if heads[group] == 0:
        heads[group] = index

    if not tree[cur]:
        return

    heavy = sorted(tree[cur], key=lambda x: -tree_sizes[x])[0]

    parents[index + 1] = indices[cur]
    decompose(heavy, depth + 1)

    for nxt in tree[cur]:
        if nxt == heavy:
            continue
        parents[index + 1] = indices[cur]
        group += 1
        decompose(nxt, depth + 1)


def compute_dist(x, y):
    node_counts = 0

    while groups[x] != groups[y]:
        x_head = heads[groups[x]]
        y_head = heads[groups[y]]
        if depths[x_head] < depths[y_head]:
            x, y = y, x

        head = heads[groups[x]]

        node_counts += read(1, 1, N, head, x)

        x = parents[head]

    if x == y:
        return node_counts

    if depths[x] < depths[y]:
        x, y = y, x

    node_counts += read(1, 1, N, y + 1, x)

    return node_counts


def init_segment_tree(node, start, end):
    if start == end:
        segment_tree[node] = 1
        return segment_tree[node]

    mid = (start + end) >> 1
    left_node = init_segment_tree(node * 2, start, mid)
    right_node = init_segment_tree(node * 2 + 1, mid + 1, end)
    segment_tree[node] = left_node + right_node

    return segment_tree[node]


def update(node, start, end, index):
    if not (start <= index <= end):
        return segment_tree[node]

    if start == end:
        segment_tree[node] = 0
        return 0

    mid = (start + end) >> 1
    left_node = update(node * 2, start, mid, index)
    right_node = update(node * 2 + 1, mid + 1, end, index)
    segment_tree[node] = left_node + right_node

    return segment_tree[node]


def read(node, start, end, left, right):
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
    _read = 1
    _new_line = "\n"
    N = int(input())
    parents = list(map(int, input().split()))
    Q = int(input())
    tree = [list() for _ in range(N + 1)]

    for child, parent in enumerate(parents):
        child += 2
        tree[parent].append(child)

    tree_sizes = [1 for _ in range(N + 1)]
    group = 0
    index = 0
    groups = [0 for _ in range(N + 1)]
    parents = [0 for _ in range(N + 1)]
    depths = [0 for _ in range(N + 1)]
    heads = [0 for _ in range(N + 1)]
    indices = [0 for _ in range(N + 1)]

    dfs(1, 0)
    decompose(1, 0)

    height = ceil(log(N, 2)) + 1
    size = 2 ** height
    segment_tree = [0 for _ in range(size)]
    init_segment_tree(1, 1, N)

    result = list()

    for _ in range(Q):
        commands = list(map(int, input().split()))
        command = commands[0]

        if command == _read:
            start, end = commands[1:]
            value = compute_dist(indices[start], indices[end])
            result.append(value)
        else:
            index = commands[1]
            update(1, 1, N, indices[index])

    print(_new_line.join(map(str, result)))
