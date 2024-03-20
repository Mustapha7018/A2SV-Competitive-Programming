class Solution:
    def findGCD(self, nums: List[int]) -> int:

        maxx, minn = max(nums), min(nums)

        try:
            max_ = max(i for i in range(2, minn + 1) if maxx % i == 0 and minn % i == 0)
            return max_
        
        except:
            return 1

        

        