def unnaturalConditions():
    a = int('5' * n)
    b = int('4' * (n - 1) + '5')

    print(a)
    print(b)

if __name__ == '__main__':
    n, m = map(int, input().split())
    unnaturalConditions()
