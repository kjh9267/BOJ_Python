# https://www.acmicpc.net/problem/2467

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _space = ' '
    N = int(input())
    data = list(sorted(map(int, input().split()), key=lambda x: abs(x)))
    min_value = float('inf')
    result = -1

    for index in range(1, N):
        if min_value > abs(data[index - 1] + data[index]):
            min_value = abs(data[index - 1] + data[index])
            result = index

    print(_space.join(map(str, sorted([data[result - 1], data[result]]))))
