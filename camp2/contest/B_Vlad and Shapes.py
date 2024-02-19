def vladAndShapes(matrix, n):
    arr = []
 
    for row in matrix:
        arr.append(row.count('1'))
 
    new = [i for i in arr if i != 0]
 
    return 'TRIANGLE' if len(set(new)) == len(new) else 'SQUARE'
 
 
if __name__ == '__main__':
 
    t = int(input())
 
    for _ in range(t):
        n = int(input())
        matrix = []
 
        for _ in range(n):
 
            matrix.append(input())
 
        print(vladAndShapes(matrix, n))
 
