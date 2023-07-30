class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        count = [0] * (len(nums) + 1)
        count[0] = 1
        odd = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd += 1
            if odd >= k:
                res += count[odd - k]
            count[odd] += 1
        return res
