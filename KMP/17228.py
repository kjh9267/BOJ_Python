# https://www.acmicpc.net/problem/17228
import sys
from collections import deque
sys.setrecursionlimit(999999999)


def init():
    start = 1
    matched = 0

    while start + matched < len(word):
        if word[matched] == word[start + matched]:
            matched += 1
            fix[start + matched - 1] = matched
        elif matched == 0:
            start += 1
        else:
            start += matched - fix[matched - 1]
            matched = fix[matched - 1]


def dfs(cur, prev, string, start, matched):
    global count
    count += 1

    start, matched = kmp(start, matched, string)

    for nxt, value in graph[cur]:
        if nxt == prev:
            continue
        string.append(value)
        dfs(nxt, cur, string, start, matched)
        string.pop()


def kmp(start, matched, string):
    while start + matched < len(string):
        if matched < len(word) and string[start + matched] == word[matched]:
            matched += 1
            if matched == len(word):
                words.add(count)
        elif matched == 0:
            start += 1
        else:
            start += matched - fix[matched - 1]
            matched = fix[matched - 1]

    return start, matched


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    graph = [list() for _ in range(N)]

    for _ in range(N - 1):
        start, end, value = input().split()
        start, end = map(lambda x: int(x) - 1, (start, end))

        graph[start].append((end, value))
        graph[end].append((start, value))

    word = input().rstrip()
    fix = [0 for _ in range(len(word))]

    init()

    words = set()
    count = -1
    dfs(0, -1, deque(), 0, 0)

    print(len(words))
