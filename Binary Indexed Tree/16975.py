# https://www.acmicpc.net/problem/16975


def range_update(left, right, value):
    update(left, value, -(left - 1) * value)
    update(right + 1, -value, right * value)


def update(index, m_value, a_value):
    while index <= N:
        a_tree[index] += a_value
        m_tree[index] += m_value
        index += (index & -index)


def sum(index):
    a_value = 0
    m_value = 0
    i = index

    while i > 0:
        a_value += a_tree[i]
        m_value += m_tree[i]
        i -= (i & -i)

    return m_value * index + a_value


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _update = 1
    _new_line = '\n'
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    a_tree = [0 for _ in range(N + 1)]
    m_tree = [0 for _ in range(N + 1)]
    M = int(input())
    result = list()

    for index in range(1, N + 1):
        range_update(index, index, nums[index])

    for _ in range(M):
        commands = list(map(int, input().split()))
        command = commands[0]

        if command == _update:
            left, right, value = commands[1:]
            range_update(left, right, value)
        else:
            index = commands[1]
            value = sum(index) - sum(index - 1)
            result.append(value)

    print(_new_line.join(map(str, result)))