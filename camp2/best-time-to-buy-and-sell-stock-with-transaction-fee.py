class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        memo = {}

        buy = 1
        sell = 0

        def dp(i, choice) -> int:

            if i == N: return 0

            state = (i, choice)

            if state in memo: return memo[state]

            if choice == buy:
                memo[state] = max(-prices[i] + dp(i + 1, sell), dp(i + 1, buy))

            else:
                memo[state] = max(prices[i] - fee + dp(i + 1, buy), dp(i + 1, sell))

            res = memo[state]

            return res

        return dp(0, 1)

        



