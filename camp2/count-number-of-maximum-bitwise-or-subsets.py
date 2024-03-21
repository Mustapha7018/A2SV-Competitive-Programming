class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        maxOR = reduce(lambda x,y: x | y, nums)

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

        
        