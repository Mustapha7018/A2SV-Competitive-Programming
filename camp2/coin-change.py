# BOTTOM UP APPROACH
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        N = len(coins)
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[-1] != float('inf') else -1



# TOP DOWN APPROACH
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        N = len(coins)
        memo = {}

        def dpFunc(amt, idx) -> int:

            if idx < 0:

                if amt == 0: return 0

                if amt != 0: return float('inf')


            if amt < 0: return float('inf')

            state = (amt, idx)

            if state in memo: return memo[state]

            memo[state] = min(1 + dpFunc(amt - coins[idx], idx), dpFunc(amt, idx - 1))
            res = memo[state]

            return res

        Func = dpFunc(amount, N - 1)

        return Func if Func != float('inf') else -1
        
