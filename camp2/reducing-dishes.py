class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort()
        N = len(satisfaction)
        maxSum = 0

        for i in range(N - 1, -1, -1):
            currSum = 0
            idx = 1
            for j in range(i, N):

                currSum += satisfaction[j] * idx
                idx += 1

            maxSum = max(maxSum, currSum)

        return maxSum


        




