# https://www.acmicpc.net/problem/10816


def compute_count(target):
    minimum_value = lower_bound(target)
    maximum_value = upper_bound(target)

    return maximum_value - minimum_value + 1


def lower_bound(target):
    lo = -1
    hi = N

    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if data[mid] >= target:
            hi = mid
        else:
            lo = mid

    return hi


def upper_bound(target):
    lo = -1
    hi = N

    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if data[mid] <= target:
            lo = mid
        else:
            hi = mid

    return lo


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _space = ' '
    N = int(input())
    data = list(sorted(map(int, input().split())))
    M = int(input())
    result = list(map(compute_count, map(int, input().split())))

    print(_space.join(map(str, result)))