# https://www.acmicpc.net/problem/1786


def init():
    start = 1
    matched = 0

    while start + matched < M:
        if word[matched] == word[start + matched]:
            matched += 1
            fix[start + matched - 1] = matched
        elif matched == 0:
            start += 1
        else:
            start += matched - fix[matched - 1]
            matched = fix[matched - 1]


def kmp():
    count = 0
    start = 0
    matched = 0

    while start + matched < N:
        if matched < M and word[matched] == data[start + matched]:
            matched += 1
            if matched == M:
                count += 1
                result.append(start + 1)
        elif matched == 0:
            start += 1
        else:
            start += matched - fix[matched - 1]
            matched = fix[matched - 1]

    return count


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _space = " "
    data = input().rstrip()
    word = input().rstrip()
    N = len(data)
    M = len(word)
    fix = [0 for _ in range(M)]
    result = list()

    init()
    count = kmp()

    print(count)
    print(_space.join(map(str, result)))