# BOTTOM UP APPROACH
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text2)
        n = len(text1)

        dp = [[0] * (m+1)  for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                    
        return dp[0][0]


# TOP DOWN APPROACH
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def dp(i, j):

            if i >= len(text1) or j >= len(text2):
                return 0

            if text1[i] == text2[j]:
                return dp(i + 1, j + 1) + 1

            return max(dp(i + 1, j), dp(i, j + 1))
        
        return dp(0, 0)

        




   
        
