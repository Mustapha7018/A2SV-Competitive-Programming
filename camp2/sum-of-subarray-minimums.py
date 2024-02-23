class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        N = len(arr)
        prev = [-1] * N
        res = [0] * N

        monStack = []

        for i in range(N):

            while monStack and arr[monStack[-1]] > arr[i]:
                monStack.pop()

            if monStack:
                prev[i] = monStack[-1]

            monStack.append(i)

        
        for i in range(N):
            res[i] = res[prev[i]] + arr[i] * (i - prev[i])

        return sum(res) % ((10 ** 9) + 7)




        
        