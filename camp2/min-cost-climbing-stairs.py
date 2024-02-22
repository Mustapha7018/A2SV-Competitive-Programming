# BOTTOM UP APPROACH
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        N = len(cost)
        cost.append(0)
        dp = [float('inf')] * (N+1)

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, N+1):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        return dp[-1]




# TOP DOWN APPROACH
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
                









            

            

            

            
        
