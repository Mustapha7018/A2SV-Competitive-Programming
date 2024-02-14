class Solution:
    def minDifference(self, nums: List[int]) -> int:

        N = len(nums)
        l, r = 0, N-4

        if N <= 4:
            return 0

        nums.sort()
        mins = []

        while l < r and r < N:
            mins.append(nums[r] - nums[l])

            l += 1
            r += 1

        return min(mins)


  
    
        
