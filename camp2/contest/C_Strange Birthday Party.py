def strangeBirthdayParty():
    friends.sort(reverse=True)

    j = 0
    res = 0
    for i in range(n):
        if friends[i] > j:
            res += prices[j]
            j += 1
        else:
            res += prices[friends[i] - 1]

    return res

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        friends = list(map(int, input().split()))
        prices = list(map(int, input().split()))

        print(strangeBirthdayParty())
