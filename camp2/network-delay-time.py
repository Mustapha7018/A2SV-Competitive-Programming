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
        