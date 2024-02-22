class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        N = len(nums)
        memo = {}

        def dpFUNC(idx, currSum) -> int:
            
            if idx >= N:
                if currSum == target:
                    return 1

                return 0

            state = (idx, currSum)

            if state in memo: return memo[state]

            memo[state] = dpFUNC(idx + 1, nums[idx] + currSum) + dpFUNC(idx + 1, currSum - nums[idx])
            res = memo[state]

            return res

        return dpFUNC(0, 0)

        