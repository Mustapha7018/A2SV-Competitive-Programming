class Solution:
    def countPrimes(self, num: int) -> int:

        arr = [True] * num
        count = 0
        
        for i in range(2, num):
            if arr[i]:
                for j in range(i * i, num, i):
                    arr[j] = False

                count += 1

        return count
        