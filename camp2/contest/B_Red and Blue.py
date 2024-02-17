from itertools import accumulate

def redAndBlue(n, R, m, B):

    presum_R = list(accumulate(R))
    presum_B = list(accumulate(B))

    max_r = max(presum_R)
    max_b = max(presum_B)
    
    maxSeq = max(max_r, 0) + max(max_b, 0)

    return maxSeq

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())
        R = list(map(int, input().split()))
        m = int(input())
        B = list(map(int, input().split()))

        print(redAndBlue(n, R, m, B))

