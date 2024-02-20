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

            
            



    
   
