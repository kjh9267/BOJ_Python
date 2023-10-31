# https://www.acmicpc.net/problem/1929


def init_primes():
    sqrt = int(N ** (1 / 2))
    primes[0] = False
    primes[1] = False

    for num in range(2, sqrt + 1):
        if not primes[num]:
            continue
        for multiple_num in range(num * 2, N + 1, num):
            primes[multiple_num] = False


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    M, N = map(int, input().split())
    _new_line = "\n"
    primes = [True for _ in range(N + 1)]
    result = list()

    init_primes()

    for num in range(M, N + 1):
        if primes[num]:
            result.append(num)

    print(_new_line.join(map(str, result)))
