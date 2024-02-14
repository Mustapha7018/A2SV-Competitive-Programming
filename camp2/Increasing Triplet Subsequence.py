class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        N = len(nums)

        F, S, T = float('inf'), float('inf'), float('inf')

        for i in range(N):
            if nums[i] <= F:
                F = nums[i]

            elif nums[i] <= S:
                S = nums[i]

            else:
                return True

        return False



        
