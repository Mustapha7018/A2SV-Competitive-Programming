class Solution:
    def maxProduct(self, words: List[str]) -> int:

        N = len(words)
        maxProduct = 0
        
        for i in range(N):
            for j in range(i + 1, N):

                word1 = set(words[i])
                word2 = set(words[j])

                length = len(words[i]) * len(words[j])
                
                if word1 & word2:
                    continue

                else:
                    maxProduct = max(maxProduct, length)

        return maxProduct








        