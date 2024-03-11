def marathon():

    pos = arr[0]

    temp = sorted(arr, reverse=True)
    return (temp.index(pos))

if __name__ == '__main__':

    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        print(marathon())
