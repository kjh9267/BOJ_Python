# https://www.acmicpc.net/problem/2207
import sys
sys.setrecursionlimit(999999999)


def dfs_all():
    visited = [0 for _ in range(M * 2 + 1)]
    finished = [False for _ in range(M * 2 + 1)]
    stack = list()
    sccs = list()

    for node in range(1, M * 2 + 1):
        if visited[node] == 0:
            dfs(node, visited, finished, stack, sccs)

    if is_possible(sccs):
        return True

    return False


def is_possible(sccs):
    for scc in sccs:
        for node in scc:
            if node + M in scc or node - M in scc:
                return False

    return True


def dfs(cur, visited, finished, stack, sccs):
    global count
    count += 1
    visited[cur] = count
    parent = visited[cur]
    stack.append(cur)

    for nxt in graph[cur]:
        if visited[nxt] == 0:
            parent = min(parent, dfs(nxt, visited, finished, stack, sccs))
        elif not finished[nxt]:
            parent = min(parent, visited[nxt])

    if parent == visited[cur]:
        extract_scc(cur, stack, finished, sccs)

    return parent


def change_node(x):
    if x > 0:
        return x
    return M - x


def inverse(x):
    if x > M:
        return x - M
    return x + M


def extract_scc(cur, stack, finished, sccs):
    scc = set()

    while stack:
        value = stack.pop()
        finished[value] = True
        scc.add(value)

        if value == cur:
            break

    sccs.append(scc)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _yes = '^_^'
    _no = 'OTL'
    _new_line = "\n"

    N, M = map(int, input().split())
    graph = [list() for _ in range(2 * M + 1)]
    count = 0

    for index in range(N):
        x, y = map(lambda x: change_node(int(x)), input().split())
        xx, yy = inverse(x), y
        graph[xx].append(yy)

        xx, yy = x, inverse(y)
        graph[yy].append(xx)

    if dfs_all():
        print(_yes)
    else:
        print(_no)
