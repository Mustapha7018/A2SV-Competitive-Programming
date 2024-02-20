class Solution:
    def tribonacci(self, n: int) -> int:

        memo = {}

        def dpFunc(num) -> int:

            if num == 0: return 0

            if num == 1: return 1

            if num == 2: return 1

            if num in memo:
                return memo[num]

            memo[num] = dpFunc(num - 1) + dpFunc(num - 2) + dpFunc(num - 3)
            res = memo[num]

            return res

        return dpFunc(n)

        