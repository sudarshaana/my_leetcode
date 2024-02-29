class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        R = len(grid)
        C = len(grid[0])
        
        if grid[0][0] == 1 or grid[R-1][C-1] == 1:
            return -1
        
        if R==1 and C==1:
            return 1

        visited = set()
        q = deque()
        q.append((0, 0, 1))
        
        
        directions = [
            (0,1), (0,-1), (1,0), (-1, 0), 
            #(0,1), (0,-1), (1,0), (-1, 0), 
            (1,1), (1,-1), (-1,1), (-1,-1)
            #(1,1), (1,-1), (-1,1), (-1,1) 
            
        ]

        while q:
            r, c, d = q.popleft()

            for rr, cc in directions:
                nr = r + rr
                nc = c + cc

                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited and grid[nr][nc]==0:
                    visited.add((nr, nc))
                    q.append((nr, nc, d+1))
                    
                    if (nr, nc) == (R - 1, C - 1): 
                        return d + 1
                    
                    
        return -1
    
    