# https://www.acmicpc.net/problem/9250
from collections import deque


class TrieNode:
    root = None

    def __init__(self, end, fail, children):
        self.end = end
        self.fail = fail
        self.children = children

    def insert(self, word, depth):
        if depth == len(word) - 1:
            self.end = True
            return

        index = ord(word[depth + 1]) - 97
        if not self.children[index]:
            self.children[index] = TrieNode(False, None, [None for _ in range(26)])

        self.children[index].insert(word, depth + 1)

    @classmethod
    def bfs(cls):
        queue = deque()
        queue.append(cls.root)

        cls.root.fail = cls.root

        while queue:
            cur = queue.popleft()

            for index, nxt in enumerate(cur.children):
                if not nxt:
                    continue
                if cur == cls.root:
                    nxt.fail = cls.root
                else:
                    node = cur.fail
                    while node != cls.root and not node.children[index]:
                        node = node.fail

                    if node.children[index]:
                        node = node.children[index]

                    nxt.fail = node

                nxt.end = nxt.fail.end or nxt.end
                queue.append(nxt)

    @classmethod
    def find(cls, string):
        node = cls.root

        for char in string:
            index = ord(char) - 97

            while node != cls.root and not node.children[index]:
                node = node.fail

            if node.children[index]:
                node = node.children[index]

            if node.end:
                return True

        return False


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _new_line = "\n"
    _yes = "YES"
    _no = "NO"
    N = int(input())
    words = [input().rstrip() for _ in range(N)]
    Q = int(input())
    data = [input().rstrip() for _ in range(Q)]
    trie = TrieNode(False, None, [None for _ in range(26)])
    TrieNode.root = trie
    result = list()

    for word in words:
        trie.insert(word, -1)

    trie.bfs()

    for string in data:
        if trie.find(string):
            result.append(_yes)
        else:
            result.append(_no)

    print(_new_line.join(result))
