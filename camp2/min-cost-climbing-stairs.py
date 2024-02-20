class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        N = len(cost)
        cost = cost + [0]
        memo = {}

        def dp(idx):

            if idx <= 1: return cost[idx]

            if idx in memo:
                return memo[idx]

            memo[idx] = cost[idx] + min(dp(idx - 1), dp(idx - 2))
            res = memo[idx]

            return res

        return dp(N)
                









            

            

            

            
        