class Solution:
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height)-1
        max_volume = float('-inf')

        while l <= r:
            curr_volume = min(height[l], height[r]) * (r - l)
            max_volume = max(curr_volume, max_volume)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_volume
        
