class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        perms = sorted(permutations([str(i) for i in range(1, n+1)]))
        return ''.join(perms[k - 1])
        