class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        xor = x ^ y
        countDistance = 0

        while xor > 0:
            if xor & 1 == 1:
                countDistance += 1

            xor >>= 1

        return countDistance



        