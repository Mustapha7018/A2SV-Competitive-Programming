'''
* build your resultant matrix
* get all the zeros in the queue with a step of 0
* explore the neighbors of each zero and be adding a step of 1 when appending them to the queue
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS = len(mat)
        COLS = len(mat[0])

        new_grid = [[0] * COLS for _ in range(ROWS)]

        valid_move = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = set()
        queue = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] == 0:
                    queue.append((row, col, 0))
                    visited.add((row, col))

        while queue:
            r,c, dist  = queue.popleft()
            new_grid[r][c] = dist

            for k, v in valid_move:
                new_r = r+k
                new_c = c+v

                if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c, dist+1))

        return new_grid
            
            





        

        
