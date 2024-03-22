class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        N = len(nums)
        maxVal = nums[0]
        prefixSum = list(accumulate(nums))

        for i in range(N):
            avg = (prefixSum[i] + i) // (i + 1)
            maxVal = max(maxVal, avg)

        return maxVal
