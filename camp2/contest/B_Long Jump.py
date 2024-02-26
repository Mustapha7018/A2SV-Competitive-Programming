def longJump(n, arr) -> int:

    dp = [0] * (n)

    for i in range(n, 0, -1):
        if i + arr[i - 1] > n:
            dp[i - 1] = arr[i - 1]

        else:
            dp[i - 1] = arr[i - 1] + dp[i - 1 + arr[i - 1]]


    return max(dp)

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        print(longJump(n, arr))
