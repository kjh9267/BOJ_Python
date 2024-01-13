# https://www.acmicpc.net/problem/13309
from math import ceil
from math import log
import sys
sys.setrecursionlimit(999999999)


def dfs(cur):
    for nxt in tree[cur]:
        tree_sizes[cur] += dfs(nxt)

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
    next_index = index + 1
    parents[next_index] = indices[cur]
    decompose(heavy, depth + 1)

    for nxt in tree[cur]:
        if nxt != heavy:
            next_index = index + 1
            parents[next_index] = indices[cur]
            group += 1
            decompose(nxt, depth + 1)


def is_connected_pair(x, y):
    not_connected = False

    while groups[x] != groups[y]:
        x_head = heads[groups[x]]
        y_head = heads[groups[y]]
        if depths[x_head] < depths[y_head]:
            x, y = y, x

        head = heads[groups[x]]
        not_connected |= is_connected(1, 1, N, head, x)

        x = parents[head]

    if x == y:
        return not_connected

    if depths[x] < depths[y]:
        x, y = y, x

    not_connected |= is_connected(1, 1, N, y + 1, x)

    return not_connected


def update(node, start, end, index):
    if not (start <= index <= end):
        return False

    if start == end:
        segment_tree[node] = True
        return True

    mid = (start + end) >> 1
    left_node = update(node * 2, start, mid, index)
    right_node = update(node * 2 + 1, mid + 1, end, index)
    segment_tree[node] |= left_node or right_node

    return segment_tree[node]


def is_connected(node, start, end, left, right):
    if left > end or right < start:
        return False
    if left <= start and end <= right:
        return segment_tree[node]

    mid = (start + end) >> 1
    left_node = is_connected(node * 2, start, mid, left, right)
    right_node = is_connected(node * 2 + 1, mid + 1, end, left, right)

    return left_node or right_node


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _read = 0
    _new_line = "\n"
    _yes = 'YES'
    _no = 'NO'
    N, Q = map(int, input().split())
    tree = [list() for _ in range(N + 1)]

    for child in range(2, N + 1):
        parent = int(input())
        tree[parent].append(child)

    tree_sizes = [1 for _ in range(N + 1)]
    dfs(1)

    group = 1
    index = 0
    groups = [0 for _ in range(N + 1)]
    parents = [0 for _ in range(N + 1)]
    depths = [0 for _ in range(N + 1)]
    heads = [0 for _ in range(N + 1)]
    indices = [0 for _ in range(N + 1)]
    decompose(1, 0)

    height = ceil(log(N, 2)) + 1
    size = 2 ** height
    segment_tree = [False for _ in range(size)]

    result = list()

    for _ in range(Q):
        commands = list(map(int, input().split()))
        left, right, command = commands

        if command == _read:
            not_connected = is_connected_pair(indices[left], indices[right])

            if not_connected:
                result.append(_no)
            else:
                result.append(_yes)
        else:
            not_connected = is_connected_pair(indices[left], indices[right])

            if not_connected:
                result.append(_no)
                update(1, 1, N, indices[right])
            else:
                result.append(_yes)
                update(1, 1, N, indices[left])

    print(_new_line.join(map(str, result)))
