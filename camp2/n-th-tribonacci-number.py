# BOTTOM UP APPROACH
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * (n + 1)

        if n == 0 or n == 1: return n

        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        
        print(dp)
        return dp[-1]



# TOP DOWN APPROACH
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

        
