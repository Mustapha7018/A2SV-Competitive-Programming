def vitamins() -> int:
    
    dp = [float('inf')] * 8
    dp[0] = 0


    for k, v in array:
        for i in range(7):

            new = i | v
            dp[new] = min(dp[new], dp[i] + k)

    return dp[7] if dp[7] != float('inf') else -1


if __name__ == '__main__':

    n = int(input())
    array = []

    for _ in range(n):
        c, s = map(str, input().split())

        temp = 0
        for i in range(len(s)):
            num = ord(s[i]) - ord('A')
            temp += (1 << num)
       
        array.append([int(c), temp])

    print(vitamins())
    
