class Solution:
    def subStrHash(self, string: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
        N = len(string)
        string = string[::-1]

        hash_ = 0
        res = ''

        for i in range(k):
            hash_ += (ord(string[i]) - ord('a') + 1) * (pow(power, k - i - 1, modulo))
            hash_ %= modulo
    

        if hash_ == hashValue:
            res = string[:k]

        p = pow(power, k - 1, modulo)

        for i in range(k, N):
            hash_ -= (ord(string[i - k]) - ord('a') + 1) * p
            hash_ *= power
            hash_ += (ord(string[i]) - ord('a') + 1)
            hash_ %= modulo

            if hash_ == hashValue:
                res = string[i-k+1: i+1]

        return res[::-1]


        

        

        