class UnionFind:

    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1] * n

    
    def find(self, node):
        while node != self.root[node]:
            self.root[node] = self.root[self.root[node]]
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
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        instance = UnionFind(N)

        for k, v in edges:
            if instance.find(k - 1) == instance.find(v - 1):
                return [k, v]

            instance.union(k - 1, v - 1)

        

        
        
