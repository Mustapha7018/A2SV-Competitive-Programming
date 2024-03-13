class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        M = len(word1)
        N = len(word2)

        def dp(i, j):
            state = (i, j)
            if state in memo: return memo[state]

            if i == M and j == N:
                return 0

            if i == M:
                return N - j

            if j == N:
                return M - i

            if word1[i] == word2[j]:
                return dp(i+1, j+1)


            memo[state] = 1 + min(dp(i, j+1), dp(i+1, j), dp(i+1, j+1))
            res = memo[state]
            return res

        return dp(0, 0)

            

        