def berlAndMusic():

    res = [0] * n
    perms = []

    s = sorted([[rating[i],songs[i],i] for i in range(n)])
    
    for item in s:
        perms.append(item[2])

    
    for i in range(n):
        res[perms[i]] = i + 1

    return ' '.join(map(str, res))


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        songs = list(map(int, input().split()))
        rating = input()

        print(berlAndMusic())
