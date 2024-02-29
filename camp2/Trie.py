'''
IMPLEMENTATION OF TRIE DATA STRUCTURE

'''
# ARRAY IMPLEMENTATION

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')

            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            
            curr = curr.children[idx]
        curr.is_end = True


    def search(self, word: str) -> bool:
        curr = self.root 

        for w in word:
            idx = ord(w) - ord('a')
            if curr.children[idx] == None:
                return False 

            curr = curr.children[idx]

        return curr.is_end


    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for p in prefix:
            idx = ord(p) - ord('a')
            if curr.children[idx] == None:
                return False
            
            curr = curr.children[idx]

        return True



# DICTIONARY IMPLEMENTATION

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        curr.is_end = True


    def search(self, word: str) -> bool:
        curr = self.root

        for w in word:
            if w not in curr.children:
                return False
            
            curr = curr.children[w]

        return curr.is_end


    def startsWith(self, prefix: str) -> bool:
        curr = self.root 

        for p in prefix:
            if p not in curr.children:
                return False 

            curr = curr.children[p]
        
        return True



