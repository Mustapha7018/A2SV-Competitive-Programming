def vladAndBestFive():
 
    A = s.count('A')
    B = s.count('B')
 
    return 'A' if A > B else 'B'
 
if __name__ == '__main__':
    t = int(input())
 
    for _ in range(t):
        s = input()
 
        print(vladAndBestFive())
