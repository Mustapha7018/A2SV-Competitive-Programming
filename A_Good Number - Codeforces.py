def goodNumber():
    count = 0
    for num in arr:
        digits_set = set(str(num))
        for i in range(k + 1):
            if str(i) not in digits_set:
                break
        else:
            count += 1
    return count

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = [int(input()) for _ in range(n)]

    print(goodNumber())
