"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

min_len = 2
                   
Input: target = 7, nums = [2,3,1,2,4,3,1]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
"""


def solve(target, nums):
    
    n = len(nums)
    size = 0
    min_len = float('inf')
    curr_sum = 0

    l = 0
    
    for r in range(n):
        curr_sum += nums[r]
        size += 1
        while curr_sum >= target:
            min_len = min(min_len, size)
            
            curr_sum -= nums[l]
            l += 1
            size -= 1
            
    return 0 if min_len == float('inf') else min_len

print(solve(target = 4, nums = [1,4,4]))
            
            
    
            
            
            
        
    
    
    
    
    
    
