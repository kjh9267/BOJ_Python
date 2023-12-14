# https://www.acmicpc.net/problem/1017


def bipartite_match(a):
    a_matched = [_not_matched for _ in range(a_group_size)]
    b_matched = [_not_matched for _ in range(b_group_size)]
    matched = 0

    for _ in range(a_group_size * 2):
        a %= a_group_size
        visited = [False for _ in range(a_group_size)]
        if dfs(a, a_matched, b_matched, visited):
            matched += 1
        a += 1

    if matched != N // 2:
        return

    if _not_matched in a_matched or _not_matched in b_matched:
        return

    first_num = nums[0]
    result.add(a_group[b_matched[b_group.index(first_num)]])


def dfs(a, a_matched, b_matched, visited):
    if visited[a]:
        return False
    visited[a] = True

    for b, even in enumerate(b_group):
        if not primes[a_group[a] + even]:
            continue
        if b_matched[b] == _not_matched or dfs(b_matched[b], a_matched, b_matched, visited):
            a_matched[a] = b
            b_matched[b] = a
            return True

    return False


def init_primes():
    sqrt = int(_limit ** (1 / 2))
    primes[1] = False

    for num in range(2, sqrt + 1):
        if not primes[num]:
            continue
        for multiple_num in range(num * 2, _limit, num):
            primes[multiple_num] = False


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _not_matched = -1
    _limit = 2_001
    _space = " "
    N = int(input())
    nums = list(map(int, input().split()))
    primes = [True for _ in range(_limit)]
    result = set()
    if nums[0] % 2 == 0:
        a_group = list(filter(lambda x: x % 2 == 1, nums))
        b_group = list(filter(lambda x: x % 2 == 0, nums))
    else:
        a_group = list(filter(lambda x: x % 2 == 0, nums))
        b_group = list(filter(lambda x: x % 2 == 1, nums))
    a_group_size = len(a_group)
    b_group_size = len(b_group)

    init_primes()

    for a in range(a_group_size):
        bipartite_match(a)

    if not result:
        print(_not_matched)
    else:
        print(_space.join(map(str, sorted(result))))
