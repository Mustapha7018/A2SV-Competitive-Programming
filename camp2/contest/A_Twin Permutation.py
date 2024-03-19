def twinPermutation(n, array):
    for i in range(n):
        array[i] = (n - array[i]) + 1

    return ' '.join(map(str, array))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int, input().split()))

        print(twinPermutation(n, array))
