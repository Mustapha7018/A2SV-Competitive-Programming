import sys
import threading
from functools import cache

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

def easyProblem():
    n = int(input())
    s = input()
    a = list(map(int, input().split()))

    check = "hard"

    @cache
    def dp(i, j):
        state = (i, j)
        
        if j == len(check): return float('inf')
        
        if i == len(s): return 0
        
        if s[i] == check[j]:
            res = min(dp(i+1, j) + a[i], dp(i+1, j+1))

        else:
            res = dp(i+1, j)

        return res
    
    print(dp(0, 0))
    
    
main_thread = threading.Thread(target=easyProblem)
main_thread.start()
main_thread.join()
