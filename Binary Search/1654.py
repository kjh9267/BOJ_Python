# https://www.acmicpc.net/problem/1654


def binary_search():
    lo = 1
    hi = max_value + 1

    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        count = 0

        for value in nums:
            count += value // mid

        if count >= N:
            lo = mid
        else:
            hi = mid

    return lo


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    K, N = map(int, input().split())
    nums = [int(input()) for _ in range(K)]
    max_value = max(nums)
    print(binary_search())
