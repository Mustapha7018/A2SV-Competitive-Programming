class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        diff = sorted(costs, key=lambda x: x[0] - x[1])
        minCost = 0

        for i in range(len(costs) // 2):
            minCost += diff[i][0]
        
        for i in range(len(costs) // 2, len(costs)):
            minCost += diff[i][1]

        return minCost
