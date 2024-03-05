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
            if self.size[node1] > self.size[node2]:
                self.root[node2] = node1
                self.size[node1] += self.size[node2]

            else:
                self.root[node1] = node2
                self.size[node2] += self.size[node1]


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    
        instance = UnionFind(n)

        for k, v in edges:
            instance.union(k, v)

        return instance.find(source) == instance.find(destination)


        
