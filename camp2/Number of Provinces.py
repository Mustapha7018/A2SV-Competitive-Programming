class UnionFind:

    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1] * n

    
    def find(self, node):
        while node != self.root[node]:
            node = self.root[node]
        
        return node

    
    def union(self, u, v):
        node1 = self.find(u)
        node2 = self.find(v)

        if node1 != node2:
            if self.size[node1] < self.size[node2]:
                self.root[node1] = node2
                self.size[node2] += self.size[node1]

            else:
                self.root[node2] = node1
                self.size[node1] += self.size[node2]

    
    def isConnected(self, u, v):
        self.root[self.find(u)] == self.root[self.find(v)]
        

class Solution:
    def findCircleNum(self, connected: List[List[int]]) -> int:

        N = len(connected)  
        M = len(connected[0])

        instance = UnionFind(N)


        for i in range(N):
            for j in range(M):
                if connected[i][j] == 1:
                    instance.union(i, j)

        sett = set()

        for i in range(N):
            curr = instance.find(i)
            sett.add(curr)

        return len(sett)





                
    

                    
