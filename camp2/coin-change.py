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
        