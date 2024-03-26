class Solution:
    def longestPrefix(self, string: str) -> str:
        N = len(string)
        LPS = [0] * N

        for i in range(1, N):
            j = LPS[i - 1]

            while j > 0 and string[i] != string[j]:
                j = LPS[j - 1]

            if string[i] == string[j]:
                j += 1

            LPS[i] = j

        return string[:LPS[-1]]

        