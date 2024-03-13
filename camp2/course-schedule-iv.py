class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        dist = [[False] * numCourses for _ in range(numCourses)]
        res = []

        for i in range(numCourses):
            dist[i][i] = True

        for k, v in prerequisites:
            dist[k][v] = True

        print(dist)

        for l in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dist[i][j] = dist[i][j] or (dist[i][l] and dist[l][j])


        for k, v in queries:
            res.append(dist[k][v])
            
        return res

        

        