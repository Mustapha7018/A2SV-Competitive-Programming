"""
Question Description
You have some apples and a basket that can carry up to 5000 units of weight. 
Given an integer array weight where weight[i] is the weight of the ith apple, return the maximum number of apples you can put in the basket.


Example 1:
Input: weight = [100,200,150,1000]# total = 1450
Output: 4
Explanation: All 4 apples can be carried by the basket since their sum of weights is 1450.


Example 2:
Input: weight = [900,950,800,1000,700,800]
Output: 5      
Explanation: The sum of weights of the 6 apples exceeds 5000 so we choose any 5 of them.

[2, 6, 3, 7, 3, 2, 1]

[1, 2, 2, 0, 0, 1, 1] => m = max(arr)
[1, 2, 2, 3, 3, 6, 7] =n

O(n+m)


Constraints:
1 <= weight.length <= 3000
1 <= weight[i] <= 3000
"""

def max_apples(weight, basket=5000):
    
    if sum(weight) <= basket:
        return len(weight)
    
    else:
        weight.sort()
        count = 0
        curr_sum = 0
        n = len(weight)
        for i in range(n):
            curr_sum += weight[i]
            if curr_sum <= basket:
                count += 1
                
        return count
    
print(max_apples([900,950,800,1000,700,800]))

'''
n = 10**5
m = 1000
from math import log
print('built in', n*log(n, 2))
'''
print('count', n+m)      
