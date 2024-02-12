class Solution:
    def removeDuplicateLetters(self, string: str) -> str:

        counter = Counter(string)
        monStack = []
        seen = set()

        for char in string:

            if char in seen:
                continue
            counter[char] -= 1

            while monStack and monStack[-1] > char and counter[monStack[-1]] > 0:
                curr = monStack.pop()
                seen.remove(curr)

            monStack.append(char)
            seen.add(char)

        return ''.join(monStack)

        


        
