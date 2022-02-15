def solution(strings):
    A = 'A'
    B = 'B'
    result = 0

    # 1,     2,   4,  8,  16,  32
    # start, AA, B ~, BA, B ~, A

    for string in strings:
        string += 'C'

        N = len(string)
        state = [0 for _ in range(N + 1)]
        state[0] = 1

        for index in range(N):
            if (state[index] & 1) > 0:
                go_state_2(A, index, state, string)
                go_state_8(A, B, index, state, string)

            if (state[index] & 2) > 0:
                go_state_4(B, index, state, string)

            if (state[index] & 4) > 0:
                go_state_4(B, index, state, string)
                go_state_2(A, index, state, string)
                go_state_8(A, B, index, state, string)

            if (state[index] & 8) > 0:
                go_state_16(B, index, state, string)

            if (state[index] & 16) > 0:
                go_state_32(A, index, state, string)
                go_state_16(B, index, state, string)
                go_state_2(A, index, state, string)
                go_state_8(A, B, index, state, string)

            if (state[index] & 32) > 0:
                go_state_2(A, index, state, string)
                go_state_8(A, B, index, state, string)

        if (state[N - 1] & 32) > 0 or (state[N - 1] & 4) > 0:
            result += 1

        print(state)

    return result


def go_state_16(B, index, state, string):
    if string[index] == B:
        state[index + 1] |= 16


def go_state_32(A, index, state, string):
    if string[index] == A:
        state[index + 1] |= 32


def go_state_4(B, index, state, string):
    if string[index] == B:
        state[index + 1] |= 4


def go_state_8(A, B, index, state, string):
    if string[index] == B and string[index + 1] == A:
        state[index + 2] |= 8


def go_state_2(A, index, state, string):
    if string[index] == A and string[index + 1] == A:
        state[index + 2] |= 2


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    print(solution(['AABAAA', 'BABABB', 'BABBAAAB', 'BABAAABAABBABBA']))
    print(solution(['AA', 'BAB', 'BAAAA', 'ABBABB', 'AABBBBABBAAAA']))
    print(solution(['AABAABAAB', 'AABBBAABBB', 'AABBBABBABABBBAAABBBABBBA']))