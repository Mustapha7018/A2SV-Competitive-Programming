class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        N = len(nums)
        memo = {}

        def dpFunc(idx, targetSum) -> bool:

            if idx >= N:
                return False

            if targetSum <= 0:
                return targetSum == 0


            state = (idx, targetSum)

            if state in memo:
                return memo[state]

            memo[state] = dpFunc(idx + 1, targetSum - nums[idx]) or dpFunc(idx + 1, targetSum)
            res = memo[state]

            return res

        return sum(nums) % 2 == 0 and dpFunc(0, sum(nums) // 2)





