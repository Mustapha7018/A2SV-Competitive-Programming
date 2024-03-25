def promisingString():
 
    res = 0
  
    for i in range(n):
        plus = minus = 0
 
        for j in range(i, n):
            if string[j] == '-':
                minus += 1
 
            if string[j] == '+':
                plus += 1
 
            diff = minus - plus
            if diff % 3 == 0 and minus >= plus:
                res += 1
 
    return res
 
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        string = input()
 
        print(promisingString())
