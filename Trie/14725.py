# https://www.acmicpc.net/problem/14725


class TrieNode:
    def __init__(self, start, end, children):
        self.start = start
        self.end = end
        self.children = children

    def insert(self, words, index):
        if words[index] == _space:
            self.start = True

        if index == len(words) - 1:
            self.end = True
            return

        next_value = ord(words[index + 1]) - 65
        if next_value < 0:
            next_value = 26

        if not self.children[next_value]:
            self.children[next_value] = TrieNode(False, False, [None for _ in range(27)])

        if next_value == 26:
            self.end = True

        self.children[next_value].insert(words, index + 1)

    def find(self, depth, word):
        if self.start:
            word = list()
            depth += 1

        if self.end:
            result.append(_depth * depth + ''.join(word))

        for index, next_node in enumerate(self.children):
            if not next_node:
                continue

            next_node.find(depth, word + [chr(index + 65)])


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _space = ' '
    _depth = '--'
    _new_line = '\n'
    N = int(input())
    data = [' '.join(input().split()[1:]) for _ in range(N)]
    trie = TrieNode(True, False, [None for _ in range(27)])
    result = list()

    for words in data:
        trie.insert(words, -1)

    trie.find(-1, list())

    print(_new_line.join(result))