from collections import defaultdict

def maximalAND(n, k, array) -> int:

    bitmask = [0] * 31
    res = 0

    for num in array:
        for i in range(31):
            if num & 1:
                bitmask[i]+=1

            num >>= 1
    
    
    for i in range(30,-1,-1):
        curr = n - bitmask[i]
        
        if k >= curr:
            res += pow(2, i)
            k -= curr

    return res
    


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        array = list(map(int, input().split()))

        print(maximalAND(n, k, array))




