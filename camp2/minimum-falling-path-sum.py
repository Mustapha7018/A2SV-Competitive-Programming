class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        N = len(matrix)
        memo = {}

        
        def dp(r, c) -> int:

            if c < 0 or c >= N: return float('inf')
            if r >= N: return 0

            state = (r, c)

            if state in memo: return memo[state]

            memo[state] = min(dp(r + 1, c - 1), dp(r + 1, c), dp(r + 1, c + 1)) + matrix[r][c]
            res = memo[state]

            return res
        
        ans = float('inf')
        for i in range(N):
            ans = min(ans, dp(0, i))

        return ans
