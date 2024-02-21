class Solution:
    def rob(self, house: List[int]) -> int:

        N = len(house)
        memo = {}

        def dpFunc(l, r):

            if N == 1: return house[0]

            if l > r: return 0

            state = (l, r)

            if state in memo: return memo[state]

            memo[state] = max(house[l] + dpFunc(l + 2, r), dpFunc(l + 1, r))
            res = memo[state]

            return res

        return max(dpFunc(0, N - 2), dpFunc(1, N - 1))


        