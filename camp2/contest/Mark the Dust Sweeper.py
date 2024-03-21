def markTheDustSweeper():
    ops = 0
    flag = False

    for i in range(n - 1):
        if rooms[i] != 0:
            flag = True
            ops += rooms[i]
       
        elif flag:
            ops += 1

    return ops

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        rooms = list(map(int, input().split()))

        print(markTheDustSweeper())
