def polandBallAndForest():
    
    parent = list(range(n+1)) 
    rank = [0] * (n+1)     
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
    
    for i in range(n):
        union(i + 1, seq[i])
    
    trees = len(set(find(i) for i in range(1, n + 1)))
    return trees
 
if __name__ == '__main__':
    n = int(input())
    seq = list(map(int, input().split()))
 
    print(polandBallAndForest())
