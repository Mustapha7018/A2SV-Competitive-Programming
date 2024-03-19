def coverInWater():
    return 2 if '...' in cells else cells.count('.') 

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        cells = input()

        print(coverInWater())
