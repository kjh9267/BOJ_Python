# https://www.acmicpc.net/problem/12917
from collections import deque


class Character:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        if groups[self.value] != groups[other.value]:
            return groups[self.value] < groups[other.value]
        return groups[self.value + prefix] < groups[other.value + prefix]


def compute_suffix_array():
    global prefix
    global groups

    for index in range(N):
        groups[index] = ord(data[index]) - 97

    groups[N] = -1

    while prefix < N:
        suffix_array.sort()
        new_groups = [0 for _ in range(N + 1)]
        new_groups[N] = -1

        for index in range(1, N):
            if suffix_array[index - 1] < suffix_array[index]:
                new_groups[suffix_array[index].value] = new_groups[suffix_array[index - 1].value] + 1
            else:
                new_groups[suffix_array[index].value] = new_groups[suffix_array[index - 1].value]

        prefix <<= 1
        groups = new_groups


def compute_lcp_array():
    indices = [0 for _ in range(N)]

    for index in range(N):
        indices[suffix_array[index].value] = index

    matched = 0
    for index in range(N):
        if indices[index] == 0:
            continue

        prev_index = suffix_array[indices[index] - 1].value

        while True:
            if prev_index + matched >= N or index + matched >= N:
                break
            if data[prev_index + matched] != data[index + matched]:
                break
            matched += 1

        lcp_array[indices[index]] = matched
        matched = max(matched - 1, 0)


def sweep_all():
    result = 0
    left = 0

    for right in range(N - 1):
        if data[suffix_array[left].value] != data[suffix_array[right + 1].value]:
            result = max(result, sweep(left, right + 1))
            left = right + 1

    result = max(result, sweep(left, N))

    return result


def sweep(start, end):
    result = 0
    stack = deque()

    for index in range(start, end + 1):
        value = lcp_array[index]
        result = max(result, index)

        while stack:
            if lcp_array[stack[-1]] < value:
                break

            popped_value = stack.pop()

            if stack:
                temp = lcp_array[popped_value] * (index - stack[-1])
                result = max(result, temp)
            else:
                temp = index - start
                result = max(result, temp)

        stack.append(index)

    return result


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    data = input().rstrip()
    N = len(data)
    prefix = 1
    suffix_array = [Character(index) for index in range(N)]
    groups = [0 for _ in range(N + 1)]
    lcp_array = [0 for _ in range(N)]

    compute_suffix_array()
    compute_lcp_array()
    lcp_array = lcp_array + [0]

    result = sweep_all()
    print(result)
