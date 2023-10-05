# https://www.acmicpc.net/problem/1043


def find(x):
    if parents[x] < 0:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def merge(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    if x in aware:
        parents[y] = x
    else:
        parents[x] = y


def is_possible():
    for participant in party:
        participant = find(participant)

        if participant in aware:
            return False

    return True


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, M = map(int, input().split())
    aware = set(map(int, input().split()[1:]))
    parties = [list(map(int, input().split()))[1:] for _ in range(M)]
    parents = [-1 for _ in range(N + 1)]
    result = 0

    for party in parties:
        for index in range(1, len(party)):
            merge(party[index - 1], party[index])

    for party in parties:
        if is_possible():
            result += 1

    print(result)