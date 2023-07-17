class Solution:
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]
        for i in range(len(nums), 0, -1):
            for j in range(i - 1):
                if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        result = ''.join(nums)
        return '0' if result[0] == '0' else result
