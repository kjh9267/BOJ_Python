# https://www.acmicpc.net/problem/9248


class Character:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        if groups[self.value] != groups[other.value]:
            return groups[self.value] < groups[other.value]
        return groups[self.value + prefix] < groups[other.value + prefix]


def compute_suffix_array():
    global groups
    global prefix
    prefix = 1
    groups[N] = -1

    for index in range(N):
        groups[index] = data[index]

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
        if indices[index] > 0:
            prev_index = suffix_array[indices[index] - 1].value

            while True:
                if index + matched >= N or prev_index + matched >= N:
                    break
                if data[index + matched] != data[prev_index + matched]:
                    break
                matched += 1

            lcp_array[indices[index]] = matched
            matched = max(0, matched - 1)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _space = " "
    _new_line = '\n'
    _x = 'x'
    data = list(map(ord, input().rstrip()))
    N = len(data)
    suffix_array = [Character(index) for index in range(N)]
    lcp_array = [0 for _ in range(N)]
    groups = [0 for _ in range(N + 1)]

    compute_suffix_array()
    compute_lcp_array()

    lcp_array[0] = _x
    result = _new_line.join(
        (_space.join(map(lambda x: str(x.value + 1), suffix_array)),
         _space.join(map(lambda x: str(x), lcp_array)))
    )

    print(result)
