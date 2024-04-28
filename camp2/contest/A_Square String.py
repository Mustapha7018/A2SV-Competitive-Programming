def squareString():
    mid = len(string) // 2
 
    return 'YES' if string[:mid] == string[mid:] else 'NO'
 
 
if __name__ == '__main__':
    t = int(input())
 
    for _ in range(t):
        string = input()
        print(squareString())
