class Solution:
    def findComplement(self, num: int) -> int:

        comp, i = 0, 1

        while i <= num:
            if i & num == 0:
                comp += i

            i <<= 1

        return comp

     


        
        