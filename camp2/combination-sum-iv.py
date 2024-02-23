class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        N = len(nums)
        memo = {}

        def dpFUNC(currSum) -> int:

            if currSum == target: return 1

            if currSum > target: return 0

            if currSum in memo: return memo[currSum]

            res = 0

            for i in range(N):
                res += dpFUNC(currSum + nums[i])
                memo[currSum] = res

            return memo[currSum]

        return dpFUNC(0)



        