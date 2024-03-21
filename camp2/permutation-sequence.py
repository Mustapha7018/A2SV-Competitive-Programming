# bactracking
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        res, curr = [], []

        def backtrack():
            if len(curr) == n:
                res.append(curr.copy())
                return

            if len(res) == k:
                return

            for j in range(1, n+1):
                if j not in curr:
                    curr.append(j)
                    backtrack()
                    curr.pop()
        backtrack()
        return ''.join([str(num) for num in res[-1]])



# itertools.permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        perms = sorted(permutations([str(i) for i in range(1, n+1)]))
        return ''.join(perms[k - 1])
        
