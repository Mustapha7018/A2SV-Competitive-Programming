# Precomputation
from itertools import accumulate
 
array = []
for i in range(1, 200001):
    n = str(i)
    summ = 0
 
    for i in n:
        summ += int(i)
    array.append(summ)
  
presum = list(accumulate(array))
 
t = int(input())
for _ in range(t):
    n = int(input())
 
    print(presum[n - 1])
