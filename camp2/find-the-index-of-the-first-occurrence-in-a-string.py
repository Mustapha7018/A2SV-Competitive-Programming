# RABIN-KARP ALGORITHM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        A = 31
        M = (10 ** 9) + 7

        def hash(string):
            s = len(string)
            needleHash = 0

            for i in range(n):
                needleHash += (ord(string[i]) - ord('a') + 1) * (A ** (s - i - 1))

            return (needleHash % M)

        m = len(haystack)
        n = len(needle)

        if n > m:
            return -1
            
        hash_ = hash(needle)
        newHash = 0

        size = haystack[:n]
        windowHash = hash(size)

        if windowHash == hash_:
            return 0

        for i in range(n, m):
            windowHash -= (ord(haystack[i - n]) - ord('a') + 1) * (A ** (n - 1)) 
            windowHash *= A
            windowHash += (ord(haystack[i]) - ord('a') + 1)
            windowHash %= M

            if windowHash == hash_:
                return i - n + 1

        return -1

        




            

            
        