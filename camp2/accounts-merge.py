class UnionFind:
    def __init__(self, n):
        self.root = {i: i for i in range(n)}
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        N = len(accounts)
        dsu = UnionFind(N)
        emailToID = {}
        
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToID:
                    dsu.union(i, emailToID[email])
                emailToID[email] = i

        idToEmail= {}

        for email, id in emailToID.items():
            rootID = dsu.find(id)

            if rootID not in idToEmail:
                idToEmail[rootID] = []

            idToEmail[rootID].append(email)

        return [[accounts[id][0]] + sorted(emails) for id, emails in idToEmail.items()]



       
            



            


        
                



