class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        N = len(nums)
        memo = {}

        def dp(l, r, turn):

            if l > r: return 0

            state = (l, r, turn)

            if state in memo: return memo[state]

            if turn:
                memo[state] = max(nums[l] + dp(l + 1, r, False), dp(l, r - 1, False) + nums[r])
            else:
                memo[state] = min(dp(l + 1, r, True) - nums[l], dp(l, r - 1, True) - nums[r])

            return memo[state]

        return dp(0, N - 1, True) >= 0

        


        