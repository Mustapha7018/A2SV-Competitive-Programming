def summ():
 
    if a + b == c:
        return 'YES'
      
    elif a + c == b:
        return 'YES'
 
    elif b + c == a:
        return 'YES'
 
    else:
        return 'NO' 
 
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
 
        print(summ())
