# https://www.acmicpc.net/problem/1253
from sys import stdin


def binary_search(lo, hi, num, target, avoid):
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if data[mid] + num == target and mid != avoid:
            return True
        elif data[mid] + num < target:
            lo = mid
        else:
            hi = mid

    return False


if __name__ == '__main__':
    input = stdin.readline
    N = int(input())
    result = 0
    data = list(sorted(map(int, input().split())))

    for index1, num in enumerate(data):
        flag = False
        for index2 in range(N):
            if index1 == index2:
                continue
            if binary_search(-1, index2, data[index2], num, index1):
                flag = True
                break
            if binary_search(index2, N, data[index2], num, index1):
                flag = True
                break
        if flag:
            result += 1

    print(result)