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
    def equationsPossible(self, equations: List[str]) -> bool:
        N = 26
        du = UnionFind(N)
        array = []

        for eqn in equations:
            
            temp1 = du.find((ord(eqn[0]) - ord('a')))
            temp2 = du.find((ord(eqn[3]) - ord('a')))
            sign = eqn[1:3]

            if (sign == '==' and temp1 != temp2) or (sign == '==' and temp1 == temp2):
                du.union((ord(eqn[0]) - ord('a')), (ord(eqn[3]) - ord('a')))

            else:
                array.append(eqn)

        if array:
            for arr in array:
                temp1 = du.find((ord(arr[0]) - ord('a')))
                temp2 = du.find((ord(arr[3]) - ord('a')))
                sign = eqn[1:3]

                if temp1 == temp2:
                    return False

        return True

            
        