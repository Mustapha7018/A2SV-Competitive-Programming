class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:

        N = len(arr)
        temp = None
        

        for i in range(N-1, 0, -1):
            if arr[i] < arr[i - 1]:
                temp = i-1

                break
 
        if temp == None:
            return arr
        
        second = None

        for i in range(N-1, temp, -1):
            if arr[i] < arr[temp]:
                second = i
                
                
                while i > temp+1 and  arr[i] == arr[i - 1]:
                    i -=1
                    second=i
            
                break
            
        
        if second:
            arr[temp], arr[second] = arr[second], arr[temp]

        return arr
                

        
        