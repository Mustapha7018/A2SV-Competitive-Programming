class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        N = len(arr)
        arr.sort()

        if arr[0] == 1:
            pass

        else:
            arr[0] = 1

        for i in range(1, N):

            if abs(arr[i] - arr[i - 1]) <= 1:
                continue

            else:
                arr[i] = arr[i - 1] + 1

        return arr[-1]
