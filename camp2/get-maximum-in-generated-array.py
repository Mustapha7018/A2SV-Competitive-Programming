class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        memo = {}
        maxx = -1

        def dpFunc(num) -> int:

            if num < 2: return num

            if num in memo: return memo[num]

            res = 0
            if num % 2 == 1:
                t = (num - 1) // 2
                memo[num] = dpFunc(t) + dpFunc(t + 1)
                res = memo[num]

            else:
                memo[num] = dpFunc(num // 2)
                res = memo[num]

            return res

        for i in range(n + 1):
            maxx = max(maxx, dpFunc(i))

        return maxx
        