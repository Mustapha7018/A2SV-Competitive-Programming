def minimumVariedNumbers(s):
    res = []
 
    for i in range(9, 0, -1):
        if s >= i:
            res.append(str(i))
            s -= i
 
    return int(''.join(res[::-1]))
 
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = int(input())
 
        print(minimumVariedNumbers(s))
