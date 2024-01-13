# https://www.acmicpc.net/problem/13510
import sys
from math import ceil
from math import log
sys.setrecursionlimit(999999999)


def dfs(cur):
    if visited[cur]:
        return 0

    visited[cur] = True

    for _, nxt, _ in tree[cur]:
        tree_sizes[cur] += dfs(nxt)

    return tree_sizes[cur]


def decompose(cur, prev, depth, index, group):
    index[0] += 1
    indices[cur] = index[0]

    depths[index[0]] = depth
    groups[index[0]] = group[0]

    if heads[group[0]] == 0:
        heads[group[0]] = index[0]

    tree[cur].sort(key=lambda x: -tree_sizes[x[1]])
    link, heavy, cost = tree[cur][0]

    if heavy == prev:
        if len(tree[cur]) == 1:
            return
        link, heavy, cost = tree[cur][1]

    if not visited[heavy]:
        visited[heavy] = True

        next_index = index[0] + 1
        parents[next_index] = indices[cur]
        child_nodes[link] = next_index
        costs[next_index] = cost
        decompose(heavy, cur, depth + 1, index, group)

    for link, nxt, cost in tree[cur]:
        if nxt == heavy:
            continue
        if visited[nxt]:
            continue
        visited[nxt] = True

        group[0] += 1
        next_index = index[0] + 1
        parents[next_index] = indices[cur]
        child_nodes[link] = next_index
        costs[next_index] = cost
        decompose(nxt, cur, depth + 1, index, group)


def init_segment_tree(node, start, end):
    if start == end:
        segment_tree[node] = costs[start]
        return segment_tree[node]

    mid = (start + end) >> 1
    left_node = init_segment_tree(node * 2, start, mid)
    right_node = init_segment_tree(node * 2 + 1, mid + 1, end)

    segment_tree[node] = max(left_node, right_node)
    return segment_tree[node]


def update(node, index, start, end, value):
    if not (start <= index <= end):
        return segment_tree[node]
    if start == end:
        segment_tree[node] = value
        return segment_tree[node]

    mid = (start + end) >> 1
    left_node = update(node * 2, index, start, mid, value)
    right_node = update(node * 2 + 1, index, mid + 1, end, value)

    segment_tree[node] = max(left_node, right_node)
    return segment_tree[node]


def find_maximum_value(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return segment_tree[node]

    mid = (start + end) >> 1
    left_node = find_maximum_value(node * 2, start, mid, left, right)
    right_node = find_maximum_value(node * 2 + 1, mid + 1, end, left, right)

    return max(left_node, right_node)


def find_maximum_value_of_path(x, y):
    if x == y:
        return 0

    maximum_value = 0
    while groups[x] != groups[y]:
        x_head = heads[groups[x]]
        y_head = heads[groups[y]]

        if depths[x_head] < depths[y_head]:
            x, y = y, x

        head = heads[groups[x]]

        value = find_maximum_value(1, 1, N, head, x)
        maximum_value = max(maximum_value, value)
        x = parents[head]

    if x == y:
        return maximum_value

    if depths[x] < depths[y]:
        x, y = y, x

    value = find_maximum_value(1, 1, N, y + 1, x)
    maximum_value = max(maximum_value, value)

    return maximum_value


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _update = 1
    _new_line = "\n"
    N = int(input())
    tree = [list() for _ in range(N + 1)]

    for link in range(1, N):
        start, end, cost = map(int, input().split())
        tree[start].append((link, end, cost))
        tree[end].append((link, start, cost))

    visited = [False for _ in range(N + 1)]
    tree_sizes = [1 for _ in range(N + 1)]
    dfs(1)

    visited = [False for _ in range(N + 1)]
    index = [0]
    indices = [0 for _ in range(N + 1)]
    depths = [0 for _ in range(N + 1)]
    group = [1]
    groups = [0 for _ in range(N + 1)]
    heads = [0 for _ in range(N + 1)]
    parents = [0 for _ in range(N + 1)]
    child_nodes = [0 for _ in range(N + 1)]
    costs = [0 for _ in range(N + 1)]

    visited[1] = True
    decompose(1, 0, 1, index, group)

    height = ceil(log(N, 2)) + 1
    size = 2 ** height
    segment_tree = [0 for _ in range(size)]

    init_segment_tree(1, 1, N)

    M = int(input())
    result = list()

    for _ in range(M):
        commands = list(map(int, input().split()))
        command = commands[0]

        if command == _update:
            index, cost = commands[1:]
            update(1, child_nodes[index], 1, N, cost)
        else:
            x, y = commands[1:]
            maximum_value_of_path = find_maximum_value_of_path(indices[x], indices[y])
            result.append(maximum_value_of_path)

    print(_new_line.join(map(str, result)))
