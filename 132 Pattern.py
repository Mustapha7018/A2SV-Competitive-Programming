class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        monotonicStack = []
        N = len(nums)
        left_pair = [float('inf')]

        for i in range(1, N):
            left_pair.append(min(left_pair[-1], nums[i-1]))
            

        for i in range(N-1, -1, -1):
            while monotonicStack and monotonicStack[-1] < nums[i]:
                right = monotonicStack.pop()
                left = left_pair[i]
                
                if right > left:
                    return True
            
            monotonicStack.append(nums[i])
        
        return False





            






        
            
            






        
