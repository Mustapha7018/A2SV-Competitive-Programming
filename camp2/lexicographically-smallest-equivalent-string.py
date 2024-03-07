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
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        N = 26
        uf = UnionFind(N)

        for i in range(len(s1)):
            uf.union(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))
        
        smallest_char = [chr(i + ord('a')) for i in range(N)]
        for i in range(N):
            root = uf.find(i)
            smallest_char[root] = min(smallest_char[root], chr(i + ord('a')))

        res = ''
        for char in baseStr:
            root = uf.find(ord(char) - ord('a'))
            res += smallest_char[root]

        return res


