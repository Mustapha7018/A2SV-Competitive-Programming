# BOTTOM UP APPROACH
class Solution:
    def rob(self, house: List[int]) -> int:

        N = len(house)

        dp = [0] * N
        dp[0] = house[0]

        for i in range(1, N):
            dp[i] += max(house[i] + dp[i - 2], dp[i - 1])

        return dp[-1]



# TOP DOWN APPROACH
class Solution:
    def rob(self, house: List[int]) -> int:
        N = len(house)
        memo = {}

        def dpFunc(idx):

            if idx == 0:
                return house[idx]

            if idx == 1:
                return max(house[0], house[1])

            if idx in memo:
                return memo[idx]

            memo[idx] = max(house[idx] + dpFunc(idx - 2), dpFunc(idx - 1))
            res = memo[idx]

            return res

        return dpFunc(N - 1)

            
            



    
   
