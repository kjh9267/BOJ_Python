# https://www.acmicpc.net/problem/5052


class TrieNode:
    def __init__(self, end, children):
        self.__end = end
        self.__children = children

    def insert(self, phone_number, depth):
        if self.__end:
            return False

        if depth == len(phone_number) - 1:
            self.__end = True
            return True

        index = phone_number[depth + 1]

        if not self.__children[index]:
            self.__children[index] = TrieNode(False, [None for _ in range(_children_size)])

        return self.__children[index].insert(phone_number, depth + 1)


def is_possible():
    for phone_number in phone_numbers:
        if not trie_node.insert(phone_number, -1):
            return False

    return True


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _yes = "YES"
    _no = 'NO'
    _new_line = "\n"
    _children_size = 10
    T = int(input())
    result = list()

    for _ in range(T):
        N = int(input())
        phone_numbers = [tuple(map(int, input().rstrip())) for _ in range(N)]
        phone_numbers.sort()
        trie_node = TrieNode(False, [None for _ in range(_children_size)])

        if not is_possible():
            result.append(_no)
        else:
            result.append(_yes)

    print(_new_line.join(map(str, result)))
