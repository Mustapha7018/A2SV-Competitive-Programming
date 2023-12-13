'''
* Count the number of occurances of each number in the array
* Check if the count of number x is less than or equals to the 
'''

from collections import Counter
def destroyer():

    counter = Counter(robots)
    
    for i in range(max(counter)):
        if counter[i] < counter[i+1] or i+1 not in counter:
            return "NO"

    return "YES"


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        robots = list(map(int, input().split()))

        print(destroyer())
