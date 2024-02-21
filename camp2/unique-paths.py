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
        