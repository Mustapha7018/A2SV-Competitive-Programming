class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:


        prefix_sum = [0] * (len(nums))
        prefix_sum[0] = nums[0]
        output = 0
        summ = 0

        for i in range(len(prefix_sum)):
            summ += nums[i]
            prefix_sum[i] = summ
        
        dic = defaultdict(int)
        dic[0] = 1

        for i in range(len(prefix_sum)):
            mod = prefix_sum[i] % k
            if mod in dic:
                output += dic[mod]
            dic[mod] += 1

        return output

        















                






            
