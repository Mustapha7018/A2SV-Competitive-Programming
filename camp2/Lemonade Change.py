class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        hashmap = defaultdict(int)

        for bill in bills:
            hashmap[bill] += 1

            if bill == 5:
                continue
            
            elif bill == 10 and hashmap[5] >= 1:
                hashmap[5] -= 1
            
            elif bill == 20 and hashmap[5] >= 1 and hashmap[10] >= 1:
                hashmap[5] -= 1
                hashmap[10] -= 1

            elif bill == 20 and hashmap[5] >= 3:
                hashmap[5] -= 3

            else:
                return False
        
        return True


        

