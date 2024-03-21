# using itertools.combinations
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        maxOR = reduce(lambda x, y: x | y, nums)
        N = len(nums)
        count = 0
        
        for i in range(1, N + 1):
            subsets = combinations(nums, i)

            for sub in subsets:
                temp = reduce(lambda x, y: x | y, sub)

                if temp == maxOR:
                    count += 1

        return count



# Backtracking approach
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        maxOR = reduce(lambda x, y: x | y, nums)

        array = []
        N = len(nums)
        nums.sort()

        def backtrack(i, curr) -> List[List[int]]:
            array.append(curr.copy())
        
            for j in range(i, N):
                curr.append(nums[j])
                backtrack(j + 1, curr)
                curr.pop()

        backtrack(0, [])

        count = 0
        for arr in array:
            if arr:
                temp = reduce(lambda x, y: x | y, arr)
                if temp == maxOR:
                    count += 1
        return count

        
        
