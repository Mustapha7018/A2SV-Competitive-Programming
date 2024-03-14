class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        heap = [(0, 0)]
        heapify(heap)
        visited = set()

        MOD = (10 ** 9) + 7
        arr = [0]*(n)
        
        for road in roads:
            u, v, w = road
            graph[u].append([v, w])
            graph[v].append([u, w])

        while heap:  
            cost, node = heappop(heap)

            if node in visited:
                continue


            arr[node] = cost

            visited.add(node)

            for child in graph[node]:
                if child[0] not in visited:
                    heappush(heap, (cost + child[1], child[0]))

        memo = {}

        def dp(node, c):
            if node in memo: return memo[node]

            if node == 0:
                return 1

            add = 0
            for child in graph[node]:
                nod, cost = child

                if c + cost + arr[nod] == arr[-1]:
                    add += dp(nod, c + cost)
                
            memo[node] = add

            return memo[node]

        return dp(n - 1, 0) % MOD

                            




        