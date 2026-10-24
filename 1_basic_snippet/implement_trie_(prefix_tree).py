class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_char = False


# Basic implementation of Trie / PrefixTree
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:  # runtime O(1), space O(1)
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.end_char = True

    def search(self, word: str) -> bool:  # runtime O(1), space O(1)
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.end_char

    def startsWith(self, prefix: str) -> bool:  # runtime O(1), space O(1)
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True


# Question URL: https://neetcode.io/problems/implement-prefix-tree/question
# Solution: ? -- runtime O(1), space O(1)
