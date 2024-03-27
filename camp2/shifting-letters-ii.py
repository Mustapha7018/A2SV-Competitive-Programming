class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        def val(char):
            return ord(char) - ord('a')

        diff = [0] * (len(s) + 2)
        finalStr = ''

        for l, r, d in shifts:
            if d == 0:
                diff[l+1] += -1
                diff[r+2] -= -1

            else:
                diff[l+1] += 1
                diff[r+2] -= 1

        for i in range(1, len(diff)):
            diff[i] += diff[i - 1]

        for i in range(len(s)):
            finalStr += chr(((val(s[i]) + diff[i+1]) % 26) + ord('a')) 

        return finalStr


        
        