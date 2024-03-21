# using gcd function
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minn = min(nums)
        maxx = max(nums)

        def gcd(a, b):
            if b == 0: return a

            return gcd(b, a % b)
        
        return gcd(maxx, minn)


# class Solution:
#     def findGCD(self, nums: List[int]) -> int:

#         maxx, minn = max(nums), min(nums)

#         try:
#             max_ = max(i for i in range(2, minn + 1) if maxx % i == 0 and minn % i == 0)
#             return max_
        
#         except:
#             return 1

        

        
