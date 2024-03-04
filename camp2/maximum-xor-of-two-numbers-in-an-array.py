class TrieNode:

    def __init__(self):
        self.isEnd = False
        self.children = {}

class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, binary: str) -> None:
        curr = self.root

        for b in binary:
            if b not in curr.children:
                curr.children[b] = TrieNode()
            curr = curr.children[b]

        curr.isEnd = True

    def search(self, binary: str) -> int:
        curr = self.root
        xor = ''

        for b in binary:
            opposite = '1' if b == '0' else '0'
            if opposite in curr.children:
                xor += opposite
                curr = curr.children[opposite]
            else:
                xor += b
                curr = curr.children[b]

        return int(xor, 2)

         

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        maxx = max(nums).bit_length()
        binaries = [bin(num)[2:].zfill(maxx) for num in nums]

        for binary in binaries:
            trie.insert(binary)

        max_xor = 0
        for binary in binaries:
            xor = trie.search(binary) ^ int(binary, 2)
            max_xor = max(max_xor, xor)

        return max_xor

                




                


        


        


    

