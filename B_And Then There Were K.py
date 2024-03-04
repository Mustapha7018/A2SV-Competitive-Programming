def andThenThereWereK():

    return 2 ** (n.bit_length() - 1) - 1


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())

        print(andThenThereWereK())
