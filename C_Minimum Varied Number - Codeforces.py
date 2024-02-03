def minVariedNum(s):

    res = []
    digits = []
    curr = 9
    
    while s > 0 and curr > 0:

        if curr <= s:
            digits.append(str(curr))
            s -= curr
        curr -= 1

    res.append(''.join(sorted(digits)))

    return int(res[0])



if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        s = int(input())

        print(minVariedNum(s))




