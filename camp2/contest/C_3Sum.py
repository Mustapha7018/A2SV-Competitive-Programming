from typing import List
def sum3(n: int, array: List[int]) -> str:

    last_digits = []

    for num in array:
        if last_digits.count(num % 10) < 3:
            last_digits.append(num % 10) 

    m = len(last_digits)

    for i in range(m):
        for j in range(i + 1, m):
            for k in range(j + 1, m):
                if (last_digits[i] + last_digits[j] + last_digits[k]) % 10 == 3:
                    return 'YES'
    return 'NO'

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        array = list(map(int, input().split()))

        print(sum3(n, array))
