# Dijkstra's Algorithm
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for time in times:
            u, v, w = time
            graph[u].append([v, w])

        heap = [(0, k)]
        heapify(heap)
        visited = set()

        while heap:
            l = len(heap)
            for _ in range(l):
                (cost, node) = heappop(heap)
                visited.add(node)
                if len(visited) == n:
                    return cost

                for child in graph[node]:
                    if child[0] not in visited:
                        heappush(heap, (cost+child[1], child[0]))

        return -1


# Floyed Warshall Algorithm
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]

        for u, v, w in times:
            dist[u-1][v-1] = w

        for i in range(n):
            dist[i][i] = 0

        for l in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][l] + dist[l][j])

        maxx = max(dist[k - 1])
        return  maxx if maxx != float('inf') else -1

        



        
