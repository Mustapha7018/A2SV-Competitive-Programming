class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root

        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            
            curr = curr.children[w]
        curr.is_end = True


        
    def search(self, word: str) -> bool:

        def helper(i, curr, word):

            if i == len(word):
                return curr.is_end

            if word[i] == '.':
                res = False
                for w in curr.children.values():
                    res = res or helper(i + 1, w, word) 
                return res

            else:
                if word[i] not in curr.children:
                    return False

                curr = curr.children[word[i]]
                return helper(i + 1, curr, word)

        return helper(0, self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)