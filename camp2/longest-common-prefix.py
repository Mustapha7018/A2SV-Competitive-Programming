class TrieNode:

    def __init__(self):
        self.is_end = False
        self.children = {}


class Solution:

    def __init__(self):
        self.root = TrieNode()

    
    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        curr.is_end = True


    def longestCommonPrefix(self, strings: List[str]) -> str:

        curr = self.root
        minWord = min(strings, key=len)
        res = ''

        for word in strings:
            self.insert(word)

        for c in minWord:
            if len(curr.children) > 1:
                return res
            
            res += c
            curr = curr.children[c]
        
        return res


















        
        