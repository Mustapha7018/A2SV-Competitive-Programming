class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}
        self.word = ""  

class Solution:
    def insert(self, root: TrieNode, word: str) -> None:
        curr = root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True
        curr.word = word 

    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        for word in words:
            self.insert(root, word)

        queue = deque([root])
        longest = ""

        while queue:
            curr = queue.popleft()
            for child in curr.children.values():
                if child.endOfWord:  
                    queue.append(child)
                    if len(child.word) > len(longest) or (len(child.word) == len(longest) and child.word < longest):
                        longest = child.word

        return longest
