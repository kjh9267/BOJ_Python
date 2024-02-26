# https://www.acmicpc.net/problem/3033


class Character():
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        if groups[self.value] != groups[other.value]:
            return groups[self.value] < groups[other.value]
        return groups[self.value + prefix] < groups[other.value + prefix]


def compute_suffix_array():
    global prefix
    global groups
    groups[N] = -1

    for index in range(N):
        groups[index] = ord(data[index]) - 97

    while prefix < N:
        new_groups = [0 for _ in range(N + 1)]
        new_groups[N] = -1

        suffix_array.sort()

        for index in range(1, N):
            if suffix_array[index - 1] < suffix_array[index]:
                new_groups[suffix_array[index].value] = new_groups[suffix_array[index - 1].value] + 1
            else:
                new_groups[suffix_array[index].value] = new_groups[suffix_array[index - 1].value]

        groups = new_groups
        prefix <<= 1


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
        matched = max(0, matched - 1)


def solve():
    max_size = 0

    for index in range(1, N):
        max_size = max(max_size, lcp_array[index])

    return max_size


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    data = input().rstrip()
    prefix = 1
    suffix_array = [Character(index) for index in range(N)]
    groups = [0 for _ in range(N + 1)]
    lcp_array = [0 for _ in range(N)]

    compute_suffix_array()
    compute_lcp_array()
    result = solve()

    print(result)
