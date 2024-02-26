def constanzeMachine(string) -> int:

    MOD = ((10 ** 9) + 7)
    N = len(string)

    dp = [0] * (N+1)
    dp[0] = 1
    dp[1] = 1

    if 'w' in string or 'm' in string:
        return 0 

    for i in range(2, N + 1):
        prev1 = string[i - 1]
        prev2 = string[i - 2]

        if (prev1 + prev2 == 'uu') or (prev1 + prev2 == 'nn'):
            dp[i] = (dp[i - 2] + dp[i - 1]) % MOD

        else:
            dp[i] = dp[i - 1]

   
    return dp[N] % MOD


if __name__ == '__main__':
    string = input()

    print(constanzeMachine(string))
