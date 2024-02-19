def printPedestal(n):
 
    h1, h2, h3 = 2, 3, 1
 
    r = n - 6
    
 
    while r >= 3:
        h1 += 1
        h2 += 1
        h3 += 1
 
        r -= 3
    
    if r == 1:
        h2 += r 
 
    elif r == 2:
        h1 += 1
        h2 += 1
 
    print(h1, h2, h3)
 
 
if __name__ == '__main__':
    t = int(input())
 
    for _ in range(t):
        n = int(input())
 
        printPedestal(n)
