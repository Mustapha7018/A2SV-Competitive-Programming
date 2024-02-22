# BOTTOM UP APPROACH
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[-1][-1] = 1

        
        def bounds(r, c) -> int:
            if 0 <= r < m and 0 <= c < n:
                return dp[r][c]

            return 0

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                dp[row][col] += (bounds(row + 1, col)) + (bounds(row, col + 1))

        return dp[0][0]



# TOP DOWN APPROACH
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = {}

        def dpFUNC(a, b) -> int:

            if a == m - 1 or b == n - 1: return 1

            state = (a, b)

            if state in memo: return memo[state]

            memo[state] = dpFUNC(a, b + 1) + dpFUNC(a + 1, b)
            res = memo[state]

            return res

        return dpFUNC(0, 0)
        
