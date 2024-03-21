def perfectBitmasksClassroom() -> int:

    y = x & -x # 111000 gives you 001000

    while (not x & y) or (not x ^ y):
        y += 1

    return y

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        x = int(input())

        print(perfectBitmasksClassroom())
