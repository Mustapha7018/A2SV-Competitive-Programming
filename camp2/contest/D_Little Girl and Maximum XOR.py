def littleGirlAndMaxXOR():
 
    if a == b:
        return 0
 
    return 2 ** ((a ^ b).bit_length()) - 1
 
 
if __name__ == '__main__':
    a, b = map(int, input().split())
 
    print(littleGirlAndMaxXOR())
