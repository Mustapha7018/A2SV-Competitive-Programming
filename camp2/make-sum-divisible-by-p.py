class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        total = reduce(lambda x, y: x + y, nums)
        target = total % p

        if target == 0:
            return 0

        currSum = 0
        res = float('inf')
        prefixSum = {0: -1}

        for i, num in enumerate(nums):
            currSum = (currSum + num) % p
            prefixSum[currSum] = i
            
            if (currSum - target) % p in prefixSum:
                res = min(res, i - prefixSum[(currSum - target) % p])

        return res if res < len(nums) else -1


