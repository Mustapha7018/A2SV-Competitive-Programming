class TrieNode:

    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()

            curr = curr.children[w]
            curr.count += 1

    
    def search(self, prefix: str) -> bool:
        curr = self.root
        res = 0

        for p in prefix:
            curr = curr.children[p]
            res += curr.count

        return res



class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        res = []

        for word in words:
            trie.insert(word)

        for word in words:
            temp = trie.search(word)
            res.append(temp)

        return res
        