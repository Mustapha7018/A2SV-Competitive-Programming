def numberReplacement():

    hashmap = {}

    for i in range(n):
        if array[i] not in hashmap:
            hashmap[array[i]] = string[i]

        elif hashmap[array[i]] != string[i]:
            return 'NO'

    return 'YES'



if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        array = list(map(int, input().split()))
        string = input()

        print(numberReplacement())
