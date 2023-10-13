# https://www.acmicpc.net/problem/5052


def insert(trie_node, phone_number, index):
    end, children = trie_node

    if end:
        return False

    if index == len(phone_number) - 1:
        trie_node[0] = True
        return True

    next_value = phone_number[index + 1]

    if not children[next_value]:
        children[next_value] = [False, [None for _ in range(10)]]

    return insert(children[next_value], phone_number, index + 1)


def is_possible():
    for phone_number in phone_numbers:
        if not insert(trie_node, phone_number, -1):
            return False

    return True


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _yes = "YES"
    _no = 'NO'
    _new_line = "\n"
    T = int(input())
    result = list()

    for _ in range(T):
        N = int(input())
        phone_numbers = [tuple(map(int, input().rstrip())) for _ in range(N)]
        phone_numbers.sort()
        # end, children
        trie_node = [False, [None for _ in range(10)]]

        if not is_possible():
            result.append(_no)
        else:
            result.append(_yes)

    print(_new_line.join(map(str, result)))



