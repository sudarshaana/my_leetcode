class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        from collections import deque
        visited = set()
        q = deque()

        ROW = len(matrix)
        COL = len(matrix[0])
        
        combinations = [
            [-1,0],
            [0,-1],
            [0, 1],
            [1, 0]
        ]
        
        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))
                    
        while q:
            x, y = q.popleft()
            for dirr in combinations:
                newX, newY = x+ dirr[0], y+ dirr[1]
                if newX < ROW and newX >=0 and newY < COL and newY >= 0 and (newX, newY) not in visited:
                    matrix[newX][newY] = matrix[x][y] + 1
                    q.append([newX, newY])
                    visited.add((newX, newY))
                    
        return matrix